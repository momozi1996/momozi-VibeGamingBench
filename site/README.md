# 展示站 (GitHub Pages)

把枯燥的 leaderboard 变成**「能看、能玩、能懂」的公众页面**。

## 打开（本地）

```bash
bash scripts/gen_site.sh          # 生成 site/data/ 数据
python3 -m http.server            # 访问 http://localhost:8000/site/index.html
```

## 部署到 GitHub Pages

把 `.github/workflows/site.yml` 放在仓库里即可自动发布；GitHub 端要开一次 Settings → Pages → Source = GitHub Actions。

## 页面模块

| 模块 | 解决什么问题 |
|---|---|
| **Playground** | 直接试玩每个 agent 交的游戏，如果没交 index.html 就显示「未交付可玩界面」占位卡 |
| **Lifecycle** | 用 GameGen/GameFix/GameOpt 三阶段讲清楚 BMK 练的什么能力 |
| **Leaderboard** | 可点表头排序；维度 = B/S/P/回归 |
| **Findings** | 大数字 + 一句话结论，低代码读者也能 get |
| **Case reel** | 过程回放（录屏/轮次 diff），点击后播放 |

## 数据来源（谁的产出）

```
site/index.html                            # 展示页
site/play/<task>_reference.html            # 每题过样板（可玩）
site/play/<task>_<agent>.html              # 每个 agent 交付后的可玩副本
site/data/playables.json                   # 上面两个的索引（自动生成）
site/data/leaderboard.json                 # leaderboard 数据（自动从 runs/ 聚合）
```

只要 `runs/` 里多了一个 agent 的 json，对应 `play/` 里出现可玩 HTML，**重跑 `bash scripts/gen_site.sh` 就能让首页自动更新**。
