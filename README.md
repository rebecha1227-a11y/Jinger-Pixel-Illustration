# Jinger Pixel Illustration

一个把固定高清复古像素个人 IP 反复用于内容配图的 Agent Skill。

它支持两条独立路线：

1. **16:9 长文配图**：一张暖色封面，加上按文章视觉节拍生成的正文图。一个观点用迷你场景，步骤、清单、对比和结构用信息设计。
2. **3:4 知识卡片**：原文驱动的编辑式像素信息卡。页面先定内容模块、版式和文字，再决定角色是否作为讲解者出场。

两条路线共用一个已确认的角色包，但不会默认同时生成。

## 核心流程

```text
锁角色 → 读内容 → 定每张图的任务 → 选择视觉语法
→ 生成 → 对照返修 → 正确交付
```

角色可以来自真人、宠物、表情包、动漫角色、品牌 IP、吉祥物或已有形象。没有 `confirmed` 角色时，Skill 会先创建或导入角色包，展示干净主锚点和半身锚点，等用户明确确认后才开始配图。

## 安装

```bash
npx skills add rebecha1227-a11y/Jinger-Pixel-Illustration -g -y
```

或者：

```bash
npx github:rebecha1227-a11y/Jinger-Pixel-Illustration
npx github:rebecha1227-a11y/Jinger-Pixel-Illustration --codex
```

安装后重启客户端，然后说：

```text
使用 $jinger-pixel-illustration
```

## 你需要提供什么

| 内容 | 示例 |
|---|---|
| 角色参考 | 真人照、宠物、表情包、已有插画、品牌吉祥物 |
| 成品类型 | 16:9 长文、3:4 知识卡片，或两者 |
| 内容来源 | 文章 Markdown、正文、网页内容或已确认的要点 |
| 可选约束 | 水印、Logo、产品图、特殊道具、输出数量 |

知识卡片的数量由信息模块决定，不为了固定页数填充内容；单一聚焦问题也可以只做一张深讲卡。最终系列默认不超过九张，除非用户明确要求不同计划。

## 文件结构

```text
SKILL.md                         Agent 入口与路由
agents/openai.yaml               客户端显示信息
references/                      按需加载的工作流和设计合同
assets/                          角色像素与三类成品的画风锁
examples/                        公开示例，不是默认试用角色
scripts/                         角色注册与确定性校验
```

运行时生成的角色包和成品都保存到项目自己的 `.jinger-pixel-assets/`，不会写进 Skill 仓库。

## 无生图能力时

Skill 会交付角色锚点、visual plan、完整 Prompt、参考图路径和保存计划，并明确说明暂时没有 PNG 成品，不会伪装成已完成。

## 授权

工作流、脚本和文档见 [LICENSE](LICENSE)。Jinger 角色图和相关资产见 [LICENSE-ASSETS](LICENSE-ASSETS)。公开示例只用于说明角色包格式，请使用自己有权使用的素材。
