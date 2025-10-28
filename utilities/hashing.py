# #Process of encrypting, but irreversible
# import bcrypt
# password = b'unknown99'
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# user_input = input("Enter password: ").strip().encode('utf-8')
# if bcrypt.checkpw(user_input, hashed):
#     print("Match accurate!")
# else:
#     print("Incorrect password")
import pwinput
password = pwinput.pwinput("Enter password: ", mask= "*")