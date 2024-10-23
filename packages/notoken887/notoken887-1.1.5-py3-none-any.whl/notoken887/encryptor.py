class TokenCryptor:
    def encrypt(self, token):
        return f"ENC#{token[::-1]}"

    def decrypt(self, encrypted_token):
        return encrypted_token[4:][::-1]
