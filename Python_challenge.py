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

for c in encrypted_msg:
    print(chr(ord(c)-2))
