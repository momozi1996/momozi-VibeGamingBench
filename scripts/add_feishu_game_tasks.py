#!/usr/bin/env python3
"""Import the Feishu game-prompt catalog into the native MZ task format.

The linked workbook contains two useful sheets:

* ``直接1`` — 100 structured game/type/technology seeds.
* ``直接生成`` — 120 Chinese game-generation prompts.

The importer keeps the source wording as a provenance/evidence field, wraps it
in the VibeGamingBench delivery contract, and emits one English + one Chinese
variant per concept. English variants are translated once at import time and
stored in the source manifest so later validation is offline and reproducible.

Usage:

    python3 scripts/add_feishu_game_tasks.py \
      --direct1 /path/to/direct1.json \
      --direct-generated /path/to/directgen.json \
      --import --translate
    python3 scripts/add_feishu_game_tasks.py --write
    python3 scripts/add_feishu_game_tasks.py
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml
try:
    import requests
except ImportError:  # pragma: no cover - optional import-time dependency
    requests = None

from prompt_contract import input_scheme_for_family
from task_metadata import classify_difficulty


ROOT = Path(__file__).resolve().parent.parent
TASKS_ROOT = ROOT / "bench" / "tasks"
SOURCES_ROOT = ROOT / "bench" / "sources"
MANIFEST_PATH = SOURCES_ROOT / "feishu_game_prompts.json"

SOURCE_WORKBOOK_URL = (
    "https://wvixbzgc0u7.feishu.cn/wiki/Il2IwLfZtiU3Nqk4K4acsQQKndf"
    "?sheet=Z03L1A"
)
SOURCE_WORKBOOK_TOKEN = "GBYhs8lZchFZe0tFvjUcXbz2nOS"
SOURCE_CAPTURE_DATE = "2026-09-04"
SOURCE_SHEETS = {
    "structured": {"id": "88f3e3", "name": "直接1"},
    "generated": {"id": "Z03L1A", "name": "直接生成"},
}

LANGUAGE_SUFFIX = {"en": " (English)", "zh": " (中文)"}
RUBRIC_MAPPING = {
    "completeness": ["M1", "M2", "M3"],
    "richness": ["D1", "D2", "D3", "D4"],
    "player_exp": ["V1", "V2", "V3"],
    "visual": ["A1", "A2", "A3", "A4"],
}

FAMILY_LABELS = {
    "action": {"en": "action game", "zh": "动作游戏"},
    "adventure": {"en": "adventure game", "zh": "冒险游戏"},
    "arcade": {"en": "arcade game", "zh": "街机游戏"},
    "cardgame": {"en": "card game", "zh": "卡牌游戏"},
    "horror": {"en": "horror game", "zh": "恐怖游戏"},
    "idle": {"en": "idle game", "zh": "放置游戏"},
    "narrative": {"en": "narrative game", "zh": "叙事游戏"},
    "openworld": {"en": "open-world game", "zh": "开放世界游戏"},
    "platformer": {"en": "platformer", "zh": "平台跳跃游戏"},
    "puzzle": {"en": "puzzle game", "zh": "解谜游戏"},
    "racing": {"en": "racing game", "zh": "竞速游戏"},
    "rhythm": {"en": "rhythm game", "zh": "节奏游戏"},
    "roguelike": {"en": "roguelike game", "zh": "Roguelike 游戏"},
    "rpg": {"en": "role-playing game", "zh": "角色扮演游戏"},
    "shooter": {"en": "shooter", "zh": "射击游戏"},
    "simulation": {"en": "simulation game", "zh": "模拟游戏"},
    "sports": {"en": "sports game", "zh": "体育游戏"},
    "strategy": {"en": "strategy game", "zh": "策略游戏"},
    "survival": {"en": "survival game", "zh": "生存游戏"},
    "tycoon": {"en": "tycoon game", "zh": "经营游戏"},
    "visualnovel": {"en": "visual novel", "zh": "视觉小说"},
}

GENERIC_TITLE_FAMILIES = {
    "像素风模板": "arcade",
    "复古8-16bit": "arcade",
    "手绘风": "narrative",
    "低多边形": "adventure",
    "写实风": "simulation",
    "卡通风": "arcade",
    "科幻风": "shooter",
    "奇幻风": "adventure",
    "蒸汽朋克": "adventure",
    "赛博朋克": "shooter",
    "中世纪题材": "strategy",
    "古代历史": "strategy",
    "未来世界": "simulation",
    "科幻宇宙": "shooter",
    "魔法奇幻题材": "rpg",
    "神话传说": "adventure",
    "西部牛仔": "shooter",
    "都市现代": "simulation",
    "末日废土": "survival",
    "地牢探索": "roguelike",
    "卡牌收集": "cardgame",
}

KEYWORD_FAMILY_RULES = [
    (
        "visualnovel",
        ["视觉小说", "纯文字RPG", "interactive fiction", "visual novel", "文字剧情"],
    ),
    ("horror", ["恐怖", "惊悚", "心理恐怖", "跳脸", "zombie survival horror"]),
    ("roguelike", ["roguelike", "roguelite", "肉鸽", "随机地牢", "永久死亡"]),
    ("rhythm", ["节奏", "音乐游戏", "音符", "rhythm", "music game"]),
    ("racing", ["赛车", "竞速", "racing", "kart", "赛道"]),
    ("sports", ["足球", "篮球", "棒球", "橄榄球", "冰球", "网球", "高尔夫", "极限运动"]),
    ("shooter", ["fps", "tps", "射击", "枪", "shooter", "弹幕", "大逃杀", "moba"]),
    ("strategy", ["策略", "战棋", "塔防", "即时战略", "回合制策略", "4x", "大战略", "自动走棋"]),
    ("cardgame", ["卡牌", "card", "deck", "抽卡", "卡组"]),
    ("platformer", ["平台", "跑酷", "横版", "银河城", "类魂", "platformer"]),
    ("puzzle", ["解谜", "拼图", "三消", "物理解谜", "找物", "魔方", "puzzle"]),
    ("idle", ["放置", "点击游戏", "点击器", "idle", "clicker"]),
    ("tycoon", ["城市建造", "农场", "经营", "管理", "tycoon"]),
    ("survival", ["生存", "沙盒", "crafting", "survival", "末日"]),
    ("simulation", ["模拟", "城市", "交通", "飞行", "太空模拟", "动物模拟", "生态"]),
    ("rpg", ["rpg", "角色扮演", "crpg", "jrpg", "冒险者"]),
    ("action", ["动作", "格斗", "砍杀", "潜行", "近战", "action"]),
    ("openworld", ["开放世界", "open world", "自由漫游"]),
    ("adventure", ["冒险", "探索", "adventure"]),
]

DIMENSION_3D = [
    "3d",
    "three.js",
    "threejs",
    "babylon",
    "webgl",
    "webgpu",
    "css-3d",
    "体素",
    "立体",
]


class LiteralDumper(yaml.SafeDumper):
    pass


def _represent_str(dumper: yaml.Dumper, value: str):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


LiteralDumper.add_representer(str, _represent_str)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def translate_text(text: str, cache: dict[str, str]) -> str:
    """Translate one prompt through Google's public translation endpoint.

    This is only used while importing a snapshot. The translated result is
    written to the manifest; normal validation and task generation are offline.
    """
    if not text:
        return ""
    if text in cache:
        return cache[text]
    query = text
    # Keep URL requests comfortably below the endpoint's query-size limit.
    if len(query) > 4300:
        chunks = re.split(r"(\n{2,}|[.!?。！？；;])", query)
        groups: list[str] = []
        current = ""
        for chunk in chunks:
            if len(current) + len(chunk) > 4000 and current:
                groups.append(current)
                current = ""
            current += chunk
        if current:
            groups.append(current)
    else:
        groups = [query]

    translated: list[str] = []
    for group in groups:
        params = urllib.parse.urlencode(
            {
                "client": "gtx",
                "sl": "zh-CN",
                "tl": "en",
                "dt": "t",
                "q": group,
            }
        )
        url = f"https://translate.googleapis.com/translate_a/single?{params}"
        last_error = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(url, timeout=30) as response:
                    payload = json.loads(response.read().decode("utf-8"))
                result = "".join(
                    part[0]
                    for part in payload[0]
                    if isinstance(part, list) and part and part[0]
                )
                translated.append(result)
                break
            except Exception as exc:  # pragma: no cover - network dependent
                last_error = exc
                time.sleep(1.5 * (attempt + 1))
        else:
            # Google Translate throttles bursty imports. MyMemory is a
            # deterministic public fallback and the translated text is cached
            # in the manifest, so this fallback is only used at import time.
            fallback_params = urllib.parse.urlencode(
                {"q": group, "langpair": "zh-CN|en"}
            )
            fallback_url = (
                "https://api.mymemory.translated.net/get?" + fallback_params
            )
            try:
                with urllib.request.urlopen(fallback_url, timeout=30) as response:
                    fallback = json.loads(response.read().decode("utf-8"))
                result = (
                    fallback.get("responseData", {}).get("translatedText", "")
                )
                if not result:
                    raise RuntimeError("empty MyMemory translation")
                translated.append(result)
            except Exception as fallback_error:  # pragma: no cover
                raise RuntimeError(
                    f"translation failed after retries: {last_error}; "
                    f"MyMemory fallback failed: {fallback_error}"
                )
        time.sleep(0.25)
    value = "".join(translated).strip()
    if not value:
        raise RuntimeError("translation returned empty text")
    cache[text] = value
    return value


def translate_text_fast(text: str) -> str:
    """Single-shot translation used by the parallel importer."""
    if not text:
        return ""
    text = text[:4000]
    # MyMemory is comparatively stable for this one-time import. Google
    # Translate remains the fallback for terms or sentences MyMemory declines.
    if requests is not None:
        try:
            fallback_params = urllib.parse.urlencode(
                {"q": text, "langpair": "zh-CN|en"}
            )
            response = requests.get(
                f"https://api.mymemory.translated.net/get?{fallback_params}",
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=12,
            )
            response.raise_for_status()
            result = (
                response.json()
                .get("responseData", {})
                .get("translatedText", "")
                .strip()
            )
            if result and not result.startswith("MYMEMORY WARNING"):
                return result
        except Exception:
            pass
    params = urllib.parse.urlencode(
        {"client": "gtx", "sl": "zh-CN", "tl": "en", "dt": "t", "q": text}
    )
    try:
        request = urllib.request.Request(
            f"https://translate.googleapis.com/translate_a/single?{params}",
            headers={"User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
        result = "".join(
            part[0]
            for part in payload[0]
            if isinstance(part, list) and part and part[0]
        ).strip()
        if result:
            return result
    except Exception:
        pass

    fallback_params = urllib.parse.urlencode(
        {"q": text[:4500], "langpair": "zh-CN|en"}
    )
    request = urllib.request.Request(
        "https://api.mymemory.translated.net/get?" + fallback_params,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        fallback = json.loads(response.read().decode("utf-8"))
    result = fallback.get("responseData", {}).get("translatedText", "").strip()
    if not result:
        raise RuntimeError("empty translation")
    return result


def translate_batch(texts: list[str]) -> dict[str, str]:
    unique = list(dict.fromkeys(text for text in texts if text))
    if not unique:
        return {}
    output: dict[str, str] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(translate_text_fast, text): text for text in unique}
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            text = futures[future]
            try:
                output[text] = future.result()
            except Exception as exc:
                raise RuntimeError(
                    f"parallel translation failed for text {text[:80]!r}: {exc}"
                ) from exc
            if index % 50 == 0:
                print(f"translated {index}/{len(unique)} text segments")
    return output


def family_for(*values: str) -> str:
    text = " ".join(values).lower()
    # Prefer unambiguous genre markers before broad words such as "adventure",
    # "management", or "simulation". This keeps "turn-based RPG" from being
    # misclassified as a tycoon simply because the technology line says
    # "state management".
    priority_rules = [
        ("openworld", ["开放世界", "开放探索", "open world", "自由漫游"]),
        ("roguelike", ["roguelike", "roguelite", "肉鸽", "随机地牢"]),
        ("rpg", ["rpg", "role-playing", "crpg", "jrpg", "角色扮演"]),
        ("horror", ["恐怖", "惊悚", "心理恐怖", "跳脸"]),
        ("rhythm", ["节奏", "音乐游戏", "音符", "rhythm", "music game"]),
        ("racing", ["赛车", "竞速", "racing", "kart", "赛道"]),
        ("sports", ["足球", "篮球", "棒球", "橄榄球", "冰球", "网球", "高尔夫", "极限运动"]),
        ("cardgame", ["卡牌", "card", "deck", "抽卡", "卡组"]),
        ("strategy", ["策略", "战棋", "塔防", "即时战略", "回合制策略", "4x", "大战略", "自动走棋", "moba"]),
        ("shooter", ["fps", "tps", "射击", "shooter", "弹幕", "大逃杀"]),
        ("platformer", ["平台", "跑酷", "横版", "银河城", "类魂", "platformer"]),
        ("puzzle", ["解谜", "拼图", "三消", "物理解谜", "找物", "魔方", "puzzle"]),
        ("idle", ["放置", "点击游戏", "点击器", "idle", "clicker"]),
        ("action", ["动作", "战斗", "格斗", "砍杀", "潜行", "近战", "爆炸", "action"]),
        ("survival", ["生存", "沙盒", "crafting", "survival", "末日"]),
        ("tycoon", ["城市建造", "农场", "经营管理", "tycoon"]),
        ("simulation", ["模拟", "交通", "飞行", "太空模拟", "动物模拟", "生态"]),
        ("narrative", ["叙事", "剧情", "文字剧情", "visual novel"]),
        ("adventure", ["冒险", "探索", "adventure"]),
    ]
    for family, keywords in priority_rules:
        if any(keyword.lower() in text for keyword in keywords):
            return family
    for title, family in GENERIC_TITLE_FAMILIES.items():
        if title.lower() in text:
            return family
    return "adventure"


def dimension_for(*values: str) -> str:
    text = " ".join(values).lower()
    return "3D" if any(signal in text for signal in DIMENSION_3D) else "2D"


def normalize_technology(value: str) -> str:
    return value.replace("DOM‑Overlay", "DOM Overlay").replace("CSS‑3D", "CSS-3D").strip()


def slug(value: str, fallback: str) -> str:
    ascii_value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return ascii_value or fallback


def seed_brief_zh(title_zh: str, title_en: str, tech: str) -> str:
    return (
        f"围绕“{title_zh}（{title_en}）”制作一个完整可玩的浏览器游戏垂直切片。"
        f"这是一个由题目类型驱动的原创实现，必须使用或合理解释以下技术约束：{tech}。"
        "请把题目类型转化为明确的核心循环、玩家输入、状态变化、成功与失败条件；"
        "不得停在静态展示，必须能开始、游玩、结算并重玩。"
    )


def vibe_contract(language: str, family: str, dimension: str, technology: str) -> str:
    scheme = input_scheme_for_family(family)
    if language == "zh":
        interaction = {
            "pointer-first": "以鼠标/指针为主，支持点击、悬停、拖拽或框选；自然需要时再加入键盘快捷键。",
            "keyboard-first": "以键盘为主，提供方向键或 WASD、Space、Enter、Esc；自然需要时加入鼠标。",
            "both": "同时支持键盘和指针：键盘负责移动或动作，指针负责空间选择、菜单和目标操作。",
        }[scheme]
        return f"""\
