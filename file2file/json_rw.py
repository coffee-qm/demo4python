import json

"""
Reader&Writer for json
"""


class JsonRW:
    def __init__(self):
        print('Init')

    # read
    @staticmethod
    def read(file_path):
        _data = []
        with open(file_path, 'r') as f:
            _data = json.load(f)
        return _data

    # write
    @staticmethod
    def write(file_path, data):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, Dumper=json.RoundTripDumper)


# main
if __name__ == '__main__':
    _file_path = r'test/resources/files/data.json'
    result = JsonRW().read(file_path=_file_path)
    print(f'result:{result}')
