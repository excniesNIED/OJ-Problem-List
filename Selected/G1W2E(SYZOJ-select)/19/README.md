Display ID

```
SYZOJ-019
```

Title

```
望眼欲穿的广告牌
```

Description

```
有一天，UW.FOORP 坐在HKPU受诅咒的喷泉边望着校门口的电子广告牌发呆。广告牌上不断滚动着一句话，UW看着它发挥着自己超强的记忆力，不断把看上去最小（字典序）的显示内容记在自己的脑海。现在给你一个字符串s和广告牌能容纳的字符上限k，你能做到和UW一样的事情吗。

给定一个字符串s，和广告牌的容纳字符上限k，广告牌始终单排的从右向左滚动字符，当字符串的所有字母都显示过后，会从字符串的第一个字符开始无衔接的继续滚动。广告牌始终是显示k个字符的状态。
```

Input Description

```
我说的广告牌大概就是这样：

输入字符上限k和给定的字符串s

$0<s.length, k<1e6$

$'a'<=s[i]<='z', 0<=i<s.length$
```

Output Description

```
对每组数据输出UW记忆中最小的显示内容
```

Input Samples 1

```
4 aab
```

Output Samples 1

```
aaba
```

Input Samples 2

```
4 abcdef
```

Output Samples 2

```
abcd
```

Hint

```

```