## HTML 提交合同

交付两个文件：`index.html` 和 `game_logic.js`。{dimension} 呈现可使用
{technology}，但规则层必须与 DOM、Canvas、WebGL 或 WebGPU 渲染解耦。

页面无需构建步骤即可打开，首屏三秒内出现可操作内容。禁止运行时请求图片、
模型、视频或音频；允许程序化几何、Canvas2D、SVG、CSS、Web Audio、Shader、
固定版本库和 `data:` URI。若使用 CDN，只允许固定版本的官方库依赖。

交互方案（{scheme}）：{interaction}
完整游戏区和 HUD 在 1280x720 下清晰可读；手机 390x844、360x800 和 430x932
不得出现横向滚动或关键控件溢出。必须有开始、进行中、暂停、失败/胜利、重开
和状态恢复流程。

`index.html` 负责呈现与输入，`game_logic.js` 负责确定性状态与规则，并暴露：

```javascript
(function (root) {{
  function createGame(opts) {{ return {{ phase: "title", score: 0 }}; }}
  function advance(game, input, dt) {{ return game; }}
  const api = {{ createGame, advance }};
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GameLogic = api;
}}(typeof window !== "undefined" ? window : globalThis));
```

`advance()` 不得访问 DOM 或渲染对象。随机内容必须可用 seed 复现。
"""
    interaction = {
        "pointer-first": "Use pointer input as the primary control with click, hover, drag, or selection; add keyboard shortcuts only where natural.",
        "keyboard-first": "Use keyboard input as the primary control with arrows or WASD plus clear Space, Enter, and Escape actions; add pointer input where natural.",
        "both": "Support keyboard and pointer input: use keyboard for movement/actions and pointer input for spatial selection, menus, or targeting.",
    }[scheme]
    return f"""\
