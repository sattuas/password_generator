from models.generator import PasswordGenerator


def confirm_option(text):
    option = ''
    while True:
        option = str(input(f'{text} [Y/n] ')).strip()[0]
        if option in 'Yy':
            return True
        elif option in 'Nn':
            return False

print("===== PASSWORD GENERATOR ======")

letter_upper = False
letter_lower = False
symbols = False
numbers = False


while True:
    print("[ 1 ] GERAR SENHA")
    print("[ 0 ] SAIR")
    option = int(input("Input your option: "))

    match option:
        case 1:
            letter_upper = confirm_option("capital letters?")
            letter_lower = confirm_option("lower letters?")
            symbols = confirm_option("symbols?")
            numbers = confirm_option("numbers?")

            print("generating password...")
            pw = PasswordGenerator(16, letter_upper, letter_lower, symbols, numbers)
            print(f'generated password: {pw.generate()}')
        case 0:
            print("closing...")
            break
        case _:
            print("error! invalid option")


# pw = PasswordGenerator(16, True, True, True, True)

# print(f'senha gerada: {pw.generate()}')