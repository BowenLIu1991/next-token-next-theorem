# 文献与工具清单（v4）

> 状态：✅ 已确认 / ⚠️ 需核实 / ⬜ 待补
> 报告前必须把 ⚠️ 全部处理掉。
> 当前主讲 32 页：简介 2，全景 3，GRPO 12，系统与工程 16–23，AI × math 24–31，结论 32。REFLEX 已整页删除。下表旧 S 引用保留历史，以最新大纲与浏览器为准。

## 2026-11-10 补充核对与方法边界

| 来源 | 页面 | 使用范围 |
|---|---|---|
| 本人提供的履历 | 2 | 天体力学研究与职位；现单位匿名，不公开业务成绩与联系方式 |
| Chen & Li, [A Theoretical Framework for Self-Play Theorem Proving Algorithms](https://arxiv.org/abs/2606.01861) | 26 | 定理语义图上的可逆随机游走、prover/conjecturer 与多样性；有条件的理论保证，不是 OpenAI 方法披露，也不是依赖 DAG/MCTS |
| OpenAI, [Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/) | 27 | 已读官方公告；平均约 3 Pro 小时为算力等价值 |
| [openai/math](https://github.com/openai/math)，[首发口径的固定版本](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a) | 27 | 通过搜索索引读取 README：722 手稿、372 结果族、约 4,000 尝试问题。直接读取仓库超时；没有逐篇检查或本地编译。发布统计不是成功率，当前仓库计数可变化 |
| OpenAI, [NS 公告](https://openai.com/zh-Hans-CN/index/navier-stokes-solution/)，[openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) | 28 | 已读英文官方正文与检索到的仓库说明；带光滑外力、三维、正黏性、全空间与周期情形、Clay C/D；约 10,000 并发、88h 加 17h 为公司披露 |
| Bastounis, Circelli & Hansen, [Navier–Stokes lost in translation](https://arxiv.org/abs/2610.08144) | 28 | 自然语言证明与 Lean 证明对应差异的讨论；未据此断言最终定理错误 |
| Clay Mathematics Institute, [2026-09-11 announcement](https://www.claymath.org/news/navier-stokes-announcement/) | 28 讲稿 | 表述 apparently settled，同时说明评估审慎进行；不写成已授奖 |

**实现猜测**：外部图/树状态 + Agent 提议 + Lean 检查 + 更新节点，是演讲者的假设；MCTS 仅为选点策略的可能实现。“问题爆破”为个人概括，非原文引语。没有从上述来源推断 OpenAI 已采用 DAG/MCTS。

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
| REFLEX | Y. Zhang, **B. Liu**, X. Zhang, A. Mandal, C. Xu, Z. Wu, *REFLEX: Reinforcement Feedback Learning with LLMs for E-commerce Query Expansion*, WSDM 2026, 1288–1292 | 第 16 页 GRPO 实例：搜索引擎在环、无人工标注奖励、SFT 预热 + GRPO、消融结果 | ✅ 依据论文与作者材料；结果限于该数据集与 3B 骨干 |

下表中的训练机制 S 页码为旧稿；相关细节现位于备份模式，不在主讲中展开。GRPO 与 REFLEX 的主讲页码按当前顺序（第 14–16 页）。

| 主题 | 文献 / 工具 | 用途 | 状态 |
|---|---|---|---|
| 指令微调 | Ouyang et al., *InstructGPT*, 2022 | S16 | ✅ |
| RLHF | Christiano et al., 2017 | S17 | ✅ |
| DPO | Rafailov et al., 2023 | S17 | ✅ |
| RLVR 术语 | Lambert et al., *Tulu 3*, 2024 | S18 | ⚠️ 术语出处待确认 |
| GRPO | Shao et al., [*DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models*](https://arxiv.org/abs/2402.03300), arXiv:2402.03300, 2024 | 第 14 页目标函数、第 15 页机制 / 备份 B10 | ✅ 公式按论文 GRPO 目标整理 |
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
| 代码审查参考案例 | Addy Osmani, Morgan Westlee Lunt & Qing Wang, [*How the Claude Code team does code review*](https://claude.dev/blog/solving-code-review-at-anthropic/), 2026-10-15 | 已从主讲删除；保留为备用素材 | ✅ 已读原文；monorepo 与 Claude Code 独立仓库数字分开；团队自述，非独立效果验证 |
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
