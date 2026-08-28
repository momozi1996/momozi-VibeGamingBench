"""Generate bilingual benchmark tasks adapted from Summer Engine templates.

The public template crawl is reduced to a compact mechanic-signature manifest:
source identity, URL, page hash, category, presentation format, four primary
mechanics, and the recommended system names. Long-form site copy and media are
not vendored into this repository.

Typical maintenance flow:

1. Import a fresh full crawl while preserving reviewed Chinese translations:
   ``python3 scripts/add_summerengine_tasks.py --import-crawl /tmp/catalog.json``
2. Review the title and mechanic translations in
   ``bench/sources/summerengine_core_zh.json``.
3. Generate or refresh the 314 task directories:
   ``python3 scripts/add_summerengine_tasks.py --write``
4. Run without flags to verify that every generated file is reproducible.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from task_metadata import classify_difficulty


ROOT = Path(__file__).resolve().parent.parent
TASKS_ROOT = ROOT / "bench" / "tasks"
SOURCES_ROOT = ROOT / "bench" / "sources"
MANIFEST_PATH = SOURCES_ROOT / "summerengine_templates.json"
CORE_ZH_PATH = SOURCES_ROOT / "summerengine_core_zh.json"
SOURCE_INDEX_URL = "https://www.summerengine.com/templates"
SOURCE_CAPTURE_DATE = "2026-08-28"
EXPECTED_TEMPLATES = 157
EXPECTED_CATEGORY_COUNTS = {
    "action-fighting": 13,
    "adventure": 10,
    "arcade": 2,
    "horror": 15,
    "narrative": 9,
    "platformer": 11,
    "puzzle": 9,
    "racing-sports": 13,
    "rpg": 19,
    "shooter": 12,
    "simulation": 18,
    "strategy": 14,
    "survival": 12,
}
LANGUAGE_SUFFIX = {"en": " (English)", "zh": " (中文)"}
CATEGORY_LABELS = {
    "action-fighting": {
        "en": "action and fighting",
        "zh": "动作与战斗",
        "family": "action",
    },
    "adventure": {"en": "adventure and exploration", "zh": "冒险与探索", "family": "adventure"},
    "arcade": {"en": "arcade and casual", "zh": "街机与休闲", "family": "arcade"},
    "horror": {"en": "horror", "zh": "恐怖", "family": "horror"},
    "narrative": {"en": "narrative", "zh": "叙事", "family": "narrative"},
    "platformer": {"en": "platformer", "zh": "平台跳跃", "family": "platformer"},
    "puzzle": {"en": "puzzle", "zh": "解谜", "family": "puzzle"},
    "racing-sports": {"en": "racing and sports", "zh": "赛车与体育", "family": "racing"},
    "rpg": {"en": "role-playing", "zh": "角色扮演", "family": "rpg"},
    "shooter": {"en": "shooter", "zh": "射击", "family": "shooter"},
    "simulation": {"en": "simulation", "zh": "模拟经营", "family": "simulation"},
    "strategy": {"en": "strategy", "zh": "策略", "family": "strategy"},
    "survival": {"en": "survival and crafting", "zh": "生存与制造", "family": "survival"},
}
PERSPECTIVE_ZH = {
    "first-person": "第一人称",
    "first-person with third-person toggle": "可切换第三人称的第一人称",
    "front-facing": "正面视角",
    "isometric": "等距视角",
    "side-on": "侧视角",
    "side-scrolling": "横向卷轴视角",
    "side-view": "侧视角",
    "text-based": "文本界面",
    "third-person": "第三人称",
    "top-down": "俯视角",
}
DIMENSION_ZH = {"2D": "2D", "2.5D": "2.5D", "3D": "3D"}

# These source templates are explicitly named after commercial games. Their
# benchmark-facing IDs and titles are replaced with original, mechanic-led names.
ORIGINAL_IDENTITIES = {
    "dark-souls-style": ("gravefire-action-rpg", "Gravefire Pilgrim"),
    "elden-ring-style": ("shattered-realm-action-rpg", "Shattered Realm Pilgrimage"),
    "soulslike": ("sanctuary-cycle-action-rpg", "Sanctuary Cycle"),
    "celeste-style": ("summit-dash", "Summit Dash"),
    "hollow-knight-style": ("hollow-realm-metroidvania", "Hollow Realm Seeker"),
    "metroidvania": ("ability-gated-exploration", "Ability-Gated Exploration"),
    "amnesia-style": ("lantern-sanity-horror", "Lantern of Dread"),
    "dead-space-style": ("derelict-dismemberment-horror", "Derelict Dismemberment"),
    "outlast-style": ("night-vision-escape-horror", "Night-Vision Escape"),
    "resident-evil-style": ("mansion-survival-horror", "Mansion Survival Protocol"),
    "silent-hill-style": ("fogbound-psychological-horror", "Fogbound Guilt"),
    "diablo-style": ("infernal-loot-action-rpg", "Infernal Loot Hunt"),
    "final-fantasy-style": ("crystal-party-rpg", "Crystalbound Party Quest"),
    "hades-style": ("underworld-escape-roguelite", "Underworld Escape"),
    "monster-hunter-style": ("colossal-quarry-action-rpg", "Colossal Quarry"),
    "persona-style": ("calendar-bonds-rpg", "Calendar Bonds"),
    "pokemon-style": ("creature-league-rpg", "Creature League"),
    "skyrim-style": ("open-realm-dragon-rpg", "Open-Realm Dragon Quest"),
    "undertale-style": ("mercy-bullet-story-rpg", "Mercy Under Fire"),
    "animal-crossing-life-style": ("island-neighbors-life-sim", "Island Neighbors"),
    "harvest-moon-style": ("seasonal-homestead-sim", "Seasonal Homestead"),
    "stardew-valley-style": ("valley-farm-friendship-sim", "Valley Farm and Friendship"),
    "the-sims-style": ("household-life-sandbox", "Household Life Sandbox"),
    "balatro-style": ("wildcard-poker-deckbuilder", "Wildcard Poker Deckbuilder"),
    "civilization-style": ("hex-era-empire-strategy", "Hex-Era Empire"),
    "factorio-style": ("automated-belt-factory", "Automated Belt Factory"),
    "slay-the-spire-style": ("spirebound-combat-deckbuilder", "Spirebound Deck Expedition"),
    "minecraft-style": ("infinite-voxel-survival", "Infinite Voxel Survival"),
    "terraria-style": ("layered-2d-crafting-sandbox", "Layered Crafting Frontier"),
    "sokoban": ("crate-grid-puzzle", "Crate Grid Puzzle"),
    "musou": ("army-sweeper", "Army Sweeper"),
}

DEBRAND_REPLACEMENTS = {
    "Animal Crossing": "Island Neighbors",
    "Balatro": "Wildcard Poker",
    "Biter": "Pollution Creature",
    "Biters": "Pollution Creatures",
    "Bonfire": "Sanctuary",
    "B-side cassette tapes": "challenge tapes",
    "B-side": "challenge-side",
    "Celeste": "Summit Dash",
    "Civilization": "Hex-Era Empire",
    "Dark Souls": "Gravefire",
    "Dead Space": "Derelict Dismemberment",
    "Diablo": "Infernal Loot Hunt",
    "Elden Ring": "Shattered Realm",
    "Estus flask": "refillable healing flask",
    "Factorio": "Automated Belt Factory",
    "Final Fantasy": "Crystalbound Party Quest",
    "Hades": "Underworld Escape",
    "Harvest Moon": "Seasonal Homestead",
    "Hollow Knight": "Hollow Realm Seeker",
    "Gym badge": "league emblem",
    "Gym leader": "league captain",
    "Elite Four": "final league council",
    "Limit break": "crisis ultimate",
    "Marika": "the waystone",
    "Materia": "socketed spell crystal",
    "Minecraft": "Infinite Voxel Survival",
    "Monster Hunter": "Colossal Quarry",
    "Musou gauge": "army-break gauge",
    "musou system": "army-break system",
    "Nether and End": "infernal and void",
    "nail combat": "blade combat",
    "Outlast": "Night-Vision Escape",
    "Persona": "Calendar Bonds",
    "Pokemon": "Creature League",
    "Pokémon": "Creature League",
    "Pokédex": "creature catalog",
    "Pokedex": "creature catalog",
    "PP system": "skill-charge system",
    "Redstone-style": "logic-wire",
    "Resident Evil": "Mansion Survival Protocol",
    "Silent Hill": "Fogbound Guilt",
    "Skyrim": "Open-Realm Dragon Quest",
    "Slay the Spire": "Spirebound Deck Expedition",
    "Soul/rune": "lost",
    "Soul currency": "lost currency",
    "Soul meter": "focus meter",
    "Corpse-run Shade": "corpse-run hostile ghost",
    "Spirit ash": "summoned companion",
    "Stake of the waystone": "nearby retry shrine",
    "Stardew Valley": "Valley Farm and Friendship",
    "Terraria": "Layered Crafting Frontier",
    "The Sims": "Household Life Sandbox",
    "Undertale": "Mercy Under Fire",
    "Witch Time": "last-frame dodge slowdown",
    "ATB": "active-time turn gauge",
    "bonfires": "sanctuaries",
    "bonfire": "sanctuary",
    "Estus": "healing flask",
    "HMs": "field-skill manuals",
    "HM use": "field-skill use",
    "PC box": "creature storage",
    "Site of grace": "field sanctuary",
    "sites of grace": "field sanctuaries",
    "TMs": "skill manuals",
    "TM/HM": "skill and field-skill manuals",
    "STAB": "same-type",
    "multiple sims": "multiple household members",
    "Rune currency": "lost currency",
}
BANNED_GENERATED_TERMS = (
    "animal crossing",
    "balatro",
    "celeste",
    "dark souls",
    "dead space",
    "diablo",
    "elden ring",
    "factorio",
    "final fantasy",
    "hades",
    "harvest moon",
    "hollow knight",
    "marika",
    "minecraft",
    "monster hunter",
    "outlast",
    "persona",
    "pokemon",
    "pokémon",
    "resident evil",
    "silent hill",
    "skyrim",
    "slay the spire",
    "stardew valley",
    "terraria",
    "the sims",
    "undertale",
)

ART_DIRECTION = {
    "action-fighting": {
        "en": "Bold combat silhouettes, readable hit flashes, strong anticipation poses, impact particles, and arenas whose hazards remain legible during fast motion.",
        "zh": "采用鲜明战斗轮廓、清晰命中特效、明确的动作预备姿态与冲击粒子；高速运动中仍能读懂场地危险。",
    },
    "adventure": {
        "en": "Authored landmarks, layered routes, environmental storytelling, clear interaction highlights, and lighting that guides exploration without flattening the scene.",
        "zh": "使用可辨识地标、分层路线、环境叙事与明确交互高亮；灯光应引导探索，同时保留场景层次。",
    },
    "arcade": {
        "en": "Immediate arcade readability, energetic motion, saturated accents against a restrained background, and celebratory score and combo feedback.",
        "zh": "强调即时街机可读性、充满动势的动画、克制背景上的高饱和强调色，以及有庆祝感的分数与连击反馈。",
    },
    "horror": {
        "en": "Controlled darkness, purposeful negative space, unsettling material contrast, spatial audio cues, and restrained effects that preserve threat readability.",
        "zh": "控制黑暗与留白，使用令人不安的材质反差、空间音频线索和克制特效，同时保证威胁仍可辨认。",
    },
    "narrative": {
        "en": "Character-focused staging, expressive portraits or models, legible dialogue hierarchy, motivated transitions, and scene composition that changes with relationships and choices.",
        "zh": "以角色为中心安排镜头与舞台，使用有表现力的肖像或模型、清晰对话层级和有动机的转场；构图随关系与选择变化。",
    },
    "platformer": {
        "en": "Crisp player and hazard silhouettes, stable depth separation, readable landing surfaces, motion trails, and responsive squash, stretch, and impact effects.",
        "zh": "玩家与危险物轮廓清晰，景深层级稳定，落脚面容易判断，并使用运动轨迹、挤压拉伸与冲击反馈增强手感。",
    },
    "puzzle": {
        "en": "A calm, precise visual language with distinct state colors, clean spatial grouping, smooth transformations, and no decorative element that obscures puzzle information.",
        "zh": "采用冷静精确的视觉语言、可区分的状态色、清楚的空间分组和平滑变换；装饰不得遮挡谜题信息。",
    },
    "racing-sports": {
        "en": "Strong speed and trajectory cues, readable competitors, clear field markings, dynamic cameras, and replay-worthy finish, collision, and scoring moments.",
        "zh": "突出速度与轨迹提示、可辨识对手和清晰场地标记，并使用动态镜头呈现值得回放的冲线、碰撞与得分瞬间。",
    },
    "rpg": {
        "en": "A cohesive world identity, readable party and enemy roles, expressive abilities, layered locations, and progression changes that are visible on characters and equipment.",
        "zh": "建立统一世界观、清晰队伍与敌人定位、富有表现力的技能和分层地点；成长变化应在角色与装备上可见。",
    },
    "shooter": {
        "en": "Readable targets and projectiles, disciplined muzzle and impact effects, strong cover silhouettes, useful depth cues, and camera treatment that supports aiming.",
        "zh": "目标与弹道必须清晰，枪口和命中特效保持克制，掩体轮廓明确，景深提示有效，镜头反馈服务于瞄准。",
    },
    "simulation": {
        "en": "A coherent operational world with legible machines and actors, animated flows, state-driven color changes, and dense but organized management information.",
        "zh": "构建连贯的运营世界，让机器和角色易于辨识；通过流动动画与状态驱动配色展示变化，管理信息紧凑但有序。",
    },
    "strategy": {
        "en": "A scan-friendly tactical field, distinct unit roles, visible ranges and ownership, restrained effects, and information hierarchy that supports repeated decisions.",
        "zh": "战术场地应便于扫视，单位定位、范围和归属清楚；特效保持克制，信息层级支持玩家连续决策。",
    },
    "survival": {
        "en": "Tactile resources and tools, readable environmental danger, weather and time changes, visible wear and construction stages, and a world that records player intervention.",
        "zh": "资源与工具要有触感，环境危险清晰，天气和时间变化明确；磨损、建造阶段及玩家对世界的改造都应可见。",
    },
}

CONTENT_REQUIREMENT = {
    "action-fighting": {
        "en": "Include at least three opponents or fighter archetypes, escalating encounters, defensive and offensive choices, and a final match or boss with victory, defeat, and rematch states.",
        "zh": "至少加入三种对手或战斗定位、逐步升级的遭遇、攻防选择，以及带胜利、失败和重赛状态的最终对局或首领战。",
    },
    "adventure": {
        "en": "Build at least three connected locations with distinct discoveries, one optional route, an escalating objective chain, and a final resolution changed by player actions.",
        "zh": "制作至少三个相连地点，提供不同发现、一条可选路线、逐步升级的目标链，以及会被玩家行动改变的最终结果。",
    },
    "arcade": {
        "en": "Provide a short session with escalating pace, score and combo logic, at least three challenge patterns, a high-score result, and an immediate replay flow.",
        "zh": "提供节奏不断加快的短局体验，包含分数与连击逻辑、至少三种挑战模式、最高分结算和立即重玩的流程。",
    },
    "horror": {
        "en": "Create at least three connected threat spaces, escalating pressure, limited safety or resources, a learnable antagonist pattern, and complete escape, survival, or failure outcomes.",
        "zh": "制作至少三个相连的威胁空间、逐步增强的压力、有限安全区或资源、可学习的敌对行为，以及完整逃生、生还或失败结局。",
    },
    "narrative": {
        "en": "Include at least three consequential decision points, persistent relationship or evidence state, visibly different branches, and two reachable endings with replay navigation.",
        "zh": "至少加入三个会产生后果的决策点、持续保存的关系或证据状态、明显不同的分支，以及两个可到达结局和重玩导航。",
    },
    "platformer": {
        "en": "Create at least three authored challenge sections, checkpoints, escalating combinations of movement and hazards, collectibles or optional mastery routes, and a finish and retry loop.",
        "zh": "制作至少三个经过设计的挑战段落、检查点、逐步组合的移动与危险、收集物或高难可选路线，以及完整终点与重试闭环。",
    },
    "puzzle": {
        "en": "Provide at least six authored puzzles across three mechanic combinations, enforce valid and invalid states, include reset and undo or hint support, and end with a synthesis puzzle.",
        "zh": "至少提供六个手工谜题，覆盖三种机制组合；必须判定有效与无效状态，提供重置及撤销或提示，并以综合谜题收束。",
    },
    "racing-sports": {
        "en": "Include a complete event with practice or setup, at least three competitors or challenge tiers, rule-valid scoring, escalating pressure, final standings, and replay.",
        "zh": "加入完整赛事流程，包括练习或准备、至少三名对手或三个挑战等级、符合规则的计分、递增压力、最终排名和重玩。",
    },
    "rpg": {
        "en": "Include at least three encounter types, meaningful build or party choices, resources and status effects, progression between encounters, and a final objective with more than one viable strategy.",
        "zh": "至少加入三种遭遇、有意义的构筑或队伍选择、资源与状态效果、遭遇间成长，以及可用多种策略完成的最终目标。",
    },
    "shooter": {
        "en": "Provide at least three enemy archetypes, weapon or ability tradeoffs, escalating waves or spaces, readable damage and ammunition state, and a final objective with victory, defeat, and retry.",
        "zh": "至少加入三种敌人、武器或能力取舍、逐步升级的波次或空间、清晰伤害与弹药状态，以及带胜负和重试的最终目标。",
    },
    "simulation": {
        "en": "Simulate at least three interacting actor or resource types, expose cause and effect, add escalating demand or incidents, and provide measurable success, failure, and restart states.",
        "zh": "至少模拟三类互相影响的角色或资源，明确展示因果关系，加入不断升级的需求或事件，并提供可量化的成功、失败与重开状态。",
    },
    "strategy": {
        "en": "Include at least three unit, card, building, or policy roles, an opposing system that reacts to the player, resource tradeoffs, escalating scenarios, and a complete win/loss loop.",
        "zh": "至少加入三种单位、卡牌、建筑或政策定位，一个会响应玩家的对抗系统、资源取舍、逐步升级的局势，以及完整胜负闭环。",
    },
    "survival": {
        "en": "Include at least three resource or threat types, crafting or construction decisions, escalating environmental pressure, persistent world changes, and complete survive/fail/retry outcomes.",
        "zh": "至少加入三种资源或威胁、制造或建造决策、不断增强的环境压力、持续世界变化，以及完整生还、失败和重试结果。",
    },
}

SUPPORTING_ZH = {
    "action-fighting": [
        "输入缓冲与动作取消",
        "命中、受击与无敌帧判定",
        "敌人状态机与难度升级",
        "锁定目标与战斗镜头",
        "资源槽与冷却",
        "装备或招式升级",
        "训练或挑战模式",
        "胜负结算与重赛",
    ],
    "adventure": [
        "地图探索与区域解锁",
        "任务日志与目标追踪",
        "可交互物体与工具",
        "NPC 对话和条件分支",
        "收集物与秘密区域",
        "检查点与快速移动",
        "环境谜题",
        "行动后果与结局",
    ],
    "arcade": [
        "分数与倍率",
        "连击与精度",
        "逐级加速的难度",
        "道具或临时强化",
        "即时视听反馈",
        "最高分记录",
        "短局目标",
        "快速重开",
    ],
    "horror": [
        "有限光源或关键资源",
        "巡逻、调查与追逐状态",
        "躲藏与噪声传播",
        "环境叙事与线索",
        "理智、恐惧或感染状态",
        "安全区与检查点",
        "动态音频威胁提示",
        "多种生还或失败结果",
    ],
    "narrative": [
        "条件对话与历史记录",
        "关系、信任或证据变量",
        "章节和场景切换",
        "选择后果持久化",
        "路线锁定与解锁",
        "可读的角色状态",
        "存档与章节重玩",
        "多个可到达结局",
    ],
    "platformer": [
        "土狼时间与输入缓冲",
        "检查点与快速重生",
        "移动平台和动态危险",
        "收集物与可选路线",
        "敌人或首领模式",
        "能力解锁",
        "关卡完成度追踪",
        "计时或挑战重放",
    ],
    "puzzle": [
        "有效与无效状态判定",
        "撤销和重置",
        "分级提示",
        "关卡选择",
        "逐步叠加机制",
        "完成度与最佳成绩",
        "交互状态高亮",
        "综合终局谜题",
    ],
    "racing-sports": [
        "符合项目规则的计分",
        "对手 AI 与难度等级",
        "练习或赛前设置",
        "体力、速度或能量管理",
        "碰撞与犯规判定",
        "赛事进度和排名",
        "回放或幽灵数据",
        "比赛结算与重赛",
    ],
    "rpg": [
        "角色属性与成长",
        "装备、技能或牌组构筑",
        "任务与世界状态",
        "敌人弱点与状态效果",
        "资源和物品经济",
        "同伴、派系或关系",
        "检查点与地图推进",
        "首领战与分支结果",
    ],
    "shooter": [
        "瞄准、射击与命中判定",
        "弹药、装填或冷却",
        "多种敌人行为",
        "武器或能力配置",
        "掩体、移动或闪避",
        "伤害与危险反馈",
        "波次或目标推进",
        "胜负结算与重试",
    ],
    "simulation": [
        "资源生产与消耗",
        "角色、机器或设施状态",
        "供需与价格变化",
        "任务队列和优先级",
        "突发事件与故障",
        "升级和研究",
        "统计图表与预测",
        "可量化的经营结果",
    ],
    "strategy": [
        "资源与行动经济",
        "单位、卡牌或建筑克制",
        "地图控制与视野",
        "对手 AI 决策",
        "升级或科技路线",
        "明确的范围和预览",
        "多阶段局势升级",
        "完整胜负条件",
    ],
    "survival": [
        "采集与物品栏",
        "制作和建造",
        "饥饿、温度或生命维持",
        "昼夜、天气或区域危险",
        "工具耐久与修理",
        "敌对生物或袭击",
        "持久世界改造",
        "生还、失败与重试",
    ],
}

RUBRIC_MAPPING = {
    "completeness": ["M1", "M2", "M3"],
    "richness": ["D1", "D2", "D3", "D4"],
    "player_exp": ["V1", "V2", "V3"],
    "visual": ["A1", "A2", "A3", "A4"],
}


class LiteralDumper(yaml.SafeDumper):
    """Render multiline strings as YAML block scalars."""


def _represent_str(dumper: yaml.Dumper, value: str):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


LiteralDumper.add_representer(str, _represent_str)


def _clean_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _debrand(value: str) -> str:
    result = _clean_space(value)
    for source, replacement in sorted(
        DEBRAND_REPLACEMENTS.items(), key=lambda pair: len(pair[0]), reverse=True
    ):
        pattern = rf"(?<![\w]){re.escape(source)}(?![\w])"
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    result = re.sub(r"\bstyle\b", "inspired", result, flags=re.IGNORECASE)
    result = re.sub(r"\s+", " ", result).strip()
    return result


def _validate_no_ip(value: str, context: str) -> None:
    found = [
        term
        for term in BANNED_GENERATED_TERMS
        if re.search(rf"(?<![\w]){re.escape(term)}(?![\w])", value, flags=re.IGNORECASE)
    ]
    if found:
        raise ValueError(f"{context}: generated text still contains branded terms {found}")


def _identity(template: dict[str, Any]) -> tuple[str, str]:
    source_slug = template["slug"]
    if source_slug in ORIGINAL_IDENTITIES:
        return ORIGINAL_IDENTITIES[source_slug]
    return source_slug, _debrand(template["title"])


def _load_core_zh() -> dict[str, list[str]]:
    raw = json.loads(CORE_ZH_PATH.read_text(encoding="utf-8"))
    if len(raw) != EXPECTED_TEMPLATES:
        raise ValueError(
            f"{CORE_ZH_PATH}: expected {EXPECTED_TEMPLATES} translations, found {len(raw)}"
        )
    for source_id, values in raw.items():
        if len(values) != 5 or not all(isinstance(value, str) and value for value in values):
            raise ValueError(f"{CORE_ZH_PATH}: {source_id} must contain title plus four mechanics")
    return raw


def _import_crawl(crawl_path: Path) -> None:
    source = json.loads(crawl_path.read_text(encoding="utf-8"))
    items = source if isinstance(source, list) else source.get("templates", source.get("items"))
    if not isinstance(items, list):
        raise ValueError(f"{crawl_path}: expected a template list")
    translations = _load_core_zh()
    compact: list[dict[str, Any]] = []

    for record in items:
        template = record["template"]
        source_id = template["id"]
        slug, title_en = _identity(template)
        onboarding = template.get("onboardingContext") or {}
        features_en = [_debrand(feature["title"]) for feature in template.get("features", [])]
        systems_en = [_debrand(value) for value in onboarding.get("recommendedSystems", [])]
        if source_id not in translations:
            raise ValueError(f"{source_id}: missing reviewed Chinese core translation")
        title_zh, *mechanics_zh = translations[source_id]
        entry = {
            "source_id": source_id,
            "source_slug": template["slug"],
            "source_title": template["title"],
            "source_url": record["url"],
            "html_sha256": record["html_sha256"],
            "category": template["categorySlug"],
            "category_label": template["categoryLabel"],
            "dimension": template["dimension"],
            "perspective": template["perspective"],
            "task_slug": slug,
            "title_en": title_en,
            "title_zh": title_zh,
            "mechanics_en": features_en,
            "mechanics_zh": mechanics_zh,
            "supporting_systems_en": systems_en,
        }
        for field in ("title_en", "mechanics_en", "supporting_systems_en"):
            values = entry[field] if isinstance(entry[field], list) else [entry[field]]
            for index, value in enumerate(values):
                _validate_no_ip(value, f"{source_id}.{field}[{index}]")
        compact.append(entry)

    compact.sort(key=lambda item: (item["category"], item["task_slug"]))
    counts = Counter(item["category"] for item in compact)
    if len(compact) != EXPECTED_TEMPLATES:
        raise ValueError(f"expected {EXPECTED_TEMPLATES} templates, found {len(compact)}")
    if dict(sorted(counts.items())) != EXPECTED_CATEGORY_COUNTS:
        raise ValueError(f"unexpected category counts: {dict(sorted(counts.items()))}")
    task_ids = [f"mz_summer-{item['category']}-{item['task_slug']}" for item in compact]
    if len(task_ids) != len(set(task_ids)):
        duplicates = [task_id for task_id, count in Counter(task_ids).items() if count > 1]
        raise ValueError(f"duplicate generated task IDs: {duplicates}")

    crawl_sha256 = hashlib.sha256(crawl_path.read_bytes()).hexdigest()
    payload = {
        "schema_version": 1,
        "source_index_url": SOURCE_INDEX_URL,
        "source_capture_date": SOURCE_CAPTURE_DATE,
        "source_catalog_sha256": crawl_sha256,
        "template_count": len(compact),
        "category_counts": EXPECTED_CATEGORY_COUNTS,
        "note": (
            "Compact provenance and mechanic signatures derived from the public template pages. "
            "Long-form page copy, images, and suggested prompts are intentionally not vendored."
        ),
        "templates": compact,
    }
    SOURCES_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"imported {len(compact)} compact template records into {MANIFEST_PATH}")


def _load_manifest(require_translations: bool = True) -> dict[str, Any]:
    raw = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    templates = raw.get("templates", [])
    if raw.get("template_count") != EXPECTED_TEMPLATES or len(templates) != EXPECTED_TEMPLATES:
        raise ValueError(f"{MANIFEST_PATH}: expected {EXPECTED_TEMPLATES} templates")
    counts = Counter(item["category"] for item in templates)
    if dict(sorted(counts.items())) != EXPECTED_CATEGORY_COUNTS:
        raise ValueError(f"{MANIFEST_PATH}: category counts differ: {dict(counts)}")
    for item in templates:
        if len(item.get("mechanics_en", [])) != 4:
            raise ValueError(f"{item['source_id']}: expected four primary mechanics")
        if len(item.get("supporting_systems_en", [])) < 4:
            raise ValueError(f"{item['source_id']}: expected at least four supporting systems")
        if require_translations:
            if not item.get("title_zh"):
                raise ValueError(f"{item['source_id']}: title_zh is missing")
            if len(item.get("mechanics_zh", [])) != len(item["mechanics_en"]):
                raise ValueError(f"{item['source_id']}: mechanics_zh is incomplete")
    return raw


def _join_list(values: list[str], language: str) -> str:
    if language == "en":
        if len(values) == 1:
            return values[0]
        return ", ".join(values[:-1]) + f", and {values[-1]}"
    return "、".join(values)


def _supporting_subset(item: dict[str, Any], language: str) -> list[str]:
    if language == "zh":
        return SUPPORTING_ZH[item["category"]]
    systems = item["supporting_systems_en"]
    # Eight systems preserve breadth without turning every prompt into a catalog dump.
    replacements = {
        "God" + "ot rigid body physics": "Rigid-body physics",
        "God" + "ot 2D rigid body physics environment": "2D rigid-body physics environment",
    }
    return [
        next(
            (
                value.replace(old, new)
                for old, new in replacements.items()
                if old in value
            ),
            value,
        )
        for value in systems[:8]
    ]


def _presentation_contract(item: dict[str, Any], language: str) -> str:
    dimension = item["dimension"]
    if language == "en":
        renderer = (
            "Use Three.js and WebGL for the playable presentation."
            if dimension in {"3D", "2.5D"}
            else "Use HTML Canvas 2D or Three.js/WebGL for the playable presentation."
        )
        return f"""\
