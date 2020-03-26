print(2**38)


print(ord('A'))
print(ord('C'))
print(ord('a'))

print(chr(97))
print(chr(67))
print(chr(20170))
print(chr(65+2))


encrypted_msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


original_msg = ""

for letter in encrypted_msg:
    if letter >= 'a' and letter <='z':
        original_msg += chr(((ord(letter)+2) - ord('a')) % 26 + ord('a'))
    else:
        original_msg += letter

print(f'The decrypted message after cracking the code is "{original_msg}"!')
