import coder

class VigenereEncoder:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetSize = len(alphabet)
    matrix = {alphabet[i]: {alphabet[j]: alphabet[j+i] for j in range(alphabetSize)} for i in range(alphabetSize)}
    reverseMatrix = {key: {matrix[key][char]: char for char in matrix[key].keys()} for key in matrix.keys()}

    @staticmethod
    def encode(text, key):
        return __code(text, key, matrix)

    @staticmethod
    def decode(text, key):
        return __code(text, key, reverseMatrix)

    @staticmethod
    def __code(text, key, matrixToUse):
        text=super()._normalize(text)
        codedText = ''
        for indx in range(len(text)):
            codedText += matrixToUse[key[indx]][text[indx]]

        return codedText

