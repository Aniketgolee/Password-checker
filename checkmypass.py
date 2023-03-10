
import hashlib
import sys
from lib2to3.pgen2 import literals

import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetchinf{request_api_data},check api')
    return res

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for h, count in hashes:
     if h == hash_to_check:
        return count
    return 0


def pwned_api_check(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1[:5], sha1[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response,tail)


def main (args):
   for password in args:
      count = pwned_api_check(password)
      if count:
         print(f'{password}was found{count} you shold probabaly change your password')
      else:
         print(f'{password} not found carry on!')       

if __name__ == '__main__':    
 
 sys.exit(main(sys.argv[1:]))






