# Calculadora de Conta para Restaurante

## Descrição

Um programa em Python que calcula quanto cada pessoa deve pagar em uma conta de restaurante, incluindo gorjeta. O programa solicita o valor total da conta, o percentual de gorjeta desejado (10%, 12% ou 15%) e o número de pessoas que vão dividir a despesa.

## Funcionalidades

- **Limpeza de console**: Limpa a tela para melhor legibilidade
- **Validação de entrada numérica**: Garante que o usuário digite valores numéricos válidos
- **Validação com palavras-chave**: Aceita tanto números quanto palavras (ex: "dez", "doze", "quinze")
- **Cálculo de gorjeta**: Calcula automaticamente o valor da gorjeta sobre o total
- **Divisão entre pessoas**: Distribui o valor total (com gorjeta) entre o número de pessoas

## Como usar

1. Execute o programa:
   ```bash
   python main.py
   ```

2. Siga as instruções na tela:
   - Digite o valor total da conta
   - Escolha o percentual de gorjeta (10, 12 ou 15)
   - Digite a quantidade de pessoas dividindo a conta

3. O programa exibirá o valor que cada pessoa deve pagar

## Exemplo de uso

```
Bem vindo a calculadora de conta para restaurante!
Qual foi o valor total da conta?
$ 100
Opção válida escolhida: 15.0
Qual o percentual de gorjeta que gostaria de pagar? 10, 12 or 15?
 
15
Quantas pessoas irão dividir a conta?
 
4
Cada pessoa deverá pagar: $ 28.75
```

## Funções principais

- `clear_console()`: Limpa o console baseado no sistema operacional (Windows/Linux)
- `right_answer_numeric(user_question)`: Valida entrada numérica do usuário
- `right_answer(user_question)`: Valida entrada com números e palavras-chave
- `calculator(total_bill, tip_amount, people)`: Calcula o valor por pessoa com gorjeta
- `main()`: Função principal que coordena o programa

## Requisitos

- Python 3.x

## Notas

- Os percentuais de gorjeta aceitos são: 10%, 12% e 15%
- O programa aceita palavras em português para os percentuais: "dez", "doze" e "quinze"
- Os valores são arredondados para 2 casas decimais
