data = 'I am a student'

def encryption(data):
    ans_enc = []
    for i in range(len(data)):
        if data[i].islower():
            a = 219 - ord(data[i])
        else:
            a = ord(data[i])
        ans_enc.append(chr(a))
    print(ans_enc)
    return ans_enc



def decryption(data):
    ans_dec = ''
    for i in range(len(data)):
        if data[i].islower():
            a = chr(219 - int(ord(data[i])))
        else:
            a = data[i]
        ans_dec = ans_dec + a
    print(ans_dec)


enc = encryption(data)
dec = decryption(enc)