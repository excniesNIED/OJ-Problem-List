Display ID

```
P1805
```

Title

```
关灯
```

Description

```
在某条道路上，有盏灯排成一排，它们有的是开着的，有的是关着的。
由于天马上就要亮了，上级给了你一个任务：把所有的灯都关掉。
只不过，这些灯都比较智能，不会被轻易关掉。它们的开或关遵循如下规则：
- 每一步只能开或关一盏灯。
- 编号为1的灯可以随意开或关
- 如果编号为1,2,···，k－1的灯都关上了了，并且编号为k的灯在开着，我们可以随意开或关第k十1盏灯。
在关灯之前，请你计算：至少要多少步才能关上所有灯?
```

Input Description

```
第1行一个整数，表示灯的个数。
第2行有n个整数，如果第个整数$O_i=0$，表示第个盏灯初始的时候是关着的；如果$O_i=1$，表示第盏灯初始的时
候是开着的。
```

Output Description

```
共一行一个整数，表示最少需要多少步才能关上所有灯。
```

Input Samples 1

```
4
1 0 1 0
```

Output Samples 1

```
6
```

Hint

```
【输出解释】
- 初始状态1010；
- 第1步1110；
- 第2步0110；
- 第3步0100；
- 第4步1100；
- 第5步1000；
- 第6步0000。
数据范围及约定
- 对于$40%$的数据，$n≤30$;
- 对于$70%$的数据，$n≤300$;
- 对于$100%$的数据，$n≤1000$。
```
