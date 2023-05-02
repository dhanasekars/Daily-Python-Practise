""" 
Created on : 26/04/23 11:38 am
@author : ds  
"""

import hashlib
import os

message = "Hello, world from Python!"
hash_object = hashlib.sha384(message.encode())
# print(hash_object.hexdigest())
# print(hash_object.digest())
# print(hash_object.name)


# using salt
# Define a password and salt

password = "myhashedstrongpassword"
password_to_check = "myhashedstrongpassword"

salt = os.urandom(16)
salted_hash_object = hashlib.sha256(salt + password.encode())
salted_hex_digit = salted_hash_object.hexdigest()

stored_password = salt + b':' + salted_hex_digit.encode()
print(stored_password)

retrieved_salt, retrieved_hex_dig = stored_password.split(b':')
hash_object_retrieved = hashlib.sha256(retrieved_salt + password_to_check.encode())
hex_dig_to_check = hash_object_retrieved.hexdigest()

if hex_dig_to_check.encode() == retrieved_hex_dig:
    print("Password is correct")
else:
    print("Password is incorrect")