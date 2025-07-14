# Problem: Strictly Increasing Sequences with Given Sum

## Description

給定一個正整數 $L$，請問存在幾種**嚴格遞增**的正整數數列 $\{a_i \in \mathbb{Z}^+\}_{i=1}^n$ 滿足：

$$
L = \sum_{i=1}^{n} a_i
$$

其中，嚴格遞增定義為：

$$
a_{i-1} < a_i \quad \forall i \in \{2, 3, \cdots, n\}
$$

---

## Problem (English)

Given a positive integer $L$, how many strictly increasing sequences of positive integers $\{a_i \in \mathbb{Z}^+\}_{i=1}^n$ exist such that:

$$
L = \sum_{i=1}^{n} a_i
$$

Here, strictly increasing is defined as:

$$
a_{i-1} < a_i \quad \text{for all } i \in \{2, 3, \cdots, n\}
$$

---

## Input Format

- 每組測試資料第一行為一個正整數 $T$，表示接下來有 $T$ 筆測試資料。$(1 \leq T \leq 10)$  
- 每筆測試資料包含一行，內含一個正整數 $L$。$(1 \leq L \leq 300)$

**Input Description:**

- The first line of each test case contains a positive integer $T$ $(1 \leq T \leq 10)$, indicating the number of test cases.
- Each test case consists of a single line containing a positive integer $L$ $(1 \leq L \leq 300)$.

---

## Output Format

- 對每組測試資料輸出一行，包含一個整數，表示符合條件的數列有幾種。

**Output Description:**

- For each test case, output a single line containing an integer that represents the number of sequences satisfying the given condition.

---

## Example

### Input
