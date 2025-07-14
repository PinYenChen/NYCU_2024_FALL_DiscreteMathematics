# Problem: Asymmetric Nim Game

## Description

Nim 是一個簡單的雙人遊戲，一開始在桌面上會有 $n$ 個小石子，玩家 $A$ 和 $B$ 輪流拿走一定數量的小石子，當任何人無法再從桌上拿走小石子時即輸掉遊戲。

- 玩家 $A$ 每次操作可以拿走的小石子數量屬於集合 $\{a_1, a_2, \cdots, a_m\}$  
- 玩家 $B$ 每次操作可以拿走的小石子數量屬於集合 $\{b_1, b_2, \cdots, b_m\}$

若每次皆由玩家 $A$ 先手，請問玩家 $A$ 是否有**必勝策略**？

---

## Problem (English)

Nim is a simple two-player game where there are initially $n$ small stones on the table.  
Players $A$ and $B$ take turns removing some number of stones, and the game ends when a player can no longer move.

- Player $A$ can remove a number of stones from the set $\{a_1, a_2, \cdots, a_m\}$
- Player $B$ can remove stones from the set $\{b_1, b_2, \cdots, b_m\}$

If player $A$ starts the game, determine whether they have a **winning strategy**.

---

## Input Format

- 第一行是一個正整數 $T$，表示接下來有 $T$ 組測資。$(1 \leq T \leq 100)$  
- 每組測資接下來三行：
  - 第一行為兩個整數 $n, m$，表示初始石子數與可選步數集合大小。$(1 \leq n \leq 5000), (1 \leq m < 500)$
  - 第二行包含 $m$ 個正整數，表示玩家 $A$ 可移除的石子數量 $a_1, \cdots, a_m$
  - 第三行包含 $m$ 個正整數，表示玩家 $B$ 可移除的石子數量 $b_1, \cdots, b_m$

---

## Output Format

對於每筆測試資料輸出一行字串：

- 若玩家 $A$ 有必勝策略，輸出 `A`
- 否則輸出 `B`

### Output Description

For each test case, output a single line:

- Output `A` if player $A$ has a winning strategy  
- Otherwise, output `B`

---
