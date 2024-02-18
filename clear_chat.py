import os

import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

user_token = os.getenv('DS_TOKEN')
target_username = ''


@client.event
async def on_ready():
    print(f'Logged in as \"{client.user.name}\" (ID: {client.user.id})')
    await clear_private_chat(target_username)
    print('Clearing finished!')
    try:
        await client.close()
    except Exception as e:
        raise e


@client.event
async def clear_private_chat(username: str):
    # print(client.private_channels)
    for private_chat in client.private_channels:
        if isinstance(private_chat, discord.DMChannel):
            # print('Found private chat')
            if private_chat.recipient.name == target_username:
                print(f'Chat with {target_username} found!')
                message_counter = len(await private_chat.history(limit=None).flatten())
                print(f'Chat with {target_username} contains {message_counter} messages.')
                want_delete = input('Are you sure you want to delete them? [yes/no]\n')
                if want_delete == 'yes':
                    async for message in private_chat.history():
                        if message.author.name == client.user.name:
                            try:
                                print(f'[Deleted] {message.content}')
                                await message.delete()
                            except discord.Forbidden:
                                print(f'You do not have proper permissions to delete \"{message.content}\"')
                                continue
                            except discord.NotFound as enf:
                                print(enf)
                                continue
                            except discord.HTTPException as dh:
                                raise dh
                else:
                    try:
                        await client.close()
                        print('[EXIT] Action Canceled!')
                    except Exception as e:
                        raise e


def main():
    if user_token == '':
        print('Please provide discord auth token in .env file (DS_TOKEN=\"your_auth_token\")')
        return 0
    global target_username
    target_username = input('Provide the username of the user you want to clear the chat with:\n')
    try:
        client.run(user_token, bot=False)
    except Exception as e:
        raise e


if __name__ == '__main__':
    main()
