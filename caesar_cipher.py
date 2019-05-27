import client
from caesarcipher import CaesarCipher

cifrado = client.data["cifrado"]
print(cifrado)

decifrando = CaesarCipher(cifrado, offset=10)
print('Decifrado', decifrando.decoded)

# option=int(input('Digite 1 para encriptar ou 2 para decifrar'))
# if(option==1):
#     string=cifrado
#     key=int(input("Numero de Casas: \t"))
#     encrypt_str=""
#     for i in string:
#         if(i.isupper()==True):
#             encrypt_str=encrypt_str+chr((((ord(i)+key)%65)%26)+65)
#         elif(i.islower()==True):
#             encrypt_str=encrypt_str+chr((((ord(i)+key)%97)%26)+97)
#         elif(i.isdigit()==True):
#             encrypt_str=encrypt_str+chr((((ord(i)+key)%48)%26)+48)
#         else:
#             encrypt_str=encrypt_str+i
#     print(encrypt_str)
# elif(option==2):
#     select=input()
# string=cifrado
# key=int(input("Numero de Casas: \t"))
# decrypt_str=""
# if(key>0):
#     for i in string:
#         if(i.isupper()==True):                        
#             if(ord(i)-key<65):
#                 decrypt_str=decrypt_str+chr((((26+ord(i)-key)%65)%26)+65)
#             else:
#                 decrypt_str=decrypt_str+chr((((ord(i)-key)%65)%26)+65)
#         elif(i.islower()==True):
#             if(ord(i)-key<97):
#                 decrypt_str=decrypt_str+chr((((26+ord(i)-key)%97)%26)+97)
#             else:
#                 decrypt_str=decrypt_str+chr((((ord(i)-key)%97)%26)+97)
#         elif(i.isdigit()==True):
#             if(ord(i)-key<48):
#                 decrypt_str=decrypt_str+chr((((10+ord(i)-key)%48)%26)+48)
#             else:
#                 decrypt_str=decrypt_str+chr((((ord(i)-key)%48)%26)+48)
#         else:
#             decrypt_str=decrypt_str+i
#     print(decrypt_str)