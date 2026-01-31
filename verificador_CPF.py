
import re
import sys

entrada_CPF = input("Digite o seu CPF: ")
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada_CPF
)

entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if entrada_e_sequencial:
    print('Você digitou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contagem_regressiva_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contagem_regressiva_1
    contagem_regressiva_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11

digito_1 = digito_1 if digito_1 <=9 else 0

# Cálculo do segundo digito

dez_digitos = nove_digitos + str(digito_1)
contagem_regressiva_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contagem_regressiva_2
    contagem_regressiva_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11

digito_2 = digito_2 if digito_2 <=9 else 0

cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF é inválido. Verifique se digitou corretamente!')