## HTML Submission Format

Deliver a self-contained browser game in two files:

- `index.html` - the complete playable presentation. {renderer}
- `game_logic.js` - the deterministic state and rules layer, exporting
  `createGame(opts)` and `advance(game, input, dt)`.

The page must open without a build step or local server and render within three
seconds on a normal laptop. Use procedural geometry, generated textures, shaders,
particles, synthesized audio, and CSS. Do not fetch external images, models,
video, or audio at runtime. Three.js may be loaded from its official CDN when
used; pin any permitted library to a specific version.

Support keyboard and pointer input, with gamepad or touch added where appropriate.
Keep the complete play area and HUD readable at 1280x720. Include a styled start
flow, concise in-game guidance, pause and restart controls, a complete outcome
loop, and visible feedback for every important action.

`index.html` must not use `fetch()` or `XMLHttpRequest`. Keep `index.html` under
160 KB and `game_logic.js` under 320 lines.
"""
    renderer = (
        "使用 Three.js 和 WebGL 完成可玩呈现。"
        if dimension in {"3D", "2.5D"}
        else "使用 HTML Canvas 2D 或 Three.js/WebGL 完成可玩呈现。"
    )
    return f"""\
## HTML 提交格式

用两个文件交付一个可独立运行的浏览器游戏：

