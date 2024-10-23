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

cryptor = TokenCryptor()
ENCTOKEN = "MTI5Nzc4MzcxNjcxMzU5NDkyMA.GI3C-D.bX6Hc8XjqSKGkFn44hbLiwf3uuruZSlohn78BI"

# Encrypt the token
converted_token = cryptor.encrypt(ENCTOKEN)
print(f"Converted TOKEN: {converted_token}")

# Decrypt back to verify
decrypted_token = cryptor.decrypt(converted_token)
print(f"Decrypted TOKEN: {decrypted_token}")
