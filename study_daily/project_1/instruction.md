# 2017-11-05
```
1. 项目概述
  使用描述统计学和统计检验分析斯特鲁普效应——一个实验心理学的经典成果。为读者提供直观的数据，并根据结果利用统计推断得出结论。
  
2. 准备好提交你的项目了吗？请准备好以下文件：
  pdf 或 html 文档，包含能够回答之前页面上问题的答案。
  你在此次提交过程中参考或使用的网站、书籍、论坛、GitHub 库和其他资源（网络资源或非网络资源）的列表。该列表可以随附在答案文档
  的底部，或者放在单独的纯文本文件中。
  
3. 注意：
  集中例-》均值，变异例-〉标准差/方差，然后也可以选其他量
  
实验stroop:
	1.同一组样本；
	2.分别在一致和不一致的情况下进行实验；
	3.记录实验所需时间；
	
congruent		incongruent
12				17
8				15
10				12
9				20

实验性统计检验
相依样本
Ho:mu_congruent=mu_incongruent
Ha:mu_congruent≠mu_incongruent
双尾检验
α:0.05
自由度df:24+24-2
t临界值:2.2009(maybe)
样本量:n
congruent偏差平方和:sum(sum_d_congruent)
incongruent偏差平方和:sum(sum_d_incongruent)
congruent_sd:sqrt(sum_d_congruent/(n-1))
incongruent_sd:sqrt(sum_d_incongruent/(n-1))
样本量一致不需要方差求和
使用公式：
t_statistic=(mu_congruent-mu_incongruent)/(sqrt((congruent_sd/n)+(incongruent_sd/n)))
置信区间:
r^2:t_statistic^2/(t_statistic^2+df)
```
