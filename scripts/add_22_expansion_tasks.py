"""Add 22 new game concepts as 44 independent English/Chinese benchmark tasks.

The first 12 concepts adapt the campaign seeds from the AIGA article supplied by
the benchmark author. The remaining 10 concepts adapt prompts supplied directly
by the benchmark author. All task wording and rubrics are authored for this
benchmark rather than copied verbatim from either source.

Run with ``--write`` to create missing task directories. Running without the flag
validates that all generated files still match this catalog.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from task_metadata import classify_difficulty


ROOT = Path(__file__).resolve().parent.parent
TASKS_ROOT = ROOT / "bench" / "tasks"
AIGA_SOURCE_URL = "https://www.aiga.io/zh/blog/ai-rpg-prompts-playable-campaigns"
LANGUAGES = {
    "en": " (English)",
    "zh": " (中文)",
}
FAMILY_LABELS = {
    "en": {
        "openworld": "open-world adventure",
        "puzzle": "puzzle",
        "rhythm": "rhythm-action",
        "simulation": "simulation",
        "strategy": "strategy",
    },
    "zh": {
        "openworld": "开放世界冒险",
        "puzzle": "解谜",
        "rhythm": "节奏动作",
        "simulation": "模拟",
        "strategy": "策略",
    },
}

COMMON_EN = """\
## HTML Submission Format

Deliver a self-contained 3D browser game in two files:

- `index.html` - the complete playable presentation, rendered with Three.js.
- `game_logic.js` - the deterministic state and rules layer, exporting
  `createGame(opts)` and `advance(game, input, dt)`.

The page must open without a build step or local server and render within three
seconds on a normal laptop. Use procedural geometry, shaders, particles, generated
audio, and CSS; do not fetch external images, models, video, or audio at runtime.
Three.js may be loaded from its official CDN. Any additional library explicitly
required by this task may also be loaded from a pinned CDN URL.

Support keyboard controls and the pointer. Touch or device-sensor controls may be
added where appropriate, but must have a desktop fallback. Keep the main game
readable at 1280x720. Include a styled title screen, short in-game guidance, pause
or restart controls, a complete win/loss or completion loop, and visible feedback
for every important action. This must feel like a polished vertical slice rather
than a passive scene or disconnected technical demo.

`index.html` must not use `fetch()` or `XMLHttpRequest`. Keep `index.html` under
160 KB and `game_logic.js` under 320 lines.
"""

COMMON_ZH = """\
## HTML 提交格式

用两个文件交付一个可独立运行的 3D 浏览器游戏：

- `index.html` - 使用 Three.js 完成全部可玩呈现。
- `game_logic.js` - 确定性的状态与规则层，导出 `createGame(opts)` 和
  `advance(game, input, dt)`。

页面不能依赖构建步骤或本地服务器，普通笔记本应在三秒内完成首屏渲染。使用程序化
几何体、着色器、粒子、合成音频和 CSS；运行时不得获取外部图片、模型、视频或音频。
Three.js 可以从官方 CDN 加载；若本题明确要求其他库，也可以使用固定版本的 CDN。

必须支持键盘和鼠标。可按题目需要加入触摸或设备传感器控制，但必须提供桌面端替代
方案。主游戏在 1280x720 下应清晰可读。需要有经过设计的标题画面、简短的游戏内引导、
暂停或重新开始控制、完整的胜负或完成闭环，以及每项关键操作的明确反馈。最终结果应当
是打磨过的纵向切片，而不是被动场景或彼此割裂的技术演示。

