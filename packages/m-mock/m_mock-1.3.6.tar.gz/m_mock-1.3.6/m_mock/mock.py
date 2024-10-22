import re

from m_mock import m_random


class MockM:

    def __init__(self):
        # 创建一个字典，将关键词映射到相应的模块和方法
        self.keyword_mapping = {
            'date': (m_random.m_date, 'date'),
            'datetime': (m_random.m_date, 'datetime'),
            'time': (m_random.m_date, 'time'),
            'timestamp': (m_random.m_date, 'timestamp'),
            'now': (m_random.m_date, 'now'),
            'float': (m_random.m_float, 'float'),
            'natural': (m_random.m_natural, 'natural'),
            'integer': (m_random.m_integer, 'integer'),
            'boolean': (m_random.m_boolean, 'boolean'),
            'character': (m_random.m_character, 'character'),
            'string': (m_random.m_string, 'string'),
            'pick': (m_random.m_helper, 'pick'),
            'cfirst': (m_random.m_name, 'cfirst'),
            'clast': (m_random.m_name, 'clast'),
            'cname': (m_random.m_name, 'cname'),
            'first': (m_random.m_name, 'first'),
            'last': (m_random.m_name, 'last'),
            'name': (m_random.m_name, 'name'),
            'increment': (m_random.m_miscellaneous, 'increment'),
            'id': (m_random.m_miscellaneous, 'id'),
            'uuid': (m_random.m_miscellaneous, 'uuid'),
            'mix_sentence': (m_random.m_text, 'mix_sentence'),
            'sentence': (m_random.m_text, 'sentence'),
            'csentence': (m_random.m_text, 'csentence'),
            'paragraph': (m_random.m_text, 'paragraph'),
            'cparagraph': (m_random.m_text, 'cparagraph'),
        }

    def mock(self, mock_str):
        keyword = self.get_mocker_key(mock_str)
        args = self.get_mocker_params_to_tuple(mock_str)

        # 通过关键词获取对应的模块和方法名
        module_method_pair = self.keyword_mapping.get(keyword)

        if module_method_pair:
            # 解构赋值得到模块和方法名
            module, method_name = module_method_pair
            # 直接调用对应的方法并传入参数
            return getattr(module, method_name)(*args)
        else:
            return mock_str

    @classmethod
    def get_mocker_key(cls, mock_str):
        if not mock_str.startswith('@'):
            raise m_random.MockPyExpressionException()
        if not mock_str.endswith(')'):
            # 非)结尾说明是@date,则直接返回属性名
            return mock_str[1:]
        regular = '(?<=(\\@)).*?(?=(\\())'
        keyword = re.search(regular, mock_str).group(0)
        return keyword

    @classmethod
    def get_mocker_params_to_tuple(cls, mock_params) -> tuple:
        """
        将参数组装为元组，方便后续解包

        :param mock_params: ('%Y.%m.%d %H:%M:%S','+1')
        :return: 元组
        """

        # 正则表达式匹配字符串中括号内的内容
        regular = '[\\(|（].*[\\)|）]$'
        match = re.search(regular, mock_params)
        if match is None:
            return ()
        group = match.group(0)
        if group == '()':
            return ()
        end_val = group[-1:]
        if not end_val.endswith(','):
            group = f'{group[:-1]},)'
        args = eval(group)
        return args


m_mock = MockM()
