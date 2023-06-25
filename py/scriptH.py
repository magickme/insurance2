#incomplete exercise 

def caesar_cipher_decode(cipher_text, offset):
    decoded_text = ""

    for c in cipher_text:
        if c.isalpha():
            ascii_start = ord('a') if c.islower() else ord('A')
            decoded_char = chr((ord(c) - ascii_start - offset) % 26 + ascii_start)
            decoded_text += decoded_char
        else:
            decoded_text += c

    return decoded_text

cipher_text = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10
decoded_message = caesar_cipher_decode(cipher_text, offset)
print(decoded_message)
