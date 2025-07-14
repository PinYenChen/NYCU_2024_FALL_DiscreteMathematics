# Circle Division by Chords

## Description

設一圓上有 $n$ 個相異點，將此 $n$ 個點兩兩相連，這些弦最多可以將圓分割成幾個區域？

---

## Problem

Given a circle $A$ with $n$ distinct points, when all pairs of these $n$ points are connected,  
how many regions can the circle be divided into at most by these chords?

---

## Input Format

N  
n₁  
n₂  
...  
nₙ  


- 第一行為一個正整數 $N$，表示接下來有 $N$ 筆測試資料 $(1 \leq N \leq 100)$
- 接下來 $N$ 行中，每行一個正整數 $n$，表示圓上有 $n$ 個相異點 $(1 \leq n \leq 1000)$

---

## Output Format

對每個輸入的 $n$，輸出一行整數，代表最多可以將圓分割成幾個區域。

---

## Input Example

3  
1  
2  
3  

## Output Example

1  
2  
4  

---

## Hint

這是一個經典組合數列問題。最多分割出的區域數可由以下公式計算：

$$
R(n) = 1 + \binom{n}{2} + \binom{n}{4}
$$

或使用完整公式：

$$
R(n) = 1 + \binom{n}{2} + \binom{n}{4}
$$

因為只有當四條邊構成一個凸四邊形時，才會產生交點與新區域（當不三點共線）。

---

## Constraints

- $1 \leq N \leq 100$
- $1 \leq n \leq 1000$

