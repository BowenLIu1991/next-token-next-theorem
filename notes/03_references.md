# 文献与工具清单（v4）

> 状态：✅ 已确认 / ⚠️ 需核实 / ⬜ 待补
> 报告前必须把 ⚠️ 全部处理掉。
> 当前主讲 51 页：代码审查案例第 34–37 页，系统总图第 38 页，AI × math 第 39–44 页，结论第 45–51 页。下表的 S 引用保留历史素材标识，当前显示页码以浏览器和最新大纲为准。

---

## 讲法参考

| 主题 | 来源 | 用途 | 状态 |
|---|---|---|---|
| "模型就是一个函数" | 李宏毅（Hung-yi Lee）NTU 机器学习 / 生成式 AI 课程 | S10 的讲法框架 | ✅ |
| "ChatGPT 输出下一个 token 的概率" | 同上 | S10–S11 | ✅ |

---

## Token 与模型结构

| 主题 | 文献 / 工具 | 用途 | 状态 |
|---|---|---|---|
| BPE | Sennrich et al., *Neural Machine Translation of Rare Words with Subword Units*, 2016 | S5 | ✅ |
| SentencePiece | Kudo & Richardson, 2018 | S5 | ✅ |
| Byte-level BPE | Radford et al., *GPT-2*, 2019 | S5 | ✅ |
| 分词工具 | OpenAI `tiktoken`；HuggingFace `tokenizers` | S4、S6 实测 | ✅ |
| Transformer | Vaswani et al., 2017 | S10–S12 | ✅ |
| 注意力回路 | Elhage et al., *A Mathematical Framework for Transformer Circuits*, 2021 | 备份 B3 | ✅ |
| 位置编码 | Su et al., *RoPE*, 2021 | 备份 B2 | ✅ |
| Scaling law | Kaplan et al., 2020；Hoffmann et al., 2022 | S14 | ✅ |

## 训练

### 2026-10-31 主讲：奖励、游戏与跨领域迁移

