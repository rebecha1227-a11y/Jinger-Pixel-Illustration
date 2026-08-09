#!/usr/bin/env node
/**
 * Install Jinger Pixel Illustration into local Agent Skills folders.
 * Usage:
 *   npx github:rebecha1227-a11y/Jinger-Pixel-Illustration
 *   npx github:rebecha1227-a11y/Jinger-Pixel-Illustration --cursor
 *   npx github:rebecha1227-a11y/Jinger-Pixel-Illustration --claude
 *   npx github:rebecha1227-a11y/Jinger-Pixel-Illustration --codex
 */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SKILL_NAME = "jinger-pixel-illustration";
const SKILL_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const IGNORE = new Set([
  ".git",
  ".gitignore",
  ".DS_Store",
  "node_modules",
  ".jinger-pixel-assets",
  "output",
  "package-lock.json",
]);

const AGENTS = {
  claude: path.join(".claude", "skills", SKILL_NAME),
  cursor: path.join(".cursor", "skills", SKILL_NAME),
  codex: path.join(".codex", "skills", SKILL_NAME),
};

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    if (IGNORE.has(entry.name)) continue;
    const from = path.join(src, entry.name);
    const to = path.join(dest, entry.name);
    if (entry.isDirectory()) copyDir(from, to);
    else fs.copyFileSync(from, to);
  }
}

function parseTargets(argv) {
  const flags = argv.filter((arg) => arg.startsWith("--")).map((arg) => arg.slice(2));
  const known = flags.filter((name) => name in AGENTS);
  if (known.length > 0) return known;
  return Object.keys(AGENTS);
}

function main() {
  if (!fs.existsSync(path.join(SKILL_ROOT, "SKILL.md"))) {
    console.error("找不到 SKILL.md，安装脚本需要在仓库根目录运行。");
    process.exit(1);
  }

  const home = os.homedir();
  const targets = parseTargets(process.argv.slice(2));
  const installed = [];

  for (const name of targets) {
    const dest = path.join(home, AGENTS[name]);
    copyDir(SKILL_ROOT, dest);
    installed.push(dest);
    console.log(`已安装到 ${dest}`);
  }

  console.log("");
  console.log(`Jinger Pixel Illustration 已装好（${installed.length} 处）。`);
  console.log("请重启 Cursor / Claude Code / Codex，然后可以说：");
  console.log("使用 $jinger-pixel-illustration");
}

main();
