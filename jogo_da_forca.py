# EXERCÍCIOS:	JOGO	DA	FORCA 
def verifica_letra(letra):  # verificar se existe na palavra secreta
    if len(letra) > 1:
        return print('INVALIDO DIGITE APENAS UMA LETRA')
    if letra not in palavra_secreta.upper():
        return False
    else:
        return True


def nao_tem_letra():  # caso não tenha a letra na palavra secreta
    print(f'A letra {letra} não está na palavra secreta')
    letras_erradas.append(letra)
    print(f'Letras digitadas erradas: {letras_erradas}')
    return


def tem_letra(palavra_secreta, palavra_certa, letra):  # caso exista  a letra na palavra secreta
    qtde_letra = palavra_secreta.count(letra)
    procura=0
    for i in range(0, qtde_letra):
        posicao = palavra_secreta.index(letra,procura)
        palavra_certa.pop(posicao)
        palavra_certa.insert(posicao,letra)
        procura = posicao+1

    pass


print('*' * 40)
print(f'{" BEM VINDO AO JOGO DA FORCA ":*^40}')
print('*' * 40)

palavra_secreta = ('Carambola')
palavra_secreta = palavra_secreta.upper()
print(palavra_secreta)
palavra_certa = ['__' for x in range(0, len(palavra_secreta))]
letras_erradas = []
tentativa = 5


while True:
    if ''.join(palavra_certa) == palavra_secreta:
        print(f'Parabéns você acertou! A palavra secreta é {"".join(palavra_certa)}')
        break

    print('_' * 60)
    print(f'Você tem apenas {tentativa} tentativas.')
    print(f'Palavra secreta : {palavra_certa}')

    letra = str(input('Digite uma letra: ')).strip().upper()

    if letra in letras_erradas or letra in palavra_certa:
        print(f'Você ja digitou a letra {letra} ')
        continue
    if verifica_letra(letra) is False:
        nao_tem_letra()
        tentativa -= 1
        if tentativa == 0:
            print('_' * 60)
            print('FIM de JOGO - Acabaram suas tentativas\n'
                  f'A palavra secreta era {palavra_secreta}')
            break

    else:
        tem_letra(palavra_secreta, palavra_certa, letra)
