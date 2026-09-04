"""Import three public theme sources and generate independent bilingual tasks.

Sources:

- 20 browser-game prompts from the supplied CNBlogs article.
- 8 entries in the "Games & 3D" section of the supplied EvoLink page.
- Every valid AIGA Shared Worlds detail referenced by the captured sitemap.

The import step stores source hashes and compact world metadata. Generated task
prompts use reviewed benchmark wording rather than copying long source prompts.

Typical use:

    python3 scripts/add_three_source_tasks.py --import-crawls
    python3 scripts/add_three_source_tasks.py --write
    python3 scripts/add_three_source_tasks.py
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from task_metadata import classify_difficulty
from prompt_contract import clean_yaml, input_scheme_for_family, render_contract


ROOT = Path(__file__).resolve().parent.parent
TASKS_ROOT = ROOT / "bench" / "tasks"
SOURCES_ROOT = ROOT / "bench" / "sources"
CNBLOGS_MANIFEST = SOURCES_ROOT / "cnblogs_game_prompts.json"
EVOLINK_MANIFEST = SOURCES_ROOT / "evolink_game_prompts.json"
AIGA_MANIFEST = SOURCES_ROOT / "aiga_shared_worlds.json"
AIGA_LOCALIZATIONS = SOURCES_ROOT / "aiga_world_localizations.tsv"

SOURCE_CAPTURE_DATE = "2026-08-28"
CNBLOGS_URL = "https://www.cnblogs.com/shuihx/articles/19853326"
EVOLINK_URL = "https://evolink.ai/zh/kimi-k3-prompts"
AIGA_INDEX_URL = "https://www.aiga.io/zh/shared-worlds?langCode=zh%2Cen"
AIGA_API_ROOT = "https://www.aiga.io/api/public-worlds"

EXPECTED_CNBLOGS = 20
EXPECTED_EVOLINK = 8
EXPECTED_AIGA_URLS = 145
EXPECTED_AIGA_VALID = 144
EXPECTED_AIGA_TOMBSTONES = 1
LANGUAGE_SUFFIX = {"en": " (English)", "zh": " (中文)"}
RUBRIC_MAPPING = {
    "completeness": ["M1", "M2", "M3"],
    "richness": ["D1", "D2", "D3", "D4"],
    "player_exp": ["V1", "V2", "V3"],
    "visual": ["A1", "A2", "A3", "A4"],
}

BANNED_GENERATED_TERMS = (
    "aincrad",
    "aloy",
    "arnor",
    "clone wars",
    "courage the cowardly",
    "darth revan",
    "deus ex",
    "duke nukem",
    "hades",
    "middle-earth",
    "nathan drake",
    "piece of eden",
    "robocop",
    "terminator",
    "uncharted",
    "xcom",
)

FAMILY_LABELS = {
    "action": {"en": "action combat", "zh": "动作战斗"},
    "adventure": {"en": "adventure and exploration", "zh": "冒险探索"},
    "arcade": {"en": "arcade", "zh": "街机"},
    "cardgame": {"en": "card strategy", "zh": "卡牌策略"},
    "horror": {"en": "survival horror", "zh": "生存恐怖"},
    "narrative": {"en": "narrative adventure", "zh": "叙事冒险"},
    "openworld": {"en": "open-world adventure", "zh": "开放世界冒险"},
    "platformer": {"en": "platformer", "zh": "平台跳跃"},
    "puzzle": {"en": "puzzle", "zh": "解谜"},
    "racing": {"en": "racing", "zh": "竞速"},
    "rpg": {"en": "role-playing", "zh": "角色扮演"},
    "shooter": {"en": "shooter", "zh": "射击"},
    "simulation": {"en": "simulation", "zh": "模拟"},
    "sports": {"en": "sports", "zh": "体育"},
    "strategy": {"en": "strategy", "zh": "策略"},
    "survival": {"en": "survival and crafting", "zh": "生存制造"},
}

PERSPECTIVE_ZH = {
    "first-person": "第一人称",
    "isometric": "等距视角",
    "side-scrolling": "横向卷轴视角",
    "top-down": "俯视角",
    "third-person": "第三人称",
}

ART_DIRECTION = {
    "action": {
        "en": "Strong combat silhouettes, readable anticipation, restrained hit flashes, authored arenas, and impact animation that never hides hazards.",
        "zh": "使用鲜明战斗轮廓、清楚的动作预备、克制命中特效与经过设计的场地；冲击动画不能遮挡危险。",
    },
    "adventure": {
        "en": "Memorable landmarks, layered routes, environmental storytelling, useful lighting guidance, and distinct interaction states.",
        "zh": "使用可辨识地标、分层路线、环境叙事、有效灯光引导和清晰交互状态。",
    },
    "arcade": {
        "en": "Immediate arcade readability, energetic motion, strong score feedback, and a restrained scene with vivid gameplay accents.",
        "zh": "强调即时街机可读性、充满动势的动画、明确分数反馈，以及克制场景中的鲜明玩法强调色。",
    },
    "cardgame": {
        "en": "Readable cards, deliberate table composition, expressive state changes, clear targeting, and satisfying draw, play, and resolve animation.",
        "zh": "卡牌、桌面构图与目标必须清晰，并为抽牌、出牌、结算和状态变化提供有表现力的动画。",
    },
    "horror": {
        "en": "Controlled darkness, threatening negative space, spatial audio cues, readable danger silhouettes, and effects that preserve player orientation.",
        "zh": "控制黑暗与威胁留白，使用空间音频线索和可辨识危险轮廓；特效不能破坏方向判断。",
    },
    "narrative": {
        "en": "Character-focused staging, expressive portraits or models, a legible dialogue hierarchy, and scene composition that responds to relationships.",
        "zh": "以角色为中心安排镜头与舞台，使用有表现力的形象、清晰对话层级，以及会响应关系变化的构图。",
    },
    "openworld": {
        "en": "Distinct district identities, visible traversal routes, authored landmarks, reactive inhabitants, and world changes that remain visible after choices.",
        "zh": "各区域具有独特身份，路线和地标清晰，居民会响应玩家，选择造成的世界变化应持续可见。",
    },
    "platformer": {
        "en": "Crisp player and hazard silhouettes, readable landing surfaces, stable depth separation, motion trails, and responsive squash and impact.",
        "zh": "玩家、危险与落脚面轮廓清楚，景深层级稳定，并通过运动轨迹、挤压拉伸与冲击反馈增强手感。",
    },
    "puzzle": {
        "en": "A calm and precise visual language with distinct state colors, clean spatial grouping, smooth transformations, and no obscured puzzle information.",
        "zh": "采用冷静精确的视觉语言、可区分状态色、清楚空间分组和平滑变换，任何装饰都不能遮挡谜题信息。",
    },
    "racing": {
        "en": "Strong speed and trajectory cues, readable track boundaries, recognizable rivals, dynamic cameras, and replay-worthy collision and finish moments.",
        "zh": "突出速度与轨迹提示、清晰赛道边界和可辨识对手，并用动态镜头呈现碰撞与冲线时刻。",
    },
    "rpg": {
        "en": "A cohesive world identity, readable character and enemy roles, expressive abilities, layered locations, and visible equipment and progression changes.",
        "zh": "建立统一世界身份、清晰角色与敌人定位、富有表现力的技能和分层地点；装备与成长变化应可见。",
    },
    "shooter": {
        "en": "Readable targets and projectiles, disciplined muzzle and impact effects, strong cover silhouettes, useful depth cues, and camera feedback that supports aiming.",
        "zh": "目标、弹道与掩体轮廓必须清晰，枪口和命中特效保持克制，景深与镜头反馈服务于瞄准。",
    },
    "simulation": {
        "en": "A coherent operational world with legible actors and machines, animated flows, state-driven color, and dense but organized management information.",
        "zh": "构建连贯运营世界，角色和机器易于辨识；用流动动画和状态配色展示变化，管理信息紧凑有序。",
    },
    "sports": {
        "en": "Readable players and ball trajectories, clear field markings, responsive motion, broadcast-inspired cameras, and decisive scoring feedback.",
        "zh": "球员、球路和场地标记清晰，运动响应灵敏，并以赛事转播式镜头和明确得分反馈呈现比赛。",
    },
    "strategy": {
        "en": "A scan-friendly tactical field, distinct roles, visible ranges and ownership, restrained effects, and information hierarchy for repeated decisions.",
        "zh": "战术场地便于扫视，单位定位、范围与归属清楚；特效保持克制，信息层级支持连续决策。",
    },
    "survival": {
        "en": "Tactile resources and tools, readable environmental danger, changing weather and time, visible wear and construction, and a world that records intervention.",
        "zh": "资源与工具要有触感，环境危险、天气和时间变化清楚；磨损、建造及玩家对世界的改造都应可见。",
    },
}

GENRE_ZH = {
    "adventure": "冒险",
    "comedy": "喜剧",
    "cosmic-horror": "宇宙恐怖",
    "cyberpunk": "赛博朋克",
    "dark-fantasy": "黑暗奇幻",
    "dystopian": "反乌托邦",
    "fantasy": "奇幻",
    "high-fantasy": "高魔奇幻",
    "historical": "历史",
    "horror": "恐怖",
    "mystery": "悬疑",
    "noir": "黑色侦探",
    "post-apocalyptic": "末日废土",
    "romance": "情感",
    "romantic-comedy": "浪漫喜剧",
    "romantic-fantasy": "浪漫奇幻",
    "scifi": "科幻",
    "space-opera": "太空歌剧",
    "steampunk": "蒸汽朋克",
    "superhero": "超能力",
    "surrealism": "超现实",
    "survival": "生存",
    "survival-horror": "生存恐怖",
    "urban-fantasy": "都市奇幻",
}

WORLD_SIZE_ZH = {
    "small": "小型",
    "medium": "中型",
    "large": "大型",
    "huge": "超大型",
}

TONE_ZH = {
    "cinematic": "电影化",
    "comedic-profanity": "荒诞喜剧",
    "dark": "黑暗",
    "epic": "史诗",
    "gritty": "冷峻写实",
    "lighthearted": "轻快",
    "mysterious": "神秘",
    "street-gritty": "街头冷峻",
    "surreal": "超现实",
    "wholesome": "温暖",
}

AIGA_PRIMARY = {
    "action": {
        "en": (
            "Build a responsive combat loop with directional attacks, defense or dodge "
            "timing, enemy telegraphs, stamina or ability limits, and readable hit states.",
            "Track health, stamina or focus, ability recovery, enemy pressure, and the "
            "consequences of mercy, aggression, or collateral damage.",
        ),
        "zh": (
            "构建响应灵敏的战斗循环，包含方向攻击、防御或闪避时机、敌人预警、体力或能力限制和清楚受击状态。",
            "追踪生命、体力或专注、技能恢复、敌人压力，以及仁慈、进攻或附带破坏造成的后果。",
        ),
    },
    "adventure": {
        "en": (
            "Investigate landmarks, collect and combine clues or tools, solve contextual "
            "obstacles, and unlock routes through demonstrated understanding.",
            "Track evidence, inventory, current hypotheses, route access, and the risk of "
            "losing time, trust, or irreplaceable opportunities.",
        ),
        "zh": (
            "调查地标、收集并组合线索或工具、解决情境障碍，并通过证明理解来解锁路线。",
            "追踪证据、背包、当前推断、路线权限，以及损失时间、信任或不可替代机会的风险。",
        ),
    },
    "horror": {
        "en": (
            "Use stealth, sound, light, hiding, limited defense, or environmental tools to "
            "survive threats whose search behavior can be learned and manipulated.",
            "Manage health, composure or sanity, light or power, scarce supplies, noise, "
            "and an escalating threat state.",
        ),
        "zh": (
            "使用潜行、声音、照明、藏身、有限防御或环境工具应对威胁，其搜索规律必须可学习和利用。",
            "管理生命、镇定或理智、照明或电力、稀缺物资、噪声和不断升级的威胁状态。",
        ),
    },
    "narrative": {
        "en": (
            "Use schedules, direct dialogue choices, remembered facts, and character-led "
            "tasks so relationships change what can be attempted next.",
            "Track time, trust, affection or respect, promises, discovered secrets, and "
            "event prerequisites without reducing relationships to cosmetic meters.",
        ),
        "zh": (
            "使用日程、直接对话选择、被记住的事实和角色任务，让关系变化真正改变下一步可做之事。",
            "追踪时间、信任、好感或尊重、承诺、已发现秘密和事件前置条件，关系不能只是装饰数值。",
        ),
    },
    "openworld": {
        "en": (
            "Combine traversal, local jobs, environmental interaction, and spontaneous "
            "events so each district offers a different way to make progress.",
            "Track route access, local danger, favors, supplies, attention, and district "
            "state while optional events compete with the main objective.",
        ),
        "zh": (
            "组合移动、局部任务、环境交互和突发事件，让每个区域提供不同推进方式。",
            "追踪路线权限、局部危险、人情、补给、警觉和区域状态，让可选事件与主目标争夺时间。",
        ),
    },
    "racing": {
        "en": (
            "Drive or fly through validated checkpoints with responsive acceleration, "
            "braking, steering, grip or drift, collisions, rivals, and recoverable mistakes.",
            "Track speed, vehicle condition, heat or fuel, lap or route progress, penalties, "
            "split time, and current position.",
        ),
        "zh": (
            "以响应灵敏的加速、制动、转向、抓地或漂移穿过合法检查点，并处理碰撞、对手和可恢复失误。",
            "追踪速度、载具状态、热量或燃料、圈数或路线进度、处罚、分段时间和当前名次。",
        ),
    },
    "rpg": {
        "en": (
            "Use abilities, equipment, quests, enemy encounters, and dialogue outcomes in "
            "one connected character-build loop with meaningful tactical choices.",
            "Track health, ability resources, experience, equipment, quest state, faction "
            "standing, and at least one irreversible build choice.",
        ),
        "zh": (
            "把技能、装备、任务、敌人遭遇和对话结果连接成角色构筑循环，并提供有意义的战术选择。",
            "追踪生命、能力资源、经验、装备、任务状态、派系声望和至少一个不可逆构筑选择。",
        ),
    },
    "shooter": {
        "en": (
            "Implement responsive aiming, firing, reload or cooldown, projectile or hit "
            "validation, enemy telegraphs, cover or movement pressure, and distinct weapons.",
            "Track health or shields, ammunition or heat, weapon state, enemy alert, "
            "objective progress, and damage consequences.",
        ),
        "zh": (
            "实现灵敏瞄准、射击、换弹或冷却、弹道或命中判定、敌人预警、掩体或移动压力和不同武器。",
            "追踪生命或护盾、弹药或热量、武器状态、敌人警觉、目标进度和伤害后果。",
        ),
    },
    "simulation": {
        "en": (
            "Operate a visible workflow through direct assignments, timing, capacity, "
            "maintenance, and quality decisions whose outputs feed later work.",
            "Track time, workload, capacity, quality, money or supplies, actor condition, "
            "and a report derived from live operations.",
        ),
        "zh": (
            "通过直接分配、时机、容量、维护和质量决策操作可见工作流，其产出会进入后续环节。",
            "追踪时间、工作量、容量、质量、金钱或补给、参与者状态，并根据实时运营生成报表。",
        ),
    },
    "sports": {
        "en": (
            "Implement the sport's direct controls, legal scoring, possession or turn "
            "changes, opponents, timing, and skill execution under pressure.",
            "Track score, time, stamina, position or ranking, player attributes, fouls or "
            "mistakes, and match momentum.",
        ),
        "zh": (
            "实现该运动的直接操控、合法得分、球权或回合转换、对手、计时和压力下的技术动作。",
            "追踪比分、时间、体力、位置或排名、球员属性、犯规或失误和比赛势头。",
        ),
    },
    "strategy": {
        "en": (
            "Issue tactical or operational orders, commit limited units or workers, and "
            "resolve conflicts where positioning, timing, information, and risk matter.",
            "Track controlled locations, units or agents, economy, intelligence, threat, "
            "faction power, and the delayed consequences of earlier orders.",
        ),
        "zh": (
            "下达战术或运营命令、投入有限单位或人员，并结算位置、时机、情报和风险都重要的冲突。",
            "追踪控制地点、单位或角色、经济、情报、威胁、派系力量和早期命令的延迟后果。",
        ),
    },
    "survival": {
        "en": (
            "Scavenge, craft, shelter, travel, and respond to environmental or creature "
            "threats through tools whose durability and utility are visible.",
            "Track health, hunger or energy, infection or exposure, inventory, tool wear, "
            "weather or time, shelter, and companion safety.",
        ),
        "zh": (
            "通过耐久和用途清楚的工具进行搜集、制造、庇护、旅行，并应对环境或生物威胁。",
            "追踪生命、饥饿或能量、感染或暴露、库存、工具磨损、天气或时间、庇护所和同伴安全。",
        ),
    },
}


def _item(
    source_item: str,
    slug: str,
    title_en: str,
    title_zh: str,
    family: str,
    dimension: str,
    perspective: str,
    vision_en: str,
    vision_zh: str,
    mechanics_en: list[str],
    mechanics_zh: list[str],
) -> dict[str, Any]:
    return {
        "source_item": source_item,
        "slug": slug,
        "title_en": title_en,
        "title_zh": title_zh,
        "family": family,
        "dimension": dimension,
        "perspective": perspective,
        "vision_en": vision_en,
        "vision_zh": vision_zh,
        "mechanics_en": mechanics_en,
        "mechanics_zh": mechanics_zh,
    }


CNBLOGS_ITEMS = [
    _item(
        "01",
        "ninja-village",
        "Shadows over Kagemura",
        "影越雾隐村",
        "platformer",
        "2D",
        "side-scrolling",
        "A side-scrolling ninja mission through an ancient village where traversal, stealth, and projectile combat form one continuous route.",
        "一场穿越古代村落的横版忍者任务，让移动、潜行和投射战斗组成一条连续路线。",
        ["Run, jump, ledge-grab, and cross layered platforms with forgiving coyote time.", "Aim and throw arcing shuriken with cooldown, ammunition, and hit feedback.", "Face patrol enemies that investigate sound, chase, attack, and return to posts.", "Manage health and stamina while checkpoints, collectibles, and a final gate track level progress."],
        ["支持奔跑、跳跃、边缘攀附和分层平台移动，并提供合理的土狼时间。", "瞄准并投掷具有抛物线轨迹的飞镖，包含冷却、弹药和命中反馈。", "敌人会巡逻、调查声响、追击、攻击并返回岗位。", "管理生命与体力，并通过检查点、收集物和最终关门推进关卡。"],
    ),
    _item(
        "02",
        "deep-space-strike",
        "Deep-Space Strike",
        "深空突击",
        "shooter",
        "3D",
        "third-person",
        "A six-degree-of-freedom space battle in which a nimble ship survives enemy formations, upgrades weapons, and breaks a staged flagship.",
        "一场六自由度太空战斗：灵活飞船躲避敌舰编队、升级武器，并摧毁分阶段旗舰。",
        ["Fly with responsive thrust, yaw, pitch, roll, braking, and a readable chase camera.", "Switch among laser, missile, and spread weapons with distinct ammunition and targeting behavior.", "Fight spawned enemy formations and dodge patterned fire with shield and collision rules.", "Choose weapon upgrades between waves and complete a multi-stage boss encounter."],
        ["以响应灵敏的推进、偏航、俯仰、滚转和制动控制飞船，并使用清晰追尾镜头。", "切换激光、导弹和扩散武器，各自拥有不同弹药与锁定行为。", "对抗生成的敌舰编队并躲避规律弹幕，处理护盾与碰撞规则。", "波次之间选择武器升级，并完成多阶段首领战。"],
    ),
    _item(
        "03",
        "mythic-duel",
        "Mythic Duel",
        "神话决斗",
        "action",
        "2D",
        "side-scrolling",
        "A stylized mythic fighting game built around input buffering, readable hit states, defensive timing, and branching combos.",
        "一款风格化神话格斗游戏，核心是输入缓冲、清晰受击状态、防御时机和分支连招。",
        ["Implement light and heavy strikes with hitboxes, recovery, knockback, and input buffering.", "Recognize at least three combo strings with cancel windows and visible combo feedback.", "Support guard, dodge, armor, hit-stun, and guard-break states with deterministic priority.", "Provide an AI rival, health and energy meters, and a charged ultimate with a complete rematch loop."],
        ["实现轻重攻击的判定框、后摇、击退和输入缓冲。", "识别至少三套连招，包含取消窗口和明确连击反馈。", "支持格挡、闪避、霸体、受击硬直与破防状态，并使用确定优先级。", "提供 AI 对手、生命与能量槽，以及可蓄力大招和完整再战闭环。"],
    ),
    _item(
        "04",
        "clockwork-rider",
        "Clockwork Rider",
        "发条骑手",
        "adventure",
        "2D",
        "side-scrolling",
        "A mechanical mount crosses a gear city and abandoned factory, using momentum, steam power, and linked machinery to open the route.",
        "一具机械坐骑穿越齿轮城和废弃工厂，利用惯性、蒸汽动力与联动机械打开路线。",
        ["Control a weighty mechanical mount with acceleration, braking, jumping, and terrain-aware inertia.", "Trigger linked gears, lifts, pressure plates, and factory machines that physically alter routes.", "Collect fuel and salvage while balancing boost, attacks, and a limited steam-energy meter.", "Reveal map fog, unlock shortcuts, and finish a factory escape sequence under escalating pressure."],
        ["控制具有重量感的机械坐骑，支持加速、制动、跳跃和适应地形的惯性。", "触发联动齿轮、升降机、压力板和工厂机械，让路线产生实际变化。", "收集燃料与零件，并在加速、攻击和有限蒸汽能量之间平衡。", "揭开地图迷雾、开放捷径，并在压力升级中完成工厂逃离。"],
    ),
    _item(
        "05",
        "cloudfront-squadron",
        "Cloudfront Squadron",
        "云锋中队",
        "shooter",
        "2D",
        "top-down",
        "A vertical aerial shooter climbs through cloud layers, enemy formations, upgrade branches, and a bullet-pattern boss.",
        "一款纵向空战射击游戏，穿越云层、敌机编队、升级分支和弹幕首领战。",
        ["Move with precise analog-like response while the battlefield scrolls continuously.", "Fire a primary weapon and limited secondary skill with cooldown and readable targeting.", "Fight distinct formations and dodge escalating projectile patterns with fair collision margins.", "Select upgrades for fire rate, spread, and shield before a staged boss and score summary."],
        ["以精确的类模拟响应移动，战场持续向前滚动。", "使用主武器和次数有限的副技能，并显示冷却与目标反馈。", "对抗不同编队并躲避逐步升级的弹幕，碰撞边界必须公平。", "在分阶段首领战前选择射速、弹道或护盾升级，并提供得分结算。"],
    ),
    _item(
        "06",
        "castle-line-defense",
        "Castle Line Defense",
        "城堡防线",
        "strategy",
        "2D",
        "top-down",
        "A medieval tower-defense battle where placement, economy, enemy paths, and tower specialization remain visible and reversible.",
        "一场中世纪塔防战，放置、经济、敌人路径和防御塔专精都应清晰可见且可调整。",
        ["Place arrow, cannon, and mage towers on valid cells with cost checks and range previews.", "Spawn multiple enemy types that follow a path, take typed damage, and threaten the castle.", "Upgrade and sell towers while economy, target priority, and wave timing create tradeoffs.", "Run several escalating waves with pause, speed control, victory, defeat, and restart."],
        ["在有效格子放置箭塔、炮塔和法师塔，并检查费用和显示范围。", "生成多种沿路径移动、承受不同伤害并威胁城堡的敌人。", "升级或出售防御塔，让经济、目标优先级和波次时机形成取舍。", "运行多轮升级进攻，支持暂停、加速、胜负和重新开始。"],
    ),
    _item(
        "07",
        "enchanted-block-path",
        "Enchanted Block Path",
        "幻林方块之路",
        "puzzle",
        "2D",
        "top-down",
        "A dreamlike forest puzzle about dragging constrained blocks to reconnect paths and awaken energy nodes in few moves.",
        "一款梦幻森林解谜游戏，玩家拖动受约束方块，用较少步数重新连通路径并唤醒能量节点。",
        ["Drag blocks with grid snapping, collision, movement limits, and clear invalid-action feedback.", "Detect connected paths and energy-node activation from the actual board state.", "Track moves and time, compare against a target solution, and support undo, hint, and reset.", "Provide at least three layouts with distinct constraints and persistent level progress."],
        ["拖动方块时支持网格吸附、碰撞、移动限制和无效操作反馈。", "根据真实棋盘状态检测路径连通和能量节点激活。", "记录步数与时间，对比目标解法，并支持撤销、提示和重置。", "提供至少三个约束不同的布局，并保存关卡进度。"],
    ),
    _item(
        "08",
        "island-relic-mystery",
        "Island Relic Mystery",
        "秘岛遗迹谜案",
        "adventure",
        "2D",
        "top-down",
        "An island exploration mystery combines environmental mechanisms, clue collection, item use, fog removal, and branching treasure outcomes.",
        "一场岛屿探索谜案，把环境机关、线索收集、物品使用、迷雾揭开和分支宝藏结局连接起来。",
        ["Explore several island zones and reveal map fog by visiting landmarks and solving local obstacles.", "Collect clues and inventory items, then drag or select them for context-sensitive use.", "Solve sequence, symbol, and environment puzzles with hints that respond to discovered evidence.", "Unlock multiple treasure routes and endings based on optional clues and irreversible choices."],
        ["探索多个岛屿区域，通过访问地标和解决局部阻碍揭开地图迷雾。", "收集线索与物品，并通过拖拽或选择在正确场景中使用。", "解决顺序、符号和环境谜题，提示会响应已发现证据。", "根据可选线索和不可逆选择解锁不同宝藏路线与结局。"],
    ),
    _item(
        "09",
        "arcane-board-command",
        "Arcane Board Command",
        "奥术棋盘指挥",
        "strategy",
        "2D",
        "top-down",
        "A turn-based board duel gives every piece a distinct movement rule and active skill against a deliberate AI opponent.",
        "一场回合制棋盘对决，每枚棋子都有独立移动规则和主动技能，对手是会规划的 AI。",
        ["Select pieces and preview legal movement, attacks, and skill ranges on a custom grid.", "Implement distinct line attack, area control, revival, and mobility skills with cooldowns.", "Alternate timed turns against an AI that evaluates objectives, danger, and skill value.", "Support win detection, undo within fair limits, replay, and several functionally different boards."],
        ["选择棋子并在自定义网格上预览合法移动、攻击和技能范围。", "实现直线攻击、范围控制、复活和位移等不同技能及冷却。", "与会评估目标、危险和技能价值的 AI 进行限时交替回合。", "支持胜负判定、合理悔棋、重玩和多个功能不同的棋盘。"],
    ),
    _item(
        "10",
        "alien-array-defense",
        "Alien Array Defense",
        "异星阵列防御",
        "strategy",
        "2D",
        "top-down",
        "A hybrid defense game lets the player build automated weapon networks while manually aiming emergency fire against alien waves.",
        "一款混合防御游戏：玩家建设自动武器网络，并在外星波次中手动瞄准提供紧急火力。",
        ["Deploy automated turrets, laser relays, and anti-air missiles with valid coverage previews.", "Aim and fire a manual weapon while switching cleanly between manual and automatic control.", "Create chained tower interactions, enemy waves, base health, and a resource economy.", "Expose wave progress, damage alerts, pause and speed controls, and a decisive final assault."],
        ["部署自动炮塔、激光中继与防空导弹，并显示有效覆盖范围。", "瞄准并发射手动武器，同时在手动和自动控制间清晰切换。", "实现塔之间的链式联动、敌人波次、基地生命和资源经济。", "显示波次进度、受损警报、暂停与加速，并提供决定性的最终进攻。"],
    ),
    _item(
        "11",
        "corner-cafe-shift",
        "Corner Cafe Shift",
        "街角咖啡馆",
        "simulation",
        "2D",
        "isometric",
        "A compact cafe shift turns queues, drink preparation, customer mood, revenue, and upgrades into one timed operational loop.",
        "一段紧凑咖啡馆班次，把排队、饮品制作、顾客情绪、营收和升级连接成限时运营循环。",
        ["Seat queued customers, read orders, and route them through a visible service flow.", "Prepare drinks through ordered steps with timers, mistakes, and recoverable remakes.", "Track patience, satisfaction, tips, revenue, and a report derived from live transactions.", "Buy equipment, decor, and menu upgrades that visibly alter later shifts and service capacity."],
        ["安排排队顾客入座、读取订单，并让服务流程清晰可见。", "按顺序完成饮品制作步骤，包含计时、失误和可恢复重做。", "根据实时交易追踪耐心、满意、打赏、营收并生成报表。", "购买设备、装潢和菜单升级，让后续班次与服务容量发生可见变化。"],
    ),
    _item(
        "12",
        "four-season-farm",
        "Four-Season Farm",
        "四季农场",
        "simulation",
        "2D",
        "top-down",
        "A farm life loop connects soil work, crop growth, animal care, weather, inventory, markets, and daily objectives.",
        "一套农场生活循环，把土地、作物成长、动物照料、天气、背包、市场和每日目标连接起来。",
        ["Till, plant, water, and harvest plots whose growth responds to time, season, and weather.", "Feed and care for animals whose health and products depend on repeated attention.", "Manage inventory, forecast yield, and trade through prices that change by supply and season.", "Complete daily tasks and facility upgrades across several days with save and reset behavior."],
        ["开垦、播种、浇水和收割，作物成长会响应时间、季节与天气。", "喂养并照料动物，其健康和产物取决于持续关注。", "管理库存、预测产量，并按供需与季节变化的价格交易。", "跨多个游戏日完成每日任务和设施升级，并支持保存与重置。"],
    ),
    _item(
        "13",
        "companion-evolution",
        "Companion Evolution Lab",
        "伙伴进化实验室",
        "rpg",
        "2D",
        "top-down",
        "A creature-care game links feeding, training, bonding, skill learning, collection, and conditional evolution.",
        "一款伙伴养成游戏，把喂食、训练、亲密、技能学习、图鉴收集和条件进化连接起来。",
        ["Feed, train, and interact through actions that change distinct attributes and consume time or items.", "Display growth curves, current needs, affection, and the consequences of overtraining or neglect.", "Learn and equip skills while inventory items create meaningful build choices.", "Trigger multiple evolution forms from transparent conditions and record discoveries in a collection catalog."],
        ["通过消耗时间或道具的喂食、训练和互动改变不同属性。", "显示成长曲线、当前需求、亲密度，以及过度训练或忽视的后果。", "学习并装备技能，让背包道具形成有意义的构筑选择。", "根据透明条件触发多种进化形态，并把发现记录到图鉴。"],
    ),
    _item(
        "14",
        "campus-constellations",
        "Campus Constellations",
        "校园星轨",
        "narrative",
        "2D",
        "top-down",
        "A campus relationship story uses schedules, dialogue choices, event flags, and affection state to produce distinct routes and endings.",
        "一段校园关系故事，以日程、对话选择、事件标记和好感状态产生不同路线与结局。",
        ["Navigate a daily schedule and select locations that trigger character-specific events.", "Choose dialogue responses that update trust, affection, and remembered conversation flags.", "Unlock multiple routes through prerequisites rather than a single linear script.", "Provide save, load, route overview, and several endings that visibly reflect accumulated choices."],
        ["在每日日程中选择地点，触发角色专属事件。", "选择对话回应，更新信任、好感和被记住的谈话标记。", "通过前置条件解锁多条路线，而不是单一线性脚本。", "提供存档、读档、路线概览，以及能明显反映累积选择的多个结局。"],
    ),
    _item(
        "15",
        "fruit-chain-reactor",
        "Fruit Chain Reactor",
        "水果连锁反应",
        "puzzle",
        "2D",
        "top-down",
        "A polished fruit match game combines valid swaps, cascades, special pieces, limited turns, and adaptive goals.",
        "一款打磨过的水果消除游戏，包含合法交换、连锁、特殊棋子、有限步数和动态目标。",
        ["Swap adjacent fruit only when the move creates a valid match and animate rejection otherwise.", "Resolve matches and cascades deterministically while score and combo feedback follow the board.", "Create bomb, rainbow, and time-control pieces from larger patterns with distinct effects.", "Run several objectives under turn or time limits with reshuffle, win, loss, and restart."],
        ["只有形成有效匹配时才允许交换相邻水果，否则播放拒绝反馈。", "确定性结算匹配与连锁，分数和连击反馈必须跟随棋盘状态。", "通过更大图案生成炸弹、彩虹和时间控制道具，并具有不同效果。", "在步数或时间限制下运行多个目标，支持重排、胜负和重开。"],
    ),
    _item(
        "16",
        "pixel-vault-run",
        "Pixel Vault Run",
        "像素秘境疾行",
        "platformer",
        "2D",
        "side-scrolling",
        "A precision pixel platformer mixes double-jump, dash, checkpoints, hidden rooms, collectibles, and a compact multi-stage route.",
        "一款精确像素平台游戏，组合二段跳、冲刺、检查点、隐藏房间、收集物和紧凑多阶段路线。",
        ["Run and jump with coyote time, buffered input, variable jump height, and stable collision.", "Use double-jump and dash with readable recharge, air-control, and hazard interaction.", "Activate checkpoints, respawn quickly, and track collectibles without losing legitimate progress.", "Hide optional rooms behind discoverable triggers and finish several escalating platform sections."],
        ["奔跑与跳跃支持土狼时间、输入缓冲、可变跳高和稳定碰撞。", "使用二段跳与冲刺，并提供清楚充能、空中控制和危险互动。", "激活检查点、快速重生并追踪收集物，不能丢失合法进度。", "通过可发现触发器隐藏可选房间，并完成多段升级平台挑战。"],
    ),
    _item(
        "17",
        "street-court-rise",
        "Street Court Rise",
        "街球崛起",
        "sports",
        "2.5D",
        "top-down",
        "A compact basketball game combines movement, passing, shooting, steals, team selection, match timing, and player development.",
        "一场紧凑篮球比赛，把移动、传球、投篮、抢断、阵容选择、比赛计时和球员培养连接起来。",
        ["Control an active player, pass between teammates, and switch defenders responsively.", "Aim shots with power and angle feedback while distance, pressure, and attributes affect accuracy.", "Implement steals, rebounds, possession changes, clock rules, score validation, and a working opponent.", "Improve speed, shooting, and rebounding between matches and preserve a local record history."],
        ["控制当前球员、在队友间传球，并快速切换防守人。", "通过力度与角度反馈瞄准，距离、防守压力和属性会影响命中率。", "实现抢断、篮板、球权转换、计时规则、得分判定和有效对手。", "比赛之间培养速度、投篮与篮板，并保留本地战绩。"],
    ),
    _item(
        "18",
        "aether-deck-duel",
        "Aether Deck Duel",
        "以太卡组对决",
        "cardgame",
        "2D",
        "top-down",
        "A fantasy card duel connects drawing, mana, targeting, status resolution, deck construction, and deterministic turn phases.",
        "一场奇幻卡牌对决，把抽牌、法力、目标、状态结算、卡组构筑和确定性回合阶段连接起来。",
        ["Draw, select, target, and play cards through clear turn phases and valid-action checks.", "Resolve attack, defense, damage-over-time, buff, and debuff effects in deterministic order.", "Manage mana, hand limits, discard, draw pile, and hoverable card details.", "Build or edit a deck between battles and complete a full opponent, victory, defeat, and rematch loop."],
        ["在清晰回合阶段中抽牌、选择、指定目标和出牌，并检查操作合法性。", "按确定顺序结算攻击、防御、持续伤害、增益和减益。", "管理法力、手牌上限、弃牌堆、抽牌堆和可悬停查看的卡牌详情。", "战斗之间构筑或编辑卡组，并提供完整对手、胜负与再战闭环。"],
    ),
    _item(
        "19",
        "neon-vector-rally",
        "Neon Vector Rally",
        "霓虹矢量拉力赛",
        "racing",
        "2.5D",
        "third-person",
        "A future circuit racer combines analog acceleration, inertia, drifting, lap validation, opponents, and vehicle tuning.",
        "一款未来赛道竞速游戏，组合线性油门、惯性、漂移、圈数判定、对手和车辆调校。",
        ["Drive with analog-like throttle, braking, steering, grip loss, and recoverable collisions.", "Validate checkpoints and laps while comparing split times and race position.", "Score controlled drifts from angle, speed, duration, and track limits with visible tire trails.", "Tune mutually exclusive performance parts and complete a race with rivals, finish order, and replay."],
        ["以类模拟油门、制动、转向、抓地力损失和可恢复碰撞驾驶。", "验证检查点和圈数，并比较分段时间与比赛名次。", "根据角度、速度、持续时间和赛道边界计算漂移分，并显示轮胎轨迹。", "调校互斥性能部件，并与对手完成包含冲线排名和重玩的比赛。"],
    ),
    _item(
        "20",
        "spellbound-frontier",
        "Spellbound Frontier",
        "法术边境",
        "rpg",
        "2D",
        "isometric",
        "A light fantasy RPG connects exploration, real-time abilities, monsters, quests, inventory, travel, dialogue, and a branching skill tree.",
        "一款轻量奇幻 RPG，把探索、实时技能、怪物、任务、背包、传送、对话和分支技能树连接起来。",
        ["Move through several connected zones and fight monsters with at least three cooldown abilities.", "Accept, track, update, and complete quests through actual world interactions.", "Collect, equip, and use inventory items while experience and levels unlock meaningful choices.", "Spend skill points on a branching tree, unlock travel points, and finish a quest-line boss."],
        ["穿越多个相连区域，并使用至少三种带冷却的技能对抗怪物。", "通过真实世界交互接取、追踪、更新和完成任务。", "收集、装备并使用背包物品，经验和等级会解锁有意义选择。", "在分支技能树投入点数、解锁传送点，并完成任务线首领战。"],
    ),
]

EVOLINK_ITEMS = [
    _item(
        "prompt-voxel-pod-racer-prototype",
        "voxel-pod-racer",
        "Voxel Pod Circuit",
        "体素飞梭赛道",
        "racing",
        "3D",
        "third-person",
        "A generated voxel circuit tests responsive pod handling, collisions, checkpoint discipline, lap pressure, and rival racing.",
        "一条程序化体素赛道检验飞梭操控、碰撞、检查点纪律、圈速压力和对手竞速。",
        ["Drive a hovering pod with acceleration, braking, steering, drift, and recoverable wall impacts.", "Build a readable voxel track with legal checkpoints, shortcuts, hazards, and a finish line.", "Race at least two distinct rivals whose behavior changes with position and track region.", "Track lap and split times, position, penalties, completion, and a reliable restart."],
        ["驾驶悬浮飞梭，支持加速、制动、转向、漂移和可恢复墙体碰撞。", "生成清晰体素赛道，包含合法检查点、捷径、危险和终点线。", "与至少两名不同对手竞速，其行为会随名次和赛段变化。", "追踪圈速、分段、名次、处罚、完成状态并可靠重开。"],
    ),
    _item(
        "prompt-threejs-aircraft-carrier-prototype",
        "carrier-flight-deck",
        "Carrier Flight-Deck Command",
        "航母飞行甲板指挥",
        "simulation",
        "3D",
        "third-person",
        "A playable carrier-deck simulation asks the player to marshal aircraft, manage launch timing, and recover a returning plane safely.",
        "一款可玩的航母甲板模拟，要求玩家调度飞机、管理放飞时机并安全回收返航机。",
        ["Navigate a detailed carrier deck with orbit and first-person camera modes and clear spatial scale.", "Direct deck crew markers and taxi aircraft through conflict-free staging positions.", "Execute one complete launch sequence involving preparation, catapult timing, and safe deck clearance.", "Recover an incoming aircraft by aligning the deck state, arresting zone, and weather window."],
        ["在细致航母甲板上使用环绕与第一人称镜头导航，并保持空间尺度清楚。", "指挥甲板人员标记和滑行飞机进入不会冲突的准备位置。", "完成包含准备、弹射时机和甲板清空的完整放飞流程。", "通过调整甲板状态、拦阻区和天气窗口回收返航飞机。"],
    ),
    _item(
        "prompt-paper-world-agent-game",
        "paper-world-adventure",
        "Folded Frontier",
        "折纸边境",
        "adventure",
        "2.5D",
        "third-person",
        "A cohesive paper-world adventure mixes layered traversal, one enemy encounter, dialogue, a collectible, and a decisive completion state.",
        "一场统一的纸片世界冒险，组合分层移动、敌人遭遇、对话、收集品和明确完成状态。",
        ["Explore a layered paper environment with responsive movement and stable 2D/3D depth rules.", "Fight or evade one complete enemy encounter with readable attack and damage feedback.", "Collect a meaningful object that changes a route, ability, or dialogue outcome.", "Talk with characters, resolve a small quest, and reach a clear completion scene."],
        ["在分层纸片环境中探索，移动响应灵敏且 2D/3D 深度规则稳定。", "完成一次可战斗或规避的敌人遭遇，并提供清楚攻击与伤害反馈。", "收集会改变路线、能力或对话结果的重要物品。", "与角色对话、解决小型任务并抵达明确完成场景。"],
    ),
    _item(
        "prompt-blender-v8-engine-model",
        "v8-repair-puzzle",
        "V8 Assembly Bay",
        "V8 装配工位",
        "puzzle",
        "3D",
        "third-person",
        "A detailed V8 engine becomes a playable disassembly, diagnosis, and repair puzzle rather than a passive model viewer.",
        "一台细致 V8 发动机被改造成拆解、诊断和维修解谜游戏，而不是被动模型浏览器。",
        ["Rotate, zoom, isolate, and explode a complete engine assembly with stable part selection.", "Remove and reinstall labeled blocks, heads, intake, pulleys, belts, and exhaust components in legal order.", "Diagnose randomized faults from motion, sound, heat, and inspection clues before choosing repairs.", "Reassemble, calibrate, and run a final test whose results expose missed or incorrect work."],
        ["稳定选择零件，并支持旋转、缩放、隔离和爆炸拆解完整发动机。", "按合法顺序拆装缸体、缸盖、进气、皮带轮、皮带和排气部件。", "根据运动、声音、热量和检查线索诊断随机故障，再选择维修方案。", "重新装配、校准并运行最终测试，结果会揭示遗漏或错误操作。"],
    ),
    _item(
        "prompt-multiplayer-voxel-browser-game",
        "voxel-shared-outpost",
        "Voxel Shared Outpost",
        "体素共享前哨",
        "survival",
        "3D",
        "first-person",
        "A small browser voxel world supports multi-tab local players who gather, build, and defend one synchronized outpost.",
        "一个小型浏览器体素世界支持多标签页本地玩家共同采集、建造并保卫同步前哨。",
        ["Move in first person through a generated voxel world with grounded collision and tool use.", "Place and remove blocks through valid range, inventory, and authoritative conflict rules.", "Synchronize player names, transforms, and block edits between tabs using BroadcastChannel with a solo fallback.", "Gather resources and cooperatively defend a shared objective before a timed extraction."],
        ["以第一人称穿越生成的体素世界，包含稳定碰撞和工具使用。", "根据有效距离、库存和权威冲突规则放置或移除方块。", "通过 BroadcastChannel 在标签页间同步玩家姓名、位置与方块编辑，并提供单人替代。", "采集资源并合作保卫共享目标，直至限时撤离。"],
    ),
    _item(
        "prompt-self-testing-apocalyptic-fps",
        "apocalyptic-fps",
        "Ashline City",
        "灰线之城",
        "shooter",
        "3D",
        "first-person",
        "A compact apocalyptic city FPS provides one complete objective through recognizable landmarks, scarce ammunition, and escalating enemies.",
        "一款紧凑末日城市 FPS，通过可辨识地标、稀缺弹药和不断升级的敌人提供完整目标。",
        ["Move, look, aim, fire, reload, and collide responsively in a compact first-person level.", "Fight several enemy types with readable telegraphs, damage, health, ammunition, and hit feedback.", "Navigate by recognizable procedural landmarks and complete a multi-step objective rather than a score-only arena.", "Reach a decisive win or loss state with accessible restart and preserved control guidance."],
        ["在紧凑第一人称关卡中实现响应灵敏的移动、观察、瞄准、射击、换弹和碰撞。", "对抗多种敌人，包含清楚预警、伤害、生命、弹药和命中反馈。", "通过可辨识程序化地标导航，并完成多步骤目标而不是纯刷分竞技场。", "抵达明确胜负状态，并提供易用重开和持续可见的操作指引。"],
    ),
    _item(
        "prompt-chameleon-hide-and-seek-game",
        "chameleon-hide-seek",
        "Chameleon Hide and Seek",
        "变色龙捉迷藏",
        "arcade",
        "2D",
        "top-down",
        "A chameleon blends into procedural color zones to evade a searching predator across three increasingly demanding rounds.",
        "一只变色龙融入程序化颜色区域，在三轮逐步升级的追捕中躲避捕食者。",
        ["Move through procedural hiding areas and sample or select nearby camouflage colors.", "Calculate detection from color match, movement, distance, cover, and predator attention.", "Show readable camouflage quality without relying on color alone and provide generated sound feedback.", "Run three fair rounds with scoring, escalating detection behavior, game over, and full restart."],
        ["穿过程序化藏身区域，并采样或选择附近的伪装颜色。", "根据颜色匹配、移动、距离、遮挡和捕食者注意计算暴露概率。", "清晰显示伪装质量，不能只依赖颜色，并提供程序化声音反馈。", "运行三轮公平且逐步升级的追捕，包含得分、结束和完整重开。"],
    ),
    _item(
        "prompt-browser-wuxia-rpg",
        "wuxia-valley-rpg",
        "Valley of the Two Techniques",
        "双式山谷",
        "rpg",
        "3D",
        "third-person",
        "A cohesive martial-arts RPG links a village, wilderness, responsive traversal, two combat techniques, weather, inventory, dialogue, and a final encounter.",
        "一款连贯武侠 RPG，把村庄、野外、灵敏移动、两种战技、天气、背包、对话和最终遭遇连接起来。",
        ["Explore one village, one wilderness route, and an enterable interior with responsive traversal.", "Fight with two distinct martial techniques, defensive timing, stamina, and readable enemy states.", "Complete a quest chain through NPC dialogue, inventory items, and world-state changes.", "Respond to weather and finish a final encounter that tests travel, combat, and quest decisions."],
        ["探索一座村庄、一条野外路线和可进入室内，并保持移动响应灵敏。", "使用两种不同战技、防御时机和体力系统战斗，敌人状态必须清楚。", "通过 NPC 对话、背包物品和世界状态变化完成任务链。", "应对天气，并完成同时检验移动、战斗和任务选择的最终遭遇。"],
    ),
]


class LiteralDumper(yaml.SafeDumper):
    """Render multiline strings as readable YAML blocks."""


def _represent_str(dumper: yaml.Dumper, value: str):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


LiteralDumper.add_representer(str, _represent_str)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _load_localizations() -> dict[str, dict[str, str]]:
    with AIGA_LOCALIZATIONS.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != EXPECTED_AIGA_VALID:
        raise ValueError(
            f"{AIGA_LOCALIZATIONS}: expected {EXPECTED_AIGA_VALID} rows, found {len(rows)}"
        )
    localizations = {row["world_id"]: row for row in rows}
    if len(localizations) != len(rows):
        raise ValueError(f"{AIGA_LOCALIZATIONS}: duplicate world_id")
    for world_id, row in localizations.items():
        for field in ("title_en", "title_zh", "vision_en", "vision_zh"):
            if not row[field].strip():
                raise ValueError(f"{AIGA_LOCALIZATIONS}: {world_id}.{field} is empty")
            _validate_no_ip(row[field], f"{world_id}.{field}")
    return localizations


def _import_fixed_manifest(
    path: Path,
    source_name: str,
    source_url: str,
    html_path: Path,
    items: list[dict[str, Any]],
    expected: int,
) -> None:
    if not html_path.is_file():
        raise FileNotFoundError(html_path)
    if len(items) != expected:
        raise ValueError(f"{source_name}: expected {expected} items, found {len(items)}")
    source_ids = [item["source_item"] for item in items]
    if len(source_ids) != len(set(source_ids)):
        raise ValueError(f"{source_name}: duplicate source item")
    payload = {
        "schema_version": 1,
        "source_name": source_name,
        "source_url": source_url,
        "source_capture_date": SOURCE_CAPTURE_DATE,
        "source_html_sha256": _sha256(html_path),
        "item_count": len(items),
        "note": (
            "Compact benchmark adaptations. Long page copy and media are not vendored; "
            "source identity and page hash preserve provenance."
        ),
        "items": items,
    }
    _write_json(path, payload)


def _sitemap_world_urls(sitemap_path: Path) -> dict[str, str]:
    root = ET.parse(sitemap_path).getroot()
    result: dict[str, str] = {}
    uuid_pattern = re.compile(
        r"(?P<world_id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$",
        re.IGNORECASE,
    )
    for node in root.iter():
        if not node.tag.endswith("loc") or not node.text or "/shared-worlds/" not in node.text:
            continue
        url = node.text.strip()
        match = uuid_pattern.search(url)
        if match:
            result[match.group("world_id").lower()] = url
    if len(result) != EXPECTED_AIGA_URLS:
        raise ValueError(
            f"{sitemap_path}: expected {EXPECTED_AIGA_URLS} world URLs, found {len(result)}"
        )
    return result


def _compact_world(world: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "worldId",
        "title",
        "description",
        "theme",
        "hero",
        "genre",
        "mode",
        "worldSize",
        "narrativeTone",
        "langCode",
        "readingAge",
        "availableArtStyles",
        "primaryBannerArtStyle",
        "primaryBannerImage",
        "bannerByStyle",
    )
    return {field: world[field] for field in fields if field in world}


def _import_aiga_manifest(
    sitemap_path: Path,
    index_html_path: Path,
    details_dir: Path,
) -> None:
    if not sitemap_path.is_file():
        raise FileNotFoundError(sitemap_path)
    if not index_html_path.is_file():
        raise FileNotFoundError(index_html_path)
    if not details_dir.is_dir():
        raise FileNotFoundError(details_dir)

    source_urls = _sitemap_world_urls(sitemap_path)
    localizations = _load_localizations()
    records = []
    valid_ids = set()
    for world_id, source_url in sorted(source_urls.items()):
        detail_path = details_dir / f"{world_id}.json"
        if not detail_path.is_file():
            raise FileNotFoundError(detail_path)
        raw = json.loads(detail_path.read_text(encoding="utf-8"))
        world = raw.get("world")
        is_valid = bool(
            isinstance(world, dict)
            and world.get("worldId") == world_id
            and world.get("title")
            and world.get("description")
        )
        record = {
            "world_id": world_id,
            "source_url": source_url,
            "source_api_url": f"{AIGA_API_ROOT}/{world_id}",
            "source_api_sha256": _sha256(detail_path),
            "valid": is_valid,
            "source_record": _compact_world(world or {}),
        }
        if is_valid:
            if world_id not in localizations:
                raise ValueError(f"{world_id}: missing reviewed localization")
            record["localized"] = {
                key: localizations[world_id][key]
                for key in ("title_en", "title_zh", "vision_en", "vision_zh")
            }
            valid_ids.add(world_id)
        else:
            record["invalid_reason"] = "detail API returned no world identity, title, or description"
        records.append(record)

    if valid_ids != set(localizations):
        raise ValueError(
            "AIGA localization set differs from valid detail set: "
            f"missing={sorted(valid_ids - set(localizations))}, "
            f"extra={sorted(set(localizations) - valid_ids)}"
        )
    valid_count = sum(record["valid"] for record in records)
    tombstone_count = len(records) - valid_count
    if valid_count != EXPECTED_AIGA_VALID or tombstone_count != EXPECTED_AIGA_TOMBSTONES:
        raise ValueError(
            f"AIGA expected {EXPECTED_AIGA_VALID} valid + {EXPECTED_AIGA_TOMBSTONES} "
            f"tombstone, found {valid_count} + {tombstone_count}"
        )

    payload = {
        "schema_version": 1,
        "source_name": "AIGA Shared Worlds",
        "source_index_url": AIGA_INDEX_URL,
        "source_capture_date": SOURCE_CAPTURE_DATE,
        "source_index_html_sha256": _sha256(index_html_path),
        "source_sitemap_url": "https://www.aiga.io/sitemap.xml",
        "source_sitemap_sha256": _sha256(sitemap_path),
        "catalog_url_count": len(records),
        "valid_world_count": valid_count,
        "tombstone_count": tombstone_count,
        "source_language_counts": dict(
            sorted(
                Counter(
                    (record["source_record"].get("langCode") or "unspecified")
                    for record in records
                    if record["valid"]
                ).items()
            )
        ),
        "note": (
            "All sitemap world detail URLs were requested. Valid world-definition fields, "
            "art-style references, source hashes, and one empty tombstone are retained."
        ),
        "worlds": records,
    }
    _write_json(AIGA_MANIFEST, payload)


def _import_crawls(args: argparse.Namespace) -> None:
    SOURCES_ROOT.mkdir(parents=True, exist_ok=True)
    _import_fixed_manifest(
        CNBLOGS_MANIFEST,
        "CNBlogs 20 browser game prompts",
        CNBLOGS_URL,
        args.cnblogs_html,
        CNBLOGS_ITEMS,
        EXPECTED_CNBLOGS,
    )
    _import_fixed_manifest(
        EVOLINK_MANIFEST,
        "EvoLink Kimi K3 Games & 3D prompts",
        EVOLINK_URL,
        args.evolink_html,
        EVOLINK_ITEMS,
        EXPECTED_EVOLINK,
    )
    _import_aiga_manifest(args.aiga_sitemap, args.aiga_index_html, args.aiga_details_dir)
    print(
        "imported source manifests: "
        f"{EXPECTED_CNBLOGS} CNBlogs + {EXPECTED_EVOLINK} EvoLink + "
        f"{EXPECTED_AIGA_VALID} valid AIGA worlds "
        f"(plus {EXPECTED_AIGA_TOMBSTONES} tombstone)"
    )


def _load_fixed_manifest(
    path: Path, expected: int, source_url: str
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    items = raw.get("items", [])
    if raw.get("source_url") != source_url:
        raise ValueError(f"{path}: source_url differs")
    if raw.get("item_count") != expected or len(items) != expected:
        raise ValueError(f"{path}: expected {expected} items")
    for item in items:
        if len(item.get("mechanics_en", [])) != 4:
            raise ValueError(f"{path}: {item.get('slug')} expected four English mechanics")
        if len(item.get("mechanics_zh", [])) != 4:
            raise ValueError(f"{path}: {item.get('slug')} expected four Chinese mechanics")
    return raw, items


def _load_aiga_manifest() -> dict[str, Any]:
    raw = json.loads(AIGA_MANIFEST.read_text(encoding="utf-8"))
    worlds = raw.get("worlds", [])
    valid = [world for world in worlds if world.get("valid")]
    tombstones = [world for world in worlds if not world.get("valid")]
    if (
        raw.get("catalog_url_count") != EXPECTED_AIGA_URLS
        or len(worlds) != EXPECTED_AIGA_URLS
        or raw.get("valid_world_count") != EXPECTED_AIGA_VALID
        or len(valid) != EXPECTED_AIGA_VALID
        or raw.get("tombstone_count") != EXPECTED_AIGA_TOMBSTONES
        or len(tombstones) != EXPECTED_AIGA_TOMBSTONES
    ):
        raise ValueError(f"{AIGA_MANIFEST}: unexpected AIGA counts")
    return raw


def _validate_no_ip(value: str, context: str) -> None:
    found = [
        term
        for term in BANNED_GENERATED_TERMS
        if re.search(rf"(?<![\w]){re.escape(term)}(?![\w])", value, flags=re.IGNORECASE)
    ]
    if found:
        raise ValueError(f"{context}: generated text contains branded terms {found}")


def _aiga_family(world: dict[str, Any]) -> str:
    source = world["source_record"]
    mode = source.get("mode")
    genre = source.get("genre")
    localized = world["localized"]
    signal = f"{localized['title_en']} {localized['vision_en']}".lower()
    if mode == "interactive-story":
        return "adventure"
    if any(word in signal for word in ("race", "racer", "rally", "circuit")):
        return "racing"
    if any(word in signal for word in ("tennis", "football", "basketball", "athlete")):
        return "sports"
    if genre in {"survival-horror", "horror", "cosmic-horror"}:
        return "horror"
    if any(
        word in signal
        for word in ("date", "wedding", "hearts", "romance", "relationship", "committee")
    ) or genre in {"romance", "romantic-comedy"}:
        return "narrative"
    if any(
        word in signal
        for word in ("architect", "idol", "singer", "band", "music", "academy: art", "logistics")
    ):
        return "simulation"
    if any(
        word in signal
        for word in ("fps", "marine", "stronghold breaker", "laser", "shooting")
    ):
        return "shooter"
    if mode == "open-world-kingpin" or any(
        word in signal
        for word in ("commander", "global panic", "control territory", "lead armies")
    ):
        return "strategy"
    if any(
        word in signal
        for word in ("fighter", "fists", "martial", "gladiator", "enforcer", "vigilante")
    ):
        return "action"
    if genre in {"survival", "post-apocalyptic"}:
        return "survival"
    if genre in {"high-fantasy", "dark-fantasy", "fantasy", "urban-fantasy", "romantic-fantasy"}:
        return "rpg"
    if genre == "comedy":
        return "narrative"
    if genre == "superhero":
        return "action"
    return "openworld"


def _aiga_features(world: dict[str, Any], language: str) -> list[str]:
    source = world["source_record"]
    mode = source.get("mode")
    title = world["localized"][f"title_{language}"]
    primary, pressures = AIGA_PRIMARY[world["family"]][language]
    if language == "en":
        if mode == "open-world-kingpin":
            return [
                f"Explore at least three connected districts or territories from {title}, each with distinct opportunities, hazards, and ownership state.",
                "Complete jobs through negotiation, trade, tactical conflict, or service to earn reputation with transparent gain and loss rules.",
                "Manage at least three factions whose trust, hostility, alliances, and control change after persistent player choices.",
                "Balance health, resources, influence, and attention while territory events continue to evolve without waiting for the player.",
                "Persist reputation, faction relations, owned or protected locations, depleted resources, and unresolved consequences across the whole run.",
                "Reach a playable influence milestone that combines territory, faction, resource, and reputation systems, then support continued play or a scored conclusion.",
            ]
        if mode == "interactive-story":
            return [
                f"Explore at least three connected story locations from {title} with direct movement, inspectable landmarks, and unlockable routes.",
                "Solve multiple spatial, sequence, or inventory puzzles whose state is represented in the rules layer.",
                "Talk with distinct characters and make choices that alter trust, available help, and later scene objectives.",
                "Collect or create meaningful objects that change navigation, puzzle solutions, or character outcomes.",
                "Persist discovered facts, relationships, changed locations, and completed favors so later scenes acknowledge earlier actions.",
                "Finish a playable final scene that combines exploration, puzzle, and relationship decisions into visibly different outcomes.",
            ]
        return [
            f"Explore at least three connected locations adapted from {title}, each with a landmark, local objective, hazard, and unlockable route.",
            primary,
            "Introduce distinct characters or factions whose schedules, trust, hostility, and available help respond to player behavior.",
            pressures,
            "Persist discoveries, relationships, altered locations, depleted resources, and unresolved consequences throughout the run.",
            "Conclude with a mastery objective or confrontation that combines traversal, the primary challenge, relationships, and accumulated world state.",
        ]

    if mode == "open-world-kingpin":
        return [
            f"探索《{title}》中的至少三个相连城区或领地，每处都有不同机会、危险和归属状态。",
            "通过谈判、贸易、战术冲突或服务完成差事，并用透明规则获得或失去声望。",
            "管理至少三个派系，其信任、敌意、联盟和控制权会在玩家选择后持续变化。",
            "平衡健康、资源、影响力和警觉度，领地事件会在玩家不介入时继续演化。",
            "在整局中持续保存声望、派系关系、占有或保护地点、消耗资源与未解决后果。",
            "抵达同时检验领地、派系、资源和声望系统的可玩影响力里程碑，并支持继续游玩或计分结局。",
        ]
    if mode == "interactive-story":
        return [
            f"探索《{title}》中的至少三个相连故事地点，支持直接移动、检查地标和解锁路线。",
            "解决多种空间、顺序或背包谜题，其状态必须存在于规则层。",
            "与不同角色交谈，选择会改变信任、可用帮助和后续场景目标。",
            "收集或制作会改变导航、谜题解法或角色结局的重要物品。",
            "持续保存已发现事实、关系、改变地点和完成的人情，让后续场景承认早期行动。",
            "以可玩的最终场景收束，把探索、谜题和关系决定组合成明显不同的结果。",
        ]
    return [
        f"探索由《{title}》改写的至少三个相连地点，每处都有地标、局部目标、危险和可解锁路线。",
        primary,
        "加入不同角色或派系，其日程、信任、敌意和可用帮助会响应玩家行为。",
        pressures,
        "整局持续保存发现、关系、地点变化、资源消耗和未解决后果。",
        "以综合目标或对峙结束，同时检验移动、主要挑战、角色关系和累积世界状态。",
    ]


def _fixed_features(item: dict[str, Any], language: str) -> list[str]:
    mechanics = item[f"mechanics_{language}"]
    if language == "en":
        return mechanics + [
            "Provide at least three functionally distinct content variations that change timing, route choice, resource use, or risk rather than only labels and colors.",
            "Use a three-stage arc that teaches the core interaction, combines systems under pressure, and ends in a complete win, loss, or scored completion loop.",
        ]
    return mechanics + [
        "提供至少三种功能不同的内容变化，实质改变时机、路线、资源使用或风险，不能只更换标签和颜色。",
        "使用三阶段短流程：教学核心交互、在压力下组合系统，并以完整胜利、失败或计分完成闭环收束。",
    ]


def _presentation_contract(family: str, dimension: str, language: str) -> str:
    # The shared v0.6 contract keeps generated source families in sync with the
    # migrated checked-in task pool.
    return render_contract(
        language,
        family,
        dimension,
    )


def _prompt(item: dict[str, Any], language: str) -> str:
    title = item[f"title_{language}"]
    vision = item[f"vision_{language}"]
    family = item["family"]
    dimension = item["dimension"]
    features = item[f"features_{language}"]
    art = ART_DIRECTION[family][language]
    perspective = item["perspective"].replace("-", " ")
    if language == "en":
        numbered = "\n".join(
            f"{index}. **System {index}** - {feature}"
            for index, feature in enumerate(features, 1)
        )
        source_context = ""
        if item["source_group"] == "aiga":
            source = item["source_record"]
            source_context = (
                "\n\n## World Parameters\n\n"
                f"Treat this as an original adaptation of a **{source.get('genre') or 'genre-blended'}** "
                f"shared world with **{source.get('worldSize') or 'medium'}** scope and a "
                f"**{source.get('narrativeTone') or 'responsive'}** tone. Do not reproduce "
                "commercial characters, names, lore, logos, or protected visual designs."
            )
        return f"""\
