import string


def main():
    choice0 = int(input('How many IP addresses do you require per filial? ')) #int para falar que o input vai ser um numero
    if 1024 <= choice0 <= 2048:
        print('For', choice0, 'you will need the following IP mask: /21')
        choice_mask21 = input('Is that coerrect? [Y/N]')
        if choice_mask21 :
           
            print("Let's start things off.")
            ip_mask21 = input('What was the IP address provided to you? Example: 111.222 ') #sem 'int' pq o ip nao vai ser u nmr inteiro
            clean_output_21 = ip_mask21.replace(' ', '.')
            matrizip_21 = clean_output_21 + '.0.0'
            print(matrizip_21)


    else:
        print('no')


if __name__ == "__main__":
    main()
