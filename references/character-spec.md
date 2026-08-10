# Character Spec 模板

每个用户填写**自己的**角色。公开仓库只放本模板 + 示例。

- 真实照片、宠物图、表情包、Logo、私有设定 → 本地 `.jinger-pixel-assets/`，不要提交 GitHub
- 作者示范（画风锁，不是试用角色）→ `examples/jinger/`
- 公开填写示例（含图）→ `examples/ania/`

创建角色时按本模板写一份，存进该角色目录的 `character-spec.md`。

---

```markdown
# {角色名}

- name: {角色名}
- character_type: {human / pet / mascot / anime / brand / meme}
- watermark: @{handle或角色名}
- vibe: {最多3个词}
- accent_colors: [{色1}, {色2}, {色3}]

## 锁死外观

人类按下面填。宠物 / 吉祥物 / 表情包 / 品牌 IP 改成对应部位（毛色、耳朵、花纹、标志表情、标志色）。没有的项写「无」，不要编。

- 脸 / 神态 / 五官或表情：
- 肤色或毛色 / 主色：
- 发型 / 耳朵 / 头饰 / 剪影：
- 体型比例：（高清像素立绘；不要无故改成 Q 版大头，除非参考本身就是）
- 上衣或躯干花纹：
- 裤子 / 裙子 / 下半身：
- 鞋 / 爪子 / 尾巴：
- 帽 / 眼镜 / 耳机等头配件：
- 包 / 项链 / 其他标志物：

## 签名剪影

缩成很小的图时，仍能认出的 2–4 个记忆点（神态、剪影、标志色、花纹、帽子、包等）：

- 
- 

## 只允许改

动作、姿态、朝向、视线、轻微表情。场景道具可临时出现。

## 不允许改

神态记忆点、签名剪影、标志色/花纹/服装、身体比例、高清像素画风。
没有用户明确要求，禁止换到认不出、改成通用二次元、改成 3D / 写实。
```

---

## 参考图优先级

冲突时按此顺序，**画风锁不能盖过身份**：

1. 干净全身 `character-reference-clean`
2. 三视图 `character-sheet`（如果有；可选）
3. 半身 `character-bust`
4. 本文件文字设定
5. 捆绑画风锁图（`assets/character/` + `assets/style-lock/`，只学颗粒和密度）

## 生图时注入的身份锚点（短，勿整份粘贴）

Use the provided confirmed character reference as the primary identity reference.
Preserve recognizable identity: attitude/expression, signature silhouette, colors, markings, and outfit/accessories if present.
The character may change pose, gesture, and environment; keep the same memorable features.
Do not redesign the character. Do not substitute a generic character.
Do not copy another reference character's identity. Keep HD retro pixel art.