# {title}

Build a complete, playable **{dimension} {FAMILY_LABELS[family]["en"]} game** as
a polished browser vertical slice from a **{perspective}** viewpoint.

## Core Vision

{vision}{source_context}

## Required Playable Systems

{numbered}

## Progression and Persistent State

Use a short three-stage arc. Introduce the central interaction, combine it with
world pressure and meaningful choices, then finish with a mastery scenario.
Important rules, objectives, resources, relationships, selection state, danger,
progress, and outcome must be visible in stable HUD regions and represented in
`game_logic.js`. Systems must share state instead of appearing as disconnected
buttons, menus, or visual demonstrations.

## Art Direction

{art}

{_presentation_contract(family, dimension, "en")}""".strip()

    numbered = "\n".join(
        f"{index}. **系统 {index}** - {feature}"
        for index, feature in enumerate(features, 1)
    )
    source_context = ""
    if item["source_group"] == "aiga":
        source = item["source_record"]
        genre = GENRE_ZH.get(source.get("genre"), "混合类型")
        world_size = WORLD_SIZE_ZH.get(source.get("worldSize"), "中型")
        tone = TONE_ZH.get(source.get("narrativeTone"), "响应式")
        source_context = (
            "\n\n## 世界参数\n\n"
            f"把它作为原创的 **{genre}** 共享世界改写，范围为 **{world_size}**，"
            f"叙事基调为 **{tone}**。不得复刻商业角色、"
            "名称、设定、标志或受保护的视觉设计。"
        )
    return f"""\
