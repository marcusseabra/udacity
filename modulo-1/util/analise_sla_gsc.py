import os
import re
import csv
from datetime import datetime

DATADIR='/home/seabra/dev/udacity/modulo-1/util/Indicadores/'
DATADIR_DESTINO='/home/seabra/dev/udacity/modulo-1/'

ARQUIVO_TRANSICAO_RMS = "IND - Transicao RMs.csv"
ARQUIVO_RESPONSAVEIS_RMS = "IND - Responsaveis.csv"

def leitura_transicao():
    transicoes_rms = []

    with open(os.path.join(DATADIR, ARQUIVO_TRANSICAO_RMS), 'rt') as arquivo_csv:
        reader = csv.DictReader(arquivo_csv, delimiter = ';')
        for linhas in reader:
            transicoes_rms.append(linhas)

    arquivo_csv.close()
    return transicoes_rms

#    for rm in transicoes_rms:
#        if rm['rm'] == "13593":
#            print("Situacao Atual: " + rm['situacao'] + " - Transicao: " + rm['data_transicao'])

def definicao_responsaveis():
    transicoes_rms = leitura_transicao()
    responsaveis_rms = []

    with open(os.path.join(DATADIR, ARQUIVO_RESPONSAVEIS_RMS), 'rt') as arquivo_csv:
        reader = csv.DictReader(arquivo_csv, delimiter = ';')
        for linhas in reader:
            responsaveis_rms.append(linhas)

    arquivo_csv.close()

    for transicoes in transicoes_rms:
        dataHoraTransicao = datetime.strptime(transicoes['data_transicao'], "%Y-%m-%d %H:%M:%S")
        if transicoes['rm'] == "13593":
            for responsaveis in responsaveis_rms:
                if responsaveis['rm'] == transicoes['rm']:
                    dataHoraResponsavel = datetime.strptime(responsaveis['data_atribuicao'], "%Y-%m-%d %H:%M:%S")
                    if dataHoraTransicao < dataHoraResponsavel:
                        print(transicoes['situacao_anterior']
                                + " - "
                                + responsaveis['responsavel']
                                + " - "
                                + responsaveis['data_atribuicao'])
                    elif dataHoraResponsavel == dataHoraTransicao:
                        print(transicoes['situacao']
                                + " - "
                                + responsaveis['responsavel']
                                + " - "
                                + responsaveis['data_atribuicao'])

definicao_responsaveis()
