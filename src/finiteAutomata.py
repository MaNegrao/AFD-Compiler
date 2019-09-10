class finiteAutomata(object):
    # default settings
    __initial_state = 0
    __error_state = -1
    __alphabet = []
    __FA = {}


    __input_folder = 'set'

    __tokens_file = 'tokens.csv'
    __gramma_file = ''

    def __init__(self, file):
        self.mapGramma(file)
        self.mapTokens()
    
    def mapGramma(file):

    def mapTokens(file):    