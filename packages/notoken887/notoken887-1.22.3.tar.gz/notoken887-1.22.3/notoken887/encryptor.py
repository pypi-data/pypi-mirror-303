class TokenCryptor:
    replacement_table = {
        'M': 'x',
    }

    decryption_table = {
        'x': 'M',
    }

    def encrypt(self, token):
        transformed = ''.join(self.replacement_table.get(char, char) for char in token)
        return transformed  

    def decrypt(self, encrypted_token):
        transformed = ''.join(self.decryption_table.get(char, char) for char in encrypted_token)
        return transformed
