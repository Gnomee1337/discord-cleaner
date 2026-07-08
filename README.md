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

# Security Disclaimer

This repository contains software that may be capable of interacting with remote services, automating actions, or performing security-related operations.

The project is intended exclusively for:
- Educational purposes
- Security research
- Testing systems you own or are explicitly authorized to test

Do **not** use this software against systems, networks, or services without prior authorization.

The authors assume no liability for misuse or any damages resulting from the use of this software.
