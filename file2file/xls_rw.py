import xlrd
import xlwt

from format_data import FormatData

"""
Reader&Writer for xls
"""


class XlsRW:
    def __init__(self):
        print('Init')

    # read
    @staticmethod
    def read(file_path, sheet_name='', need_trans=False):
        _workbook = xlrd.open_workbook(file_path)  # get workbook
        _result = {}
        for _sheet_name in _workbook.sheet_names():
            print(f'Try to read sheet {_sheet_name} from xls-file {file_path}')
            if sheet_name != '' and sheet_name != _sheet_name:
                continue
            _sheet = _workbook.sheet_by_name(_sheet_name)
            _rows_count = _sheet.nrows  # get rows count
            _data = []
            for _row_idx in range(_rows_count):
                _row_data = _sheet.row_values(_row_idx)
                _data.append(_row_data)
            if need_trans:
                _result[_sheet_name] = FormatData.trans(data=_data, fmt='list_2_dict')
                continue
            _result[_sheet_name] = _data
        return _result

    # write
    @staticmethod
    def write(file_path, data, sheet_name='', need_trans=False):
        _workbook = xlwt.Workbook()
        for _root_key in data.keys():
            _sheet_name = _root_key
            print(f'Try to write sheet: {_sheet_name} to xls-file:{file_path}')
            if sheet_name != '' and sheet_name != _sheet_name:
                continue
            _sheet_data = data[_root_key]
            if need_trans:
                _schema = list(_sheet_data[0].keys())
                _sheet_data = FormatData.trans(data=_sheet_data, fmt='dict_2_list', schema=_schema)
            print(f'_sheet_data:{_sheet_data}')
            _sheet = _workbook.add_sheet(_sheet_name)
            for _row_idx in range(len(_sheet_data)):
                _row = _sheet_data[_row_idx]
                for _col_idx in range(len(_row)):
                    _sheet.write(_row_idx, _col_idx, _row[_col_idx])
        _workbook.save(file_path)


# main
if __name__ == '__main__':
    _file_path = r'test/resources/files/data.xls'
    result = XlsRW.read(file_path=_file_path, sheet_name="data")
    print(f'result:{result}')
