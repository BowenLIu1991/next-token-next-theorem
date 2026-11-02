# 幻灯片

`index.html` 是自包含的 16:9 幻灯片，双击即可打开，无需联网、无外部依赖。

## 操作

| 键 | 功能 |
|---|---|
| `→` `↓` `Space` `PageDown` | 下一页 |
| `←` `↑` `PageUp` `Backspace` | 上一页 |
| `Home` / `End` | 首页 / 末页 |
| `N` | 显示讲稿备注 |
| `F` | 全屏 |
| 右上角「全屏」按钮 | 点击进入或退出全屏；也可用 `Esc` 退出 |
| `?s=3` | 直接跳到第 4 页（URL 参数） |

## 当前范围

当前主讲 39 页（完整 deck：Token → 模型 → 训练概览与奖励 → 应用 → AI × math → 结论）。第 2 页为可点击的全景导航；原两页采样介绍、“一个测试或反例”页及“训练与工作，使用不同的循环”页已删除；应用开头的“从会说话到会干活”“2023”“Prompt”三页，以及 CoT 与 CoT pruning 两页也已删除；编程、数学、产品设计和交易合并为第 20 页的四类对比，第 22 页总结环境、反馈、loss 与反向传播，第 14–16 页为 GRPO 公式、机制与 REFLEX 实例，第 23 页是“模型没有记忆”，第 24 页收束四个短板与三类能力，第 25 页讲 Context window 的膨胀，第 26 页把 Context 有限、Context engineering 与 Memory 合成一页，第 27 页讲 Tool calling，第 28 页讲 Harness，第 29 页为系统图，第 30 页讲 Skill，第 31 页讲长时间运行如何把 loop 固化成 skill。

显示页码由当前顺序自动计算；源文件 S 注释及静态页码占位保留历史标识，后续页码以浏览器显示为准。下述试讲调整是删页前的历史记录。

2026-10-31 试讲调整：S1–S11 保留；S12 训练概览；S13–S24 奖励、游戏、数学与代码的共性及开放任务的边界。原训练细节保存于 `training-details` 模板中，默认不显示；用 `?appendix=1` 单独打开 12 页备份。浏览器翻页、审核与 PDF 页数统计均区分主讲与备份。

- `index.html`：中文源文件
- `en.html`：English source
- `docs/index.html`：English deployment copy (primary)
- `docs/zh.html`：中文 deployment copy

后续每加一节，就在 `index.html` 的 `#stage` 里追加一个 `<section class="slide">`，并更新页码。

## 设计约定

- 画布固定 1280 × 720，按窗口等比缩放。
- 浅色纸面 + 单一朱红强调色；token 序列用深色面板。
- 每页一个视觉焦点；正文只放短句和数字，长解释进 `data-notes`。
- 字号：标题 44–58px，正文 15.5–19px，注释 12px。

## 预览

```bash
# 用 Chrome 无头截图（用于自检）
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1280,720 --virtual-time-budget=4000 \
  --run-all-compositor-stages-before-draw \
  --screenshot=../assets/figures/preview.png \
  "file://$PWD/index.html?s=0"
```
