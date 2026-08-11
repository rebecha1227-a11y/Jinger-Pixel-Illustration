# 知识卡 · 风格系统（Style System）

固定层。换文章时**不要改**这一层。只服务 3:4 知识卡片。

流水线位置：LAYOUT 之后 → STYLE SYSTEM（本文件）→ CHARACTER → IMAGE-2。

目标气质对齐：`assets/style-lock/knowledge-card-editorial-3x4.png`  
（米白暖棕底 + 复古像素 + RPG/独立游戏 UI 模块 + 信息模块化；只学版式/密度/色纪律，不学样例角色脸）

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

知识卡用**克制双色逻辑**，不要每张换一盘彩虹：

| 层级 | 用法 | 示例 |
|---|---|---|
| 底 | 几乎纯色暖米白 / 象牙 | `#F5F0E8` 一带 |
| 结构 | 深棕 / 炭灰：标题、边框、模块线、正文 | cocoa / espresso / `#2B2B2B` |
| 强调 | **整张只选 1 个强调色** | 箭头、关键词高亮、关键 UI；Jinger 套图可从角色固有色里选草莓粉发色 **或** 奶油毛衣色当强调，**不要两个一起抢** |
| 灰 | 可选弱底块，不算第二套品牌强调色 | 浅灰模块底 |

禁止：霓虹第三色、每张换高饱和装饰色、复杂渐变背景。  
角色服装/头发按角色包固有色上色（那是身份，不是「又开一盘强调色」）。

写入 prompt 时可加：

```text
COLOR DISCIPLINE: cream/ivory background + dark brown/black structure text and frames.
Exactly ONE accent color for emphasis (arrows/keywords/key UI). No extra saturated decoration colors.
```

## 背景（静儿硬偏好）

- **简约、几乎纯色**的暖米白 / 米色平面
- 允许极轻的像素纹理
- **禁止**：复杂房间、书架墙、软木板堆满、写实桌面、风景、重渐变、照片背景

背景只为信息层级服务，不是「角色住的房间」。

## 系列感

同一套知识卡应像「同一本个人知识宇宙的连续页」：同一角色、同一色纪律、同一 UI 语言；变的是版式模具与内容模块。
