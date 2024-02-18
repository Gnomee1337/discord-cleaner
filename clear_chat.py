import os
import discord
from dotenv import load_dotenv
import requests

load_dotenv()

client = discord.Client()
user_token = os.getenv('DS_TOKEN')
target_username = os.getenv('CHAT_TARGET')


@client.event
async def on_ready():
    print(f'Logged in as \"{client.user.name}\" (ID: {client.user.id})')
    await clear_private_chat(target_username)


@client.event
async def clear_private_chat(username: str):
    # print(client.private_channels)
    for private_chat in client.private_channels:
        if isinstance(private_chat, discord.DMChannel):
            # print('Found private chat')
            if private_chat.recipient.name == target_username:
                print(f'Chat with {target_username} found!')
                # message_counter = len(await private_chat.history(limit=None).flatten())
                # # messages = await private_chat.history().flatten()
                # print(message_counter)
                async for message in private_chat.history():
                    if message.author.name == client.user.name:
                        try:
                            print(f'[Deleted] {message.content}')
                            # await message.delete()
                        except discord.Forbidden:
                            print(f'You do not have proper permissions to delete \"{message.content}\"')
                            continue
                        except discord.NotFound as enf:
                            print(enf)
                            continue
                        except discord.HTTPException as dh:
                            raise dh
                    # await message.delete()
                    # else:
                    #     continue

                # messages_counter = 0
                # for message in private_channel.text_channels:
                #     print(channel.name)
                #     async for message in channel.history(limit=None):
                #         # if message.author.name == client.user.name:
                #         counter += 1
                # print(counter)
                # # for message in messages:
                # #     print(await message.delete())


# # For Discord servers
# # @client.event
# async def clear_chat(target_username: str):
#     print(client.guilds)
#     for private_channel in client.guilds:
#         if isinstance(private_channel, discord.Guild):
#             print('Found private chat')
#             if private_channel.name == target_username:
#                 print(f'Yes its {target_username}')
#                 # messages = len(await private_channel.history(limit=None).flatten())
#                 counter = 0
#                 for channel in private_channel.text_channels:
#                     print(channel.name)
#                     async for message in channel.history(limit=None):
#                         # if message.author.name == client.user.name:
#                         counter += 1
#                 print(counter)
#                 # for message in messages:
#                 #     print(await message.delete())


def main():
    # TODO: input target nickname
    client.run(user_token, bot=False)


if __name__ == '__main__':
    main()
