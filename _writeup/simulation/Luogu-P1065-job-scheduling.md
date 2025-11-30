---
tags:
  - computer-science
  - algorithm
  - typescript
date: 2025-11-25
---

# 洛谷 P1065 作业调度方案 | TypeScript Week

## 1 题目描述

我们现在要利用 $m$ 台机器加工 $n$ 个工件，每个工件都有 $m$ 道工序，每道工序都在不同的指定的机器上完成。每个工件的每道工序都有指定的加工时间。

每个工件的每个工序称为一个操作，我们用记号 `j-k` 表示一个操作，其中 $j$ 为 $1$ 到 $n$ 中的某个数字，为工件号；$k$ 为 $1$ 到 $m$ 中的某个数字，为工序号，例如 `2-4` 表示第 $2$ 个工件第 $4$ 道工序的这个操作。在本题中，我们还给定对于各操作的一个安排顺序。

例如，当 $n=3,m=2$ 时，`1-1,1-2,2-1,3-1,3-2,2-2` 就是一个给定的安排顺序，即先安排第 $1$ 个工件的第 $1$ 个工序，再安排第 $1$ 个工件的第 $2$ 个工序，然后再安排第 $2$ 个工件的第 $1$ 个工序，等等。

一方面，每个操作的安排都要满足以下的两个约束条件。

1. 对同一个工件，每道工序必须在它前面的工序完成后才能开始；

2. 同一时刻每一台机器至多只能加工一个工件。

另一方面，在安排后面的操作时，不能改动前面已安排的操作的工作状态。

由于同一工件都是按工序的顺序安排的，因此，只按原顺序给出工件号，仍可得到同样的安排顺序，于是，在输入数据中，我们将这个安排顺序简写为 `1 1 2 3 3 2`。

还要注意，“安排顺序”只要求按照给定的顺序安排每个操作。不一定是各机器上的实际操作顺序。在具体实施时，有可能排在后面的某个操作比前面的某个操作先完成。

例如，取 $n=3,m=2$，已知数据如下（机器号/加工时间）：

| 工件号 | 工序 1 | 工序 2 |
| ------ | ------ | ------ |
| $1$    | $1/3$  | $2/2$  |
| $2$    | $1/2$  | $2/5$  |
| $3$    | $2/2$  | $1/4$  |

则对于安排顺序 `1 1 2 3 3 2`，下图中的两个实施方案都是正确的。但所需要的总时间分别是 $10$ 与 $12$。

方案 1，用时 $10$：

|      时间       |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |  10   |
| :-------------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 机器 1 执行工序 | `1-1` | `1-1` | `1-1` | `2-1` | `2-1` | `3-2` | `3-2` | `3-2` | `3-2` |  无   |
| 机器 2 执行工序 | `3-1` | `3-1` |  无   | `1-2` | `1-2` | `2-2` | `2-2` | `2-2` | `2-2` | `2-2` |

方案 2，用时 $12$：

|      时间       |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |  10   |  11   |  12   |
| :-------------: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 机器 1 执行工序 | `1-1` | `1-1` | `1-1` | `2-1` | `2-1` |  无   |  无   | `3-2` | `3-2` | `3-2` | `3-2` |  无   |
| 机器 2 执行工序 |  无   |  无   |  无   | `1-2` | `1-2` | `3-1` | `3-1` | `2-2` | `2-2` | `2-2` | `2-2` | `2-2` |

当一个操作插入到某台机器的某个空档时（机器上最后的尚未安排操作的部分也可以看作一个空档），可以靠前插入，也可以靠后或居中插入。为了使问题简单一些，我们约定： 在保证约束条件 $(1.)(2.)$ 的条件下，尽量靠前插入。并且，我们还约定，如果有多个空档可以插入，就在保证约束条件 $(1.)(2.)$ 的条件下，插入到最前面的一个空档。于是，在这些约定下，上例中的方案一是正确的，而方案二是不正确的。

显然，在这些约定下，对于给定的安排顺序，符合该安排顺序的实施方案是唯一的，请你计算出该方案完成全部任务所需的总时间。

### 1.1 输入格式

第 $1$ 行为两个正整数 $m$, $n$，用一个空格隔开，其中 $m(<20)$ 表示机器数，$n(<20)$ 表示工件数。

第 $2$ 行：$m \times n$ 个用空格隔开的数，为给定的安排顺序。

接下来的 $2n$ 行，每行都是用空格隔开的 $m$ 个正整数，每个数不超过 $20$。

其中前 $n$ 行依次表示每个工件的每个工序所使用的机器号，第 $1$ 个数为第 $1$ 个工序的机器号，第 $2$ 个数为第 $2$ 个工序机器号，等等。

后 $n$ 行依次表示每个工件的每个工序的加工时间。

可以保证，以上各数据都是正确的，不必检验。

### 1.2 输出格式

$1$ 个正整数，为最少的加工时间。

### 1.3 输入输出样例 #1

#### 1.3.1 输入 #1

```
2 3
1 1 2 3 3 2
1 2
1 2
2 1
3 2
2 5
2 4
```

#### 1.3.2 输出 #1

