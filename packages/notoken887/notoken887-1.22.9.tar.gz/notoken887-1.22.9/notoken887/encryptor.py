class TokenCryptor:
    def encrypt(self, string):
        return string.replace('M', '∩').replace('A', '◙').replace('x', '卐')

    def decrypt(self, encrypted_token):
        return encrypted_token.replace('∩', 'M').replace('◙', 'A').replace('卐', 'x')
