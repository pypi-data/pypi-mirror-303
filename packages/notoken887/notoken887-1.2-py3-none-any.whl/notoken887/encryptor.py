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

    def encrypt(self, token):
        transformed = ''.join(self.replacement_table.get(char, char) for char in token)
        return f"ENC#{transformed[::-1]}"

    def decrypt(self, encrypted_token):
        if not encrypted_token.startswith("ENC#"):
            return "Invalid token format"
        
        token = encrypted_token[4:][::-1]
        reversed_table = {v: k for k, v in self.replacement_table.items()}
        transformed = ''.join(reversed_table.get(char, char) for char in token)
        return transformed
