import os
import sys


class FileHelper:
    def __init__(self, path):
        self.path = path

    # 获取文件信息
    def get_files(self):
        #
        _data = []
        for root, dirs, files in os.walk(self.path):
            for f_name in files:
                # print(os.path.join(root, f_name))
                _f_full_path = os.path.join(root, f_name)
                _f_size = os.path.getsize(_f_full_path)
                _f_type = os.path.splitext(f_name)[1]
                _f_auth = oct(os.stat(_f_full_path).st_mode)[-3:]
                #
                _rec = [_f_full_path, f_name, _f_type, _f_auth, _f_size]
                _data.append(_rec)
        print(f'_data:{_data}')


# main
if __name__ == '__main__':
    _path = sys.argv[1]
    FileHelper(_path).get_files()
