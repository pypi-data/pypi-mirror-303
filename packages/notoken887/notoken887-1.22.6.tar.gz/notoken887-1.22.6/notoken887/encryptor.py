class TokenCryptor:
    def encrypt(self, token):
        return token.replace('M', '∩')

    def decrypt(self, encrypted_token):
        return encrypted_token.replace('∩', 'M')
