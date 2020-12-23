import coder

class alphabetHelper:

    def __init__(self):
        self.alphabetList = list('abcdefghijklmnopqrstuvwxyz')
        self.size = len(self.alphabetList)
        self.alphabetDict = {self.alphabetList[indx]: indx for indx in range(self.size)}

class CeasarCoder(coder.Coder):

    alphabet = alphabetHelper()

    @staticmethod
    def __code(text, key):
        text = super(CeasarCoder, CeasarCoder)._normalizeText(text)
        codedText = ''
        for char in text:
            codedText += CeasarCoder.alphabet.alphabetList[(CeasarCoder.alphabet.alphabetDict[char] + key) % 
                                                          CeasarCoder.alphabet.size]

        return codedText

    @staticmethod
    def encode(text, key):
        return CeasarCoder.__code(text, key)

    @staticmethod
    def decode(text, key):
        return CeasarCoder.__code(text, key*(-1))

    @staticmethod
    def train(text):
        pass

    @staticmethod
    def hack(text, model):
        pass
