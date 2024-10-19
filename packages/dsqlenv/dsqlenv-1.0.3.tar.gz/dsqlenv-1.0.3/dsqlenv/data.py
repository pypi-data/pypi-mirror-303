data="dq4W18Q+wvgJ0JSoh2mJBDGmSEujKP9Cv4iRZoKJOEajpJQKu9hrMrTI0soz76xLf5qYOrCKFEFjMTpHV//Xz+l3NVq8xuEWfoyUN6YG7fU7cLNdAKHImBTMeTG+es0mDF9cd//kswS1S2/NOmP/tm6uwz8ei8bezt08qAEopEXwmns2dj0Uutz1Fyv3KftaXmtUi435a3l0tGtl9E7FyzxXE4DZVy9wpFwO6KGnP4sAuQr5dRw77ZV7jjcp2lkHLgszKV0GjCtDHnjbSRxP2hbSkRSuhdH3Rgxd7qq1lW1RGQ3oV7lH4XactTugN+HE/MALKVgw53n6cHHecBdZWGxkH3d4pyGFW4ko6+E9AYg="

# from Crypto.Cipher import AES
# import base64
# import json

# # Define the file content to be encrypted
# file_content = {
#     "DB_USER": "xxx",
#     "DB_PASSWORD": "xxx",
#     "DB_NAME": "xxx",
#     "DB_HOST": "xxx",
#     "AES_KEY": "xxx",
#     "DB_PORT": "xxx",
#     "TABLE_NAME": "xxx",
#     "ID_COLUMN": "name",
#     "INFO_COLUMN": "data"
# }

# # AES key (must be 16 bytes)
# aes_key = "<password>".ljust(16)[:16].encode('utf-8')

# # Convert file content to JSON string
# data = json.dumps(file_content)

# # Pad the data to be a multiple of 16 bytes
# pad = 16 - len(data) % 16
# data_padded = data + pad * chr(pad)

# # Initialize AES cipher in ECB mode (Electronic Codebook mode)
# cipher = AES.new(aes_key, AES.MODE_ECB)

# # Encrypt the data and encode it to base64 for safe printing
# encrypted_data = base64.b64encode(cipher.encrypt(data_padded.encode('utf-8'))).decode('utf-8')

# print(encrypted_data)
