from models.generator import PasswordGenerator


print("===== PASSWORD GENERATOR ======")


while True:
    print("[ 1 ] GERAR SENHA")
    print("[ 0 ] SAIR")
    option = int(input("Input your option: "))

    match option:
        case 1:
            print("generating password...")
            pw = PasswordGenerator(16, True, True, True, True)
            print(f'generated password: {pw.generate()}')
        case 0:
            print("closing...")
            break
        case _:
            print("error! invalid option")


# pw = PasswordGenerator(16, True, True, True, True)

# print(f'senha gerada: {pw.generate()}')