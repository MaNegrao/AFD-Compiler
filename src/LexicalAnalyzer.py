class LexicalAnalyze(object):
    __separators = []
    __symbol_table = []
    __source_code = []

    __separators_file = 'separators.in'
    __source_code_file = 'code.in'

    def __init__ (self):
        self.read_separators()

    def read_separators(self)