# Token 实测数据（2026-10）

用 `tiktoken` 实测，脚本见 `assets/demos/token_count.py`。
编码器：`o200k_base`（GPT-4o 一代）、`cl100k_base`（GPT-4/3.5 一代）、`gpt2`（老一代）。

---

## 主表

| 样本 | 字符数 | o200k_base | cl100k_base | gpt2 |
|---|---|---|---|---|
| 英文 | 44 | 10 | 9 | 10 |
| 中文 | 15 | 13 | 18 | 28 |
| 中英混排 | 49 | 11 | 11 | 16 |
| 代码 | 26 | 10 | 10 | 14 |
| 数字 | 10 | 4 | 4 | 4 |
| 公式 | 17 | 12 | 13 | 12 |

样本内容：

- 英文：`Celestial mechanics is the poetry of orbits.`
- 中文：`天体力学是研究天体运动的学科。`
- 中英混排：`三体问题 is a classic problem in celestial mechanics.`
- 代码：`def f(x):\n    return x**2\n`
- 数字：`1234567890`
- 公式：`x'' + 2y' = dΩ/dx`

---

## 关键观察

### 1. 中文的 token 数强烈依赖 tokenizer

同一句 15 字中文：

- `o200k_base`：13 token（约 0.87 token/字）
- `cl100k_base`：18 token（1.2 token/字）
- `gpt2`：28 token（1.87 token/字）

新一代 tokenizer 对中文友好得多。**"中文更贵"只在老 tokenizer 上成立。**

### 2. 数字被切成不等长片段

`1234567890` → `["123", "456", "789", "0"]`

模型看不到"位"，自然也难以做竖式对齐。这解释了为什么算术错误常常不是"笨"，而是表示问题。

### 3. 空格与缩进是真实成本

代码样本 26 个字符，切成 10 个 token，其中三个空格缩进单独占一个 token。

### 4. 英文的切分点不在词根上

`Celestial` → `["Cel", "estial"]`，`orbits` → `["or", "bits"]`。

切分是统计驱动的，不是词法驱动的。

---

## 开场页的中文例子（《天体力学基础》）

`本书系统地介绍了天体力学`：12 个字 → `o200k_base` 10 个 token。

| 字符 | 本 | 书 | 系统 | 地 | 介绍 | 了 | 天 | 体 | 力 | 学 |
|---|---|---|---|---|---|---|---|---|---|---|
| ID | 4087 | 20121 | 31936 | 5557 | 37887 | 4531 | 867 | 7074 | 11343 | 8590 |

和英文 `Celestial mechanics is the poetry of orbits.`（46 字符 → 10 token）并排：两种文字、两句话，都是 10 个整数。中文并不是"一字一 token"：`系统`、`介绍` 各占一个 token。

---

## 附：三种编码器的词表大小

| 编码器 | 词表大小 | 代际 |
|---|---|---|
| `r50k_base` | 50,257 | GPT-2 |
| `cl100k_base` | 100,277 | GPT-4 / 3.5 |
| `o200k_base` | 200,019 | GPT-4o |

词表大小直接决定两处参数量：

```
输入 embedding：词表大小 × 维度
输出层：词表大小 × 维度
```

以 200,019 × 4,096 为例，单层约 8.2 亿参数。

---

## 用在幻灯片上的三句话

1. 同一句中文，三代 tokenizer 分别是 13 / 18 / 28 个 token。
2. `1234567890` 在模型眼里是 `123`、`456`、`789`、`0` 四块。
3. 三个空格的缩进，也要花一个 token。

---

## 复现

```bash
cd FromNextTokenToNextTheorem
TIKTOKEN_CACHE_DIR="$PWD/.tiktoken_cache" ./.venv/bin/python assets/demos/token_count.py
```

`.tiktoken_cache/` 已缓存编码文件，可离线运行。
