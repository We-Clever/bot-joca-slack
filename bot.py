import slack
import os 
from dotenv import load_dotenv
from pathlib import Path
import ezsheets
import pandas as pd
from thefuzz import fuzz
from thefuzz import process

# add to a loop
def write_on_cell(m,time_n,conversation_history,n_row):
    a = ezsheets.Spreadsheet('1_PiEQF3ugQ3h_-XvrKO_9ACeQiIAD1SWZ-RS73uyYlI')
    ss = a[0]

    df = pd.DataFrame(ss)
    a = df.index[df[0] == ''].tolist()
    c = df.index[df[1] == ''].tolist()
    b = a[n_row]
    d = c[n_row]
    # add to the right columns
    column = ['B','E','A']
    nome = column[0] + str(d)
    mensagem = column[1] + str(b)
    data = column[2] + str(d)

    ss[nome] = m['real_name']
    
    all_cases = [
                'excluir id',
                'eviar csat',
                'Zap Guru não está enviando as mensagens',
                'Adicionar número de telefone no ID',
                'Excluir conversão',
                'Excluir recusa',
                'Excluir lead',
                'NPS não envia',
                'Comissão no painel',
                'Alterar informações do Lead',
                'Tempo de espera na ligação',
                'Problemas para chamar no Whatsapp',
                'Filtro no dash não carrega',
                'VPN não está conectando',
                'Tabulação duplicada',
                'Colocar ID na agenda',
                'Redefinir senha',
                'VPn não abre',
                'Problema no dashboard']
    choice = process.extractOne(conversation_history['text'], all_cases)
    print('Opcao ?\n ' + choice[0])
    opc = str(input('y/n >>>'))
    ss[data] = time_n
    if (opc == 'y'):
        new_line = str(input('nova opcao >>>'))
        ss[mensagem] = new_line
    elif (opc == 'n'):
        ss[mensagem] = choice[0]
