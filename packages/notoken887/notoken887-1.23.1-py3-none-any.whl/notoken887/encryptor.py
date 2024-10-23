class TokenCryptor:
    def encrypt(self, string):
        return (string
                .replace('M', '∩')
                .replace('A', '►')
                .replace('B', '■')
                .replace('C', '☼')
                .replace('D', '♦')
                .replace('E', '✿')
                .replace('F', '♫')
                .replace('G', '✪')
                .replace('H', '✖')
                .replace('I', '★')
                .replace('J', '☻'))

    def decrypt(self, encrypted_token):
        return (encrypted_token
                .replace('∩', 'M')
                .replace('►', 'A')
                .replace('■', 'B')
                .replace('☼', 'C')
                .replace('♦', 'D')
                .replace('✿', 'E')
                .replace('♫', 'F')
                .replace('✪', 'G')
                .replace('✖', 'H')
                .replace('★', 'I')
                .replace('☻', 'J'))
