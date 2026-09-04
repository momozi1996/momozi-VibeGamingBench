#!/usr/bin/env node
import fs from "node:fs";

const [direct1Path, generatedPath, outPath, existingPath] = process.argv.slice(2);
if (!direct1Path || !generatedPath || !outPath) {
  console.error("usage: node translate_feishu_texts.mjs direct1.json directgen.json out.json");
  process.exit(2);
}

const readRows = (file) => {
  const payload = JSON.parse(fs.readFileSync(file, "utf8"));
  return payload.sheets[0].data.filter(
    (row) => Array.isArray(row) && row.some((value) => value !== null && value !== ""),
  );
};
const direct1 = readRows(direct1Path);
const generated = readRows(generatedPath);

const seedBrief = (row) =>
  `围绕“${row[1]}（${row[2]}）”制作一个完整可玩的浏览器游戏垂直切片。` +
  `这是一个由题目类型驱动的原创实现，必须使用或合理解释以下技术约束：${row[3]}。` +
  "请把题目类型转化为明确的核心循环、玩家输入、状态变化、成功与失败条件；" +
  "不得停在静态展示，必须能开始、游玩、结算并重玩。";

const texts = [];
for (const row of direct1) {
  texts.push(row[1], row[4] || seedBrief(row));
}
for (const row of generated) {
  texts.push(row[1], row[3]);
}
const existing = existingPath && fs.existsSync(existingPath)
  ? JSON.parse(fs.readFileSync(existingPath, "utf8"))
  : {};
const unique = [...new Set(texts.filter(Boolean))].filter((text) => !existing[text]);
const result = { ...existing };
let cursor = 0;
const workers = Array.from({ length: 3 }, async () => {
  while (true) {
    const index = cursor++;
    if (index >= unique.length) return;
    const text = unique[index].slice(0, 4000);
    let translated = "";
    let lastError = "";
    for (let attempt = 0; attempt < 5 && !translated; attempt += 1) {
      try {
        const query = new URLSearchParams({
          client: "gtx",
          sl: "zh-CN",
          tl: "en",
          dt: "t",
          q: text,
        });
        const response = await fetch(
          `https://translate.googleapis.com/translate_a/single?${query}`,
          { headers: { "User-Agent": "Mozilla/5.0" } },
        );
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const payload = await response.json();
        translated = payload[0]
          .filter((part) => Array.isArray(part) && part[0])
          .map((part) => part[0])
          .join("")
          .trim();
      } catch (error) {
        lastError = String(error);
        await new Promise((resolve) => setTimeout(resolve, 800 * (attempt + 1)));
      }
    }
    if (!translated) {
      throw new Error(`translation failed for ${text.slice(0, 80)}: ${lastError}`);
    }
    result[unique[index]] = translated;
    if ((index + 1) % 25 === 0) {
      console.error(`translated ${index + 1}/${unique.length}`);
    }
    await new Promise((resolve) => setTimeout(resolve, 180));
  }
});

await Promise.all(workers);
fs.writeFileSync(outPath, `${JSON.stringify(result, null, 2)}\n`);
console.error(`wrote ${Object.keys(result).length} translations to ${outPath}`);
