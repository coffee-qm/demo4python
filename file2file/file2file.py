import os
import argparse

from xls_rw import XlsRW
from yaml_rw import YamlRW

"""
"""


class File2File:
    def __init__(self):
        print('Init')
        self.args = self.__parse_arg__()

    #
    @staticmethod
    def __parse_arg__():
        parser = argparse.ArgumentParser(description="This is a file to file trans")  # 脚本描述
        parser.add_argument('--file', '-f', help="Trans file path.")
        parser.add_argument('--to', '-t', help="Trans file to typeB, eg:yaml.")
        parser.add_argument('--result', '-result', help="Result dir.")
        args = parser.parse_args()
        # check arguments
        if args.file is None or args.file == '' or args.to is None or args.to == '':
            print(f'Arguments error. args:{args}')
            exit(-1)
        print(f'Arguments:{args}')
        return args

    #
    def __check(self):
        # File exists
        # to is legal
        _file = self.args.file
        _f_type = os.path.splitext(_file)[1]
        _dest_dir = self.args.result
        if _dest_dir is None or _dest_dir == '':
            _dest_dir = os.path.splitext(_file)[0]
        self.dest_file = '.'.join([_dest_dir, self.args.to])
        self.trans_from = _f_type
        print(f'dest_file:{self.dest_file}, trans_from:{self.trans_from}')

    #
    def __read(self):
        _file = self.args.file
        if self.trans_from == '.xls':
            return XlsRW.read(file_path=_file, need_trans=True)
        elif self.trans_from == '.yaml':
            return YamlRW.read(file_path=_file)
        return None

    #
    def __write(self, data):
        if self.args.to == 'yaml':
            YamlRW.write(file_path=self.dest_file, data=data)
        elif self.args.to == 'xls':
            XlsRW.write(file_path=self.dest_file, data=data, need_trans=True)

    #
    def main(self):
        self.__check()  # 校验
        #
        _file = self.args.file
        _trans_to = self.args.to
        #
        _data = self.__read()
        print(f'read data:{_data}')
        self.__write(_data)


# main
if __name__ == '__main__':
    # python file2file.py -f "test/resources/files/data.xls" -t yaml -result "E:\temp\result\xxx"
    # python file2file.py -f "test/resources/files/data.yaml" -t xls -result "E:\temp\result\xxx"
    File2File().main()
