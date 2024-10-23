class TokenCryptor:
    replacement_table = {
        'a': '©',
        'b': 'ℓ',
        'c': '∑',
        'd': '∆',
        'e': 'ƒ',
        'f': '◊',
        'g': '♥',
        'h': '♦',
        'i': '✱',  # Changed from '♦' to '✱'
        'j': '♣',
        'k': '♠',
        'l': '✿',
        'm': '✵',
        'n': '✦',
        'o': '✧',
        'p': '★',
        'q': '✩',
        'r': '✪',
        's': '✬',
        't': '✭',
        'u': '✮',
        'v': '✯',
        'w': '✰',
        'x': '✲',
        'y': '✳',
        'z': '✴',  # Changed from '✳' to '✴'
        '0': '⊕',
        '1': '⊗',
        '2': '⊖',
        '3': '⊙',
        '4': '⊚',
        '5': '⊛',
        '6': '⊜',
        '7': '⊝',
        '8': '⊞',
        '9': '⊟',
        'A': 'Ω',
        'B': 'Θ',
        'C': 'Ξ',
        'D': 'Π',
        'E': 'Λ',
        'F': 'Γ',
        'G': 'Φ',
        'H': 'Ψ',
        'I': 'Σ',
        'J': 'Τ',
        'K': 'Δ',
        'L': 'ζ',  # Changed from 'Λ' to 'ζ'
        'M': 'Γ',
        'N': 'β',
        'O': 'η',
        'P': 'σ',
        'Q': 'τ',
        'R': 'χ',
        'S': 'ρ',
        'T': 'γ',
        'U': 'θ',
        'V': 'λ',
        'W': 'μ',  # Changed from 'λ' to 'μ'
        'X': 'ψ',
        'Y': 'ν',
        'Z': '∞',  # Changed from 'ν' to '∞'
    }

    def encrypt(self, token):
        transformed = ''.join(self.replacement_table.get(char, char) for char in token)
        return f"ENC#{transformed[::-1]}"

    def decrypt(self, encrypted_token):
        token = encrypted_token[4:][::-1]
        reversed_table = {v: k for k, v in self.replacement_table.items()}
        transformed = ''.join(reversed_table.get(char, char) for char in token)
        return transformed
