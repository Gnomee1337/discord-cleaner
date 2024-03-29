# Discord Cleaner

Discord Cleaner deletes all your messages from the specified private dialog in Discord

![clear-chat-preview](https://i.imgur.com/adBpDLr.jpeg)

# Use at your own risk:
>Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is forbidden, and can result in an account termination if found.

https://support.discord.com/hc/en-us/articles/115002192352

# Setup:
>*IMPORTANT NOTE:* **discord.py package must be v1.7.3 or less.** The ability to automate user actions was removed from version v2.0.0
```
$ pip install -r requirements.txt
```

# Usage:

1. Find your Discord Auth Token (https://www.google.com/search?q=how+to+get+discord+auth+token)
2. Duplicate **.env.example** file and rename it to **.env**
3. In **.env** file set your discord auth_token (`DS_TOKEN = "your_auth_token"`)
5. `$ python3 clear_chat.py`
