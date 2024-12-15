def encrypt_this(text):
    words = text.split()
    encrypted = []

    for word in words:
        if len(word) == 1:
            encrypted.append(str(ord(word[0])))
        elif len(word) == 2:
            encrypted.append(str(ord(word[0])) + word[1])
        else:
            encrypted.append(str(ord(word[0])) + word[-1] + word[2:-1] + word[1])
    
    return ' '.join(encrypted)