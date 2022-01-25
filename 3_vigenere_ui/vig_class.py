class Vigener:
    def __init__(self, key, alphabet='abcdefghijklmnopqrstuvwxyz'):
        self.key = key
        self.alphabet = alphabet
        self.keylen = len(key)
        self.alphlen = len(alphabet)
        self.lastinput = ''
        self.lastoutput = ''

    def code(self, text):
        coded_text = ''
        txt_len = len(text)
        mask = self.key * (txt_len // self.keylen + 1)
        for i in range(txt_len):
            coded_text += self.alphabet[(self.alphabet.index(text[i]) + self.alphabet.index(mask[i])) % self.alphlen]
        self.lastinput = text
        self.lastoutput = coded_text
        return coded_text

    def decode(self, text):
        decoded_text = ''
        txt_len = len(text)
        mask = self.key * (txt_len // self.keylen + 1)
        for i in range(txt_len):
            decoded_text += self.alphabet[(self.alphabet.index(text[i]) - self.alphabet.index(mask[i])) % self.alphlen]
        self.lastinput = text
        self.lastoutput = decoded_text
        return decoded_text