`index.html` 不得使用 `fetch()` 或 `XMLHttpRequest`。`index.html` 控制在
160 KB 以内，`game_logic.js` 控制在 320 行以内。
"""

RUBRIC_MAPPING = {
    "completeness": ["M1", "M2", "M3"],
    "richness": ["D1", "D2", "D3", "D4"],
    "player_exp": ["V1", "V2", "V3"],
    "visual": ["A1", "A2", "A3", "A4"],
}


CATALOG = [
    {
        "slug": "mz_openworld-missing-second",
        "title_en": "The Missing Second",
        "title_zh": "消失的一秒",
        "family": "openworld",
        "source_item": "01",
        "vision_en": "A compact open-city investigation game about a superhero who vanished during one impossible missing second. The player patrols several connected districts, reconstructs frozen incidents, and decides whether the city's celebrated rescue was actually a coordinated cover-up.",
        "vision_zh": "一款紧凑的开放城市调查游戏：一名超级英雄在无法解释的“一秒空白”中失踪。玩家巡查多个相连城区，重建被冻结的事件现场，并判断那场广受赞誉的救援是否其实是一场协同掩盖。",
        "features_en": [
            "Explore at least three connected city districts, move freely between rooftops and streets, and locate temporal anomaly scenes through a scanner.",
            "Reconstruct each missing-second scene by rotating a time echo, matching evidence positions, and locking a plausible sequence before the timer expires.",
            "Interview witnesses whose testimony changes with trust and discovered evidence, then connect clues on an interactive conspiracy board.",
            "Include multiple anomaly types, such as displaced vehicles, duplicated civilians, frozen projectiles, and corrupted security drones.",
            "Track public trust and institutional suspicion; accusations, leaked evidence, and reckless scanning must change NPC reactions and available routes.",
            "End with a playable confrontation where the player selects and proves one of several theories, producing visibly different city outcomes.",
        ],
        "features_zh": [
            "探索至少三个相连城区，可在屋顶和街道间自由移动，并通过扫描器定位时间异常现场。",
            "旋转时间残影、匹配证据位置，在倒计时结束前锁定合理事件顺序，以重建每个“消失的一秒”。",
            "询问证人；其证词会随信任度和已发现证据变化，再把线索连接到可交互的阴谋板上。",
            "加入多种异常：错位车辆、重复市民、冻结弹体和被污染的安保无人机等。",
            "追踪公众信任与机构警觉；指控、泄密和鲁莽扫描会改变 NPC 反应与可用路线。",
            "以可玩的最终对峙收束，玩家选择并证明多个理论之一，城市结局必须明显不同。",
        ],
        "progression_en": "Solving district cases upgrades scan range and time-echo control, opens restricted locations, and unlocks increasingly complex reconstructions.",
        "art_en": "A rain-slick near-future metropolis with cyan forensic projections, amber street lighting, graphic-novel shadows, and sharp temporal fracture effects.",
    },
    {
        "slug": "mz_openworld-vanta-last-broadcast",
        "title_en": "Last Broadcast from Vanta",
        "title_zh": "来自万塔的最后广播",
        "family": "openworld",
        "source_item": "02",
        "vision_en": "A lonely space-exploration campaign across a small star system. The player pilots a salvage vessel toward a dead colony's repeating emergency signal while storms, failing systems, and contradictory recordings turn navigation into a survival mystery.",
        "vision_zh": "一场横跨小型恒星系的孤寂太空探索战役。玩家驾驶打捞船追踪一座死亡殖民地反复播出的求救信号；风暴、故障系统和互相矛盾的录音让导航逐渐变成生存谜案。",
        "features_en": [
            "Pilot a ship across a navigable star map with manual thrust, docking, scanning, and at least three explorable orbital locations.",
            "Tune a multi-band receiver to isolate fragments of the Vanta broadcast while interference and false echoes obscure the correct signal.",
            "Manage hull, power, fuel, and heat by rerouting ship systems during radiation storms and debris encounters.",
            "Recover logs and physical evidence from derelicts, then arrange them on a timeline that changes the meaning of the final message.",
            "Include hazards and optional rescues that force tradeoffs between mission progress, crew safety, and dwindling resources.",
            "Reach Vanta and complete one of several playable approaches to the beacon, with different discoveries and endings.",
        ],
        "features_zh": [
            "在可导航星图中驾驶飞船，支持手动推进、停靠、扫描，并提供至少三个可探索轨道地点。",
            "调节多频段接收器以分离万塔广播片段，同时处理干扰和伪回波对正确信号的遮蔽。",
            "在辐射风暴和碎片遭遇中重分配系统，管理船体、电力、燃料与热量。",
            "从废弃飞船中回收日志和实物证据，再把它们排列到时间线上，从而改变最终信息的含义。",
            "加入危险与可选救援，在任务进度、船员安全和不断减少的资源之间制造取舍。",
            "抵达万塔并以多种可玩方式接近信标，不同方案应揭示不同真相与结局。",
        ],
        "progression_en": "Recovered components improve engines, scanner precision, and power capacity, enabling access to harsher regions and deeper signal layers.",
        "art_en": "Hard-sci-fi solitude: dark planetary silhouettes, instrument-lit interiors, volumetric signal waves, electrical arcs, and pale emergency beacons.",
    },
    {
        "slug": "mz_openworld-aurora-final-audition",
        "title_en": "Final Audition at Aurora Studio",
        "title_zh": "极光片场的最后试镜",
        "family": "openworld",
        "source_item": "03",
        "vision_en": "A supernatural exploration game set across an abandoned film studio. The player is an actor summoned for one final audition and must traverse connected sound stages where unfinished scenes replay themselves and the studio evaluates every performance.",
        "vision_zh": "一款发生在废弃电影片场的超自然探索游戏。玩家是一名被召来参加最后试镜的演员，需要穿过相连摄影棚；未完成的场景会自行重演，而片场会评判玩家的每次表演。",
        "features_en": [
            "Explore a studio backlot with at least three themed stages, backstage corridors, prop storage, and unlockable shortcuts.",
            "Perform interactive audition scenes by hitting movement, dialogue, lighting, and camera marks in the correct dramatic sequence.",
            "Manipulate rotating sets, spotlights, curtains, and practical effects to reveal paths and appease or provoke the studio presence.",
            "Meet spectral cast members with distinct motives and recover production notes that alter scene objectives.",
            "Track composure and audience approval; mistakes should distort sets, summon hazards, or rewrite the current scene.",
            "Complete a final live take that combines previous mechanics and branches according to the roles and truths the player accepted.",
        ],
        "features_zh": [
            "探索片场外景区，包含至少三个主题摄影棚、后台走廊、道具库和可解锁捷径。",
            "通过按正确戏剧顺序完成走位、台词、灯光和镜头标记，参与可交互的试镜场景。",
            "操纵旋转布景、聚光灯、幕布与实景特效，揭示道路并安抚或激怒片场中的存在。",
            "遇见动机各异的幽灵演员，并回收会改变场景目标的制作笔记。",
            "追踪镇定值与观众认可；失误会扭曲布景、召来危险或重写当前场景。",
            "完成结合此前机制的最终实拍，结局根据玩家接受的角色与真相发生分支。",
        ],
        "progression_en": "Successful takes earn role tokens that unlock new stage controls, costumes with abilities, and access to the sealed director's wing.",
        "art_en": "Decaying golden-age cinema with dusty spotlights, velvet reds, monochrome projections, painted backdrops, and theatrical supernatural transitions.",
    },
    {
        "slug": "mz_openworld-last-reservoir",
        "title_en": "The Last Reservoir",
        "title_zh": "最后的水库",
        "family": "openworld",
        "source_item": "04",
        "vision_en": "A drought-management exploration game around the final functioning reservoir. The player travels between settlements, inspects infrastructure, and returns to a council chamber to allocate water before climate events turn political compromise into physical survival.",
        "vision_zh": "一款围绕最后一座可用水库展开的干旱管理探索游戏。玩家往返各聚居地、检查基础设施，再回到议事厅分配水源；气候事件会把政治妥协变成真实的生存问题。",
        "features_en": [
            "Explore the reservoir basin and at least four connected districts, inspecting pumps, canals, wells, farms, and damaged treatment equipment.",
            "Operate a physical water-control board with valves and allocation sliders that visibly redirect animated flow through the 3D map.",
            "Balance reservoir volume, contamination, pressure, and district demand across a changing multi-day forecast.",
            "Negotiate with factions whose needs and trust change based on inspections, promises, shortages, and previous allocations.",
            "Respond to fires, pipe failures, dust storms, and illegal tapping through timed field missions and emergency rerouting.",
            "Finish with a council vote and final drought event whose playable outcome reflects both infrastructure and social legitimacy.",
        ],
        "features_zh": [
            "探索水库流域及至少四个相连地区，检查水泵、运河、水井、农田和受损净化设备。",
            "操作带阀门与分配滑块的实体水控台，让水流在 3D 地图中以动画方式重新定向。",
            "在不断变化的多日预报中平衡库容、污染、压力和各地区需求。",
            "与多个派系谈判；其需求与信任会根据检查结果、承诺、短缺和历史分配变化。",
            "通过限时野外任务与紧急改道处理火灾、爆管、沙尘暴和非法取水。",
            "以议会投票和最终干旱事件结束，其可玩结果同时取决于基础设施与社会合法性。",
        ],
        "progression_en": "Repairs and negotiated agreements unlock efficient infrastructure, better forecasts, and new allocation options while permanently changing district resilience.",
        "art_en": "A sun-bleached low-poly basin with cracked earth, turquoise flow overlays, weathered civic machinery, heat haze, and urgent red emergency lighting.",
    },
    {
        "slug": "mz_openworld-forgotten-students",
        "title_en": "Academy of Forgotten Students",
        "title_zh": "被遗忘学生的学院",
        "family": "openworld",
        "source_item": "05",
        "vision_en": "A magical campus mystery where students are being erased from records and memory. The player freely explores halls, towers, gardens, and sealed archives, preserving unstable memories before the academy rewrites itself around each disappearance.",
        "vision_zh": "一场魔法校园谜案：学生正从档案和记忆中被抹去。玩家自由探索大厅、高塔、花园与封闭档案库，在学院随失踪事件自我改写之前保存不稳定的记忆。",
        "features_en": [
            "Explore at least four connected campus zones with day/night schedules, moving stairways, secret doors, and student routines.",
            "Use a memory lens to reveal erased people, reconstruct shared moments, and pin unstable memories before they dissolve.",
            "Cross-reference portraits, attendance ledgers, dorm objects, and witness recollections in a searchable archive interface.",
            "Build trust with rival student groups whose memories conflict and whose cooperation opens different investigation routes.",
            "Avoid or confront corrective magical entities that alter corridors and remove collected evidence when the player is detected.",
            "Identify the erasure mechanism and choose whom or what to restore in a final ritual with multiple campus-wide outcomes.",
        ],
        "features_zh": [
            "探索至少四个相连校园区域，包含昼夜日程、移动楼梯、秘密门和学生行动规律。",
            "使用记忆透镜显现被抹去的人、重建共同经历，并在不稳定记忆消散前将其固定。",
            "在可搜索档案界面中交叉核对肖像、考勤簿、宿舍物件和证人回忆。",
            "与互相竞争的学生团体建立信任；其记忆彼此冲突，合作会开启不同调查路线。",
            "躲避或对抗纠正性魔法实体；玩家被发现时，它们会改变走廊并移除已收集证据。",
            "识别抹除机制，并在最终仪式中决定恢复谁或什么，形成多种影响整个校园的结局。",
        ],
        "progression_en": "Preserved memories strengthen the lens, reveal deeper historical layers, and unlock spells for stabilizing spaces and protecting evidence.",
        "art_en": "Whimsical gothic academia with luminous ink, moving portraits, moonlit courtyards, impossible staircases, and dissolving paper-particle memory effects.",
    },
    {
        "slug": "mz_openworld-solarline-rally",
        "title_en": "Solarline Rally",
        "title_zh": "太阳线拉力赛",
        "family": "openworld",
        "source_item": "06",
        "vision_en": "A solar-system racing adventure built around route choice rather than a single closed track. The player pilots a modular racer between orbital gates, balances heat and fuel, encounters rivals, and decides how much danger or compromise is acceptable to reach the final line.",
        "vision_zh": "一场以路线选择而非单一封闭赛道为核心的太阳系竞速冒险。玩家驾驶模块化赛车穿越轨道门，平衡热量与燃料，遭遇对手，并决定为抵达终点愿意承担多少风险或妥协。",
        "features_en": [
            "Drive or fly a responsive 3D racer across at least three planetary regions with drifting, boost, braking, jumps, and checkpoint validation.",
            "Choose branching routes on a navigable system map, trading distance against storms, gravity wells, tolls, and repair opportunities.",
            "Manage fuel, battery, hull, and engine heat; overboosting must create visible performance loss and possible breakdown.",
            "Race distinct rivals with recognizable vehicles and tactics, including drafting, blocking, shortcuts, and opportunistic rescues.",
            "Collect sponsors, upgrades, and route intelligence through optional events that create meaningful mechanical tradeoffs.",
            "Complete a multi-leg championship with standings, stage results, rival consequences, and at least two final outcomes.",
        ],
        "features_zh": [
            "在至少三个行星区域驾驶或飞行响应灵敏的 3D 赛车，支持漂移、加速、制动、跳跃和检查点判定。",
            "在可导航星系图上选择分支路线，在距离、风暴、引力井、通行费和维修机会之间权衡。",
            "管理燃料、电池、船体和引擎热量；过度加速必须造成可见性能下降甚至故障。",
            "与拥有可辨识载具和策略的对手竞速，包括尾流、封堵、捷径和机会性救援。",
            "通过可选事件获取赞助商、升级和路线情报，并形成有意义的机械取舍。",
            "完成多赛段锦标赛，包含积分榜、赛段结果、对手后果和至少两种最终结局。",
        ],
        "progression_en": "Between legs, players install mutually exclusive modules that alter handling, efficiency, durability, scanning, or boost behavior.",
        "art_en": "Bright retro-futurist motorsport with saturated planetary skies, holographic gates, heat trails, modular vehicles, and readable cosmic route graphics.",
    },
    {
        "slug": "mz_openworld-weather-vane-house",
        "title_en": "The Winter Clause",
        "title_zh": "风向标宅邸的冬季条款",
        "family": "openworld",
        "source_item": "07",
        "vision_en": "A winter survival mystery inside and around a sprawling family estate. A will-reading locks the heirs in during an unnatural freeze, and the player must explore the house, manage heat, observe family routines, and uncover which clause controls the weather.",
        "vision_zh": "一场发生在庞大家族宅邸内外的冬季生存谜案。遗嘱宣读后，继承人被异常严寒困住；玩家必须探索宅邸、管理热量、观察家族日程，并找出究竟哪条遗嘱条款在控制天气。",
        "features_en": [
            "Explore a multi-floor mansion, greenhouse, frozen grounds, service tunnels, and weather-vane tower with unlockable shortcuts.",
            "Manage room temperature by operating boilers, vents, fireplaces, shutters, and power circuits while fuel remains limited.",
            "Observe and question family members whose schedules, alliances, and access permissions change after each discovered clause.",
            "Solve inheritance puzzles using portraits, keys, legal documents, mechanical locks, and environmental temperature states.",
            "Survive escalating cold effects such as frozen doors, brittle floors, blackouts, and blizzard exposure during exterior trips.",
            "Reach the weather-vane mechanism and enforce, reinterpret, or destroy the final clause, producing different family outcomes.",
        ],
        "features_zh": [
            "探索多层宅邸、温室、冰封庭院、佣人地道和风向标塔，并解锁捷径。",
            "在燃料有限的情况下操作锅炉、通风口、壁炉、百叶窗和电路，管理各房间温度。",
            "观察并询问家族成员；每发现一条条款，其日程、联盟和通行权限都会变化。",
            "利用肖像、钥匙、法律文件、机械锁和环境温度状态解决继承谜题。",
            "应对不断升级的严寒影响，如冻结门、脆裂地板、停电和外出时的暴风雪暴露。",
            "抵达风向标机构，执行、重新解释或摧毁最终条款，形成不同家族结局。",
        ],
        "progression_en": "Recovered clauses and repaired heating zones expand safe exploration time, reveal hidden wings, and grant leverage in family negotiations.",
        "art_en": "A snowbound gothic manor with warm candle interiors, icy blue encroachment, brass heating machinery, stained glass, and wind-driven snow effects.",
    },
    {
        "slug": "mz_openworld-every-road-midnight",
        "title_en": "Every Road Returns Before Midnight",
        "title_zh": "每条路都在午夜前回返",
        "family": "openworld",
        "source_item": "08",
        "vision_en": "A surreal road-loop exploration game. Every route taken across a lonely region folds back toward the same motel before midnight, while landmarks subtly decay and memories persist between loops. The player must map contradictions and break the topology.",
        "vision_zh": "一款超现实公路循环探索游戏。无论选择哪条路线，玩家都会在午夜前回到同一家汽车旅馆；地标会逐渐腐化，而记忆会跨循环保留。玩家必须绘制矛盾并打破空间拓扑。",
        "features_en": [
            "Drive and walk through a connected road network with at least four distinct landmarks, branching junctions, and navigable interiors.",
            "Run a visible day-to-midnight loop in which roads reconnect differently while selected evidence, map annotations, and player knowledge persist.",
            "Let the player place map pins and compare road lengths, signs, shadows, and landmark states to identify impossible connections.",
            "Introduce changing hitchhikers, radio broadcasts, weather, and roadside hazards that reveal different clues on later loops.",
            "Track vehicle condition, fuel, fatigue, and a distortion meter that changes controls and scenery as midnight approaches.",
            "Provide several topology-breaking solutions that require performing a learned route sequence before the final midnight reset.",
        ],
        "features_zh": [
            "驾驶并步行探索相连公路网，包含至少四个独特地标、分支路口和可进入建筑。",
            "呈现清晰的白昼至午夜循环；道路连接会变化，但选定证据、地图标注和玩家知识会保留。",
            "允许玩家放置地图标记，并比较路程、路牌、阴影和地标状态，以找出不可能的连接。",
            "加入不断变化的搭车者、电台广播、天气和路边危险，在后续循环中揭示不同线索。",
            "追踪车况、燃料、疲劳和扭曲度；午夜临近时，控制与景观会随之改变。",
            "提供多种打破拓扑的方案，要求玩家在最终午夜重置前执行已学会的路线序列。",
        ],
        "progression_en": "Each verified contradiction unlocks new map tools and memory anchors, allowing more state to persist and exposing deeper routes.",
        "art_en": "Dreamlike nocturnal Americana with wet asphalt, sodium lights, analog dashboard glow, impossible horizon folds, and escalating spatial distortion.",
    },
    {
        "slug": "mz_openworld-twelve-ashes",
        "title_en": "Crowns of Twelve Ashes",
        "title_zh": "十二灰烬之冠",
        "family": "openworld",
        "source_item": "09",
        "vision_en": "A compact fantasy campaign across twelve fractured realms represented on one explorable strategic map. The player gathers crown fragments through diplomacy, field battles, and risky alliances while ash storms slowly erase unprotected territory.",
        "vision_zh": "一场横跨十二个破碎国度的紧凑奇幻战役，这些国度共同构成一张可探索战略地图。玩家通过外交、野外战斗和危险联盟收集王冠碎片，而灰烬风暴会逐步抹去未受保护的领土。",
        "features_en": [
            "Traverse a world map containing twelve recognizable realms or realm nodes, each with a settlement, ruler, local conflict, and travel hazard.",
            "Resolve negotiations through reputation, promises, tribute, evidence, and faction relationships rather than a single dialogue choice.",
            "Fight real-time tactical encounters with movement, attacks, dodging, companion commands, and clear victory or retreat conditions.",
            "Collect crown fragments with distinct powers and costs that alter travel, diplomacy, combat, or ash resistance.",
            "Simulate an advancing ash front that changes routes, destroys resources, and pressures the order in which realms are visited.",
            "Conclude with an assembly or conquest sequence whose playable structure and ending depend on surviving realms and alliances.",
        ],
        "features_zh": [
            "穿越包含十二个可辨识国度或国度节点的世界地图；每处都有聚落、统治者、地方冲突和旅行危险。",
            "通过声望、承诺、贡品、证据和派系关系解决谈判，而不是只提供一次对话选择。",
            "进行实时战术遭遇，包含移动、攻击、闪避、同伴指令以及清晰的胜利或撤退条件。",
            "收集能力与代价各异的王冠碎片，它们会改变旅行、外交、战斗或抗灰烬能力。",
            "模拟推进中的灰烬前线，改变路线、摧毁资源，并迫使玩家决定访问国度的顺序。",
            "以议会集结或征服序列收束；其玩法结构和结局取决于幸存国度与联盟。",
        ],
        "progression_en": "Fragments, companions, and realm treaties create a flexible build, while permanent realm losses ensure campaign decisions cannot all be reversed.",
        "art_en": "A stylized dark-fantasy atlas brought to life in 3D, with twelve strong regional palettes, ash-filled skies, heraldic UI, and magical crown effects.",
    },
    {
        "slug": "mz_openworld-drifting-lanterns",
        "title_en": "Lantern Keeper of the Drifting Isles",
        "title_zh": "漂流群岛的灯塔守护者",
        "family": "openworld",
        "source_item": "10",
        "vision_en": "A traversal and restoration game across floating islands whose guiding lanterns are going dark. The player pilots a small glider between moving landmasses, relights a navigation network, and keeps isolated communities connected through dangerous weather.",
        "vision_zh": "一款穿越与修复游戏：漂浮群岛上的引航灯正逐一熄灭。玩家驾驶小型滑翔器往返移动陆块，重新点亮导航网络，并在危险天气中维系孤立社区之间的联系。",
        "features_en": [
            "Glide, climb, and dock across at least five drifting islands whose relative positions and reachable routes change over time.",
            "Repair and relight lantern towers through hands-on mechanisms involving lenses, fuel, alignment, and timed ignition sequences.",
            "Use the illuminated network for navigation: active beams reveal safe wind lanes, hidden islands, and emergency routes.",
            "Gather fuel and repair materials through exploration, delivery jobs, and environmental traversal challenges.",
            "Protect lanterns from storms and airborne creatures using steering, temporary shields, signal flares, and rapid maintenance.",
            "Restore a full route across the archipelago and complete a final storm crossing that reflects which communities were connected.",
        ],
        "features_zh": [
            "在至少五座漂流岛屿之间滑翔、攀爬和停靠；岛屿相对位置与可达路线会随时间变化。",
            "通过镜片、燃料、校准和限时点火序列等实体机制修复并重燃灯塔。",
            "利用已点亮的网络导航：活跃光束会揭示安全风道、隐藏岛屿和紧急路线。",
            "通过探索、配送任务和环境穿越挑战收集燃料与维修材料。",
            "使用转向、临时护盾、信号弹和快速维修，保护灯塔免受风暴与空中生物侵袭。",
            "恢复贯穿群岛的完整航线，并完成最终风暴穿越；结果应体现哪些社区得到了连接。",
        ],
        "progression_en": "Upgraded glider wings, fuel tanks, lenses, and weather instruments expand range and allow access to higher, faster-moving islands.",
        "art_en": "Hopeful sky-fantasy with painterly clouds, warm lantern gold, cool storm fronts, miniature island ecosystems, and elegant wind-stream visualization.",
    },
    {
        "slug": "mz_openworld-sleeping-titan-city",
        "title_en": "City on the Sleeping Titan",
        "title_zh": "沉睡泰坦上的城市",
        "family": "openworld",
        "source_item": "11",
        "vision_en": "A vertical city-management adventure built on the back of a colossal sleeping creature. The player explores districts, studies tremors, repairs infrastructure, and decides whether to preserve the city, evacuate it, or wake the titan before involuntary movement tears everything apart.",
        "vision_zh": "一场建立在巨型沉睡生物背上的垂直城市管理冒险。玩家探索各城区、研究震动、修复基础设施，并在无意识运动撕裂城市前决定保住城市、组织撤离，还是唤醒泰坦。",
        "features_en": [
            "Explore at least four vertically layered city districts connected by lifts, bridges, ladders, and routes that shift with the titan's posture.",
            "Read a live tremor forecast and stabilize structures by placing braces, balancing loads, and repairing utilities before movement events.",
            "Track the titan's breathing, stress, and sleep depth; loud construction and resource extraction must affect those systems.",
            "Coordinate factions with conflicting plans for evacuation, sedation, awakening, and continued expansion.",
            "Respond to playable disasters such as bridge collapse, fires, rolling debris, and district tilting while directing civilian movement.",
            "Complete one of several city-scale plans during a major awakening sequence, producing materially different final city states.",
        ],
        "features_zh": [
            "探索至少四个垂直分层城区，通过升降机、桥梁、梯子和会随泰坦姿态变化的路线连接。",
            "读取实时震动预报，并在运动事件前放置支撑、平衡载荷、维修公共设施以稳定建筑。",
            "追踪泰坦的呼吸、压力和睡眠深度；高噪施工与资源开采必须影响这些系统。",
            "协调撤离、镇静、唤醒和继续扩张等计划互相冲突的派系。",
            "在桥梁坍塌、火灾、滚动物体和城区倾斜等可玩灾难中引导市民移动。",
            "在大型苏醒序列中完成多个城市级计划之一，形成实质不同的最终城市状态。",
        ],
        "progression_en": "Survey data and district support unlock stronger engineering tools, safer transit, and larger coordinated operations.",
        "art_en": "Monumental organic urbanism: dense low-poly districts over breathing stone-like skin, sweeping altitude views, warning beacons, and rhythmic titan motion.",
    },
    {
        "slug": "mz_openworld-festival-disaster",
        "title_en": "Festival Committee Disaster",
        "title_zh": "节庆委员会大灾难",
        "family": "openworld",
        "source_item": "12",
        "vision_en": "A comedic open-village management game about staging a major festival while every committee member creates a new crisis. The player runs between venues, schedules activities, solves local incidents, and tries to preserve both the celebration and community trust.",
        "vision_zh": "一款喜剧风开放村庄管理游戏：玩家要筹办大型节庆，而每位委员会成员都会制造新的危机。玩家在各场地间奔走、安排活动、解决本地事故，并努力保住庆典和社区信任。",
        "features_en": [
            "Explore a connected village with at least four festival venues, vendor streets, storage areas, and shortcuts that open during setup.",
            "Place stalls, decorations, stages, power lines, and crowd barriers while respecting space, budget, access, and safety constraints.",
            "Build a timed event schedule and personally complete short playable activities such as parade routing, cooking, music cues, or fireworks setup.",
            "Handle dynamic incidents including weather, missing supplies, animal escapes, performer conflicts, outages, and crowd congestion.",
            "Manage committee-member trust, vendor satisfaction, attendance, budget, and safety through visible consequences rather than text-only reports.",
            "Run the final festival day from opening to closing ceremony, with success, partial failure, or comic catastrophe states.",
        ],
        "features_zh": [
            "探索相连村庄，包含至少四个节庆场地、商贩街、仓储区以及布置期间可开启的捷径。",
            "放置摊位、装饰、舞台、电线和人群护栏，同时满足空间、预算、通行和安全约束。",
            "建立限时活动日程，并亲自完成游行引导、烹饪、音乐提示或烟花布置等短玩法。",
            "处理天气、物资丢失、动物逃跑、演员冲突、停电和人群拥堵等动态事件。",
            "通过可见后果管理委员信任、商贩满意、到场人数、预算和安全，而不是只显示文字报表。",
            "从开幕到闭幕完整运行最终节庆日，并提供成功、部分失败或喜剧性灾难状态。",
        ],
        "progression_en": "Completed preparations unlock better equipment and volunteer abilities, while unresolved incidents carry forward and complicate the final day.",
        "art_en": "Cheerful handcrafted low-poly village art with colorful bunting, varied stalls, expressive characters, readable crowd flow, and slapstick event effects.",
    },
    {
        "slug": "mz_puzzle-neon-gravity-marble",
        "title_en": "Neon Gravity Marble Run",
        "title_zh": "霓虹重力球",
        "family": "puzzle",
        "source_item": "user-01",
        "vision_en": "A tactile 3D neon marble labyrinth controlled by keyboard tilt or device orientation. Real gravity, collisions, moving geometry, and momentum are the puzzle; the player learns to bank, brake, and redirect the ball through increasingly dangerous transparent courses.",
        "vision_zh": "一款通过键盘倾斜或设备方向控制的触感型 3D 霓虹弹珠迷宫。真实重力、碰撞、移动几何体和动量就是谜题本身；玩家需要学习压弯、制动和重定向，穿越越来越危险的透明赛道。",
        "features_en": [
            "Simulate the marble with Cannon.js, including gravity, rolling acceleration, restitution, friction, ramps, rails, and physically credible collisions.",
            "Support arrow-key tilt and device orientation with calibration, sensitivity control, and an always-available desktop fallback.",
            "Create collision feedback with camera impulse, sparks, sound, and Vibration API on supported devices without making input unreadable.",
            "Provide at least three courses with checkpoints, moving platforms, launch pads, narrow rails, hazards, collectibles, and finish gates.",
            "Track time, falls, checkpoint progress, best run, and optional pickups, with quick recovery after leaving the course.",
            "Use speed-sensitive trails or postprocessing to communicate motion blur and increasing danger at high velocity.",
        ],
        "features_zh": [
            "使用 Cannon.js 模拟弹珠，包含重力、滚动加速度、弹性、摩擦、坡道、护轨和可信碰撞。",
            "支持方向键倾斜与设备方向控制，并提供校准、灵敏度设置和始终可用的桌面替代方案。",
            "用镜头冲击、火花、声音和受支持设备上的 Vibration API 表现碰撞，同时保持操控清晰。",
            "提供至少三条赛道，包含检查点、移动平台、发射板、窄轨、危险、收集物和终点门。",
            "追踪时间、坠落次数、检查点进度、最佳成绩和可选收集物；离开赛道后应快速恢复。",
            "使用随速度变化的拖尾或后处理表现运动模糊与高速危险感。",
        ],
        "progression_en": "Later courses introduce stronger gravity, rotating frames, polarity zones, and branching risk/reward routes while preserving deterministic resets.",
        "art_en": "A dark synthwave void with translucent emissive tracks, contrasting hazard colors, luminous particles, glossy marbles, and restrained bloom.",
    },
    {
        "slug": "mz_simulation-power-grid-balancer",
        "title_en": "Power Grid Balancer",
        "title_zh": "城市电力平衡师",
        "family": "simulation",
        "source_item": "user-02",
        "vision_en": "A real-time 3D city power-dispatch simulation. The player switches buildings between consumption, storage, and vehicle-to-grid modes while renewable output and demand fluctuate, trying to prevent cascading overloads without blacking out essential services.",
        "vision_zh": "一款实时 3D 城市电网调度模拟。玩家在用电、储能和车网互动模式之间切换建筑，同时应对可再生能源与需求波动，在不切断关键服务的前提下阻止级联过载。",
        "features_en": [
            "Render a low-poly city with animated wind turbines, solar fields, substations, charging hubs, storage buildings, and visible transmission links.",
            "Let players click buildings to switch operating modes and drag or select substations to reroute capacity between grid zones.",
            "Simulate changing generation, demand, storage charge, line capacity, frequency stability, and overload propagation in real time.",
            "Animate directional energy flow and transition overloaded buildings from normal blue states to flashing red warnings before failure.",
            "Provide multiple scenarios involving calm weather, evening peaks, renewable collapse, heat waves, and emergency service priorities.",
            "Score reliability, renewable usage, cost, unmet demand, and recovery time, with clear success and cascading-blackout loss states.",
        ],
        "features_zh": [
            "渲染低多边形城市，包含动态风机、光伏场、变电站、充电枢纽、储能建筑和可见输电线路。",
            "允许点击建筑切换运行模式，并通过拖动或选择变电站在不同电网区域间重新分配容量。",
            "实时模拟发电、需求、储能电量、线路容量、频率稳定和过载传播。",
            "用动画显示能量流向；过载建筑在故障前应从正常蓝色变为闪烁红色警告。",
            "提供平稳天气、晚间峰值、可再生能源骤降、热浪和关键服务优先级等多种场景。",
            "按可靠性、绿电利用、成本、未满足需求和恢复时间评分，并提供成功与级联停电失败状态。",
        ],
        "progression_en": "Campaign scenarios unlock batteries, demand-response tools, stronger lines, and forecasting aids that introduce new strategic options rather than flat upgrades.",
        "art_en": "A crisp low-poly infrastructure diorama with varied green spaces, warm city windows, cyan energy streams, and unambiguous amber/red fault states.",
    },
    {
        "slug": "mz_strategy-cyber-attack-defense",
        "title_en": "Cyber Attack Defense",
        "title_zh": "网络攻击防御战",
        "family": "strategy",
        "source_item": "user-03",
        "vision_en": "A 3D network-defense action strategy game. Red attack packets travel through a topology toward a central server; the player intercepts threats, hardens nodes, and reads a visual prediction model to survive escalating coordinated attacks.",
        "vision_zh": "一款 3D 网络防御动作策略游戏。红色攻击封包沿拓扑飞向中央服务器；玩家拦截威胁、加固节点，并读取可视化预测模型，在不断升级的协同攻击中生存。",
        "features_en": [
            "Build a readable 3D topology with a core server, relay nodes, routes, normal traffic, and multiple attack packet types moving along paths.",
            "Let the player click packets or nodes to intercept, quarantine, reroute, or detonate threats using cooldown-limited defensive tools.",
            "Visualize a Kalman-filter-inspired prediction layer that estimates future packet paths and updates uncertainty as observations arrive.",
            "Run discrete waves with decoys, split packets, armored payloads, compromised nodes, and a final coordinated boss attack.",
            "Add node upgrades, firewall placement, resource income, combo scoring, server health, and meaningful tradeoffs between active and passive defense.",
            "Pair every intercept, miss, prediction update, and node failure with distinct 8-bit synthesized audio and visible feedback.",
        ],
        "features_zh": [
            "构建清晰的 3D 拓扑，包含核心服务器、中继节点、路径、正常流量和沿路径移动的多种攻击封包。",
            "允许点击封包或节点，使用受冷却限制的工具进行拦截、隔离、改道或引爆。",
            "可视化一个受卡尔曼滤波启发的预测层，估计封包未来路径，并随观测到来更新不确定性。",
            "运行离散波次，包含诱饵、分裂封包、装甲载荷、失陷节点和最终协同首领攻击。",
            "加入节点升级、防火墙放置、资源收入、连击得分和服务器生命，在主动与被动防御间形成取舍。",
            "为每次拦截、漏过、预测更新和节点故障配备独特的 8-bit 合成音效与可见反馈。",
        ],
        "progression_en": "Later waves expand topology complexity and unlock specialized defenses while enemy behaviors adapt to overused strategies.",
        "art_en": "A high-contrast cyber operations space with luminous topology lines, volumetric packet trails, green code rain, red threat pulses, and pixel-audio visualizers.",
    },
    {
        "slug": "mz_simulation-liquid-interaction",
        "title_en": "Liquid Interaction Lab",
        "title_zh": "抽象流体点击器",
        "family": "simulation",
        "source_item": "user-04",
        "vision_en": "A playable real-time particle-fluid laboratory centered on a sphere of roughly ten thousand particles. The player repels and attracts the fluid to complete shape, containment, and energy challenges while learning how velocity and force alter the system.",
        "vision_zh": "一个可玩的实时粒子流体实验室，核心是由约一万个粒子组成的球体。玩家通过斥力与引力完成塑形、约束和能量挑战，并理解速度与力场如何改变系统。",
        "features_en": [
            "Simulate approximately 10,000 particles through GPGPU or an equivalent GPU texture technique, with a graceful lower-count fallback.",
            "Use pointer movement as a repulsive force and pointer press as an attractive force, with radius and strength controlled by readable UI.",
            "Map particle color continuously from cool to warm based on velocity and show force direction, center of mass, and turbulence feedback.",
            "Provide playable challenge modes for forming target silhouettes, moving fluid through rings, containing an unstable core, and restoring equilibrium.",
            "Track stability, escaped particles, energy use, target accuracy, and elapsed time, with reset and slow-motion experimentation controls.",
            "Maintain smooth interaction and clear input response under load, automatically adjusting quality without changing game-state rules.",
        ],
        "features_zh": [
            "通过 GPGPU 或等效 GPU 纹理技术模拟约一万个粒子，并提供较低粒子数量的平稳降级方案。",
            "鼠标移动产生斥力，按下鼠标产生引力；力场半径与强度通过清晰 UI 控制。",
            "根据速度把粒子颜色从冷色连续映射到暖色，并显示力方向、质心和湍流反馈。",
            "提供可玩挑战：形成目标轮廓、让流体穿过圆环、约束不稳定核心以及恢复平衡。",
            "追踪稳定度、逸出粒子、能量消耗、目标精度和耗时，并提供重置与慢动作实验控制。",
            "在高负载下保持流畅和清晰响应，可自动调整画质但不能改变游戏状态规则。",
        ],
        "progression_en": "Completing experiments unlocks multi-source force fields, vortices, obstacles, viscosity presets, and more demanding target shapes.",
        "art_en": "An elegant black laboratory void with luminous fluid color gradients, subtle grids, glass target volumes, and precise scientific UI.",
    },
    {
        "slug": "mz_rhythm-rhythm-striker",
        "title_en": "Rhythm Striker",
        "title_zh": "极简 3D 节奏大师",
        "family": "rhythm",
        "source_item": "user-05",
        "vision_en": "A minimal 3D rhythm game inside an endless emissive tunnel. Geometric targets arrive on musical beats; accurate key strikes shatter them into physical debris while the tunnel, materials, and camera react to synthesized audio.",
        "vision_zh": "一款发生在无限自发光隧道中的极简 3D 节奏游戏。几何目标随节拍抵达；准确按键会把它们击碎成物理碎片，而隧道、材质和镜头会响应合成音频。",
        "features_en": [
            "Spawn geometric beat targets in multiple lanes and judge key input with Perfect, Good, and Miss timing windows tied to a deterministic chart.",
            "Use Web Audio API synthesis and an analyser so emissive materials, tunnel segments, and camera impulses respond to current frequency bands.",
            "Shatter successful targets into velocity-aware physical fragments while misses pass the player and cause a distinct tunnel distortion.",
            "Implement combo, multiplier, score, health, song progress, pause, retry, and a results screen with timing breakdown.",
            "Provide at least three charts or difficulty modes with distinct rhythms, speeds, lane patterns, and visual identities.",
            "Keep timing readable despite bloom, camera motion, debris, and audio-reactive effects; accessibility settings must reduce shake and flash.",
        ],
        "features_zh": [
            "在多条轨道生成几何节拍目标，并依据确定性谱面对按键进行 Perfect、Good 和 Miss 判定。",
            "使用 Web Audio API 合成与分析器，让自发光材质、隧道分段和镜头冲击响应当前频段。",
            "成功击中时把目标打碎成具有速度感的物理碎片；漏过时目标穿过玩家并造成独特隧道扭曲。",
            "实现连击、倍率、得分、生命、歌曲进度、暂停、重试以及带判定统计的结算画面。",
            "提供至少三张谱面或难度模式，节奏、速度、轨道组合和视觉身份均有区别。",
            "在辉光、镜头运动、碎片和音频响应特效下仍保持判定清晰，并提供降低晃动与闪烁的辅助设置。",
        ],
        "progression_en": "Clearing charts unlocks denser patterns, hold targets, alternating strike directions, and cosmetic tunnel themes without compromising deterministic timing.",
        "art_en": "A restrained neon tunnel with black negative space, strong lane colors, emissive geometry, frequency-reactive surfaces, and crisp impact typography.",
    },
    {
        "slug": "mz_puzzle-perspective-path",
        "title_en": "Perspective Path",
        "title_zh": "视觉错觉解谜",
        "family": "puzzle",
        "source_item": "user-06",
        "vision_en": "An orthographic 3D puzzle game about impossible architecture. The player rotates a sculptural building until separated paths overlap on screen, creating temporary walkable connections for a small character.",
        "vision_zh": "一款围绕不可能建筑展开的正交投影 3D 解谜游戏。玩家旋转雕塑般的建筑，直到分离道路在屏幕上重合，为小角色创造临时可通行连接。",
        "features_en": [
            "Rotate an orthographic camera around a 3D monument with snapped and free-drag controls while preserving stable framing and depth order.",
            "Detect screen-space alignment between path endpoints and enable traversal only while geometric and occlusion conditions are valid.",
            "Let the player click reachable nodes to move a character along connected routes, blocking invalid moves with clear feedback.",
            "Provide at least six escalating puzzles using rotating towers, movable bridges, elevators, switches, occluders, and multiple alignment steps.",
            "Include undo, restart, camera reset, selected-node highlighting, optional hints, and deterministic puzzle state.",
            "Complete each level by carrying or activating a goal object, then unlock a level-select path through the monument.",
        ],
        "features_zh": [
            "使用吸附角度与自由拖动控制绕 3D 建筑旋转正交相机，同时保持稳定构图与正确深度排序。",
            "检测路径端点的屏幕空间对齐，只有几何与遮挡条件有效时才允许通行。",
            "允许点击可达节点，让角色沿连接路线移动；无效移动必须给出清晰反馈。",
            "提供至少六个逐步升级的谜题，使用旋转塔、可移动桥、电梯、开关、遮挡物和多步对齐。",
            "加入撤销、重开、相机复位、选中节点高亮、可选提示以及确定性谜题状态。",
            "通过携带或激活目标物完成关卡，再解锁贯穿整座建筑的选关路径。",
        ],
        "progression_en": "New chapters introduce layered alignment rules, moving parts, split characters, and simultaneous path conditions while teaching each mechanic visually.",
        "art_en": "A calm architectural diorama with clean stone, jewel-like accents, soft shadows, impossible silhouettes, and minimal illustrated UI.",
    },
    {
        "slug": "mz_strategy-voxel-tower-defense",
        "title_en": "Voxel Tower Defense",
        "title_zh": "3D 塔防微缩模型",
        "family": "strategy",
        "source_item": "user-07",
        "vision_en": "A bright voxel tower-defense game on a miniature island. Players place and upgrade towers while enemies use A* to route around terrain and legal obstacles, creating a tactical relationship between construction and path shape.",
        "vision_zh": "一款发生在微缩岛屿上的明亮体素塔防游戏。玩家放置并升级防御塔，敌人使用 A* 绕过地形与合法障碍，让建造行为与路径形状形成战术关系。",
        "features_en": [
            "Allow pointer-based tower placement on a voxel grid with ghost previews, range indicators, cost checks, smoke particles, and a landing bounce.",
            "Move enemies with A* pathfinding from spawn to base, recalculating legal routes after placement and rejecting constructions that fully block the path.",
            "Implement at least three tower types with distinct targeting, laser or projectile behavior, damage roles, cooldowns, and upgrade branches.",
            "Run multiple waves with several enemy types, escalating stats, rewards, base health, victory, defeat, pause, and speed controls.",
            "Add destructible or changing terrain, branching lanes, and tactical tiles that influence range, speed, or damage.",
            "Create volumetric-looking hit and death explosions, readable health feedback, economy UI, and a complete results/retry flow.",
        ],
        "features_zh": [
            "允许在体素网格上通过鼠标放置防御塔，包含幽灵预览、范围提示、费用检查、烟雾粒子和落地弹跳。",
            "敌人使用 A* 从出生点前往基地，放置后重新计算合法路线，并拒绝完全堵死道路的建造。",
            "实现至少三种防御塔，具有不同索敌、激光或弹体行为、伤害定位、冷却和升级分支。",
            "运行多波敌人，包含多种敌人类型、属性升级、奖励、基地生命、胜负、暂停和速度控制。",
            "加入可破坏或变化地形、分支道路，以及影响射程、速度或伤害的战术地块。",
            "制作具有体积感的命中与死亡爆炸、清晰生命反馈、经济 UI 和完整结算/重试流程。",
        ],
        "progression_en": "New islands introduce route constraints, tower synergies, enemy resistances, and persistent unlock choices across a short campaign.",
        "art_en": "A polished pastel voxel diorama with lush terrain, toy-like towers and enemies, crisp laser lines, chunky smoke, and colorful volumetric explosions.",
    },
    {
        "slug": "mz_simulation-ai-agent-lab",
        "title_en": "AI Agent Evolution Lab",
        "title_zh": "智能体进化实验室",
        "family": "simulation",
        "source_item": "user-08",
        "vision_en": "A controlled 3D behavioral sandbox inside a transparent glass habitat. Several autonomous agents sense resources, hazards, temperature, and gravity; the player changes the environment and runs scored experiments to observe adaptation rather than watching random motion.",
        "vision_zh": "一个位于透明玻璃栖息箱中的受控 3D 行为沙盒。多个自主智能体感知资源、危险、温度与重力；玩家改变环境并运行有评分的实验，观察适应行为，而不是只看随机运动。",
        "features_en": [
            "Simulate multiple autonomous agents with visible goals, sensing range, energy, memory, and behavior-state transitions such as explore, seek, avoid, rest, and cooperate.",
            "Let players adjust temperature, gravity magnitude and direction, resource density, hazard level, and time scale with responsive controls.",
            "Click an agent to inspect its current perception, target, energy, recent decisions, and trajectory, highlighting sensed objects in the habitat.",
            "Display live charts for entropy, population energy, movement diversity, collisions, resource use, and agent-state distribution.",
            "Provide repeatable experiment scenarios with hypotheses and success conditions, plus seeded reset and side-by-side result comparison.",
            "Make environmental changes visibly affect trajectories and group behavior without instantly teleporting or directly scripting agents.",
        ],
        "features_zh": [
            "模拟多个自主智能体，具有可见目标、感知范围、能量、记忆以及探索、寻路、规避、休息和合作等状态转换。",
            "允许通过响应灵敏的控件调整温度、重力大小与方向、资源密度、危险程度和时间倍率。",
            "点击智能体可查看当前感知、目标、能量、近期决策与轨迹，并高亮其在栖息箱中感知到的物体。",
            "实时显示熵、群体能量、运动多样性、碰撞、资源使用和智能体状态分布曲线。",
            "提供可重复实验场景、假设与成功条件，并支持固定种子重置和并排结果比较。",
            "环境变化必须可见地影响轨迹和群体行为，不能直接瞬移或脚本化操纵智能体。",
        ],
        "progression_en": "Completed experiments unlock new sensors, agent traits, environment presets, and more complex multi-variable research objectives.",
        "art_en": "A clean scientific glass-box diorama with soft laboratory lighting, distinct agent colors, translucent sensor cones, plotted trajectories, and precise dashboard graphics.",
    },
    {
        "slug": "mz_puzzle-exploded-view-repair",
        "title_en": "Zero-G Exploded View",
        "title_zh": "零重力拆解动效",
        "family": "puzzle",
        "source_item": "user-09",
        "vision_en": "An interactive 3D inspection and repair puzzle built around the exploded view of a precision drone or camera. The player disassembles the device, examines labeled components, diagnoses faults, and restores the assembly in the correct order.",
        "vision_zh": "一款围绕精密无人机或相机爆炸拆解视图构建的 3D 检查维修谜题。玩家拆解设备、查看带标签零件、诊断故障，并按正确顺序恢复装配。",
        "features_en": [
            "Drive a smooth exploded-view amount with a slider and mouse wheel, giving component groups distinct spring and damping responses.",
            "Support orbit, zoom, hover highlighting, isolation, and pinned 3D labels that remain readable and point to the correct moving part.",
            "Create an inspection puzzle where players identify faulty components through visual clues, diagnostic readings, and functional descriptions.",
            "Require a valid disassembly and reassembly order with tool selection, dependency checks, snap previews, and invalid-action feedback.",
            "Include multiple device modules or fault scenarios involving optics, power, control boards, motors, cooling, and structural parts.",
            "Verify the repair with a playable system test and show performance differences based on diagnosis and assembly accuracy.",
        ],
        "features_zh": [
            "通过滑块和鼠标滚轮平滑控制爆炸拆解程度，不同零件组应具有不同弹性与阻尼响应。",
            "支持环绕、缩放、悬停高亮、隔离和固定的 3D 标签；标签应始终可读并正确指向移动零件。",
            "设计检查谜题，让玩家通过视觉线索、诊断读数和功能说明识别故障零件。",
            "要求遵循正确拆装顺序，包含工具选择、依赖检查、吸附预览和无效操作反馈。",
            "提供多个设备模块或故障场景，涉及光学、电源、控制板、电机、散热和结构零件。",
            "通过可玩的系统测试验证维修，并根据诊断与装配准确度显示性能差异。",
        ],
        "progression_en": "New repair jobs add denser assemblies, subtler faults, calibration steps, and optional efficiency challenges.",
        "art_en": "Premium industrial visualization with brushed metal, transparent plastic, rubber, glass optics, studio lighting, crisp outlines, and restrained technical labels.",
    },
    {
        "slug": "mz_puzzle-3d-terminal",
        "title_en": "The 3D Terminal",
        "title_zh": "赛博朋克 3D 终端",
        "family": "puzzle",
        "source_item": "user-10",
        "vision_en": "A command-driven 3D puzzle adventure inside a floating cyberpunk terminal. Typed commands alter the surrounding simulation: launching machines, routing energy, moving platforms, decoding matrices, and triggering dramatic spatial feedback.",
        "vision_zh": "一款发生在悬浮赛博朋克终端中的命令驱动 3D 解谜冒险。输入命令会改变周围模拟空间：启动机器、分配能源、移动平台、解码矩阵，并触发强烈空间反馈。",
        "features_en": [
            "Implement a real command parser with history, help, autocomplete or suggestions, arguments, aliases, and clear unknown-command handling.",
            "Connect commands to visible 3D systems such as launching a rocket, opening sectors, rotating code matrices, routing power, and moving a drone.",
            "Build multi-step missions where players inspect state, infer valid commands, combine arguments, and observe persistent consequences.",
            "Use strong feedback: successful commands animate the world, launches create procedural smoke, and invalid commands shake or glitch the space.",
            "Provide discoverable logs, hidden commands, optional objectives, command documentation, and at least three linked mission chapters.",
            "Track objective state, terminal access level, errors, discovered commands, and completion, with restart and safe recovery from bad input.",
        ],
        "features_zh": [
            "实现真正的命令解析器，包含历史、帮助、自动补全或建议、参数、别名和清晰的未知命令处理。",
            "把命令连接到可见 3D 系统，例如发射火箭、开启区域、旋转代码矩阵、分配能源和移动无人机。",
            "构建多步骤任务，让玩家检查状态、推断有效命令、组合参数并观察持续后果。",
            "提供强反馈：成功命令驱动世界动画，发射产生程序化烟雾，无效命令让空间晃动或故障化。",
            "提供可发现日志、隐藏命令、可选目标、命令文档以及至少三个相连任务章节。",
            "追踪目标状态、终端权限、错误、已发现命令和完成度，并支持重启与错误输入后的安全恢复。",
        ],
        "progression_en": "Completing missions raises terminal access, unlocks new command namespaces, and exposes more of the surrounding 3D machine.",
        "art_en": "A black-void cyberpunk command chamber with glass terminal planes, magenta/cyan matrices, volumetric smoke, emissive machinery, and controlled glitch effects.",
    },
]


class LiteralDumper(yaml.SafeDumper):
    pass


def _represent_str(dumper: yaml.Dumper, value: str):
    return dumper.represent_scalar(
        "tag:yaml.org,2002:str",
        value,
        style="|" if "\n" in value else None,
    )


LiteralDumper.add_representer(str, _represent_str)


def _source_meta(item: dict) -> dict:
    if str(item["source_item"]).isdigit():
        return {
            "kind": "adapted_article_prompt",
            "source_name": "AIGA AI RPG prompts",
            "source_url": AIGA_SOURCE_URL,
            "source_item": item["source_item"],
        }
    return {
        "kind": "adapted_user_prompt",
        "source_name": "benchmark author expansion prompts",
        "source_item": item["source_item"],
    }


def _prompt(item: dict, language: str) -> str:
    title = item[f"title_{language}"]
    vision = item[f"vision_{language}"]
    features = item[f"features_{language}"]
    if language == "en":
        numbered = "\n".join(f"{index}. **System {index}** - {text}" for index, text in enumerate(features, 1))
        return (
            f"# {title}\n\n"
            f"Build a complete, playable **3D {FAMILY_LABELS['en'][item['family']]} game** "
            f"as a polished browser vertical slice.\n\n"
            f"## Core Vision\n\n{vision}\n\n"
            f"## Required Playable Systems\n\n{numbered}\n\n"
            f"## Progression\n\n{item['progression_en']}\n\n"
            f"## Art Direction\n\n{item['art_en']}\n\n"
            f"{COMMON_EN}"
        ).strip()

    numbered = "\n".join(f"{index}. **系统 {index}** - {text}" for index, text in enumerate(features, 1))
    return (
        f"# {title}\n\n"
        f"制作一个完整可玩的 **3D {FAMILY_LABELS['zh'][item['family']]}游戏**，"
        f"交付为经过打磨的浏览器纵向切片。\n\n"
        f"## 核心构想\n\n{vision}\n\n"
        f"## 必须实现的可玩系统\n\n{numbered}\n\n"
        f"## 成长与推进\n\n{_translate_progression(item)}\n\n"
        f"## 美术方向\n\n{_translate_art(item)}\n\n"
        f"{COMMON_ZH}"
    ).strip()


ZH_PROGRESSION = {
    item["slug"]: text
    for item, text in zip(
        CATALOG,
        [
            "解决城区案件可升级扫描范围和时间残影控制，开放受限区域，并解锁越来越复杂的重建。",
            "回收部件可提升引擎、扫描精度和电力容量，从而进入更危险的区域并解析更深层信号。",
            "成功完成场景可获得角色代币，解锁新的摄影棚控制、带能力的服装和封闭的导演区。",
            "维修和谈判协议会解锁高效基础设施、更准确预报和新分配选项，并永久改变各区韧性。",
            "保存的记忆会强化透镜、揭示更深历史层，并解锁稳定空间与保护证据的法术。",
            "赛段之间可安装互斥模块，改变操控、效率、耐久、扫描或加速行为。",
            "找回条款并恢复供暖区可延长安全探索时间、揭示隐藏侧翼，并增加家族谈判筹码。",
            "每验证一个空间矛盾都会解锁新地图工具与记忆锚点，使更多状态跨循环保留并暴露更深路线。",
            "碎片、同伴和国度条约构成灵活流派，而永久失去国度确保战役决策不能全部逆转。",
            "升级滑翔翼、燃料箱、镜片和气象仪器可扩大航程，并进入更高、更快移动的岛屿。",
            "勘测数据与城区支持会解锁更强工程工具、更安全交通和更大规模的协同行动。",
            "完成准备工作可解锁更好设备与志愿者能力；未解决事件会延续到最终节庆日并增加复杂度。",
            "后续赛道加入更强重力、旋转框架、极性区域和风险收益分支，同时保持确定性重置。",
            "战役场景会解锁电池、需求响应工具、更强线路和预测辅助，提供新策略而非单纯数值升级。",
            "后续波次扩展拓扑复杂度并解锁专用防御，敌人会适应被过度使用的策略。",
            "完成实验可解锁多源力场、涡旋、障碍、黏度预设和更高难度目标形状。",
            "通关谱面可解锁更密集节奏、长按目标、交替打击方向和装饰性隧道主题，同时不破坏确定性节拍。",
            "新章节加入分层对齐规则、移动部件、分裂角色和同时满足的路径条件，并通过视觉方式教学。",
            "新岛屿加入路线限制、防御塔联动、敌人抗性以及短战役中的永久解锁选择。",
            "完成实验可解锁新传感器、智能体特征、环境预设和更复杂的多变量研究目标。",
            "新的维修工作加入更密集装配、更隐蔽故障、校准步骤和可选效率挑战。",
            "完成任务会提升终端权限，解锁新的命令命名空间，并显露周围 3D 机器的更多部分。",
        ],
    )
}

ZH_ART = {
    item["slug"]: text
    for item, text in zip(
        CATALOG,
        [
            "雨夜近未来都市，以青色取证投影、琥珀街灯、图像小说阴影和锐利时间裂隙构成视觉语言。",
            "硬科幻孤寂氛围：黑暗行星剪影、仪表照明船舱、体积信号波、电弧和苍白求救信标。",
            "衰败的黄金时代电影美学，包含积尘聚光灯、天鹅绒红、黑白投影、手绘布景和戏剧化超自然转场。",
            "日晒褪色的低多边形流域，结合龟裂地面、青绿水流覆盖、风化市政机械、热浪和紧急红光。",
            "奇想哥特学院风，以发光墨迹、移动肖像、月光庭院、不可能楼梯和纸粒子记忆消散效果呈现。",
            "明亮复古未来赛车美学，包含饱和行星天空、全息门、热量拖尾、模块化载具和清晰宇宙路线图形。",
            "冰雪哥特宅邸，以温暖烛光室内、蔓延冰蓝、黄铜供暖机械、彩窗和风驱雪效构成对比。",
            "梦境般的夜间公路美学，包含湿润柏油、钠灯、模拟仪表辉光、不可能折叠地平线和逐步升级的空间扭曲。",
            "被赋予 3D 生命的风格化暗黑奇幻地图，十二种强烈地域色彩、灰烬天空、纹章 UI 和魔法王冠效果。",
            "充满希望的天空奇幻风，包含绘画般云层、温暖灯火金、冷色风暴、微缩岛屿生态和优雅风流可视化。",
            "宏伟的有机城市美学：密集低多边形城区覆盖在会呼吸的石质皮肤上，结合高空远景、警示灯和节律性泰坦运动。",
            "欢快手工低多边形村庄，包含彩旗、多样摊位、表情丰富角色、可读人流和滑稽事件特效。",
            "黑暗合成波虚空，以半透明自发光赛道、对比危险色、发光粒子、光泽弹珠和克制辉光呈现。",
            "清晰低多边形基础设施微缩景观，包含多样绿地、温暖城市窗光、青色能源流和明确黄/红故障状态。",
            "高对比赛博作战空间，包含发光拓扑线、体积封包拖尾、绿色数字雨、红色威胁脉冲和像素音频可视化。",
            "优雅黑色实验室虚空，以发光流体渐变、细网格、玻璃目标体和精确科学 UI 构成。",
            "克制的霓虹隧道，以黑色负空间、强轨道色、自发光几何体、频率响应表面和清晰冲击文字呈现。",
            "宁静建筑微缩景观，使用干净石材、宝石点缀、柔和阴影、不可能剪影和极简插画 UI。",
            "精致马卡龙体素微缩岛，包含繁茂地形、玩具感塔与敌人、清晰激光、块状烟雾和彩色体积爆炸。",
            "干净科学玻璃箱景观，包含柔和实验室照明、可区分智能体颜色、半透明感知锥、轨迹和精确仪表图形。",
            "高端工业可视化，以拉丝金属、透明塑料、橡胶、玻璃光学件、棚拍灯光、清晰轮廓和克制技术标签呈现。",
            "黑色虚空赛博命令舱，包含玻璃终端平面、洋红/青色矩阵、体积烟雾、自发光机械和受控故障效果。",
        ],
    )
}


def _translate_progression(item: dict) -> str:
    return ZH_PROGRESSION[item["slug"]]


def _translate_art(item: dict) -> str:
    return ZH_ART[item["slug"]]


def _requirement(item: dict, req_id: str, description: str, category: str) -> dict:
    if category == "mechanic":
        suffix = (
            " Score 0 if the system is absent, decorative, or cannot be completed "
            "through player input. Score 1 requires the full interaction and its "
            "success/failure consequences to be observable in one playable flow."
        )
        agg = "max"
    elif category == "depth":
        suffix = (
            " Score 0 if this content is missing or differs only through labels or "
            "color swaps. Score 1 requires functionally distinct content that changes "
            "the player's decisions."
        )
        agg = "max"
    elif category == "experience":
        suffix = (
            " Score 0 if essential information or feedback is missing, unreadable, "
            "overlapping, or disconnected from the game state at 1280x720."
        )
        agg = "mean"
    else:
        suffix = (
            " Score 0 if the presentation is dominated by default controls, unlit "
            "primitives, inconsistent materials, or abrupt unanimated state changes."
        )
        agg = "mean"
    return {"id": req_id, "agg": agg, "description": description + suffix}


def _rubric(item: dict) -> dict:
    features = item["features_en"]
    requirements = [
        _requirement(item, "M1", features[0], "mechanic"),
        _requirement(item, "M2", features[1], "mechanic"),
        _requirement(item, "M3", features[2], "mechanic"),
        _requirement(item, "D1", features[3], "depth"),
        _requirement(item, "D2", features[4], "depth"),
        _requirement(item, "D3", features[5], "depth"),
        _requirement(item, "D4", item["progression_en"], "depth"),
        _requirement(
            item,
            "V1",
            "The HUD clearly communicates current objective, critical resources, "
            "selected target or mode, progress, and danger states in stable regions.",
            "experience",
        ),
        _requirement(
            item,
            "V2",
            "Every important player action has immediate, distinguishable feedback "
            "for valid input, invalid input, success, damage or failure, and state change.",
            "experience",
        ),
        _requirement(
            item,
            "V3",
            "The full loop is connected: styled title and start flow, playable core "
            "systems, progression or escalation, final success/failure state, and retry "
            "or return navigation all work without reloading the page.",
            "experience",
        ),
        _requirement(item, "A1", f"The project has a coherent authored art direction: {item['art_en']}", "art"),
        _requirement(
            item,
            "A2",
            "The 3D environment has deliberate composition, lighting, material contrast, "
            "depth cues, and themed landmarks rather than an empty floor with scattered objects.",
            "art",
        ),
        _requirement(
            item,
            "A3",
            "Primary interactive actors, machines, targets, hazards, and UI symbols have "
            "readable silhouettes and visibly different functional states.",
            "art",
        ),
        _requirement(
            item,
            "A4",
            "Movement, impacts, transitions, alerts, completion moments, and interface "
            "changes use smooth multi-frame animation, particles, camera treatment, or audio-reactive motion.",
            "art",
        ),
    ]
    return {
        "score_formula": "BUILD * (0.15*((M1+M2+M3)/3) + 0.35*((D1+D2+D3+D4)/4) + 0.15*((V1+V2+V3)/3) + 0.35*((A1+A2+A3+A4)/4))",
        "max_demos": 10,
        "max_demo_seconds": 20,
        "build_check": {
            "id": "BUILD",
            "cmd": "momozi HTML static BUILD gate",
            "description": "index.html and game_logic.js exist, a canvas/WebGL renderer is present, and no disallowed heavy runtime asset references are used.",
        },
        "categories": [
            {"name": "Core Mechanics", "items": RUBRIC_MAPPING["completeness"]},
            {"name": "Content Depth", "items": RUBRIC_MAPPING["richness"]},
            {"name": "Functional Visuals", "items": RUBRIC_MAPPING["player_exp"]},
            {"name": "Presentation & Art", "items": RUBRIC_MAPPING["visual"]},
        ],
        "requirements": requirements,
    }


def _task_yaml(item: dict, language: str, prompt: str) -> dict:
    base_id = item["slug"]
    task_id = f"{base_id}-{language}"
    title = item[f"title_{language}"] + LANGUAGES[language]
    difficulty = classify_difficulty(item["family"], _prompt(item, "en"))
    return {
        "id": task_id,
        "title": title,
        "family": item["family"],
        "difficulty": difficulty,
        "engine": "html",
        "language": language,
        "base_task_id": base_id,
        "provenance": _source_meta(item),
        "rounds": [{"name": "R1", "spec": prompt}],
        "static": [
            {"kind": "required_file", "role": "entry", "path": "index.html", "weight": 1.0},
            {"kind": "required_file", "role": "logic", "path": "game_logic.js", "weight": 1.0},
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
                "rubric": "Coherent 3D art direction, authored environments, effects, and motion polish.",
            },
        ],
    }


def _render_files(item: dict, language: str) -> dict[str, str]:
    prompt = _prompt(item, language)
    task_id = f"{item['slug']}-{language}"
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


def _validate_catalog() -> None:
    if len(CATALOG) != 22:
        raise ValueError(f"expected 22 concepts, found {len(CATALOG)}")
    slugs = [item["slug"] for item in CATALOG]
    if len(slugs) != len(set(slugs)):
        raise ValueError("duplicate task slug in expansion catalog")
    for item in CATALOG:
        for language in LANGUAGES:
            features = item[f"features_{language}"]
            if len(features) != 6 or not all(features):
                raise ValueError(f"{item['slug']}: expected six {language} features")


def _validate_or_write(write: bool) -> tuple[int, int]:
    created = 0
    validated = 0
    for item in CATALOG:
        for language in LANGUAGES:
            task_id = f"{item['slug']}-{language}"
            task_dir = TASKS_ROOT / task_id
            expected = _render_files(item, language)
            if not task_dir.exists():
                if not write:
                    raise FileNotFoundError(
                        f"{task_dir} is missing; rerun with --write to create expansion tasks"
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
                actual = (task_dir / name).read_text(encoding="utf-8")
                if actual != content:
                    raise ValueError(f"{task_dir / name}: differs from expansion catalog")
            validated += 1
    return created, validated


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    _validate_catalog()
    created, validated = _validate_or_write(args.write)
    print(
        f"expansion tasks valid: 22 concepts x 2 languages = {validated} tasks "
        f"({created} created)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
