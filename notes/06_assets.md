# 图表与素材清单（v8）

> 当前两版各 **47 页**：英文主站 `docs/index.html`，中文 `docs/zh.html`。绝大多数“图”是 HTML/CSS 或 MathML 自绘；外部图片只有 3 张截图。
> HTML 是事实来源；本清单只记素材来源与待办。

---

## 外部截图（3 张）

| 文件 | 页面 | 内容 |
|---|---|---|
| `assets/figures/deepseek_usage.png` | S5 | 余额 + 2.85 亿 token / 2,599 次请求 |
| `assets/figures/deepseek_pricing.png` | S6 | 缓存命中 / 未命中 / 输出价格 |
| `assets/figures/agent_client.png` | S34 | Agent 客户端：Thought / 工具 / 上下文 |

原始完整截图：

| 文件 | 内容 |
|---|---|
| `assets/figures/deepseek_ref_1.png` | DeepSeek 用量后台 |
| `assets/figures/deepseek_ref_2.png` | 模型细节与价格表 |
| `assets/figures/agent_client_1728_1.png` | Agent 客户端 |

---

## 自绘视觉（按章节）

| 章节 | 页面 | 视觉 |
|---|---|---|
| Token | S2–S4 | 英文 + 中文（各 10 token）两个例子、词表账本、规模标尺 |
| 模型 | S8–S11 | 输入 → 概率分布（MathML softmax）、采样、无状态 |
| 训练 | S12–S24 | 知识 → 行为 → 策略、交叉熵、PPL、压缩、SFT、RL、RL 时间线 |
| 应用 | S27–S36 | 条件分布偏移、CoT、上下文膨胀条、大海捞针热图、工具调用、Agent、记忆网格、harness |
| 应用总图 | S37 | LLM 中心；prompt/context 内圈；memory/agent loop 中圈；harness 外圈 |
| AI × math | S38–S43 | 加速前后对比、三阶段时间线、公开表述表、生成/验证/搜索流程、猜测网格、已解决/未解决 |
| 结论 | S44 | token → 概率 → 候选 → 验证 → 定理 |

> 公式统一用 MathML + STIX Two Math，不依赖外部 JS / CDN。
> 热图与部分条形图为示意，页面上已标“示意”。

---

## 备份图（不进主线）

| ID | 内容 | 用途 |
|---|---|---|
| B1 | Transformer 整体结构 | Q&A |
| B2 | attention 的 Q/K/V | Q&A |
| B3 | MLP 与残差流 | Q&A |
| B4 | KV cache | Q&A |
| B5 | BPE 合并过程 | 有人问“词表怎么来的” |
| B6 | 三种 tokenizer 完整对比 | Q&A |
| B7 | GRPO 公式与组内优势 | 训练 Q&A |
| B8 | reward hacking 五种手法 | 训练 Q&A |
| B9 | Lean 最小示例 | Q&A |
| B10 | 参考文献 | 备用 |

---

## 演示（2 个）

| ID | 内容 | 形式 | 备注 |
|---|---|---|---|
| D1 | 一句话被实时切成 token | 现场或录屏 20 秒 | 用 `tiktoken`，已缓存 |
| D2 | 中/英/代码 token 数对比 | 现场跑脚本 | 输出直接投屏 |

---

## 需要采集

- [ ] 案例 trace 的墙钟时间、token 数、人工介入次数
- [ ] 失败尝试次数与失败类型
- [ ] AI × math 引用的卷期 / 链接逐条核对（见 `03_references.md`）

---

## 排版备注

- 截图统一圆角 12px，深色底不加白边。
- token 序列用等宽字体，`▁` 表示前导空格。
- 每页一个视觉焦点。
