from pwn import *
import base64
import json



# Playing around with ASCII, calling the character position into the chr function and converting into a tring which is then added to the list_decoded variable. The variable is refactored everytime. 

# To keep good programming hygiene in mind, will put into a function that I can use at a later time if desired

# def question_one():

#     char_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

#     list_decoded = ""

#     for i in char_list:
#         list_decoded += str(chr(i))

#     print(list_decoded)
#     return


# def question_two():
#     print(bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))
#     return


# def question_three(): 
#     le_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#     le_bytes = bytes.fromhex(le_string)
#     le_base64 = base64.b64encode(le_bytes)
#     print(le_base64)

# question_three()

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST,PORT)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

request = {
    "buy": "clothes"
    }

json_send(request)

response = json_recv()

print(response)