- `index.html` - 完整可玩的呈现层。{renderer}
- `game_logic.js` - 确定性的状态与规则层，导出 `createGame(opts)` 和
  `advance(game, input, dt)`。

页面不能依赖构建步骤或本地服务器，普通笔记本应在三秒内完成首屏渲染。使用程序化
几何体、生成纹理、着色器、粒子、合成音频和 CSS；运行时不得获取外部图片、模型、
视频或音频。使用 Three.js 时可以从官方 CDN 加载；允许的库必须锁定具体版本。

必须支持键盘和鼠标，并按玩法需要加入手柄或触摸控制。完整游戏区与 HUD 在
1280x720 下应清晰可读。需要有经过设计的开始流程、简短游戏内引导、暂停与重开控制、
完整结果闭环，以及每项关键操作的明确反馈。

`index.html` 不得使用 `fetch()` 或 `XMLHttpRequest`。`index.html` 控制在
160 KB 以内，`game_logic.js` 控制在 320 行以内。
"""


def _prompt(item: dict[str, Any], language: str) -> str:
    category = CATEGORY_LABELS[item["category"]][language]
    mechanics = item[f"mechanics_{language}"]
    support = _supporting_subset(item, language)
    if language == "en":
        perspective = item["perspective"].replace("-", " ")
        core = _join_list(mechanics, "en")
        support_text = "; ".join(support)
        return f"""\
