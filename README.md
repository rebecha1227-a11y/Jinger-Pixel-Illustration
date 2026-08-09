# Jinger Pixel Illustration

高清像素个人 IP 插图 Skill。

先固定一个角色，再做成两种图：

1. **16:9 长文配图**：必须有封面 + 正文图。封面用暖色简单像素场景，正文默认白底迷你剧场。
2. **3:4 知识卡片**：整张由生图模型画成像素场景，人物和短文字一起演戏。最多 9 张。

不要默认两套一起出。没有确认角色之前，不要配图。

## 和别人的差别

大多数开源 IP skill 是简笔画 / 扁平 3D / 小黑手绘，而且通常只做长文配图。这套是：

- 高清像素
- 长文 + 知识卡片两种形态
- 卡片必须人字互动；整张生图像素场景，不是 HTML 排版卡

## 仓库结构

这个仓库**本身就是 Skill**。GitHub 打开就能看到本 README；克隆后目录名改成 `jinger-pixel-illustration` 即可安装。

```text
.
├── README.md              ← 你现在看的这份
├── SKILL.md               ← Agent 入口
├── LICENSE / LICENSE-ASSETS
├── PLAN.md                ← 设计笔记
├── assets/                ← Jinger 画风锁（不是给你当脸用）
├── references/            ← 创建角色 / 长文 / 卡片细则
├── scripts/               ← 安装脚本 + 本地角色包管理
└── templates/             ← 仅无生图时的应急占位
```

## 安装

### 方式一：通用 Skills CLI（推荐）

```bash
npx skills add rebecha1227-a11y/Jinger-Pixel-Illustration -g -y
```

### 方式二：本仓库 npx 脚本

会把 Skill 装到本机的 Cursor / Claude Code / Codex skills 目录：

```bash
npx github:rebecha1227-a11y/Jinger-Pixel-Illustration
```

只装其中一个客户端：

```bash
npx github:rebecha1227-a11y/Jinger-Pixel-Illustration --cursor
npx github:rebecha1227-a11y/Jinger-Pixel-Illustration --claude
npx github:rebecha1227-a11y/Jinger-Pixel-Illustration --codex
```

### 方式三：git clone

Claude Code / Codex：

```bash
git clone https://github.com/rebecha1227-a11y/Jinger-Pixel-Illustration.git \
  "${HOME}/.claude/skills/jinger-pixel-illustration"
```

Cursor：

```bash
git clone https://github.com/rebecha1227-a11y/Jinger-Pixel-Illustration.git \
  "${HOME}/.cursor/skills/jinger-pixel-illustration"
```

已有文件夹时，也可以把本仓库复制进去，**目录名保持** `jinger-pixel-illustration`。

## 怎么用

1. 先选这次做：只要长文 / 只要知识卡片 / 两套都要
2. 还没有角色就选：A 现成 IP 发图，或 B 用自己的照片创建
3. 看到设定图后，说「确认」才会进入配图
4. 知识卡片会先出 shot list，你点头再生图

**没有「用 Jinger 体验」入口。** Jinger 只是作者的角色，也用来锁像素密度。请创建你自己的角色。水印用你自己的号，不要印 `@讨厌吃Ginger的Jinger`。

## 无生图时

Skill 会交出完整 prompt、参考图路径和水印计划，不会假装图片已经生成。

## 授权

- 工作流、脚本、模板、文档：MIT，见 [LICENSE](LICENSE)
- Jinger 角色图与设定：不在 MIT 内，见 [LICENSE-ASSETS](LICENSE-ASSETS)

## 致谢

工作流结构参考了 [adrianpunk/punk-ip-illustrations](https://github.com/adrianpunk/punk-ip-illustrations)、[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)、[EverettFish/ip_illustration_for_yourself](https://github.com/EverettFish/ip_illustration_for_yourself)。
