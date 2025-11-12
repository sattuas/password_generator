from models.generator import PasswordGenerator


pw = PasswordGenerator(16, True, True, True, True)

print(f'senha gerada: {pw.generate()}')