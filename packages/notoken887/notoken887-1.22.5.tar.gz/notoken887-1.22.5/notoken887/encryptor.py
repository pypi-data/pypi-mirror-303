class TokenCryptor:
    def encrypt(self, token):
        return token.replace('M', '4')

    def decrypt(self, encrypted_token):
        return encrypted_token.replace('4', 'M')


# Example usage
cryptor = TokenCryptor()
text_string = "This is a test string with capital M."

encrypted_token = cryptor.encrypt(text_string)
print(f"Encrypted TOKEN: {encrypted_token}")

decrypted_token = cryptor.decrypt(encrypted_token)
print(f"Decrypted TOKEN: {decrypted_token}")
