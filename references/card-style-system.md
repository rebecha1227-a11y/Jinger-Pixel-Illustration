# 知识卡 · 风格系统（Style System）

固定层。换文章时**不要改**这一层。只服务 3:4 知识卡片。

流水线位置：LAYOUT 之后 → STYLE SYSTEM（本文件）→ CHARACTER → IMAGE-2。

目标气质对齐：`assets/style-lock/knowledge-card-editorial-3x4.png`  
（米白暖棕底 + 复古像素 + RPG/独立游戏 UI 模块 + 信息模块化；只学版式/密度/色纪律，不学样例角色脸）

完整黄金样张合同见 `card-gold-standard.md`。同一系列必须锁住：一条连续外框、同一纸面、同一字体分工、同一模块边线语言；不能只写“复古像素”就让模型自由重做视觉系统。

长文封面锁用 `assets/style-lock/warm-pixel-scene-16x9.png`；长文正文锁用 `assets/style-lock/article-body-editorial-16x9.png`。  
知识卡不要混用长文锁。

## 画风

Premium retro pixel-art **editorial** illustration.

- 必须像「从一开始就按像素画的角色与 UI」，不是「先画二次元再加像素滤镜」
- 可见像素簇、利落边缘、可控 dither、刻意的高光/阴影块
- 1990s / early-2000s 日式游戏 + 独立游戏界面语言
- 精致精灵画质；不是原始 8-bit 大色块

禁止：写实摄影、照片皮肤、3D、盲盒公仔、光滑矢量、普通 AI 动漫插画、像素滤镜感。

## 像素质量强约束（必写进 Prompt）

```text
PIXEL ART QUALITY CONTROL
The character itself must be constructed as pixel art from the start.
Do NOT render a normal anime character first and apply a pixel texture afterward.
Pixel construction must be visible in hair, eyes, face, clothing edges, accessories, shadows, highlights, outlines.
Use intentional pixel clusters. Facial features = few carefully placed pixel clusters.
Hair = grouped pixel strands, not smooth painted strands.
Clothing folds = deliberate pixel shading. Edges = controlled stair-stepping.
```

## 色彩纪律（硬约束）

知识卡用**一个主强调色家族 + 极少语义微强调**，不要每张换一盘彩虹：

| 层级 | 用法 | 示例 |
|---|---|---|
| 底 | 几乎纯色暖米白 / 象牙 | `#F5F0E8` 一带 |
| 结构 | 深棕 / 炭灰：标题、边框、模块线、正文 | cocoa / espresso / `#2B2B2B` |
| 主强调 | **整张只选 1 个低饱和强调色家族** | 琥珀金/蜂蜜黄用于文件夹、节点、序号、箭头、关键 UI |
| 语义微强调 | 可选，总面积 `<3%` | 只为 VS、重点下划线、状态差异服务；如 03 的一小段桃粉线，不得铺满模块 |
| 灰 | 可选弱底块，不算第二套品牌强调色 | 浅灰模块底 |

禁止：把语义微强调扩成第二套主色、霓虹第三色、每张换高饱和装饰色、复杂渐变背景。
角色服装/头发按角色包固有色上色（那是身份，不是「又开一盘强调色」）。

写入 prompt 时可加：

```text
COLOR DISCIPLINE: cream/ivory background + dark cocoa structure text and frames.
Use one dominant muted amber/gold accent family. One optional semantic micro-accent may occupy less than 3% of the canvas. No extra saturated decoration colors.
```

## 边框、纸面与字体合同

- **外框**：整张只有一条连续的圆角像素外框；深 espresso 外线 + 中棕内线 + 暖色高光，厚度和圆角在系列里固定。不能每个页面换边框，也不能把页面切成浮动海报卡。
- **纸面**：框内是一块平整暖象牙纸面，允许非常轻的纸纹和边缘阴影；禁止渐变舞台光、房间或散景。
- **字体分工**：主标题/英文关键词用复古像素 display；模块标题用清楚粗体；中文解释用高可读无衬线。不要把全部中文强制像素化。
- **模块线**：实体细线用于主结构和容器；虚线只用于注释/次级说明；圆角、描边、阴影深度保持一致。

## 背景（静儿硬偏好）

- **简约、几乎纯色**的暖米白 / 米色平面
- 允许极轻的像素纹理
- **禁止**：复杂房间、书架墙、软木板堆满、写实桌面、风景、重渐变、照片背景

背景只为信息层级服务，不是「角色住的房间」。

## 系列感

同一套知识卡应像「同一本个人知识宇宙的连续页」：同一角色、同一色纪律、同一 UI 语言；变的是版式模具与内容模块。
