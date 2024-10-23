class TokenCryptor:
    replacement_table = {
        'a': '©',
        'b': 'ℓ',
        'c': '∑',
        'd': '∆',
        '1': '⊗',
        '2': '⊖',
        '3': '⊙',
        '4': '⊚',
    }

    decryption_table = {
        '©': 'a',
        'ℓ': 'b',
        '∑': 'c',
        '∆': 'd',
        '⊗': '1',
        '⊖': '2',
        '⊙': '3',
        '⊚': '4',
    }

    def encrypt(self, token):
        transformed = ''.join(self.replacement_table.get(char, char) for char in token)
        return f"ENC#{transformed[::-1]}"

    def decrypt(self, encrypted_token):
        if not encrypted_token.startswith("ENC#"):
            token = encrypted_token[::-1]
            transformed = ''.join(self.decryption_table.get(char, char) for char in token)
            return transformed
        
        token = encrypted_token[4:][::-1]
        transformed = ''.join(self.decryption_table.get(char, char) for char in token)
        return transformed