# {item["title_en"]}

Build a complete, playable **{item["dimension"]} {category} game** as a polished
browser vertical slice, presented from a **{perspective}** viewpoint.

## Core Vision

Create an original game whose connected play loop centers on {core}. The systems
must affect one another through shared state instead of appearing as isolated
buttons, menus, or visual demonstrations.

## Required Playable Systems

1. **Primary mechanic A - {mechanics[0]}**: make it directly controllable or
   strategically actionable, with deterministic state changes, readable feedback,
   and observable success and failure consequences.
2. **Primary mechanic B - {mechanics[1]}**: connect it to the first mechanic so
   player decisions alter timing, position, resources, risk, or available options.
3. **Primary mechanic C - {mechanics[2]}**: implement its full input-to-outcome
   loop, including invalid actions, edge conditions, and recovery or reset behavior.
4. **Primary mechanic D - {mechanics[3]}**: make it materially change strategy,
   progression, or replay outcomes rather than serving as a label or cosmetic state.
5. **Supporting systems**: implement at least four of these mechanic signatures
   and connect them to the core loop: {support_text}.
6. **Playable breadth and outcome**: {CONTENT_REQUIREMENT[item["category"]]["en"]}

## Progression and State

Use a short three-stage arc. Introduce the core interaction clearly, combine it
with supporting systems under greater pressure, then finish with a scenario that
tests mastery. Important rules, resources, objectives, selection state, progress,
danger, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`.

## Art Direction

{ART_DIRECTION[item["category"]]["en"]}

{_presentation_contract(item, "en")}""".strip()

    perspective = PERSPECTIVE_ZH[item["perspective"]]
    core = _join_list(mechanics, "zh")
    support_text = "；".join(support)
    return f"""\
# {item["title_zh"]}

制作一个完整可玩的 **{DIMENSION_ZH[item["dimension"]]} {category}游戏**，以
**{perspective}** 呈现为经过打磨的浏览器纵向切片。

## 核心构想

围绕{core}构建原创且连贯的玩法闭环。各系统必须通过共享状态互相影响，不能只是彼此
割裂的按钮、菜单或视觉演示。

## 必须实现的可玩系统

1. **核心机制 A - {mechanics[0]}**：让玩家能够直接操控或进行策略决策；状态变化必须
   确定，反馈清晰，并能观察到成功与失败后果。
2. **核心机制 B - {mechanics[1]}**：与第一项机制连接，使玩家决策能够改变时机、位置、
   资源、风险或可用选项。
3. **核心机制 C - {mechanics[2]}**：实现从输入到结果的完整流程，包括无效操作、边界
   条件以及恢复或重置行为。
4. **核心机制 D - {mechanics[3]}**：必须实质改变策略、成长或重玩结果，不能只是标签
   或装饰状态。
5. **支撑系统**：从以下机制签名中至少实现四项，并接入核心循环：{support_text}。
6. **内容广度与结果**：{CONTENT_REQUIREMENT[item["category"]]["zh"]}

## 成长与状态

使用三个阶段组成短流程：先清楚引入核心交互，再在更高压力下组合支撑系统，最后用综合
场景检验掌握程度。重要规则、资源、目标、选择状态、进度、危险与结果必须显示在稳定的
HUD 区域，并在 `game_logic.js` 中有对应状态。

## 美术方向

{ART_DIRECTION[item["category"]]["zh"]}

{_presentation_contract(item, "zh")}""".strip()


def _requirement(req_id: str, description: str, category: str) -> dict[str, Any]:
    if category == "mechanic":
        suffix = (
            " Score 0 if it is absent, decorative, or cannot be exercised through "
            "player input. Score 1 requires connected state changes and visible "
            "success/failure consequences in a playable flow."
        )
        agg = "max"
    elif category == "depth":
        suffix = (
            " Score 0 if the content is missing or differs only through labels or "
            "color swaps. Score 1 requires functionally distinct content that changes "
            "player decisions."
        )
        agg = "max"
    elif category == "experience":
        suffix = (
            " Score 0 if essential information or feedback is missing, unreadable, "
            "overlapping, or disconnected from live game state at 1280x720."
        )
        agg = "mean"
    else:
        suffix = (
            " Score 0 if the presentation is dominated by default controls, unlit "
            "primitives, inconsistent materials, or abrupt unanimated state changes."
        )
        agg = "mean"
    return {"id": req_id, "agg": agg, "description": description + suffix}


def _rubric(item: dict[str, Any]) -> dict[str, Any]:
    mechanics = item["mechanics_en"]
    support = _supporting_subset(item, "en")
    requirements = [
        _requirement("M1", f"Primary mechanic A is complete and playable: {mechanics[0]}.", "mechanic"),
        _requirement("M2", f"Primary mechanic B is complete and connected to A: {mechanics[1]}.", "mechanic"),
        _requirement(
            "M3",
            f"Primary mechanics C and D both affect live play: {mechanics[2]}; {mechanics[3]}.",
            "mechanic",
        ),
        _requirement(
            "D1",
            "At least four supporting systems are implemented and connected: "
            + "; ".join(support)
            + ".",
            "depth",
        ),
        _requirement("D2", CONTENT_REQUIREMENT[item["category"]]["en"], "depth"),
        _requirement(
            "D3",
            "The rules layer maintains resources, objectives, selection, danger, progress, "
            "and outcome without relying on DOM text as the source of truth.",
            "depth",
        ),
        _requirement(
            "D4",
            "A three-stage progression teaches the core mechanic, combines systems under "
            "greater pressure, and ends with a mastery scenario plus a working replay flow.",
            "depth",
        ),
        _requirement(
            "V1",
            "The HUD clearly communicates current objective, critical resources, selected "
            "target or mode, progress, and danger in stable regions.",
            "experience",
        ),
        _requirement(
            "V2",
            "Important actions have immediate, distinguishable feedback for valid input, "
            "invalid input, success, damage or failure, and state changes.",
            "experience",
        ),
        _requirement(
            "V3",
            "The full loop is connected: styled start flow, playable systems, escalation, "
            "final success/failure state, and retry navigation work without page reload.",
            "experience",
        ),
        _requirement(
            "A1",
            "The project has a coherent authored art direction: "
            + ART_DIRECTION[item["category"]]["en"],
            "art",
        ),
        _requirement(
            "A2",
            f"The {item['dimension']} {item['perspective']} composition uses deliberate "
            "lighting, contrast, depth or layering, and themed landmarks instead of an "
            "empty default scene.",
            "art",
        ),
        _requirement(
            "A3",
            "Interactive actors, targets, hazards, tools, and UI symbols have readable "
            "silhouettes and visibly different functional states.",
            "art",
        ),
        _requirement(
            "A4",
            "Movement, impacts, transitions, alerts, completion moments, and interface "
            "changes use smooth multi-frame animation, particles, camera treatment, or "
            "synchronized audio feedback.",
            "art",
        ),
    ]
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
                "index.html and game_logic.js exist, a canvas/WebGL renderer is present, "
                "and no disallowed heavy runtime asset references are used."
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


def _base_id(item: dict[str, Any]) -> str:
    return f"mz_summer-{item['category']}-{item['task_slug']}"


def _task_yaml(item: dict[str, Any], language: str, prompt: str) -> dict[str, Any]:
    base_id = _base_id(item)
    task_id = f"{base_id}-{language}"
    difficulty = classify_difficulty(
        CATEGORY_LABELS[item["category"]]["family"],
        _prompt(item, "en"),
    )
    return {
        "id": task_id,
        "title": item[f"title_{language}"] + LANGUAGE_SUFFIX[language],
        "family": CATEGORY_LABELS[item["category"]]["family"],
        "difficulty": difficulty,
        "engine": "html",
        "language": language,
        "base_task_id": base_id,
        "provenance": {
            "kind": "adapted_summerengine_template",
            "source_name": "Summer Engine templates",
            "source_index_url": SOURCE_INDEX_URL,
            "source_url": item["source_url"],
            "source_template_id": item["source_id"],
            "source_category": item["category"],
            "source_dimension": item["dimension"],
            "source_perspective": item["perspective"],
            "source_html_sha256": item["html_sha256"],
        },
        "rounds": [{"name": "R1", "spec": prompt}],
        "static": [
            {"kind": "required_file", "role": "entry", "path": "index.html", "weight": 1.0},
            {
                "kind": "required_file",
                "role": "logic",
                "path": "game_logic.js",
                "weight": 1.0,
            },
        ],
        "behavior": {"script": "beh_html.mjs", "timeout": 300},
        "rubric": [
            {
                "id": "completeness",
                "weight": 0.15,
                "max": 5,
                "anchors": RUBRIC_MAPPING["completeness"],
                "rubric": "Core requested systems are implemented and connected.",
            },
            {
                "id": "richness",
                "weight": 0.35,
                "max": 5,
                "anchors": RUBRIC_MAPPING["richness"],
                "rubric": "Content variety, escalation, progression, and meaningful choices.",
            },
            {
                "id": "player_exp",
                "weight": 0.15,
                "max": 5,
                "anchors": RUBRIC_MAPPING["player_exp"],
                "rubric": "Readable state, responsive feedback, and a complete playable loop.",
            },
            {
                "id": "visual",
                "weight": 0.35,
                "max": 5,
                "anchors": RUBRIC_MAPPING["visual"],
                "rubric": (
                    "Coherent authored art direction, functional composition, effects, "
                    "and motion polish."
                ),
            },
        ],
    }


def _render_files(item: dict[str, Any], language: str) -> dict[str, str]:
    prompt = _prompt(item, language)
    _validate_no_ip(prompt, f"{item['source_id']}.{language}.prompt")
    task_id = f"{_base_id(item)}-{language}"
    return {
        f"{task_id}.task.yaml": yaml.dump(
            _task_yaml(item, language, prompt),
            Dumper=LiteralDumper,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        ),
        "prompt.md": prompt + "\n",
        "rubric.mapping.json": json.dumps(RUBRIC_MAPPING, ensure_ascii=False, indent=2) + "\n",
        "rubric.original.json": json.dumps(_rubric(item), ensure_ascii=False, indent=2) + "\n",
    }


def _validate_or_write(write: bool) -> tuple[int, int]:
    manifest = _load_manifest(require_translations=True)
    created = 0
    validated = 0
    for item in manifest["templates"]:
        for language in LANGUAGE_SUFFIX:
            task_id = f"{_base_id(item)}-{language}"
            task_dir = TASKS_ROOT / task_id
            expected = _render_files(item, language)
            if not task_dir.exists():
                if not write:
                    raise FileNotFoundError(
                        f"{task_dir} is missing; rerun with --write to generate tasks"
                    )
                task_dir.mkdir()
                created += 1
            if write:
                for name, content in expected.items():
                    (task_dir / name).write_text(content, encoding="utf-8")

            actual_names = {path.name for path in task_dir.iterdir() if path.is_file()}
            if actual_names != set(expected):
                raise ValueError(
                    f"{task_dir}: expected files {sorted(expected)}, found {sorted(actual_names)}"
                )
            for name, content in expected.items():
                if (task_dir / name).read_text(encoding="utf-8") != content:
                    raise ValueError(f"{task_dir / name}: differs from generated catalog")
            validated += 1
    return created, validated


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--import-crawl",
        type=Path,
        metavar="PATH",
        help="derive the compact source manifest from a full crawl JSON",
    )
    parser.add_argument("--write", action="store_true", help="write generated task files")
    args = parser.parse_args(argv)

    if args.import_crawl:
        _import_crawl(args.import_crawl)
        if not args.write:
            return 0
    created, validated = _validate_or_write(args.write)
    print(
        f"Summer Engine tasks valid: {EXPECTED_TEMPLATES} concepts x 2 languages = "
        f"{validated} tasks ({created} created)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
