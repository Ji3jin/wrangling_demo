# *-* encoding=utf-8 *-*
from rule_loader import RuleLoader
from base_model import CHECK_TYPE


class WrangLingDF():
    def __init__(self, df):
        self._dataframe = df
        self._dtypes = {}
        self._rule_loader = RuleLoader()
        self.pre_deal_data()
        self._wl_operation = None

    @property
    def dataframe(self):
        return self._dataframe

    @dataframe.setter
    def dataframe(self, df):
        self._dataframe = df

    @property
    def wl_operation(self):
        return self._wl_operation

    @wl_operation.setter
    def wl_operation(self, wl_operation):
        self._wl_operation = wl_operation

    @property
    def dtypes(self):
        return self._dtypes

    # 检测数据类型，并且统计数据质量（全局）
    def pre_deal_data(self):
        dtypes = self._dataframe.dtypes
        # pandas读取数据本身会进行一次检测，如果有空值或者异常值会检测成object
        # 如果正常值会检测出数据类型，此时数据质量是百分百
        print dtypes
        for item in list(dtypes.index):
            dtype = str(dtypes[item])
            # 检测所有为Object的是否为基础类型，基础类型为num，float和string
            # 如果不满足num和float的正则则为string（表现为object）
            if dtype == 'object':
                # CHECK_TYPE is num and float
                for check_type in CHECK_TYPE:
                    regex = self._rule_loader.get_option(check_type[0].value, 'regex')
                    q = self.check_dtype(item, regex)
                    if q > 0.75:
                        self._dtypes[item] = (check_type[1], q)
                        break
            # dtype为object或者为数据质量百分百的类型。如果为Object则认定Nan为异常值，统计数据质量
            q = round(float(self._dataframe[item].count()) / float(self._dataframe[item].shape[0]), 2)
            self._dtypes[item] = (dtype, q)

    def check_dtype(self, item, regex):
        right_value = self._dataframe[item].str.contains(regex, regex=True)
        q = round(float(right_value[right_value == True].count()) / float(self._dataframe[item].shape[0]), 2)
        return q

    # 关联某列的抽象模型，关联后需重新统计该列的数据质量
    def relate_deal_module(self, col_index, data_type):
        regex = self._rule_loader.get_option(data_type, 'regex')
        dtype = self._rule_loader.get_option(data_type, 'dtype')
        q = self.check_dtype(col_index, regex)
        self._dtypes[col_index] = (dtype, q)

    # 获取处理后的结果集
    def extract_dataframe(self, wl_operation):
        # 处理数据
        self.wl_operation = wl_operation
        extract_func = getattr(self._dataframe, wl_operation.attr_name)
        if wl_operation.is_callable:
            result_df = extract_func(*wl_operation.get_checked_param())
            self.dataframe = result_df
        else:
            self.dataframe = extract_func
