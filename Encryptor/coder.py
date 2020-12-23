class Coder:
    @staticmethod
    def encode(text, key):
        pass

    @staticmethod
    def decode(text, key):
        pass

    @staticmethod
    def train(text):
        pass

    @staticmethod
    def hack(text, model):
        pass

    @staticmethod
    def _normalizeText(text):
        alphabet = set('abcdefdhijklmnopqrstuvwxyz')
        text.lower()
        for char in set(text):
            if char not in alphabet:
                text.replace(char, '')
        return text
