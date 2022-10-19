import json

import gnupg

class PGPInterpreter:

    def generate_pair(self):
        gpg = gnupg.GPG(gpgbinary='/bin/gpg')
        gpg.encoding = 'utf-8'
        
        with open('false.json', 'r') as file:
            info = file.read()
            info = json.loads(info)

        input_info = gpg.gen_key_input(name_email = info['email'],
                                       passphrase = info['pass'],
                                       key_type = 'RSA',
                                       key_lenght = 1024)

        key = gpg.gen_key(input_info)
        print('hi')
        print(key)


PGPInterpreter().generate_pair()