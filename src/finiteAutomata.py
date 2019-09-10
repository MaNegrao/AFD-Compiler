

class finiteAutomata(object):
    __initial_state = 0
    __error_state = -1
    __alphabet = []
    __FA = {}

    def __init__(self, file):
        self.__mapGramma(file)