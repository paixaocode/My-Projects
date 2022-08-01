# Importo as bibliotecas
from itertools import count
from turtle import end_fill
from unittest import result
import pywhatkit as kt
import os
import logging

#Gabriel Meira Paixão

def contador_arquivo():

    countarquivo = 0
    dir = "DIRETÓRIO DA SUA PASTA NO ONEDRIVE OU SHAREPOINT (OBS: APENAS DIRETÓRIO LOCAL) O PROGRAMA NÃO ACEITA DIRETÓRIO WEB"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            countarquivo += 1
            qtd_arquivo = countarquivo
            str(qtd_arquivo)
            
#Crio um novo arquivo com a quantidade atualizada
        with open(dir_txt, 'w', encoding='utf-8') as my_file:
            my_list = [str(qtd_arquivo)]
            my_file.write(','.join(my_list))
            my_file.close()

       
def envia_msg(compara_sharepoint,compara_txt):

    result = int(compara_sharepoint) - int(compara_txt)
    kt.sendwhatmsg_to_group_instantly("COLOQUE AQUI O ID DO GRUPO DO WHATSAPP!", "Ola!, foi incluso " + str(result) + " arquivo(s)" 
    " na pasta (NOME DA PASTA QUE TEM OS ARQUIVOS OU DOCUMENTOS!) verifique assim que possivel!"
    " caso queira acessar por aqui, basta clicar no link: encurtador.com.br/elrvF")
    ##CASO NÃO QUEIRA ENVIAR A MENSAGEM EM UM GRUPO, E SIM PARA UM OU MAIS NUMEROS, BASTA VERIFICAR A DOCUMENTAÇÃO DO PYWHATKIT
    

def ler_txt():
    
# Função que le o arquivo TXT e o Sharepoint e verifica se o Sharepoint é maior que TXT    
    with open(dir_txt, 'r') as my_file:
        resultado_arquivo01 = my_file.read()
        print("A quantidade de arquivos no TXT e: " + str(resultado_arquivo01))
        print("A quantidade de arquivos no Sharepoint e: " + str(qtd_arquivo))
        my_file.close()

        #Verifico se o que tem no sharepoint é igual o TXT
        compara_sharepoint = int(qtd_arquivo)
        compara_txt = int(resultado_arquivo01)

        if compara_sharepoint > compara_txt:
            print("A quantidade no Sharepoint esta maior do que a do arquivo de verificacao! A mensagem no whatsapp sera enviada"
            " e o arquivo sera atualizado!")
            contador_arquivo()
            envia_msg(compara_sharepoint , compara_txt)
        elif compara_sharepoint < compara_txt:
            print("A quantidade que esta no arquivo TXT e maior do que a quantidade existente no Sharepoint! Um novo arquivo sera criado"
            " e atualizado, com a quantidade correta!")
            contador_arquivo()
        else:
            print("A quantidade de arquivo no Sharepoint e igual ao arquivo de verificacao, nenhuma acao sera tomada!")
        

# Conto quantos arquivos tem na pasta no Sharepoint
countarquivo = 0
dir = "DIRETÓRIO DA SUA PASTA NO ONEDRIVE OU SHAREPOINT (OBS: APENAS DIRETÓRIO LOCAL) O PROGRAMA NÃO ACEITA DIRETÓRIO WEB"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        countarquivo += 1
        qtd_arquivo = countarquivo

# Verifico se existe o arquivo TXT no diretório
    dir_txt = "C:/verificacao_sharepoint.txt" ## AQUI VOCÊ PODE COLOCAR OUTRO DIRETÓRIO PARA CRIAR O ARQUIVO TXT.
if os.path.isfile(dir_txt):
    print("O arquivo esta localizado no diretorio: " + dir_txt)
    ler_txt()
else:
    # Se não existir o arquivo eu crio ele com a quantidade atualizada
    with open(dir_txt, 'w', encoding='utf-8') as my_file:
        my_list = [str(qtd_arquivo)]
        my_file.write(','.join(my_list))
        my_file.close()

