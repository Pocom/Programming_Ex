# 二分查找（Binary Search）

## 注意事项

#### 取中位数索引

传统中位数索引写法：

```python
mid = (left + right) // 2
```

> 这行代码是有问题的，再`left`和`right`都比较大的时候，`left + right`很有可能**溢出**。

为避免溢出改进的写法：

```python
mid = left + (right - left) // 2
```

> 事实上，`int mid = left + (right - left) // 2`在`right`很大，`left`是负数且很小的时候，`right - left`也有可能溢出，不过一般情况下，`left`和`right`表示非负索引值。

Best Choice：

```python
mid = (left + right) >> 1
```

> 原文是用Java写的`int mid = (left + right) >>> 1`，即使`left`和`right`都是整型最大值，使用位运算仍然可以得到结果。

#### 循环条件

循环条件可以写成`while left<= right`，在退出循环时候，需要考虑返回`left`还是`right`，很容易出错。（返回left）



## “神奇的”二分查找

#### 基本思想

1. 首先把循环可以进行的条件写成`while left < right`，在退出循环的时候，一定有`left == right`成立，此时返回`left`或者`right`均可。
2. 排除法思想：
    * 在每一轮循环排除一半以上的元素，于是在对数级别的时间复杂度内，就可以把区间“夹逼”只剩下1个数，而这个数是不是我们要找的数，单独做一次判断。