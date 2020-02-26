import argparse
"""
"""


class ByArgParser:
    def __init__(self):
        print('Init')
        self.args = self.__parse_arg__()

    #
    @staticmethod
    def __parse_arg__():
        parser = argparse.ArgumentParser(description="This is a file to file trans")
        parser.add_argument('--file', '-f', help="file path")
        args = parser.parse_args()
        # check arguments
        if args.file is None or args.file == '':
            print(f'Arguments error. args:{args}')
            exit(-1)
        return args

    #
    def main(self):
        print(self.args.file)


# main
if __name__ == '__main__':
    ByArgParser()
