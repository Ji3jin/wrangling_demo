WrangLing DataFrame Test Command


```
>>> import pandas as pd


# 读取测试数据
>>> df = pd.read_csv('test.csv')

>>> from wrangling_core import wrangling_df

# 根据pandas的dataframe生成wrangling dataframe，初始化会判断数据类型，数据质量
>>> wl_df = wrangling_df.WrangLingDF(df)
num     float64
date     object
dtype: object

# 打印wrangling dataframe数据
>>> wl_df.dataframe
   num        date
0  NaN       sdfsf
1  NaN       sdfsf
2  1.0  01/03/1987
3  2.0  01/03/1987
4  3.0         NaN
5  4.0       sdfsf
6  5.0      sdfsdf
# 打印wrangling dataframe数据类型
>>> wl_df.dtypes
{'date': ('object', 0.86), 'num': ('float64', 0.71)}
# 重新关联wrangling dataframe指定数据列的数据质量统计参考模型并重新统计数据质量
>>> wl_df.relate_deal_module('date', 'data_type_num')
# 获取重新关联之后的数据类型
>>> wl_df.dtypes
{'date': ('int', 0.0), 'num': ('float64', 0.71)}
>>> from wrangling_core import wl_operation

# 声明一个数据处理操作，测试操作为取前n行，是一个callable属性
>>> wl_op = wl_operation.WlOperation('head',True)
# 获取操作的属性值
>>> wl_op.attr_name
'head'
# 为该callable操作添加参数，参数值为3
>>> wl_op.op_param_append(3)

>>> wl_op.get_checked_param()
(3,)
# 在wrangling dataframe上执行该操作
>>> wl_df.extract_dataframe(wl_op)
# 打印执行后的输出结果
>>> wl_df.dataframe
   num        date
0  NaN       sdfsf
1  NaN       sdfsf
2  1.0  01/03/1987

# 声明一个数据处理操作，测试操作为转置表格，该属性不是一个callable属性
>>> wl_op2 = wl_operation.WlOperation('T',False)
# 获取操作的属性值
>>> wl_op.attr_name
'head'
# 获取该操作的参数 非callable，无参数
>>> wl_op.get_checked_param()
(3,)
# 在wrangling dataframe上执行该操作
>>> wl_df.extract_dataframe(wl_op2)
# 打印执行后的输出结果
>>> wl_df.dataframe
          0      1           2           3    4      5       6
num     NaN    NaN           1           2    3      4       5
date  sdfsf  sdfsf  01/03/1987  01/03/1987  NaN  sdfsf  sdfsdf

```