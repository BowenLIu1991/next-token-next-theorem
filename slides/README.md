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
| `?s=3` | 直接跳到第 4 页（URL 参数） |

## 当前范围

已做：S1–S44（完整 deck：Token → 模型 → 训练 → 应用 → AI × math → 结论）。

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
