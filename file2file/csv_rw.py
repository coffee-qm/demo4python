import csv

"""
Reader&Writer for csv
"""


class CsvRW:
    def __init__(self):
        print('Init')

    # read
    @staticmethod
    def read(file_path):
        _data = []
        with open(file_path, 'r') as f:
            csv_reader = csv.reader(f)
            _header = next(csv_reader)
            _data.append(_header)
            for row in csv_reader:
                _data.append(row)
        return _data

    # write
    @staticmethod
    def write(file_path, header, data):
        with open(file_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)


# main
if __name__ == '__main__':
    _file_path = r'test/resources/files/data.csv'
    result = CsvRW().read(file_path=_file_path)
    print(f'result:{result}')
