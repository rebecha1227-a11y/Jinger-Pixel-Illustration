# 本地角色包

## 运行目录

优先：

```text
<project-root>/.jinger-pixel-assets/
```

没有可写项目时回退：

```text
~/.jinger-pixel-assets/
```

用户指定目录时听用户。不要把 Skill 安装目录当运行目录，不要把用户参考素材或生成角色提交到 GitHub。

## 结构

```text
.jinger-pixel-assets/
├── current-character.json
├── characters/
│   └── <slug>/
│       ├── character.json
│       ├── character-reference-clean.png   ← 必须，主身份锚点（默认全身；表情包可为头身）
│       ├── character-bust.png              ← 必须，半身/头身特写
│       ├── character-spec.md               ← 必须
│       ├── character-sheet.png             ← 可选三视图
│       └── *-v2.png
├── illustrations/
│   └── <article-slug>/
│       ├── 00-cover.png
│       └── 01-topic.png
└── cards/
    └── <slug>/
        ├── shotlist.md
        └── images/
```

`slug` 用小写英文 kebab-case。中文名放在 manifest 的 `name`。

公开仓库的 `examples/` 只是示范，不是运行时角色包。

## 状态

- `draft`：已生成或修订，等待确认；不能配图，不能激活
- `confirmed`：用户明确确认；可配图，可设为当前角色

「看起来不错」不算确认。要听到「确认 / 定稿 / 就用这个」。

没有三视图也可以 confirmed。

## 脚本

在 Skill 根目录运行。`<runtime-root>` 是 `.jinger-pixel-assets`。

注册草稿（`--sheet` 可选）：

```bash
python3 scripts/character_registry.py register \
  --root <runtime-root> \
  --slug my-character \
  --name "角色名" \
  --clean-reference path/to/character-reference-clean.png \
  --bust path/to/character-bust.png \
  --spec path/to/character-spec.md \
  [--sheet path/to/character-sheet.png]
```

确认后补三视图：

```bash
python3 scripts/character_registry.py attach-sheet \
  --root <runtime-root> \
  --slug my-character \
  --sheet path/to/character-sheet.png
```

确认并设为当前角色：

```bash
python3 scripts/character_registry.py confirm --root <runtime-root> --slug my-character
```

列出 / 切换 / 查看：

```bash
python3 scripts/character_registry.py list --root <runtime-root>
python3 scripts/character_registry.py activate --root <runtime-root> --slug <slug>
python3 scripts/character_registry.py resolve --root <runtime-root>
```

脚本不可用时，按同样结构手建文件，状态仍从 `draft` 开始。

## 作者 Jinger

仅静儿本人可运行：

```bash
python3 scripts/bootstrap_jinger.py --i-am-the-author --root <runtime-root>
```

这会把仓库内 Jinger 资产登记为 confirmed。开源用户禁止使用。
