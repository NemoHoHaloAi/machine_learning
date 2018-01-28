# 使用pandas和numpy分析一维数据
> http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.argmax.html
```
1. Numpy：
  Array：处理一维数据
  Numpy Array:
  Python List:
    共同点：
      1. 可以通过角标访问元素；
      2. 通过切片获取集合子集；
      3. 被for遍历；
    不同点：
      1. Array只能存储类型一致的元素；
2. Pandas：
  Series：基于Numpy的一维数据处理模块
  Series与Numpy Array对比：
  共同点：
   1. 通过角标访问；
   2. 通过切片访问；
   3. 被for迭代遍历；
   4. 进行四则运算，逻辑运算，索引数组等；
  不同点：
   Series有索引：
   a = pd.Series([24,26,18],index=['helong','lour','munphy'])
   访问helong的年龄的三种方式：
   a[0] -- 通过位置访问
   a.iloc[0] -- 同a[0]，但是更推荐这种用法，更加明确指明通过角标 location访问
   a.loc['helong'] -- 通过索引访问
   此时a.argmax()返回的不是角标，而是index中对应的值，此处是'lour'
```
