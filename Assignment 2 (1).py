
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast

def encrypt():
    # Encryption code
    f = open('public.pem', 'rb')
    publickey = RSA.importKey(f.read())  # read key
    txt = input("Enter string to encrypt: ")
    encryptor = PKCS1_OAEP.new(publickey)
    encrypted_txt = encryptor.encrypt(bytes(txt, 'utf-8'))
    print("Encrypted message: ", encrypted_txt)


def decrypt():
    # Decryption code
    f2 = open('private.pem', 'rb')
    publickey2 = RSA.importKey(f2.read())  # read key
    txt = input("Enter string to decrypt: ")
    decryptor = PKCS1_OAEP.new(publickey2)
    decrypted_txt = decryptor.decrypt(ast.literal_eval(str(txt)))
    print("decrypted message: ", decrypted_txt)





privatekey, publickey = RSA.generate(4096)

f = open('public.pem', 'wb')
f.write (privatekey.save_pkcs1('PEM'))   #save private key
f.write(key.privatekey().exportKey('PEM'))
f.close()


f = open('private.pem', 'wb')
f.write (publickey.save_pkcs1('PEM'))    #save public key
f.write(key.publickey().exportKey('PEM'))
f.close()


encrypt()
decrypt()