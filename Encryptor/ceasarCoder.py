import coder

class CeasarCooder(coder.Coder):
    alphabetList = list('abcdefghijklmnopqrstuvwxyz')
    alphabetSize = len(alphabetList)
    alphabetDict = {alphabetList[indx]: indx for indx in range(alphabetSize)}

    @staticmethod
    def encode(text, key):
        text = super()._normalizeText(text)
        encodedText = ''
        for char in text:
            encodedText += alphabetList[alphabetDict[char] + key]

        return encodedText

    @staticmethod
    def decode(text, key):
        text = super()._normalizeText(text)
        decodedText = ''
        for char in text:
            decodedText += alphabetList[alphabetDict[char] - key]

        return decodedText

    @staticmethod
    def train(text):
        pass

    @staticmethod
    def hack(text, model):
        pass
