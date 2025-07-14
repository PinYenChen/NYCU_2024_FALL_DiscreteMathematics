# Project Module Scheduling (Topological Sort + Longest Path)

## Description

一個專案內容可以分為多個獨立的模組進行開發，在模組之間可能會存在相依關係。  
如果將相依關係以箭頭表示，專案可表示為一張**有向無環圖（DAG）**。

箭頭指向的模組依賴於箭頭指向前的模組，如果指向前的模組尚未完成，則該模組無法開始開發。例如：

- 模組 2 需等模組 3 完成才可開始
- 模組 0 同時依賴模組 1 與 4，需等兩者都完成後才可開始

每個模組有其開發所需的時間，模組之間的銜接不需要額外時間。  
請你根據相依圖與各模組的開發時間，求出整個專案最少需要多少時間才可完成所有模組。

---

## Problem

A project is composed of several independent modules that can be developed independently.  
There might be dependencies among these modules, represented by directed edges.  
The project is modeled as a **Directed Acyclic Graph (DAG)**.

A module cannot begin development until all its prerequisite modules (those pointing to it) are completed.  
Each module takes a certain amount of time to develop. Transition between modules is assumed to take no extra time.

Given the list of dependencies and the time needed for each module, determine the **minimum time needed to complete the entire project**.

---

## Constraints

- `1 ≤ T ≤ 10` (number of test cases)
- `1 ≤ n ≤ 1000` (number of modules)
- `1 ≤ m ≤ 4000` (number of dependency edges)
- `1 ≤ wᵢ ≤ 10^5` (time needed to develop module `i`)
- Input graph is guaranteed to be a **DAG** (no cycles)

---

## Input Format
T  
n m  
w₀ w₁ ... wₙ₋₁  
u₁ v₁  
u₂ v₂  
...  

Each test case contains:

- An integer `T` indicating number of test cases
- For each test case:
  - A line with two integers `n` and `m` representing the number of modules and number of dependencies
  - A line with `n` integers `w₀` to `wₙ₋₁` representing the development time of each module
  - `m` lines, each with two integers `u` and `v`, representing a dependency: `module v` depends on `module u`

---

## Output Format
t  

- For each test case, output a single line with one integer: the **minimum number of time units** required to complete the project.

---

## Example

### Sample Input
1  
5 4  
1 2 3 4 5  
0 2  
1 2  
2 3  
3 4  


### Sample Output
15  

---

## Explanation

- 模組 0 與模組 1 沒有前置模組，分別耗時 1 與 2，可以同時開始。
- 模組 2 需等 0 和 1 完成後開始，耗時 3。
- 模組 3 依賴模組 2，耗時 4。
- 模組 4 依賴模組 3，耗時 5。

最長的耗時路徑為：
1 (模組1) → 2 (模組2) → 3 (模組3) → 4 (模組4)
=> 2 + 3 + 4 + 5 = 15


---

## Hint

本題可使用拓撲排序（Topological Sort）配合 DP（Longest Path in DAG）求解。  
記錄每個節點最早可以完成的時間，依拓撲順序更新相依模組的起始時間與完成時間。




