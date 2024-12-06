import random
import string

def generate_custom_password(num_numbers, num_uppercase, num_lowercase, include_special):
    """
    Gera uma senha personalizada com base nas preferências do usuário.
    :param num_numbers: Número de dígitos na senha.
    :param num_uppercase: Número de letras maiúsculas na senha.
    :param num_lowercase: Número de letras minúsculas na senha.
    :param include_special: Incluir caracteres especiais na senha? (True/False).
    :return: Senha gerada.
    """
    # Caracteres disponíveis
    numbers = string.digits
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    special_characters = string.punctuation if include_special else ''

    # Gerar partes da senha
    password_numbers = ''.join(random.choice(numbers) for _ in range(num_numbers))
    password_uppercase = ''.join(random.choice(uppercase_letters) for _ in range(num_uppercase))
    password_lowercase = ''.join(random.choice(lowercase_letters) for _ in range(num_lowercase))
    password_specials = ''.join(random.choice(special_characters) for _ in range(max(0, num_numbers + num_uppercase + num_lowercase - len(password_numbers + password_uppercase + password_lowercase))))
    
    # Combina e embaralha os caracteres gerados
    password = password_numbers + password_uppercase + password_lowercase + password_specials
    password = ''.join(random.sample(password, len(password)))

    return password

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Senhas Personalizado!")
    try:
        # Entrada do usuário
        num_numbers = int(input("Quantos números você deseja na senha? "))
        num_uppercase = int(input("Quantas letras maiúsculas você deseja? "))
        num_lowercase = int(input("Quantas letras minúsculas você deseja? "))
        include_special = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

        # Geração da senha
        password = generate_custom_password(num_numbers, num_uppercase, num_lowercase, include_special)
        print(f"Sua senha gerada é: {password}")
    except ValueError:
        print("Por favor, insira valores válidos para cada campo.")