## HTML Submission Contract

Deliver two files: `index.html` and `game_logic.js`. Use {technology} for the
{dimension} presentation when appropriate, but keep the rules layer independent
from DOM, Canvas, WebGL, or WebGPU rendering.

The page must open without a build step and expose meaningful interaction within
three seconds. Do not request external images, models, video, or audio at runtime.
Procedural geometry, Canvas2D, SVG, CSS, Web Audio, shaders, pinned libraries, and
`data:` URIs are allowed. If a CDN is used, pin an official library version.

Interaction scheme ({scheme}): {interaction}
Keep the play area and HUD readable at 1280x720 and avoid horizontal overflow or
unreachable controls at 390x844, 360x800, and 430x932. Include title, playing,
pause, failure/victory, restart, and state-restoration flows.

`index.html` owns presentation and input. `game_logic.js` owns deterministic rules
and exposes:

```javascript
(function (root) {{
  function createGame(opts) {{ return {{ phase: "title", score: 0 }}; }}
  function advance(game, input, dt) {{ return game; }}
  const api = {{ createGame, advance }};
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.GameLogic = api;
}}(typeof window !== "undefined" ? window : globalThis));
```

`advance()` must not access DOM or rendering objects. Random content must be
reproducible from a seed.
"""


def prompt_for(item: dict[str, Any], language: str) -> str:
    brief = item[f"brief_{language}"]
    title = item[f"title_{language}"]
    family_label = FAMILY_LABELS[item["family"]][language]
    if language == "zh":
        return f"""\
