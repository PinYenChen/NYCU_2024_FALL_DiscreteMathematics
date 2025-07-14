# 題目：

一個數據樣本的中位數定義為：先將樣本中所有數進行排序得到數列 $a_1, a_2, \cdots, a_n$，則中位數 $m$ 為：

$$
m = 
\begin{cases}
a_{(n+1)/2}, & \text{if } n \text{ is odd} \\\\
\frac{a_{n/2} + a_{n/2 + 1}}{2}, & \text{if } n \text{ is even}
\end{cases}
$$

---

現在請你實現一個資料結構有以下兩種功能：

1. 新增一個正整數到數據中  
2. 刪除數據中的一個正整數  

一開始這個資料集為空，在兩種功能操作後必須輸出目前數據的中位數。

---

## Problem:

The definition of the median of a dataset is as follows:  
Arrange all numbers in the sample in ascending order to get a sequence $a_1, a_2, \cdots, a_n$. The median $m$ is defined as:

$$
m = 
\begin{cases}
a_{(n+1)/2}, & \text{if } n \text{ is odd} \\\\
\frac{a_{n/2} + a_{n/2 + 1}}{2}, & \text{if } n \text{ is even}
\end{cases}
$$

---

Now, you're required to implement a data structure with the following functionalities:

1. Add a positive integer to the dataset  
2. Remove a positive integer from the dataset  

The dataset starts empty, and after performing either of these operations, output the current **median** of the data.
