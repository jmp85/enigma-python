'''
    
    __main__.py

    Define entry points for command line scripts

'''


class ceasar(object):
    def encode(self, string):
        return string[::-1]

    def decode(self, string):
        return string[::-1]

def select_cipher(name):
    table = {
        "ceasar" : ceasar
    }
    return table[name]()

def encipher():
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description='Encipher a text file')
    parser.add_argument(
        '-c,--cipher', 
        dest='cipher', 
        choices=['ceasar'],
        help='The cipher to use')
    args = parser.parse_args()

    cipher = select_cipher(args.cipher)

    for line in sys.stdin.readlines():
        print cipher.encode(line)
        

def decipher():
    print "Deciphering"

def decrypt():
    print "Decrypting"