```
10
```

### 1.4 说明/提示

NOIP 2006 提高组 第三题

## 2 分析

### 2.1 题面分析

本题实际属于一道模拟题，并不需要我们手动调度，按照题目说明一步一步来即可。首先我们针对给出的样例数据画图分析：

```
Step 1: Push [1, 1, 1] to machine 1
[M1]: 111
[M2]: 

Step 2: Push [1, 1] to machine 2
[M1]: 111
[M2]: 00011

Step 3: Push [2, 2] to machine 1
[M1]: 11122
[M2]: 00011

Step 4: Push [3, 3] to machine 2
[M1]: 11122
[M2]: 33011

Step 5: Push [3, 3, 3, 3] to machine 1
[M1]: 111223333
[M2]: 33011

Step 6: Push [2, 2, 2, 2, 2] to machine 2
[M1]: 111223333
[M2]: 3301122222

So final consumed time is 10 minutes.
```

题目的意思是按照给定的安排顺序安排不同零件到不同的机器上。当此时是零件的第一次加工，直接把对应加工时间长度的新元素数组添加到对应机器规划数组的末尾；当此时不是该零件第一次加工时，需要注意不能超过上一次加工工序的结束时间，因此就是在当前加工工序的对应机器规划数组的从上一次加工工序结束时间开始的一部分中，寻找尚且空余且还可以容纳本次加工工序的子数组（**即从上一次加工工序结束开始的部分中，找到长度比当前工序所花时间等于或者更多的连续 0子数组**）。

### 2.2 数据结构规划

据此我们可以先构建必要的数据结构：

``` ts
interface Items {
  /**
   * @field processOrder : The processing order of an item, like [1, 2] indicates
   * this item should be processed by machine 1 and then machine 2
   */
  processOrder?: number[];
  /**
   * @field processTime: The processing times of corresponding machine processing
   * with this item.
   */
  processTime?: number[];
}

function leastProcessTime(
  machinesNum: number,
  itemsNum: number,
  itemsProcessOrder: number[],
  items: Items[]
): number {
  const machineSchedules: number[][] = [];
  for (let i = 0; i < machinesNum; ++i) machineSchedules.push([]);
```

+ `itemsProcessOrder` 用来存放安排的顺序，例如案例数据中的 `1 1 2 3 3 2`；
+ `items` 是存放加工工件信息的数组，`Item` 接口定义了一个工件的两种信息：第一个
  是加工机器的顺序 `processOrder`，例如案例数据中工件 1 的 `1 2`；第二个是该工件
  在加工机器上所花费的时间 `processTime`，其与 `processOrder` 的数组长度一致
  且存在一一对应的关系；
+ `machineSchedules` 是一个二维数组，第一维用于存放不同机器的规划，第二维用于
  存放特定机器的规划数组。

### 2.3 特定算法实现

#### 2.3.1 循环处理 `itemsProcessOrder`

当循环处理时，我们要获取当前的加工信息：

``` ts
  for (let i = 0; i < machinesNum * itemsNum; ++i) {
    const currentItem = itemsProcessOrder[i]; // notice it begins with 1
    // currentItem is the item now processing, and it is read from itemsProcessOrder
    const currentItemProcess = itemsProcessOrder
      .filter((value, index) => (value === currentItem && index < i))
      .length + 1;
    // currentItemProcess is the order of the item now processing, the order
    // should be got from the itemsProcessOrder
    const currentMachine = (items[currentItem - 1] as Required<Items>)
      .processOrder[currentItemProcess - 1];
    // currentMachine is the machine now processing
    const currentMachineSchedule = machineSchedules[currentMachine - 1];
    // currentMachineSchedule is the current schedule of current machine
    const currentTime = (items[currentItem - 1] as Required<Items>)
      .processTime[currentItemProcess - 1];
    // currentTime is the needed time of current (machine-item) pair
    const currentVacantIndexMap = continuousElementIndex(currentMachineSchedule, 0);
    const lastTime = Math.max(
      ...machineSchedules.map((arr) => arr.lastIndexOf(currentItem) + 1)
    );
    // Notice lastTime has been added 1 so it starts from 1
```

+ `currentItem` 记录当前正在处理的工件，注意该数从 $1$ 开始；
+ `currentItemProcess` 记录当前正在处理的工件的工序，注意该数从 $1$ 开始；
+ `currentMachine` 记录当前正在处理的工序需要的机器号，由于是从 `processOrder`
  中取出的，因此该数也是从 $1$ 开始的；
+ `currentMachineSchedule` 是当前处理机器的规划数组，它是对二维数组中的数组的一个
  引用，因此无需担心没有在原数组上修改的问题；
+ `currentTime` 是当前处理工序所需要的时间；
+ `lasTime` 是该工件上一道工序的结束时间，注意是从 $1$ 开始。

#### 2.3.2 寻找所有连续空余计划

该函数只返回一个由整数对组成的数组，表示所有连续空余计划，其中第一个数字表示
**该空余计划的开始索引**（注意此处是以 $0$ 为基准的，从 $0$ 开始），第二个数字
表示**该空余计划的时间长度**。