# {title}

你是一名资深 Vibe Gaming 设计师、游戏程序员、交互设计师和 QA 工程师。
请把下面的题目证据实现成一个**完整、可运行、可测试、可重玩的原创浏览器游戏**，
而不是静态 Demo 或只展示视觉效果的样片。

## 任务身份

- 基准家族：{family_label}
- 题目维度：{item["dimension"]}
- 指定技术栈：{item["technology"]}
- 来源：飞书《提示词大全》· {item["source_sheet_name"]} · 原始序号 {item["source_index"]}

## 原始玩法简报（语义不可删改）

> {brief}

以上简报是本题的玩法与逻辑锚点。你可以为了浏览器垂直切片压缩内容数量，
但不得删除、替换或弱化其中的核心输入、规则、状态、目标、失败条件或技术约束。
当简报只给出类型和技术种子时，请明确标注你的合理化假设，并实现一个最小但
闭环完整的同类玩法；不要假装题目提供了未提供的隐藏规则。

## Vibe Gaming 实现要求

1. 先输出一页实现规格，然后直接创建文件、运行页面和执行测试，不停在方案阶段。
2. 把原始简报拆成可验证的状态机：标题、引导、进行中、暂停、失败、胜利/结算、
   重开和恢复；每个状态都有输入、状态变化、退出条件和可见反馈。
3. 建立清晰的核心循环：开始 -> 理解目标 -> 通过主要输入完成动作 -> 即时反馈 ->
   资源/进度更新 -> 成功或失败 -> 下一局、重试或返回标题。
4. 至少实现三段递进流程：第一段教会核心动作，第二段组合核心动作与压力，
   第三段用综合场景验证掌握；如果原始简报已有明确关卡数量，优先遵守原数量。
5. 每个重要动作必须有至少两种反馈（位移、缩放、粒子、颜色、声音、HUD 或镜头），
   无效输入、受伤、失败、成功和持久状态变化必须可区分。
6. HUD 只显示必要信息，并在稳定区域展示目标、关键资源、选择状态、进度、危险、
   计时/分数和当前阶段；关键状态不得只靠颜色区分。
7. 所有主要交互支持单手/键盘可用的清晰输入，点击目标至少 44x44 CSS px；
   触控与鼠标输入不能依赖 hover 才能完成。
8. 使用原创名称、原创程序化图形、原创音效或明确许可资产。不得复制原作商标、
   角色、剧情文本、美术、音乐、音效、关卡数据、服务器或反编译代码。
