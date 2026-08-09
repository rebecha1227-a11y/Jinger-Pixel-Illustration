# Jinger Pixel Illustration

高清像素个人 IP 插图 Skill。

先固定一个角色，再做成两种图：

1. **16:9 长文配图**：必须有封面 + 正文图。封面用暖色简单像素场景，正文默认白底迷你剧场。
2. **3:4 知识卡片**：奶油米白，人物和文字一起演戏，截图就能发。最多 9 张。

不要默认两套一起出。没有确认角色之前，不要配图。

## 和别人的差别

大多数开源 IP skill 是简笔画 / 扁平 3D / 小黑手绘，而且通常只做长文配图。这套是：

- 高清像素
- 长文 + 知识卡片两种形态
- 卡片必须人字互动；整张由生图模型画成像素场景，不是 HTML 排版卡

## 安装

把本目录放到支持 Agent Skills 的客户端 skills 文件夹，目录名保持 `jinger-pixel-illustration`。

例如 Claude Code / Codex：

```bash
cp -R jinger-pixel-illustration "${HOME}/.claude/skills/"
```

Cursor：

```bash
cp -R jinger-pixel-illustration "${HOME}/.cursor/skills/"
```

## 怎么用

1. 先选这次做：只要长文 / 只要知识卡片 / 两套都要
2. 还没有角色就选：A 现成 IP 发图，或 B 用自己的照片创建
3. 看到设定图后，说「确认」才会进入配图
4. 知识卡片会先出 shot list，你点头再导出

**没有「用 Jinger 体验」入口。** Jinger 只是作者的角色，也用来锁像素密度。请创建你自己的角色。水印用你自己的号，不要印 `@讨厌吃Ginger的Jinger`。

## 无生图时

Skill 会交出完整 prompt、参考图路径和水印计划，不会假装图片已经生成。

## 授权

- 工作流、脚本、模板、文档：MIT，见 [LICENSE](LICENSE)
- Jinger 角色图与设定：不在 MIT 内，见 [LICENSE-ASSETS](LICENSE-ASSETS)

## 致谢

工作流结构参考了 [adrianpunk/punk-ip-illustrations](https://github.com/adrianpunk/punk-ip-illustrations)、[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)、[EverettFish/ip_illustration_for_yourself](https://github.com/EverettFish/ip_illustration_for_yourself)。
