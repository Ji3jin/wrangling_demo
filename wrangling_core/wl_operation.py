# *-* encoding=utf-8 *-*

class WlOperation():
    def __init__(self, attr_name, is_callable):
        self._attr_name = attr_name
        self._op_param = []
        self._is_callable = is_callable

    @property
    def attr_name(self):
        return self._attr_name

    @attr_name.setter
    def attr_name(self, attr_name):
        self._attr_name = attr_name

    @property
    def is_callable(self):
        return self._is_callable

    @is_callable.setter
    def is_callable(self, is_callable):
        self._is_callable = is_callable

    @property
    def op_param(self):
        return tuple(self._op_param)

    def op_param_append(self, param):
        self._op_param.append(param)

    def get_checked_param(self):
        # check param with attr_name
        return tuple(self._op_param)
