import yaml

"""
Reader&Writer for yaml
"""


class YamlRW:
    def __init__(self):
        print('Init')

    # read
    @staticmethod
    def read(file_path):
        _data = []
        with open(file_path, 'r') as f:
            _data = yaml.load(f.read(), Loader=yaml.Loader)
        return _data

    # write
    @staticmethod
    def write(file_path, data):
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, Dumper=yaml.Dumper)


# main
if __name__ == '__main__':
    _file_path = r'test/resources/files/data.yaml'
    result = YamlRW.read(file_path=_file_path)
    print(f'result:{result}')
