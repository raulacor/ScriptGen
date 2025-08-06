import math
import pyperclip

def calculate_mask(num_ips):
    mask = 32 - math.ceil(math.log2(num_ips + 2))
    return mask

num_ips = int(input('How many IP address would you require per filial? '))
mask = calculate_mask(num_ips)
print(mask)


num_buildings = int(input('How many buildings will you be routing? '))
print('what was your given IP? ')
given_ip = input('(Example: 111.222): ')
increment = 2 ** (32 - mask - 8)


for b in range(num_buildings):
    third_octet = b * increment
    subnet = f"{given_ip}.{third_octet}.0/{mask}"
    print(f"Building {b+1}: {subnet}")


