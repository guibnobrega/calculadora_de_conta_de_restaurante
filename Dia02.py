import os

def clear_console():
    """Clear the console based on the operating system(for better readability)"""
    os.system('cls' if os.name == 'nt' else 'clear')


def right_answer_numeric(user_question):
    """
    Pergunta ao usuário uma escolha até que ele digite um valor numérico.
    Aceita tanto números quanto textos (ex.: '10, '10 reais').

    """
    
    while True:
        user_choice = input(f"{user_question}\n")
        
        # Normaliza entrada (remove espaços e coloca em minúsculas)
        normalized = user_choice.strip().lower()
        # Procura números dentro da string (ex.: "10 reais")
        number = ''.join([c for c in normalized if c.isdigit()])


            # 1. Verifica se a resposta é numérica 
        try:
            num_choice = float(number)
            
            print(f"Valor informado: {num_choice}")
            return num_choice
        except ValueError:
           print("Favor informar valor numérico, tente novamente.")

        
def right_answer(user_question):
    """
    Pergunta ao usuário uma escolha até que ele digite um valor válido.
    Aceita tanto números quanto textos (ex.: 'dez', '10 reais').
    
    valid_numbers: lista de válidos (ex.: [10, 12, 15])
    valid_texts: dicionário mapeando palavras para números (ex.: {"dez": 10, "doze": 12})
    """
    valid_numbers = [10, 12, 15]
    valid_texts = {
        "dez": 10,
        "doze": 12,
        "quinze": 15
    }
    while True:
        user_choice = input(f"{user_question} \n")
        
        # Normaliza entrada (remove espaços e coloca em minúsculas)
        normalized = user_choice.strip().lower()
        # Procura números dentro da string (ex.: "10 reais")
        number = ''.join([c for c in normalized if c.isdigit()])

            # 1. Verifica se a resposta é numérica 
        try:
            num_choice = float(number)
            if num_choice in valid_numbers:
                print(f"Opção válida escolhida: {num_choice}")
                return num_choice
        except ValueError:
            pass

        # 2. Verifica se contém palavras mapeadas
        for word, value in valid_texts.items():
            if word in normalized:
                print(f"Opção válida escolhida: {float(value)}")
                return float(value)

        print("Opção inválida, tente novamente.")


def calculator(total_bill, tip_amount,people)  :
    result = round(total_bill*(1+ (tip_amount/100))/people, 2)
    return result




def main():
    clear_console()
    print("Bem vindo a calculadora de conta para restaurante!")
    
    total_bill = right_answer_numeric("Qual foi o valor total da conta? ")

    tip_amount = right_answer("Qual o percentual de gorjeta que gostaria de pagar? 10, 12 or 15?")
    people = right_answer_numeric("Quantas pessoas irão dividir a conta? ")

    total_by_person = calculator(total_bill, tip_amount,people)

    print(f"Cada pessoa deverá pagar: R$ {total_by_person}")
    
main()