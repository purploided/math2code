#
import json
import random
import sys
import time
# imports

def delete_last_line(): #thanks stackoverflow
    "Use this function to delete the last line in the STDOUT"

    sys.stdout.write('\x1b[1A')

    sys.stdout.write('\x1b[2K')

g45 = open('/math2Code/Functions/config.json', 'r')
gf45 = json.load(g45)

if gf45["bypassTagSetting"] == "False":


    repeater = 3

    for x in range(repeater):
        tag = random.randint(1,1200)
        tag2 = random.randint(1,14000)

    print(f"{tag}{tag2}")

else:
    print('')

g4 = open('/math2Code/Functions/config.json', 'r')
gf4 = json.load(g4)

if gf4["bypassKeySetting"] == "False":

    access = input('''Enter your key here
> ''')

    key = ('1f45e', '45e41', 'hh84r')

    if access in key:
        print('')

    else:
        exit()

else:
    print('')

print('''                                 ▄▄                                       ▄▄          
                           ██  ███                                     ▀███          
                           ██   ██                                       ██          
▀████████▄█████▄  ▄█▀██▄ ██████ ███████▄   ███▀██ ▄▄██▀██  ▄██▀██▄   ▄█▀▀███   ▄▄█▀██ 
  ██    ██    ██ ██   ██   ██   ██    ██  ███   █ ██▀  ██ ██▀   ▀██▄██    ██  ▄█▀   ██
  ██    ██    ██  ▄█████   ██   ██    ██      ▄▄█ ██      ██     █████    ██  ██▀▀▀▀▀▀
  ██    ██    ██ ██   ██   ██   ██    ██   ▄▄█▀   ██▄    ▄██▄   ▄██▀██    ██  ██▄    ▄
▄████  ████  ████▄████▀██▄ ▀███████  ████▄ ██████ ██████▀  ▀█████▀  ▀████▀███▄ ▀█████▀
                                                                                    
                                                                                    
''')

g456 = open('/math2Code/Functions/config.json', 'r')
gf456 = json.load(g456)

if gf45["skipSetting"] == "False":

    print("M")
    time.sleep(0.2)
    delete_last_line()
    print("Ma")
    time.sleep(0.1)
    delete_last_line()
    print("Mad")
    time.sleep(0.3)
    delete_last_line()
    print("Made")
    time.sleep(0.2)
    delete_last_line()
    print("Made b")
    time.sleep(0.4)
    delete_last_line()
    print("Made by")
    time.sleep(0.5)
    delete_last_line()
    print("Made by N")
    time.sleep(0.3)
    delete_last_line()
    print("Made by Ni")
    time.sleep(0.4)
    delete_last_line()
    print("Made by Nic")
    time.sleep(0.5)
    delete_last_line()
    print("Made by Nico")
    time.sleep(0.1)
    delete_last_line()
    print("Made by Nicoh")
    time.sleep(0.4)
    delete_last_line()
    print("Made by Nicohl")
    time.sleep(0.3)
    delete_last_line()
    print("Made by Nicohla")
    time.sleep(0.75)
    delete_last_line()
    print("Made by Nicohlas")
    time.sleep(0.5)

else:
    print('')

print('''

Thanks for cloning!

''')

def convert_Binary(math_for_Convert):

    converted = ''.join(format(ord(i), '08b') for i in math_for_Convert)

    print(str(converted))

binaryInput = input('''Enter math/algebra
> ''')

print('Binary: ')

convert_Binary(binaryInput)

a = input('Press [ENTER] if you would like to continue')

print(''' --
Please copy and paste the code
 -- ''')

def convert_Gray(n):

    n = int(n, 2)
    n ^= (n >> 1)
 
    return bin(n)[2:]

grayInput = input('''Enter binary
> ''')
b = convert_Gray(grayInput)
print(f''' ---
Gray Code: 
{b}
 --- ''')

graycode = {
    "gray": b
}

with open('/math2Code/Functions/package.json', 'w') as dictionary:
            json.dump(graycode, dictionary)

g = open('/math2Code/Functions/config.json', 'r')
gf = json.load(g)

if gf["encryptSetting"] == "True":
    a2 = input('Press [ENTER] if you would like to continue')

    def flip(my_nu):
        return '1' if(my_nu == '0') else '0'

    def Gray_to_Binary(gray):
        binaryCode = ""
        binaryCode += gray[0]
        for i in range(1, len(gray)):

            if (gray[i] == '0'):
                binaryCode += binaryCode[i - 1]
            else:
                binaryCode += flip(binaryCode[i - 1])

        return binaryCode
    grayCode = input(''' ---
Enter Gray Code here
> ''')
    print(''' ---
Binary:''')
    print(Gray_to_Binary(grayCode))
    print(' ---')

else:
    exit()