9. 使用 localStorage 保存设置、最佳成绩和允许持久化的进度；不要上传个人数据，
   不接真实支付、广告或未审核的多人服务。

{vibe_contract(language, item["family"], item["dimension"], item.get("technology_zh", item["technology"]) if language == "zh" else item.get("technology_en", item["technology"]))}

## 验收标准

- 首次可操作时间不超过 3 秒，核心玩法 60 秒内可理解。
- 在 390x844、360x800、430x932、1280x800 四个视口无重叠、无横向滚动、
  无截断文字和不可达按钮。
- `game_logic.js` 可由 Node 直接加载，`createGame({{seed}})` 与
  `advance(game, input, dt)` 能稳定运行，规则层不依赖 DOM。
- 至少提供 12 个有意义的规则/状态测试和 5 条 Playwright 或等价端到端流程。
- README 说明启动、玩法、状态、测试、目录结构、技术取舍和与原始简报的差异。
- 完成后输出实际文件路径、启动命令、测试结果、截图路径、已知限制和原创资产说明。
"""

    return f"""\
# {title}

You are a senior Vibe Gaming designer, gameplay engineer, interaction designer,
and QA engineer. Turn the evidence below into a **complete, runnable, testable,
replayable original browser game**, not a static demo or a visual-only mockup.

## Task Identity

- Benchmark family: {family_label}
- Task dimension: {item["dimension"]}
- Required technology: {item.get("technology_en", item["technology"])}
- Source: Feishu “Prompt Catalog” · {item["source_sheet_name"]} · source index {item["source_index"]}

## Original Gameplay Brief (Semantically Immutable)

> {brief}

This brief is the gameplay and logic anchor. You may reduce content quantity for
a browser vertical slice, but must not delete, replace, or weaken its core inputs,
rules, states, goals, failure conditions, or technology constraints. If the brief
only supplies a type and technology seed, explicitly state your assumptions and
build the smallest complete same-family loop; do not pretend hidden rules were
provided.

## Vibe Gaming Implementation Requirements

1. Start by writing a one-page implementation specification, then create files,
   run the page, and execute tests; do not stop at a plan.
2. Convert the brief into a verifiable state machine: title, onboarding, playing,
   pause, failure, victory/result, restart, and restoration. Each state needs
   inputs, transitions, exit conditions, and visible feedback.
3. Build a clear loop: start -> understand objective -> perform the main action ->
   immediate feedback -> resource/progress update -> success or failure -> next,
   retry, or title.
4. Implement at least three escalating phases: teach the core action, combine it
   with pressure, and finish with a synthesis scenario. If the source brief states
   a level count, preserve it where practical.
5. Give every important action at least two feedback channels (motion, scale,
   particles, color, sound, HUD, or camera). Invalid input, damage, failure,
   success, and persistent state changes must be distinguishable.
6. Keep the HUD minimal but stable. Show objective, critical resources, selection,
   progress, danger, timer/score, and current phase; never rely on color alone.
7. Make primary interactions clear for one hand/keyboard use; pointer targets must
   be at least 44x44 CSS px, and mouse/touch input must not depend on hover.
8. Use original names, procedural artwork, original audio, or explicitly licensed
   assets. Do not copy trademarks, characters, narrative text, artwork, music,
   sound effects, level data, servers, or reverse-engineered code.
9. Use localStorage for settings, best scores, and permitted progress. Do not upload
   personal data, connect real payments or ads, or create an unreviewed multiplayer service.

{vibe_contract(language, item["family"], item["dimension"], item.get("technology_zh", item["technology"]) if language == "zh" else item.get("technology_en", item["technology"]))}

## Acceptance Criteria

- First meaningful interaction within three seconds; the core loop is understandable within 60 seconds.
- No overlap, horizontal scrolling, clipped text, or unreachable controls at
  390x844, 360x800, 430x932, and 1280x800.
- `game_logic.js` loads directly in Node; `createGame({{seed}})` and
  `advance(game, input, dt)` run deterministically and do not depend on the DOM.
- Provide at least 12 meaningful rule/state tests and five Playwright or equivalent
  end-to-end flows.
- README documents startup, gameplay, states, tests, directory structure, technical
  tradeoffs, and differences from the original brief.
- Finish by reporting actual file paths, launch commands, test results, screenshot
  paths, known limitations, and original-asset provenance.