| 主题 | 来源 | 主讲用途与边界 |
|---|---|---|
| RL 概念 | Sutton & Barto, *Reinforcement Learning: An Introduction* | S13；控制与序列决策的背景，奖励学习策略 |
| Atari DQN | Mnih et al., [*Human-level control through deep reinforcement learning*](https://www.nature.com/articles/nature14236), Nature 2015 | S14–S15；像素、游戏分数与 Breakout 演示；已有更早预印本 |
| AlphaGo | Silver et al., [*Mastering the game of Go with deep neural networks and tree search*](https://www.nature.com/articles/nature16961), Nature 2016 | S14；监督学习、自我对弈 RL 与搜索的组合 |
| OpenAI Five | [*OpenAI Five defeats Dota 2 world champions*](https://openai.com/index/openai-five-defeats-dota-2-world-champions/), 2019-04-15 | S14；具体游戏配置下的团队比赛，不代表开放现实环境 |
| AlphaStar | Vinyals et al., [*Grandmaster level in StarCraft II using multi-agent reinforcement learning*](https://www.nature.com/articles/s41586-019-1724-z), Nature 2019 | S14；部分可观测、多智能体环境 |
| 数学 RL → 代码 | Chen et al., [*AceReason-Nemotron*](https://arxiv.org/abs/2505.16400), 2025 | S17；已读摘要与正文，数学专用 RL 对强蒸馏模型提高 LiveCodeBench 表现；不是任意数学训练必然改善代码 |
| 代码 → 状态追踪 | Kim, Schuster & Toshniwal, [*Code Pretraining Improves Entity Tracking Abilities of Language Models*](https://arxiv.org/abs/2405.21068), 2024 | S17；已读摘要，具体推理子技能，不是全部逻辑能力 |
| 跨领域收益与冲突 | Li et al., [*Can One Domain Help Others?*](https://arxiv.org/abs/2507.17512), 2025 | 讲者备注；基础模型、训练域和数据配比影响迁移，观察到收益也有冲突 |

下表中的训练机制页码为旧稿；相关细节现位于备份模式，不在主讲 S13–S24 中展开。

| 主题 | 文献 / 工具 | 用途 | 状态 |
|---|---|---|---|
| 指令微调 | Ouyang et al., *InstructGPT*, 2022 | S16 | ✅ |
| RLHF | Christiano et al., 2017 | S17 | ✅ |
| DPO | Rafailov et al., 2023 | S17 | ✅ |
| RLVR 术语 | Lambert et al., *Tulu 3*, 2024 | S18 | ⚠️ 术语出处待确认 |
| GRPO | Shao et al., *DeepSeekMath*, 2024 | S18 / 备份 B10 | ✅ |
| 推理模型 | DeepSeek-R1, 2025 | S21 | ✅ |
| 过程奖励 | Lightman et al., *Let's Verify Step by Step*, 2023 | 备份 | ✅ |
| 代码 RL | Le et al., *CodeRL*, 2022 | S20 | ✅ |
| 竞赛代码 | Li et al., *AlphaCode*, 2022 | S21 | ✅ |
| AlphaProof | Hubert et al., *Olympiad-level formal mathematical reasoning with reinforcement learning*, Nature 651, 607–613, 2025 | S39–S40 | ✅ |
| AlphaFold 2 | Jumper et al., *Highly accurate protein structure prediction with AlphaFold*, Nature 596, 583–589, 2021 | S21 | ✅ |
| 2024 诺贝尔化学奖 | Baker（蛋白质设计）、Hassabis & Jumper（蛋白质结构预测），2024 | S21 | ✅ |

> AlphaFold 是监督学习，不是 RL；不要把它和 Atari / AlphaGo / AlphaStar 混成 RL。

## 上下文与 agent

| 主题 | 文献 / 工具 | 用途 | 状态 |
|---|---|---|---|
| 长上下文失效 | Liu et al., *Lost in the Middle*, 2023 | S25 | ✅ |
| Agent 设计 | Anthropic, *Building Effective Agents*, 2024 | S27–S28 | ✅ |
| 代码 agent | Yang et al., *SWE-agent*, 2024 | S28 | ✅ |
| 代码审查参考案例 | Addy Osmani, Morgan Westlee Lunt & Qing Wang, [*How the Claude Code team does code review*](https://claude.dev/blog/solving-code-review-at-anthropic/), 2026-10-15 | S36–S39：产出激增 → 人工瓶颈 → 系统检查 → 风险分工与评测积累 | ✅ 已读原文；monorepo 与 Claude Code 独立仓库数字分开；团队自述，非独立效果验证 |
| Context rot | Chroma 技术报告, 2025 | S25 | ⚠️ 行业报告，非同行评审 |
| prompt caching | 各供应商文档 | S8 | ⚠️ 价格随日期变 |

## 形式化（备份）

| 主题 | 文献 / 工具 | 用途 | 状态 |
|---|---|---|---|
| Lean 4 | lean-lang.org | 备份 B11 | ✅ |
| Mathlib | mathlib4 文档 | 备份 B11 | ✅ |
| LeanDojo | Yang et al., NeurIPS 2023 | 备份 B11 | ✅ |
| Flyspeck | Hales et al., 2017 | 可选历史锚点 | ✅ |

## AI × math（2023–2026）

| 工作 | 公开来源 | 用途 | 状态 |
|---|---|---|---|
| FunSearch | Romera-Paredes et al., *Mathematical discoveries from program search with large language models*, Nature 625, 2024 | S39–S40 | ✅ |
| AlphaGeometry | Trinh et al., *Solving olympiad geometry without human demonstrations*, Nature 625, 2024 | S39–S40 | ✅ |
| AlphaProof | Hubert et al., *Olympiad-level formal mathematical reasoning with reinforcement learning*, Nature 651, 607–613, 2025 | S39–S40 | ✅ |
| o1 | OpenAI, *Learning to reason with LLMs*, 2024-09 | S39–S40 | ✅ |
| DeepSeek-R1 | DeepSeek-AI, *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*, 2025-01 | S39–S40 | ✅ |
| AlphaEvolve | DeepMind, *AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms*, 2025-05 | S39–S40 | ✅ |
| IMO 2025 | OpenAI / Google DeepMind 赛后声明，2025-07 | S39–S40 | ✅ |
| Erdős problems | 2025–26 公开讨论；Tao 的博客与问题页 | S39、S43 | ⚠️ 逐题核实 |
| OpenAI 2026 数学进展 | OpenAI, [*Sharing AI progress in mathematics*](https://openai.com/index/sharing-ai-progress-in-mathematics/), 2026-10-06 | 当前 S41–S45 | ⚠️ 原文已重读；三小时指 ChatGPT Pro 等价算力，非墙钟时间；具体数学结果需逐项核实 |
| Erdős 单位距离 | OpenAI, *An OpenAI model has disproved a central conjecture in discrete geometry*, 2026-05-20 | S39 | ✅ |
| Navier–Stokes 声称 | OpenAI, [*On the Navier–Stokes Millennium Prize Problem*](https://openai.com/index/navier-stokes-solution/), 2026-09-08 | 当前 S42–S43 | ⚠️ 已读公司原文；本轮未验证证明或形式化覆盖范围 |
| 独立报道 | Science, *OpenAI just changed math forever...*, 2026-10-13；The Economist, 2026-10-07 | S38–S40 | ✅ |

> S40 的英文是节选 / 意译；公开材料只覆盖一部分，完整的训练配方仍不可见。引用时不要把"公开表述"当成完整方法说明。

---

## 天体力学相关 AI（备份）

| 主题 | 文献 / 工具 | 用途 | 状态 |
|---|---|---|---|
| 行星系统稳定性 | Tamayo et al., *SPOCK*, PNAS 2020 | 备份 | ✅ |
| 符号回归 | Brunton et al., *SINDy*, PNAS 2016 | 备份 | ✅ |
| Hamiltonian 网络 | Greydanus et al., NeurIPS 2019 | 备份 | ✅ |

---

## 必须实测/核对的数字

1. **S4、S6**：词表大小与中、英、代码、数字在 2–3 个 tokenizer 下的 token 数（脚本见 `07_token_and_api.md`）。
2. **S8**：报告当日的输入/输出/缓存价格。
3. **S21**：代码 RL → 数学 benchmark 的具体提升幅度，必须给出数据集、baseline、harness。
4. **S28**：同模型不同 harness 的成功率差异，优先找有 ablation 的论文。
5. **S30**：案例 trace 的墙钟时间、token 消耗、人工介入次数。

---

## 引用原则

- 只引用能打开原文的数字。
- 任何"提升 X%"必须说明 baseline、数据集、harness。
- 行业报告与同行评审论文分开标注。
- 价格与版本号注明日期。
