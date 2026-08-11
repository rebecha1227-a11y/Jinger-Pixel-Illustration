# 知识卡片页型（Shot list 用）

页型用于**拆多卡系列**，不是生图时死套的 HTML。  
真正构图：先选 `card-layout-system.md` 的**版式模具**，再按内容类型微调。  
内容必须来自原文（`card-content-analysis.md`）。

| 页型 | 干什么 | 推荐模具 | 讲解者怎么演（若出场） |
|---|---|---|---|
| 封面 cover | 一句话钩子 | `cover-hook` | 半身表情 / 手持主题物 |
| 痛点 pain | 读者卡在哪 | `qa-metaphor` 或 `two-panel` | 推开混乱模块，或坐在痛点旁 |
| 概念 concept | 一个判断/定义 | `qa-metaphor` | 举起定义框、指向中央隐喻物 |
| 步骤 steps | 3–5 步 | `steps-flow` | 指向某一步；可 `none` |
| 对比 compare | 错 vs 对 | `wrong-right-tips` | 站在「对」侧，或底栏半身讲解；表自洽可 `none` |
| 避坑 pitfall | 常见误区 | `qa-metaphor` / `wrong-right-tips` | 拦住错误做法 |
| 立刻试 cta | 下一步小动作 | `cta` | 递出 CTA 模块 |

封面必有。最后一页默认 cta。

## Shot list 额外字段

- `SOURCE SECTION`：对应原文哪一节  
- `LAYOUT MOLD`：`cover-hook` / `definition-dashboard` / `architecture-tree` / `qa-metaphor` / `wrong-right-tips` / `two-panel` / `steps-flow` / `cta`
- `MODULES` + 短说明（来自原文）  
- `CHARACTER CROP`：`none` / `bust` / `fullbody` / `multi-mini` + 理由（互动/占位/职能测试）  
- `CHARACTER SLOT` + `CHARACTER FOOTPRINT` + `CHARACTER BINDINGS`
- `LOOK LOCK` + `FRAME / SURFACE / TYPE / PANEL CONTRACT` + `DENSITY BAND`
- `IDENTITY METHOD`：默认 `edit-from-package`  

## 图内文字预算

- 封面：大标题 + 副标题 + 可选 banner；可再加 1 句核心定义  
- 知识页：模块标题 + 必要说明句；步骤/对比用编号完整短句  
- 单卡深讲：模块可更多，仍短句，不贴整段文章  
- 禁止只有三行钩子；也禁止模型发明原文没有的 tip 列表  

## 场景与色

几乎纯色暖米白 + RPG/像素 UI；对齐 `knowledge-card-editorial-3x4.png`。  
色纪律见 `card-style-system.md`（一个低饱和主强调色家族 + 可选 `<3%` 语义微强调）。不要复杂房间剧场。
