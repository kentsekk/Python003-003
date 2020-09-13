学习笔记

## Lesson 01 Pandas 简介

```
pwd = os.path.dirname(os.path.realpath(__file__))

NameError:
name '__file__' is not defined
```

```
df = pd.read_csv('book_utf8.csv')

AttributeError:
module 'pandas' has no attribute 'read_csv'
```
Solution：file named 'pandas.py' at the same folder

## Lesson 02 數據類型
了解Series数据类型
内容取出
array 转换

re ‘[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}’

## Lesson 03 数据预处理
### Series
Create a Series: pd.Series ( [ ] ), nan = np.nan
Check NaN: x.hasnans
Fill with means: x.fillna(values = x.mean())

### DataFrame
Check NaN: df.isnull().sum()
Fill:
Fill with pervious value: df.ffill()
Fill with pervious column value: df.ffill(axis=1)

Delete:
df.info()
df.dropna() （整列删去）

指定填充值：
df.fillna(‘xx’)

Drop Duplicated:
df.drop_duplicates()

## Lesson 05 数据调整
### 选取
选取某一列：df [ [‘A’, ‘C’] ] ，中间是列表形式，不能使用元祖，即（）

df.iloc[ 行， 列 ], eg, df.iloc[ : , [0,2]] = 全部行，1，3列
行的选取：df.loc[[0,2]] = 第一和第三行，df.loc[0:2] = 第一至第三行

### 比较
比较条件选取：
df[ ( df[‘A’]<5 ) & ( df[‘C’]<4 )]

### 数值替换
一对一
df[‘C’].replace(4,40) = C的4替换成40

使用numpy：
df.replace(np.NaN, 0)

多对一
df.replace([4,5,8], 1000)

多对多
df.replace({4:400,5:500,8:800})

### 排序
按照指定列降序排列
df.sort_values ( by = [‘A’], ascending = [False])
多列排序
df.sort_values ( by = [‘A’,’C’], ascending = [True,True])

### 删除
df.drop( ‘A’, axis = 1), axis 1 = 列， axie 0 = 行
或者通过选取删除，例如 df [ df[‘A’] < 5]

### 互换
df.T

### 索引重塑
```
df4 = pd.DataFrame([
                    ['a', 'b', 'c'],
                    ['d', 'e', 'f']
                    ],
                    columns = ['one','two','three'],
                    index = ['first','second']
                    )

df4.stack()
df4.unstack()
df4.stack().reset_index()


>>> df4.stack()
first   one      a
        two      b
        three    c
second  one      d
        two      e
        three    f
dtype: object
>>> df4.unstack()
one    first     a
       second    d
two    first     b
       second    e
three  first     c
       second    f
dtype: object
>>> df4.stack().reset_index()
  level_0 level_1  0
0   first     one  a
1   first     two  b
2   first   three  c
3  second     one  d
4  second     two  e
5  second   three  f
```

## Lesson 06 基本操作
[Computational tools — pandas 1.1.2 documentation](https://pandas.pydata.org/docs/user_guide/computation.html#method-summary)

### 算数运算

df[‘A’] + df[‘C’] # 空值没法参与运算

### 同一放大
df[‘A’] + 5

### 比较运算
df[‘A’] > df[‘C’]

### count非空值
df.count()

### 非空值求和
df.T.sum()
df[‘A’].sum()

## Lesson 07 分组聚合
# 聚合
```
sales = [{‘account’: ‘Jones LLC’,’type’:’a’, ‘Jan’: 150, ‘Feb’: 200, ‘Mar’: 140},
         {‘account’: ‘Alpha Co’,’type’:’b’,  ‘Jan’: 200, ‘Feb’: 210, ‘Mar’: 215},
         {‘account’: ‘Blue Inc’,’type’:’a’,  ‘Jan’: 50,  ‘Feb’: 90,  ‘Mar’: 95 }]

df2 = pd.DataFrame(sales)
df2.groupby(‘type’).groups

#用python的方式，不好处是我们不一定知道全部的type，加入type很多的话，也需要一一列出
for a, b in df2.groupby(‘type’):
    print(a)
    print(b)
```

### 聚合再计算
```
df2.groupby(‘type’).count()
```

### 各类型产品的销量数量和销售总额
```
df2.groupby(‘type’).aggregate( {‘type’:’count’, ‘Feb’:’sum’})
```

### 创建随机数据
```
group = [‘x’,’y’,’z’]

data = pd.DataFrame({
    “group”: [group[x] for x in np.random.randint(0, len(group), 10)],
    “salary”: np.random.randint(50000,120000,10),
    “age”: np.random.randint(25,60,10)
})
```
**[gourp[x] for x in np.random.randint (0, len(group), 10)**

求平均再运算：
data.groupby(‘group’).agg(‘mean’).to_dict()
data.groupby(‘group’).mean().to_dict()
data.groupby(‘group’).transform(‘mean’)

```
>>> pd.pivot_table(data,
...                 values = 'salary',
...                 columns = 'group',
...                 index = 'age',
...                 aggfunc = 'count',
...                 margins = True
...                 ).reset_index()
group  age    x    y    z  All
0       28  1.0  NaN  NaN    1
1       31  1.0  NaN  NaN    1
2       34  NaN  NaN  1.0    1
3       37  1.0  NaN  NaN    1
4       38  1.0  NaN  NaN    1
5       39  1.0  NaN  NaN    1
6       40  1.0  NaN  NaN    1
7       46  1.0  NaN  NaN    1
8       49  1.0  1.0  NaN    2
9      All  8.0  1.0  1.0   10
```

Pd.pivot_table(data, values, columns, index, aggfunc, margins)

## Lesson 08 多表拼接
[MySQL :: MySQL 8.0 Reference Manual :: 13.2.10.2 JOIN Clause](https://dev.mysql.com/doc/refman/8.0/en/join.html)
使用的较少，简单了解即可，如想深入了解，可以了解数据库的JOIN Clause

Concat 比较多用，纵向拼接大表

## Lesson 09 输出和绘图
plot 文档：
[pandas.DataFrame.plot — pandas 1.1.2 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)
seaborn 文档：
[User guide and tutorial — seaborn 0.11.0 documentation](http://seaborn.pydata.org/tutorial.html)

一般流程：
转成字典，交给python继续处理
to_dict()
