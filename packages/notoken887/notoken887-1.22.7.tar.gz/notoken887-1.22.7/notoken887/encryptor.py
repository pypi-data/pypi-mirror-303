class TokenCryptor:
    def encrypt(self, string):
        return string.replace('M', '∩')

    def decrypt(self, encrypted_token):
        return encrypted_token.replace('∩', 'M')
