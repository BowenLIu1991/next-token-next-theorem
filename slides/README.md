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

当前主讲 **41 页**：封面 1；天体力学研究简介 2；全景 3；Token 4–9；模型 10；训练与奖励 11–22；无状态 23；四短板 24；系统与工程 25–31；AI × math 32–40；结论 41。REFLEX 电商案例整页已删除，简介现单位写为“某美国电商公司”。第 36 页左右对照 DAG/MCTS，第 37 页讲个人猜测的证明图演进，第 38 页讲系统与模型瓶颈，第 39–40 页介绍 OpenAI 批量发布及 NS 声称。正文与定义使用大字号，来源和方法边界保留在讲稿与可点击引用中。

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
