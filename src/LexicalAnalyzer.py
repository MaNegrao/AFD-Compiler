class LexicalAnalyze(object):
    __separators = []
    __symbol_table = []
    __source_code = []

    __separators_file = 'separators.in'
    __source_code_file = 'code.in'

    def __init__ (self):
        self.read_separators()

    def read_separators(self):
        try:
            file = open('set/'+self.__separators_file, 'r')
            for separator in file:
                separator = separator.replace('\n', '')
                self.__separators.append(separator)
            file.close()
        except:
            print('Read Error: Separators!')
            pass