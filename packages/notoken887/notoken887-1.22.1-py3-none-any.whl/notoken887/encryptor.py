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
        return transformed[::-1]  # Return the reversed transformed token

    def decrypt(self, encrypted_token):
        token = encrypted_token[::-1]  # Reverse the encrypted token
        transformed = ''.join(self.decryption_table.get(char, char) for char in token)
        return transformed
