class TokenCryptor:
    def encrypt(self, string):
        return string.replace('M', '∩').replace('A', '►')

    def decrypt(self, encrypted_token):
        return encrypted_token.replace('∩', 'M').replace('►', 'A')
