"""
"""


class FormatData:
    @staticmethod
    def trans_list_to_dict(data):
        _header = data[0]
        _data_trans = []
        for _row in data[1:]:
            _row_trans = {}
            for _c in range(len(_header)):
                _row_trans[_header[_c]] = _row[_c]
            _data_trans.append(_row_trans)
        return _data_trans

    @staticmethod
    def trans_dict_to_list(data, schema):
        _data_trans = [schema]
        for _row in data:
            _row_trans = []
            for _c in schema:
                _row_trans.append(_row[_c])
            _data_trans.append(_row_trans)
        return _data_trans

    #
    @staticmethod
    def trans(data, fmt, schema=''):
        if data is None:
            return None
        if fmt == 'list_2_dict':
            return FormatData.trans_list_to_dict(data)
        elif fmt == 'dict_2_list':
            return FormatData.trans_dict_to_list(data, schema)
        return None


# main
if __name__ == '__main__':
    pass
