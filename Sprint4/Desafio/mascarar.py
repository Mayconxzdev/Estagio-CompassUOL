import hashlib

while True:
    input_string = input("Digite uma string para mascarar: ")
    hash_object = hashlib.sha1(input_string.encode())
    hex_dig = hash_object.hexdigest()
    print(f"Hash SHA-1: {hex_dig}")
