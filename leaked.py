#!/usr/bin/python3
import json, requests
from os import name

try:
    input = raw_input
except NameError:
    pass

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def grab_password(email):
    UserAgent = {'User-Agent': 'test-agent'}
    url  = "https://ghostproject.fr/search.php"
    data = {"param":email}
    req = requests.post(url,headers=UserAgent,data=data)
    result = req.text.split("\\n")
    if "Error" in req.text or len(result)==2:
        return False
    else:
        return result[1:-1]        

def back():
    print()
    back = input('\033[92mDo you want to contunue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        menu()
    elif back[0].upper() == 'N':
        print('\033[93m[+] Remember to checkout: https://GitHackTools.blogspot.com')
        exit(0)
    else:
        print('\033[92m?')
        exit(0)

def leaked():
    print("""\033[93m ___       _______   ________  ___  __    _______   ________  ________      
|\  \     |\  ___ \ |\   __  \|\  \|\  \ |\  ___ \ |\   ___ \|\_____  \     
\ \  \    \ \   __/|\ \  \|\  \ \  \/  /|\ \   __/|\ \  \_|\ \|____|\  \    
 \ \  \    \ \  \_|/_\ \   __  \ \   ___  \ \  \_|/_\ \  \ \\ \    \ \__\   
  \ \  \____\ \  \_|\ \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \_\\ \    \|__|   
   \ \_______\ \_______\ \__\ \__\ \__\\ \__\ \_______\ \_______\       ___ 
    \|_______|\|_______|\|__|\|__|\|__| \|__|\|_______|\|_______|      |\__\\
                                                                        \|__| 2.1
     A Checking tool for Hash codes, Passwords and Emails leaked""")

def menu():
    try:
        leaked()
        print()
        print("""\033[96mWhat do you want to check?
    1. Password Hashes      4. Grabb email passwords
    2. Hash Leaked          5. About Author
    3, Email Leaked         6. Exit (or just need Crtl+C)
    """)

        choice = input('Enter your choice (1-6): ')
        if choice == '1':
            password = input('Enter or paste a password you want to check: ')
            non_hash = requests.get('https://lea.kz/api/password/'+password)
            js = json.loads(non_hash.text)
            print("""\033[93mIT LEAKED!!! The Hash codes of the Password is:
MD5: """+js['md5']+"""
SHA1: """+js['sha1']+"""
SHA224: """+js['sha224']+"""
SHA256: """+js['sha256']+"""
SHA384: """+js['sha384']+"""
SHA512: """+js['sha512']+"""""")
            back()

        elif choice == '2':
            code = input('Enter or paste a hash code you want to check: ')
            password = requests.get('https://lea.kz/api/hash/'+code)
            js = json.loads(password.text)
            print('\033[93mTHAT HASH CODE IS LEAKED! It means: '+js['password'])
            back()

        elif choice == '3':
            email = input('\nEnter or paste a email you want to check: ')
            info = requests.gets(email)
            js = json.loads(info.txt)
            print("""\n\033[93m[-] THIS EMAIL HAS BEEN LEAKED!
    It was used for:""",info)
            back()

        elif choice == '5':
            print("""\033[93mLeaked? 2.1 - A Checking tool for Hash codes and Passwords leaked
    AUTHOR: https://GitHackTools.blogspot.com
            https://twitter.com/SecureGF
            https://fb.com/githacktools
            https://plus.google.com/+TVT618""")
            back()

        elif choice == '4':
            email = input('\nEnter or paste a email you want to check: ')
            emails = grab_password(email)
            if not emails:
                print("\033[93m[+] Passwords not found! It was not leaked!!!")
                back()
            else:
                for email in emails:
                    print(email)
            back()

        elif choice == '6':
            print("\033[93m[+] Don't forget https://GitHackTools.blogspot.com")
            exit(0)
        else:
            print('?\n')
            menu()

    except KeyboardInterrupt:
        back()

    except requests.exceptions.ConnectionError:
        print('\033[91mThe https://Lea.kz server has gone... or your Internet offline!!! You can only use "Grabb email passwords"')
        exit
    except json.decoder.JSONDecodeError:
        print('\033[93mCongratulations! It was not leaked!!!')
        print()
        back()
        
menu()