``` ts
function continuousElementIndex<T>(
  array: T[],
  element: T
): Array<[number, number]> {
  let recordIndex = 0;
  let recordLength = 0;
  const result: Array<[number, number]> = [];

  for (let i = 0; i < array.length; ++i) {
    if (array[i] === element) {
      recordLength++;
    } else {
      recordIndex = i;
      if (recordLength !== 0 && recordIndex !== 0) {
        result.push([recordIndex - recordLength, recordLength]);
      }
      recordLength = 0;
    }
  }
  if (recordLength !== 0 && recordIndex !== 0) {
    result.push([array.length - recordLength, recordLength]);
  }
  return result;
}
```

在 `recordIndex - recordLength` 中，`recordIndex` 是遇到的非 $0$ 元素的位置，
`recordLength` 是记录的空余计划长度，根据下面的说明可知 `recordIndex - recordLength`
表示的是空余计划的起始索引。由于该函数被我设计地更有通用性，最后末尾的空余计划
（然而在本题中这是不可能出现的）也一并完整处理了。

```
111122000000003333
      ↑       ↑
        Now recordIndex = 14, recordLength = 8
        The begin index is 6 = recordIndex - recordLength
```

在 [2.3.1 循环处理 `itemsProcessOrder`](#2.3.1%20循环处理%20`itemsProcessOrder`) 中的
`currentVacantIndexMap` 就是存储当前处理的机器的规划数组中所有的空余计划。

#### 2.3.3 筛选空余计划

空余计划处理出来后，需要根据两条规则进行筛选：

1. 该空余计划中是否有在上一道工序完成后仍然空余，并且剩余的这一部分仍然可以
  容纳当前处理工序的所用时间的？
2. 该空余计划是否在上一道工序结束时间之后且还能容纳当前处理工序？

``` ts
    if (
      currentMachineSchedule.length < currentTime ||
      Math.max(
        ...currentVacantIndexMap.map(
          (t) => t[0] + t[1] - Math.max(t[0], lastTime)
        )
      ) < currentTime
    ) {
      // [+] If the length of currentMachineSchedule is less than needed time of
      //     current processing step, then we need to add the job at the end of
      //     currentMachineSchedule
      // [+] If length of every continuous sub-array consisting of 0 is less
      //     than needed time of current processing step, then we need to add
      //     the job at the end of currentMachineSchedule
      //
      //  000111100222220000333
      //  ↑     ↑       ↑
      //  |   lastTime  |
      //  |             +- t[0] = 14, t[1] = 4, t[0] + t[1] - lastTime = 11
      //  +- t[0] = 0, t[1] = 3, lastTime = 7, t[0] + t[1] - lastTime = -4
      //  Notice lastTime is 1-based and t[0] is 0-based

      const initialLength = currentMachineSchedule.length;
      for (let j = 0; j < lastTime - initialLength; ++j) {
          currentMachineSchedule.push(0);
      }
      for (let j = 0; j < currentTime; ++j) {
        currentMachineSchedule.push(currentItem);
      }
    } else {
      for (let j = 0; j < currentVacantIndexMap.length; ++j) {
        if (
          currentVacantIndexMap[j][0]
            + currentVacantIndexMap[j][1] 
            - Math.max(currentVacantIndexMap[j][0], lastTime) 
          >= currentTime
        ) {
          for (let k = 0; k < currentTime; ++k) {
            currentMachineSchedule[
              Math.max(currentVacantIndexMap[j][0], lastTime)
              + k] = currentItem;
          }
          break;
        }
      }
    }
```

以下两种情况需要在规划时间末尾加上当前工序的安排

1. 当前机器的规划时间长度都无法容纳当前工序时；
2. 当前机器的空余计划都无法容纳当前工序时。注意，当前机器所有的空余计划都要考虑
  上一道工序的结束时间：如果当前空余计划开始时间比上一工序结束时间早，则应该减去
  上一工序的结束时间；如果比起上一道工序结束时间还要晚，那就只需要看当前空余计划
  是否能容纳当前工序耗时即可。

  由此可以得到条件判断中的

  ``` ts
  Math.max(
      ...currentVacantIndexMap.map(
        (t) => t[0] + t[1] - Math.max(t[0], lastTime)
      )
  ) < currentTime
  ```

当需要在末尾加上当前工序安排时，首先要看是否需要填充 $0$ （代表新的空余计划）至与上一道工序的结束时间对齐。

``` ts
const initialLength = currentMachineSchedule.length;
for (let j = 0; j < lastTime - initialLength; ++j) {
  currentMachineSchedule.push(0);
}
for (let j = 0; j < currentTime; ++j) {
  currentMachineSchedule.push(currentItem);
}
```

当需要在最靠前的可容纳空余计划塞进当前工序时，则要先找到最靠前的位置。当遇到
满足以下条件语句的位置时，就找到了最靠前的位置：

``` ts
currentVacantIndexMap[j][0]
  + currentVacantIndexMap[j][1] 
  - Math.max(currentVacantIndexMap[j][0], lastTime) 
>= currentTime
```

最终返回最后 `machineSchedules` 中一维数组长度的最大值即可。
