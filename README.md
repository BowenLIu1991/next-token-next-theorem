# From Next Token to Next Theorem
### 从下一个 token 到下一个定理

A 45-minute talk on how large language models actually work — and how next-token prediction becomes mathematical problem solving.

[**English slides**](https://bowenliu1991.github.io/next-token-next-theorem/) · [**中文版**](https://bowenliu1991.github.io/next-token-next-theorem/zh.html) · [**English PDF**](docs/from-next-token-to-next-theorem.pdf) · [**中文 PDF**](docs/from-next-token-to-next-theorem-zh.pdf)

---

## 这场报告讲什么

面向天体力学 / 动力系统研究者，不假设 AI 背景，也不做“AI 像物理”的类比。

主线只有一条：

```
token → 模型 → 训练 → 使用 → AI × math → 结论
```

- **Token**：模型看到的不是文字，是整数。
- **模型**：一个函数，输入 token 序列，输出下一个 token 的概率分布。
- **训练**：pretrain 给知识，SFT 给行为，RL 给搜索与纠错的习惯。
- **使用**：prompt、context、memory、agent loop、harness 如何组合成系统。
- **工程参考案例**：S36–S39 依据 [Claude Code 团队的代码审查实践](https://claude.dev/blog/solving-code-review-at-anthropic/)（2026-10-15），讲述代码产出激增 → 人工审查瓶颈 → 系统化检查 → 风险分工与评测积累，供学术同行参考。
- **AI × math**：FunSearch、AlphaGeometry、AlphaProof、o1 / R1、AlphaEvolve、IMO 2025，以及 2026 年 OpenAI 的公开声称。
- **结论**：概率负责广度，验证负责正确，人负责方向。

贯穿全场的一个例子是《天体力学基础》：

> 本书系统地介绍了天体力学的基本概念和定理，以及一些比较有代表性的研究成果。

从这句话的 token、下一个 token 的概率，一路讲到 SFT、RLVR 和“下一个定理”。

---

## 幻灯片

- **53 页**，16:9，1280 × 720。
- 单文件 HTML，无外部 JS / CDN；公式用 MathML + STIX。
- 键盘操作：
  - `←` `→` / `Space`：翻页
  - `N`：显示讲稿备注
  - `F`：全屏
  - `?s=N`：直接跳到第 N 页（0-based）
- 英文版是主站，中文版保留在 `zh.html`。

在线地址（启用 GitHub Pages 后）：

> 英文：https://bowenliu1991.github.io/next-token-next-theorem/  
> 中文：https://bowenliu1991.github.io/next-token-next-theorem/zh.html

GitHub Pages 设置（一次性）：

```
Settings → Pages → Build and deployment
→ Deploy from a branch
→ Branch: main
→ Folder: /docs
```

`docs/` 里已经放好 `index.html`、三张截图和 PDF，并加了 `.nojekyll`。

---

## PDF

直接下载：

- English: [docs/from-next-token-to-next-theorem.pdf](docs/from-next-token-to-next-theorem.pdf)
- 中文: [docs/from-next-token-to-next-theorem-zh.pdf](docs/from-next-token-to-next-theorem-zh.pdf)

重新生成：

```bash
# English (docs/index.html)
python3 assets/demos/render_pdf.py --html docs/index.html --out docs/from-next-token-to-next-theorem.pdf

# 中文 (docs/zh.html)
python3 assets/demos/render_pdf.py --html docs/zh.html --out docs/from-next-token-to-next-theorem-zh.pdf
```

脚本从 HTML 自动统计页数，用 Chrome 逐页截图（`?clean=1`），再用 Pillow 合成 13.333 × 7.5 英寸、当前 53 页的满版 PDF。依赖：

```bash
python3 -m pip install pillow pypdf
```

> 为什么不用 Chrome 直接 `--print-to-pdf`：Chrome 的默认打印边距会把 16:9 页面缩到约 88%，留下白边；逐页截图可以保证满版。

---

## 仓库结构

```
.
├── docs/                         # GitHub Pages 站点
│   ├── index.html                # English (primary)
│   ├── zh.html                   # 中文版
│   ├── assets/figures/           # 站点引用的截图
│   ├── from-next-token-to-next-theorem.pdf      # English
│   ├── from-next-token-to-next-theorem-zh.pdf   # 中文
│   └── .nojekyll
├── slides/
│   ├── en.html                   # English source (53 pages)
│   ├── index.html                # 中文源文件（53 页，自包含）
│   └── README.md                 # 操作与排版约定
├── notes/
│   ├── 00_discussion_log.md      # 讨论与决策记录
│   ├── 01_outline.md             # 45 分钟大纲
│   ├── 02_slide_script.md        # 逐页脚本（历史稿）
│   ├── 03_references.md          # 文献与来源
│   ├── 04_open_questions.md      # 待定事项
│   ├── 05_qa.md                  # 预判提问
│   ├── 06_assets.md              # 图表与素材
│   ├── 07_token_and_api.md       # token 与 API 专题
│   ├── 08_rl_math_code.md        # 数学/代码 RL 专题
│   └── 09_token_measurements.md  # tokenizer 实测
├── assets/
│   ├── figures/                  # 原始截图与裁切
│   └── demos/                    # token 计数 + PDF 渲染
└── README.md
```

## 审核

- 当前审核记录与待确认事项：[notes/10_review_audit.md](notes/10_review_audit.md)。
- `assets/demos/audit_deck.py` 检查页码、浏览器文字几何与缺图；内容来源、叙事和视觉阅读仍需单独审核。
- 示例：`python3 assets/demos/audit_deck.py --html docs/index.html --out /path/to/audit.json`。

---

## 本地查看

最简单：

```bash
open docs/index.html
```

或者起一个本地服务器（推荐，路径和字体加载更稳定）：

```bash
python3 -m http.server 8000
# http://localhost:8000/docs/
```

源文件在 `slides/index.html`；改完后同步到 `docs/`：

```bash
cp slides/index.html docs/index.html
# 把 ../assets/figures/ 改成 assets/figures/
sed -i '' 's#\.\./assets/figures/#assets/figures/#g' docs/index.html
```

---

## 事实与口径

这部分是报告可信度的核心。

- **AlphaFold 不是 RL**：它是监督学习，用已知蛋白质结构做标签；2024 年诺贝尔化学奖表彰的是蛋白质结构预测与设计，不是强化学习。
- **IMO 2025 是“金牌级”**，不是官方金牌；Gemini 由 IMO 协调员评分，OpenAI 由前奖牌得主评分。
- **2026 年 OpenAI 的 372 个问题**：公司公开报告，722 篇论文，其中 3 个撤回，同行评议未完成。幻灯片用“报告”，不用“证明”。
- **Navier–Stokes / 黎曼相关**：都是公开声称，争议中；372 批里的 “quasi-Riemann” 不是完整黎曼猜想证明。
- **价格与用量**：来自报告当日的截图；价格会变。
- **所有引用与链接**：见 [`notes/03_references.md`](notes/03_references.md)。

---

## 设计原则

1. 不做 AI ↔ 力学的概念类比，只讲机制。
2. 不推导反向传播，不写 attention 公式；讲“它在干什么”。
3. 每个概念给定义、例子、失败模式。
4. 主动讲边界，比只讲成功案例更能建立信任。
5. 数字标注来源；公司声称与同行评议分开写。

---

## 状态

- [x] 50 页 HTML 幻灯片（English + 中文）
- [x] PDF 导出（两版各 50 页）
- [x] GitHub Pages 目录（`docs/`，英文主站）
- [x] 讲稿、提纲、文献、Q&A
- [x] tokenizer 实测数据
- [ ] 试讲计时
- [ ] 报告当日价格复核

---

## License

© 2026 Bowen Liu. Slides and notes are shared for reading and discussion. Please contact me before reusing them in talks, courses, or publications.

GitHub: [@BowenLIu1991](https://github.com/BowenLIu1991)