"""


def requirement_set(item: dict[str, Any], language: str) -> list[dict[str, Any]]:
    brief = item[f"brief_{language}"]
    if language == "zh":
        text = {
            "M1": f"原始玩法简报的核心循环必须可玩并可由玩家输入完成：{brief}",
            "M2": "核心输入、规则、状态变化、成功条件和失败条件必须在 game_logic.js 中形成确定性状态机，而非静态按钮或装饰。",
            "M3": "至少一个核心动作必须展示合法/无效输入、边界条件、即时反馈和恢复或重置结果。",
            "D1": "至少实现三段递进流程，并让资源、计时、生命、分数、库存、冷却或其他与题材相符的状态改变决策。",
            "D2": "至少提供三种功能不同的内容、对象、关卡、敌人、谜题或策略选择，不能只是换颜色或换文案。",
            "D3": "实现暂停、重开、结算、localStorage 恢复和至少一种可观察的持久化或重玩结果。",
            "D4": "第三阶段必须综合至少两项前置机制，并提供清晰成功、失败和再次挑战流程。",
            "V1": "HUD 清楚展示当前目标、关键资源、阶段、进度和危险，且信息与实时状态同步。",
            "V2": "有效、无效、受伤、成功、失败和状态变化均有可区分的即时反馈。",
            "V3": "从开始、引导、进行中到结算、重试的完整游戏闭环无需刷新页面即可完成。",
            "A1": "使用统一且有辨识度的原创视觉方向，技术栈服务于主题而非堆叠默认控件。",
            "A2": "镜头、构图、层级、光照或平面布局经过设计，重要对象与目标易于阅读。",
            "A3": "角色、目标、危险、工具和 UI 符号拥有清晰轮廓和不同功能状态。",
            "A4": "移动、命中、转场、警报、完成和界面变化使用多帧动画、粒子、镜头或声音反馈。",
        }
    else:
        text = {
            "M1": f"The core loop from the original brief is playable and completed through player input: {brief}",
            "M2": "Core inputs, rules, state transitions, success conditions, and failure conditions form a deterministic state machine in game_logic.js rather than static buttons or decoration.",
            "M3": "At least one core action exposes valid/invalid input, edge conditions, immediate feedback, and recovery or reset behavior.",
            "D1": "Implement three escalating phases and make theme-appropriate resources, timers, health, score, inventory, cooldowns, or other state change decisions.",
            "D2": "Provide at least three functionally distinct contents, objects, levels, enemies, puzzles, or strategic choices; color/text swaps alone do not count.",
            "D3": "Implement pause, restart, result, localStorage restoration, and at least one observable persistent or replay outcome.",
            "D4": "The third phase combines at least two earlier mechanics and provides clear success, failure, and replay flows.",
            "V1": "The HUD clearly presents the objective, critical resources, phase, progress, and danger, synchronized with live state.",
            "V2": "Valid, invalid, damage, success, failure, and state changes have distinguishable immediate feedback.",
            "V3": "The complete start, onboarding, play, result, and retry loop works without a page refresh.",
            "A1": "Use a coherent, recognizable original art direction in which the chosen technology serves the theme rather than default controls.",
            "A2": "Camera, composition, layering, lighting, or 2D layout are deliberate and keep important objects and goals readable.",
            "A3": "Actors, goals, hazards, tools, and UI symbols have readable silhouettes and visibly different functional states.",
            "A4": "Movement, impacts, transitions, alerts, completion moments, and UI changes use multi-frame animation, particles, camera, or audio feedback.",
        }
    categories = {
        "M1": "mechanic",
        "M2": "mechanic",
        "M3": "mechanic",
        "D1": "depth",
        "D2": "depth",
        "D3": "depth",
        "D4": "depth",
        "V1": "experience",
        "V2": "experience",
        "V3": "experience",
        "A1": "art",
        "A2": "art",
        "A3": "art",
        "A4": "art",
    }
    aggs = {
        **{key: "max" for key in ("M1", "M2", "M3", "D1", "D2", "D3", "D4")},
        **{key: "mean" for key in ("V1", "V2", "V3", "A1", "A2", "A3", "A4")},
    }
    return [
        {"id": key, "agg": aggs[key], "description": text[key]}
        for key in categories
    ]


def rubric(item: dict[str, Any], language: str) -> dict[str, Any]:
    requirements = requirement_set(item, language)
    return {
        "score_formula": (
            "BUILD * (0.15*((M1+M2+M3)/3) + 0.35*((D1+D2+D3+D4)/4) + "
            "0.15*((V1+V2+V3)/3) + 0.35*((A1+A2+A3+A4)/4))"
        ),
        "max_demos": 10,
        "max_demo_seconds": 20,
        "build_check": {
            "id": "BUILD",
            "cmd": "momozi HTML static BUILD gate",
            "description": (
                "index.html and game_logic.js exist, a canvas/WebGL/WebGPU renderer "
                "signal is present, and no disallowed heavy runtime asset references are used."
            ),
        },
        "categories": [
            {"name": "Core Mechanics", "items": RUBRIC_MAPPING["completeness"]},
            {"name": "Content Depth", "items": RUBRIC_MAPPING["richness"]},
            {"name": "Functional Visuals", "items": RUBRIC_MAPPING["player_exp"]},
            {"name": "Presentation & Art", "items": RUBRIC_MAPPING["visual"]},
        ],
        "requirements": requirements,
    }


def task_yaml(item: dict[str, Any], language: str, prompt: str) -> dict[str, Any]:
    base_id = item["base_id"]
    task_id = f"{base_id}-{language}"
    difficulty_prompt = prompt_for(item, "en")
    return {
        "id": task_id,
        "title": f'{item[f"title_{language}"]}{LANGUAGE_SUFFIX[language]}',
        "family": item["family"],
        "difficulty": classify_difficulty(item["family"], difficulty_prompt),
        "engine": "html",
        "language": language,
        "base_task_id": base_id,
        "provenance": {
            "kind": item["provenance_kind"],
            "source_name": "Feishu Prompt Catalog",
            "source_workbook_url": SOURCE_WORKBOOK_URL,
            "source_workbook_token": SOURCE_WORKBOOK_TOKEN,
            "source_sheet_id": item["source_sheet_id"],
            "source_sheet_name": item["source_sheet_name"],
            "source_index": item["source_index"],
            "source_capture_date": SOURCE_CAPTURE_DATE,
            "source_snapshot_sha256": item["source_snapshot_sha256"],
            "source_prompt_kind": item["source_prompt_kind"],
            "source_title": item["title_zh"],
            "source_title_en": item["title_en"],
            "source_technology": item["technology"],
            "adaptation": (
                "Vibe Gaming wrapper preserving source mechanics and technical intent; "
                "adds deterministic state-machine, UX, testing, and clean-room requirements."
            ),
        },
        "rounds": [{"name": "R1", "spec": prompt}],
        "static": [
            {"kind": "required_file", "role": "entry", "path": "index.html", "weight": 1.0},
            {"kind": "required_file", "role": "logic", "path": "game_logic.js", "weight": 1.0},
        ],
        "behavior": {"script": "beh_html.mjs", "timeout": 300},
        "evaluation": {
            "input_scheme": input_scheme_for_family(item["family"]),
            "start_keys": ["Enter", "Space"],
        },
        "rubric": [
            {
                "id": "completeness",
                "weight": 0.15,
                "max": 5,
                "anchors": RUBRIC_MAPPING["completeness"],
                "rubric": "Core requested mechanics are implemented and connected.",
            },
            {
                "id": "richness",
                "weight": 0.35,
                "max": 5,
                "anchors": RUBRIC_MAPPING["richness"],
                "rubric": "Content depth, progression, persistence, and meaningful choices.",
            },
            {
                "id": "player_exp",
                "weight": 0.15,
                "max": 5,
                "anchors": RUBRIC_MAPPING["player_exp"],
                "rubric": "Readable state, responsive feedback, and complete loop.",
            },
            {
                "id": "visual",
                "weight": 0.35,
                "max": 5,
                "anchors": RUBRIC_MAPPING["visual"],
                "rubric": "Coherent authored presentation, composition, effects, and motion.",
            },
        ],
    }


def _render_files(item: dict[str, Any], language: str) -> dict[str, str]:
    prompt = prompt_for(item, language)
    task_id = f"{item['base_id']}-{language}"
    yaml_text = yaml.dump(
        task_yaml(item, language, prompt),
        Dumper=LiteralDumper,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    )
    return {
        f"{task_id}.task.yaml": yaml_text,
        "prompt.md": f"{prompt}\n",
        "rubric.mapping.json": json.dumps(RUBRIC_MAPPING, ensure_ascii=False, indent=2) + "\n",
        "rubric.original.json": json.dumps(
            rubric(item, language), ensure_ascii=False, indent=2
        )
        + "\n",
    }


def load_rows(path: Path, kind: str) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    sheet = payload.get("sheets", [{}])[0]
    rows = [
        row
        for row in sheet.get("data", [])
        if isinstance(row, list) and any(value not in (None, "") for value in row)
    ]
    output = []
    for row in rows:
        if kind == "structured":
            if len(row) < 4 or not row[0] or not row[1]:
                continue
            full_prompt = clean_text(row[4]) if len(row) > 4 else ""
            output.append(
                {
                    "source_index": int(row[0]),
                    "title_zh": clean_text(row[1]),
                    "title_en": clean_text(row[2]),
                    "technology": normalize_technology(clean_text(row[3])),
                    "technology_zh": normalize_technology(clean_text(row[3])),
                    "source_prompt": full_prompt,
                    "source_prompt_kind": (
                        "full_prompt" if full_prompt else "structured_seed"
                    ),
                }
            )
        else:
            if len(row) < 4 or not row[0] or not row[1] or not row[3]:
                continue
            output.append(
                {
                    "source_index": int(row[0]),
                    "title_zh": clean_text(row[1]),
                    "title_en": "",
                    "technology": normalize_technology(clean_text(row[2])),
                    "technology_zh": normalize_technology(clean_text(row[2])),
                    "source_prompt": clean_text(row[3]),
                    "source_prompt_kind": "full_prompt",
                }
            )
    return output


def import_manifest(
    direct1_path: Path,
    generated_path: Path,
    translate: bool,
    translations_path: Path | None = None,
) -> dict[str, Any]:
    rows = []
    structured = load_rows(direct1_path, "structured")
    generated = load_rows(generated_path, "generated")
    if len(structured) != 100:
        raise ValueError(f"直接1 expected 100 rows, found {len(structured)}")
    if len(generated) != 120:
        raise ValueError(f"直接生成 expected 120 rows, found {len(generated)}")
    source_hashes = {
        "direct1": sha256(direct1_path),
        "direct_generated": sha256(generated_path),
    }
    translation_texts: list[str] = []
    for row in structured + generated:
        translation_texts.append(row["title_zh"])
        if row["source_prompt"]:
            translation_texts.append(row["source_prompt"])
        else:
            translation_texts.append(
                seed_brief_zh(row["title_zh"], row["title_en"], row["technology"])
            )
    translation_cache: dict[str, str] = {}
    if translations_path:
        translation_cache.update(
            json.loads(translations_path.read_text(encoding="utf-8"))
        )
    elif translate:
        translation_cache = translate_batch(translation_texts)
    has_translations = bool(translation_cache)
    for category, rowset, sheet_key in (
        ("structured", structured, "structured"),
        ("generated", generated, "generated"),
    ):
        for row in rowset:
            if not row["source_prompt"]:
                row["source_prompt"] = seed_brief_zh(
                    row["title_zh"], row["title_en"], row["technology"]
                )
            if not row["title_en"]:
                row["title_en"] = (
                    translation_cache.get(row["title_zh"])
                    or (f"Feishu Game {row['source_index']}")
                )
            row["brief_zh"] = row["source_prompt"]
            row["technology_en"] = translation_cache.get(row["technology_zh"], row["technology_zh"])
            row["brief_en"] = (
                translation_cache.get(row["brief_zh"], row["brief_zh"])
            )
            row["title_en"] = (
                translation_cache.get(row["title_zh"], row["title_en"])
            )
            row["family"] = family_for(
                row["title_zh"], row["title_en"], row["technology"], row["source_prompt"]
            )
            row["dimension"] = dimension_for(
                row["title_zh"], row["title_en"], row["technology"], row["source_prompt"]
            )
            row["base_id"] = f"mz_feishu-{category}-{row['source_index']:03d}"
            row["provenance_kind"] = (
                "adapted_feishu_game_prompt"
                if row["source_prompt_kind"] == "full_prompt"
                else "structured_feishu_game_seed"
            )
            row["source_sheet_id"] = SOURCE_SHEETS[sheet_key]["id"]
            row["source_sheet_name"] = SOURCE_SHEETS[sheet_key]["name"]
            row["source_snapshot_sha256"] = source_hashes[
                "direct1" if category == "structured" else "direct_generated"
            ]
            rows.append(row)

    return {
        "schema_version": 1,
        "source_name": "Feishu Prompt Catalog",
        "source_workbook_url": SOURCE_WORKBOOK_URL,
        "source_workbook_token": SOURCE_WORKBOOK_TOKEN,
        "source_capture_date": SOURCE_CAPTURE_DATE,
        "source_hashes": source_hashes,
        "sheet_counts": {"直接1": 100, "直接生成": 120},
        "concept_count": len(rows),
        "note": (
            "Both 直接1 and 直接生成 contain a full prompt column in the source snapshot. "
            "The importer preserves those prompts as immutable gameplay evidence; if a future "
            "snapshot omits a 直接1 prompt column, it falls back to an explicitly labeled "
            "structured seed enrichment instead of fabricating a full source prompt."
        ),
        "items": rows,
    }


def write_manifest(manifest: dict[str, Any]) -> None:
    SOURCES_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def validate_manifest(manifest: dict[str, Any]) -> None:
    items = manifest.get("items", [])
    if len(items) != 220:
        raise ValueError(f"manifest expected 220 concepts, found {len(items)}")
    ids = [item["base_id"] for item in items]
    if len(set(ids)) != len(ids):
        raise ValueError("manifest has duplicate base_id")
    for item in items:
        for field in (
            "title_zh",
            "title_en",
            "technology",
            "brief_zh",
            "brief_en",
            "family",
            "dimension",
            "base_id",
            "source_sheet_id",
            "source_index",
        ):
            if not item.get(field):
                raise ValueError(f"{item.get('base_id')}: missing {field}")


def write_tasks(manifest: dict[str, Any], write: bool) -> tuple[int, int]:
    validate_manifest(manifest)
    created = 0
    validated = 0
    for item in manifest["items"]:
        for language in ("en", "zh"):
            task_id = f"{item['base_id']}-{language}"
            task_dir = TASKS_ROOT / task_id
            expected = _render_files(item, language)
            if not task_dir.exists():
                if not write:
                    raise FileNotFoundError(
                        f"{task_dir} missing; rerun with --write to generate tasks"
                    )
                task_dir.mkdir(parents=True)
                created += 1
            if write:
                for name, content in expected.items():
                    (task_dir / name).write_text(content, encoding="utf-8")
            actual = {path.name for path in task_dir.iterdir() if path.is_file()}
            if actual != set(expected):
                raise ValueError(
                    f"{task_dir}: expected {sorted(expected)}, found {sorted(actual)}"
                )
            for name, content in expected.items():
                if (task_dir / name).read_text(encoding="utf-8") != content:
                    raise ValueError(f"{task_dir / name}: differs from manifest")
            validated += 1
    return created, validated


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct1", type=Path, help="table-get JSON for 直接1")
    parser.add_argument("--direct-generated", type=Path, help="table-get JSON for 直接生成")
    parser.add_argument("--import", dest="do_import", action="store_true")
    parser.add_argument(
        "--translate",
        action="store_true",
        help="translate Chinese briefs/titles to English during import",
    )
    parser.add_argument(
        "--translations",
        type=Path,
        help="precomputed JSON mapping of Chinese text to English text",
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    if args.do_import:
        if not args.direct1 or not args.direct_generated:
            parser.error("--import requires --direct1 and --direct-generated")
        manifest = import_manifest(
            args.direct1,
            args.direct_generated,
            args.translate,
            args.translations,
        )
        write_manifest(manifest)
        print(f"wrote {MANIFEST_PATH}: {manifest['concept_count']} concepts")
    elif not MANIFEST_PATH.exists():
        parser.error(f"{MANIFEST_PATH} missing; run with --import first")
    else:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    created, validated = write_tasks(manifest, args.write)
    print(
        f"Feishu tasks valid: {len(manifest['items'])} concepts x 2 languages = "
        f"{validated} tasks; created={created}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