# {title}

制作一个完整可玩的 **{dimension} {FAMILY_LABELS[family]["zh"]}游戏**，以
**{PERSPECTIVE_ZH[item["perspective"]]}** 呈现为经过打磨的浏览器纵向切片。

## 核心构想

{vision}{source_context}

## 必须实现的可玩系统

{numbered}

## 推进与持久状态

使用三个阶段组成短流程：先清楚引入中心交互，再与世界压力和有意义选择组合，最后用
综合场景检验掌握程度。重要规则、目标、资源、关系、选择状态、危险、进度和结果必须
显示在稳定 HUD 区域，并在 `game_logic.js` 中有对应状态。各系统必须通过共享状态
互相影响，不能只是彼此割裂的按钮、菜单或视觉演示。

## 美术方向

{art}

{_presentation_contract(family, dimension, "zh")}""".strip()


def _requirement(req_id: str, description: str, category: str) -> dict[str, Any]:
    if category == "mechanic":
        suffix = (
            " Score 0 if the system is absent, decorative, or cannot be completed "
            "through player input. Score 1 requires the full interaction and its "
            "success/failure consequences in one playable flow."
        )
        agg = "max"
    elif category == "depth":
        suffix = (
            " Score 0 if this content is missing or differs only through labels or "
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
        if req_id == "A1":
            suffix += (
                " Full credit may be earned with runtime-authored procedural textures, "
                "layered materials, deliberate multi-light rigs, particles, synthesized "
                "audio, or post-processing; external asset files are not required."
            )
        agg = "mean"
    return {"id": req_id, "agg": agg, "description": description + suffix}


def _rubric(item: dict[str, Any]) -> dict[str, Any]:
    features = item["features_en"]
    family = item["family"]
    requirements = [
        _requirement("M1", features[0], "mechanic"),
        _requirement("M2", features[1], "mechanic"),
        _requirement("M3", features[2], "mechanic"),
        _requirement("D1", features[3], "depth"),
        _requirement("D2", features[4], "depth"),
        _requirement("D3", features[5], "depth"),
        _requirement(
            "D4",
            "A three-stage progression teaches the core interaction, combines systems "
            "under pressure, and ends with a mastery scenario plus working replay.",
            "depth",
        ),
        _requirement(
            "V1",
            "The HUD clearly communicates current objective, critical resources, "
            "selected target or mode, relationships, progress, and danger in stable regions.",
            "experience",
        ),
        _requirement(
            "V2",
            "Every important action has immediate and distinguishable feedback for valid "
            "input, invalid input, success, damage or failure, and persistent state change.",
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
            "The project has a coherent authored art direction: " + ART_DIRECTION[family]["en"],
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
            "Interactive actors, targets, hazards, tools, locations, and UI symbols have "
            "readable silhouettes and visibly different functional states.",
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


def _provenance(item: dict[str, Any], language: str) -> dict[str, Any]:
    if item["source_group"] == "cnblogs":
        return {
            "kind": "adapted_cnblogs_prompt",
            "source_name": "CNBlogs 20 browser game prompts",
            "source_url": CNBLOGS_URL,
            "source_item": item["source_item"],
            "source_html_sha256": item["source_html_sha256"],
        }
    if item["source_group"] == "evolink":
        return {
            "kind": "adapted_evolink_prompt",
            "source_name": "EvoLink Kimi K3 Games & 3D prompts",
            "source_url": EVOLINK_URL,
            "source_prompt_id": item["source_item"],
            "source_html_sha256": item["source_html_sha256"],
        }
    source = item["source_record"]
    return {
        "kind": "adapted_aiga_shared_world",
        "source_name": "AIGA Shared Worlds",
        "source_index_url": AIGA_INDEX_URL,
        "source_url": item["source_url"],
        "source_api_url": item["source_api_url"],
        "source_world_id": item["world_id"],
        "source_title": source.get("title"),
        "source_language": source.get("langCode"),
        "source_genre": source.get("genre"),
        "source_mode": source.get("mode"),
        "source_api_sha256": item["source_api_sha256"],
        "source_sitemap_sha256": item["source_sitemap_sha256"],
        "adaptation_language": language,
    }


def _task_yaml(item: dict[str, Any], language: str, prompt: str) -> dict[str, Any]:
    base_id = item["base_id"]
    task_id = f"{base_id}-{language}"
    difficulty = classify_difficulty(item["family"], _prompt(item, "en"))
    return {
        "id": task_id,
        "title": item[f"title_{language}"] + LANGUAGE_SUFFIX[language],
        "family": item["family"],
        "difficulty": difficulty,
        "engine": "html",
        "language": language,
        "base_task_id": base_id,
        "provenance": _provenance(item, language),
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
                "rubric": "Core requested systems are implemented and connected.",
            },
            {
                "id": "richness",
                "weight": 0.35,
                "max": 5,
                "anchors": RUBRIC_MAPPING["richness"],
                "rubric": "Content variety, escalation, persistence, and meaningful choices.",
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
                "rubric": "Coherent authored art direction, functional composition, effects, and motion polish.",
            },
        ],
    }


def _render_files(item: dict[str, Any], language: str) -> dict[str, str]:
    prompt = _prompt(item, language)
    _validate_no_ip(prompt, f"{item['base_id']}.{language}.prompt")
    task_id = f"{item['base_id']}-{language}"
    task_yaml = clean_yaml(
        yaml.dump(
            _task_yaml(item, language, prompt),
            Dumper=LiteralDumper,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        )
    )
    return {
        f"{task_id}.task.yaml": task_yaml,
        "prompt.md": prompt + "\n",
        "rubric.mapping.json": json.dumps(RUBRIC_MAPPING, ensure_ascii=False, indent=2) + "\n",
        "rubric.original.json": json.dumps(_rubric(item), ensure_ascii=False, indent=2) + "\n",
    }


def _normalized_catalog() -> list[dict[str, Any]]:
    cnblogs_meta, cnblogs_items = _load_fixed_manifest(
        CNBLOGS_MANIFEST, EXPECTED_CNBLOGS, CNBLOGS_URL
    )
    evolink_meta, evolink_items = _load_fixed_manifest(
        EVOLINK_MANIFEST, EXPECTED_EVOLINK, EVOLINK_URL
    )
    aiga = _load_aiga_manifest()
    catalog: list[dict[str, Any]] = []

    for source_group, meta, items in (
        ("cnblogs", cnblogs_meta, cnblogs_items),
        ("evolink", evolink_meta, evolink_items),
    ):
        prefix = "mz_cnblogs" if source_group == "cnblogs" else "mz_evolink"
        for index, item in enumerate(items, 1):
            normalized = dict(item)
            normalized.update(
                {
                    "source_group": source_group,
                    "source_html_sha256": meta["source_html_sha256"],
                    "base_id": f"{prefix}-{index:02d}-{item['slug']}",
                    "features_en": _fixed_features(item, "en"),
                    "features_zh": _fixed_features(item, "zh"),
                }
            )
            catalog.append(normalized)

    for world in aiga["worlds"]:
        if not world.get("valid"):
            continue
        localized = world["localized"]
        family = _aiga_family(world)
        normalized = {
            **world,
            **localized,
            "source_group": "aiga",
            "source_sitemap_sha256": aiga["source_sitemap_sha256"],
            "base_id": f"mz_aiga-world-{world['world_id'][:8]}",
            "family": family,
            "dimension": "3D",
            "perspective": "third-person",
        }
        normalized["features_en"] = _aiga_features(normalized, "en")
        normalized["features_zh"] = _aiga_features(normalized, "zh")
        catalog.append(normalized)

    expected = EXPECTED_CNBLOGS + EXPECTED_EVOLINK + EXPECTED_AIGA_VALID
    if len(catalog) != expected:
        raise ValueError(f"expected {expected} normalized concepts, found {len(catalog)}")
    base_ids = [item["base_id"] for item in catalog]
    if len(base_ids) != len(set(base_ids)):
        duplicates = [key for key, count in Counter(base_ids).items() if count > 1]
        raise ValueError(f"duplicate base IDs: {duplicates}")
    for item in catalog:
        if item["family"] not in FAMILY_LABELS:
            raise ValueError(f"{item['base_id']}: unsupported family {item['family']}")
        for field in ("title_en", "title_zh", "vision_en", "vision_zh"):
            _validate_no_ip(item[field], f"{item['base_id']}.{field}")
        if len(item["features_en"]) != 6 or len(item["features_zh"]) != 6:
            raise ValueError(f"{item['base_id']}: expected six bilingual features")
    return catalog


def _validate_or_write(write: bool) -> tuple[int, int]:
    catalog = _normalized_catalog()
    created = 0
    validated = 0
    for item in catalog:
        for language in LANGUAGE_SUFFIX:
            task_id = f"{item['base_id']}-{language}"
            task_dir = TASKS_ROOT / task_id
            expected = _render_files(item, language)
            if not task_dir.exists():
                if not write:
                    raise FileNotFoundError(
                        f"{task_dir} is missing; rerun with --write to create tasks"
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
    parser.add_argument("--import-crawls", action="store_true")
    parser.add_argument(
        "--cnblogs-html",
        type=Path,
        default=Path("/tmp/cnblogs_20_prompts.html"),
    )
    parser.add_argument(
        "--evolink-html",
        type=Path,
        default=Path("/tmp/evolink_kimi_k3_prompts.html"),
    )
    parser.add_argument(
        "--aiga-sitemap",
        type=Path,
        default=Path("/tmp/aiga_sitemap.xml"),
    )
    parser.add_argument(
        "--aiga-index-html",
        type=Path,
        default=Path("/tmp/aiga_shared_worlds.html"),
    )
    parser.add_argument(
        "--aiga-details-dir",
        type=Path,
        default=Path("/tmp/aiga_public_world_details"),
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)

    if args.import_crawls:
        _import_crawls(args)
        if not args.write:
            return 0
    created, validated = _validate_or_write(args.write)
    concepts = EXPECTED_CNBLOGS + EXPECTED_EVOLINK + EXPECTED_AIGA_VALID
    print(
        f"three-source tasks valid: {concepts} concepts x 2 languages = "
        f"{validated} tasks ({created} created)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
