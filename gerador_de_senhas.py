import random
import string

letras = string.ascii_lowercase
letras_maiuscula = string.ascii_uppercase
numeros = "0123456789"
simbolos = "!@#$%&*Ç"

for_senha = letras + letras_maiuscula + numeros + simbolos

tamanho_senha = 12

senha = "".join(random.sample(for_senha, tamanho_senha))

print("Senha = " + senha)
