from datetime import datetime, date, time
import pandas as pd
import os
from CRUD_projetosdb import Projetos

def upper_spaceless_string (string_sujo):

    if isinstance(string_sujo,str) == True:
        if len(string_sujo) == 0:
            string_limpo = None
        elif string_sujo == " ":
            string_limpo = None
        elif string_sujo[0] == " ":
                while string_sujo[0] == " ":
                    string_sujo = string_sujo.replace(string_sujo[0], "", 1)
                try:
                    string_limpo = string_sujo.upper()
                except:
                    print(f"Exception caught: {string_sujo}")
                    string_limpo = None
        else:
            try:
                string_limpo = string_sujo.upper()
            except:
                print(f"Exception caught: {string_sujo}")
                string_limpo = None
    else:
        try:
            string_limpo = str(string_sujo).upper()
        except:
            print(f"Exception caught: {string_sujo}")
            string_limpo = None
    
    return string_limpo

def troca_char (value_char):

    value_char_temp = str(value_char)

    value_char_temp = value_char_temp.replace(".","")
    value_char_temp = value_char_temp.replace(",","")
    value_char_temp = value_char_temp.replace("´","")
    value_char_temp = value_char_temp.replace("`","")
    value_char_temp = value_char_temp.replace("'","")
    value_char_temp = value_char_temp.replace("~","")
    value_char_temp = value_char_temp.replace("]","")
    value_char_temp = value_char_temp.replace("[","")        
    value_char_temp = value_char_temp.replace("  "," ")
    value_char_temp = value_char_temp.replace("Á","A")
    value_char_temp = value_char_temp.replace("À","A")
    value_char_temp = value_char_temp.replace("Â","A")
    value_char_temp = value_char_temp.replace("Ã","A")
    value_char_temp = value_char_temp.replace("Ä","A")
    value_char_temp = value_char_temp.replace("Ç","C")
    value_char_temp = value_char_temp.replace("ª","a.")
    value_char_temp = value_char_temp.replace("º","o.")
    value_char_temp = value_char_temp.replace("É","E")
    value_char_temp = value_char_temp.replace("È","E")
    value_char_temp = value_char_temp.replace("Ë","E")
    value_char_temp = value_char_temp.replace("Ê","E")
    value_char_temp = value_char_temp.replace("Í","I")
    value_char_temp = value_char_temp.replace("Ì","I")
    value_char_temp = value_char_temp.replace("Î","I")
    value_char_temp = value_char_temp.replace("Ï","I")
    value_char_temp = value_char_temp.replace("Ó","O")
    value_char_temp = value_char_temp.replace("Ò","O")
    value_char_temp = value_char_temp.replace("Ô","O")
    value_char_temp = value_char_temp.replace("Õ","O")
    value_char_temp = value_char_temp.replace("Ö","O")
    value_char_temp = value_char_temp.replace("0","O")
    value_char_temp = value_char_temp.replace("Ú","U")
    value_char_temp = value_char_temp.replace("Ù","U")
    value_char_temp = value_char_temp.replace("Û","U")
    value_char_temp = value_char_temp.replace("Ü","U")

    value_char_clean = value_char_temp

    return value_char_clean

def troca_char_CPF (value_char_CPF):

    value_char_CPF = value_char_CPF.replace(".","")
    value_char_CPF = value_char_CPF.replace(",","")
    value_char_CPF = value_char_CPF.replace("´","")
    value_char_CPF = value_char_CPF.replace("`","")
    value_char_CPF = value_char_CPF.replace("'","")
    value_char_CPF = value_char_CPF.replace("~","")
    value_char_CPF = value_char_CPF.replace("-","")
    value_char_CPF = value_char_CPF.replace("]","")
    value_char_CPF = value_char_CPF.replace("[","")
    value_char_CPF = value_char_CPF.replace(" ","")            
    value_char_CPF = value_char_CPF.replace("  ","")

    value_char_CPF_clean = value_char_CPF

    return value_char_CPF_clean  

def troca_erro (value):

    if (value == -4 or value == -3 or value == -1):
        value_clean = None
    elif (value == "#NE" or value == "#NE#" or value == "#NULO" or value == "#NULO#" or value == "NAO DIVULGAVEL" or value == "NAO INFORMADO" or value == "nan"):
        value_clean = None
    else:
        try:
            value_clean = int(value)
        except:
            print(f"Exception caught: {value}")
            value_clean = None

    return value_clean

def troca_erro_data (value_data):

    if (value_data == -4 or value_data == -3 or value_data == -1):
        value_data_clean = None
    elif (value_data == "#NE" or value_data == "#NE#" or value_data == "#NULO" or value_data == "#NULO#" or value_data == "NAO DIVULGAVEL" or value_data == "NAO INFORMADO" or value_data == "" or value_data == "nan"):
        value_data_clean = None
    else:
        try:
            value_data_clean = date(int(value_data.split("/")[2]), int(value_data.split("/")[1]), int(value_data.split("/")[0]))
        except:
            print(f"Exception caught: {value_data}")
            value_data_clean = None

    return value_data_clean

def troca_erro_hora (value_hora):

    if (value_hora == -4 or value_hora == -3 or value_hora == -1):
        value_hora_clean = None
    elif (value_hora == "#NE" or value_hora == "#NE#" or value_hora == "#NULO" or value_hora == "#NULO#" or value_hora == "NAO DIVULGAVEL" or value_hora == "NAO INFORMADO" or value_hora == "" or value_hora == "nan"):
        value_hora_clean = None
    else:
        try:
            value_hora_clean = time(int(value_hora.split(":")[0]), int(value_hora.split(":")[1]), int(value_hora.split(":")[2]))
        except:
            print(f"Exception caught: {value_hora}")
            value_hora_clean = None

    return value_hora_clean

def troca_erro_string (value_string):

    if (value_string == -4 or value_string == -3 or value_string == -1):
        value_string_clean = None
    elif (value_string == "#NE" or value_string == "#NE#" or value_string == "#NULO" or value_string == "#NULO#" or value_string == "NAO DIVULGAVEL" or value_string == "NAO INFORMADO" or value_string == "" or value_string == "nan"):
        value_string_clean = None
    else:
        value_string_temp = troca_char(value_string)
        value_string_temp = upper_spaceless_string(value_string_temp)
        try:
            value_string_clean = str(value_string_temp)
        except:
            print(f"Exception caught: {value_string}")
            value_string_clean = None

    return value_string_clean

def troca_erro_CPF (value_CPF):

    if (value_CPF == -4 or value_CPF == -3 or value_CPF == -1):
        value_CPF_clean = None
    elif (value_CPF == "#NE" or value_CPF == "#NE#" or value_CPF == "#NULO" or value_CPF == "#NULO#" or value_CPF == "NAO DIVULGAVEL" or value_CPF == "NAO INFORMADO" or value_CPF == "" or value_CPF == "nan"):
        value_CPF_clean = None
    else:
        if isinstance(value_CPF, str):
            value_CPF_temp = troca_char_CPF(value_CPF)
        else:
            value_CPF_temp = troca_char_CPF(str(value_CPF))

        if (len(value_CPF_temp) == 9):
            value_CPF_temp = "00" + value_CPF_temp
        elif (len(value_CPF_temp) == 10):
            value_CPF_temp = "0" + value_CPF_temp
        else:
            pass

        if len(value_CPF_temp) !=11:
            value_CPF_clean = None
        else:
            a = int(value_CPF_temp[0])
            b = int(value_CPF_temp[1])
            c = int(value_CPF_temp[2])
            d = int(value_CPF_temp[3])
            e = int(value_CPF_temp[4])
            f = int(value_CPF_temp[5])
            g = int(value_CPF_temp[6])
            h = int(value_CPF_temp[7])
            i = int(value_CPF_temp[8])
            y = int(value_CPF_temp[9])
            z = int(value_CPF_temp[10])

            soma_algarismos1 = (10*a)+(9*b)+(8*c)+(7*d)+(6*e)+(5*f)+(4*g)+(3*h)+(2*i) 
            digito1 = (soma_algarismos1*10)%11
            if (digito1 == 10):
                digito1 = 0

            soma_algarismos2 = (11*a)+(10*b)+(9*c)+(8*d)+(7*e)+(6*f)+(5*g)+(4*h)+(3*i)+(2*digito1) 
            digito2 = (soma_algarismos2*10)%11
            if (digito2 == 10):
                digito2 = 0   

            if (digito1 == y) and (digito2==z):
                value_CPF_clean = value_CPF_temp
            else:
                value_CPF_clean = None

    return value_CPF_clean

def troca_erro_valores (value_valores):                                #troca os valores (em R$) de patrimônio e reserva máxima de campanha
    
    if isinstance(value_valores,int) == True:
        if (value_valores <= 0 ):
            value_valores_clean = None
        else:
            value_valores_clean = value_valores
    elif (value_valores == "#NE" or value_valores == "#NE#" or value_valores == "#NULO" or value_valores == "#NULO#" or value_valores == "NAO DIVULGAVEL" or value_valores == "NAO INFORMADO"  or value_valores == "nan"):
        value_valores_clean = None
    else:
        try:
            value_valores_clean = int(value_valores)
            if (value_valores <= 0 ):
                value_valores_clean = None
        except:
            print(f"Exception caught: {value_valores}")
            value_valores_clean = None

    return value_valores_clean

def excel_to_projetosdb(filename):
    
    print(f"Importando dados da eleição de {filename.split("_")[3]}.")

    with open(filename, 'r', encoding='latin-1') as filename:
        df = pd.read_csv(filename, sep = ';', encoding='latin-1')
        df['ts_inputdata'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    df_clean = pd.DataFrame()

    #*Corrige os erros mais comuns no dataframe
    #df_clean[''] = df[''].apply()
    df_clean['DT_GERACAO'] = df['DT_GERACAO'].apply(troca_erro_data)
    df_clean['HH_GERACAO'] = df['HH_GERACAO'].apply(troca_erro_hora)
    df_clean['ANO_ELEICAO'] = df['ANO_ELEICAO'].apply(troca_erro)
    df_clean['CD_TIPO_ELEICAO'] = df['CD_TIPO_ELEICAO'].apply(troca_erro)
    df_clean['NM_TIPO_ELEICAO'] = df['NM_TIPO_ELEICAO'].apply(troca_erro_string)
    df_clean['NR_TURNO'] = df['NR_TURNO'].apply(troca_erro)
    df_clean['CD_ELEICAO'] = df['CD_ELEICAO'].apply(troca_erro)
    df_clean['DS_ELEICAO'] = df['DS_ELEICAO'].apply(troca_erro_string)
    df_clean['DT_ELEICAO'] = df['DT_ELEICAO'].apply(troca_erro_data)
    df_clean['TP_ABRANGENCIA'] = df['TP_ABRANGENCIA'].apply(troca_erro_string)
    df_clean['SG_UF'] = df['SG_UF'].apply(troca_erro_string)
    df_clean['SG_UE'] = df['SG_UE'].apply(troca_erro_string)
    df_clean['NM_UE'] = df['NM_UE'].apply(troca_erro_string)
    df_clean['CD_CARGO'] = df['CD_CARGO'].apply(troca_erro)
    df_clean['DS_CARGO'] = df['DS_CARGO'].apply(troca_erro_string)
    df_clean['SQ_CANDIDATO'] = df['SQ_CANDIDATO'].apply(troca_erro_string) #int tratado como str para fins de id
    df_clean['NR_CANDIDATO'] = df['NR_CANDIDATO'].apply(troca_erro)
    df_clean['NM_CANDIDATO'] = df['NM_CANDIDATO'].apply(troca_erro_string)
    df_clean['NM_URNA_CANDIDATO'] = df['NM_URNA_CANDIDATO'].apply(troca_erro_string)
    df_clean['NM_SOCIAL_CANDIDATO'] = df['NM_SOCIAL_CANDIDATO'].apply(troca_erro_string)
    df_clean['NR_CPF_CANDIDATO'] = df['NR_CPF_CANDIDATO'].apply(troca_erro_CPF)
    df_clean['NM_EMAIL'] = df['NM_EMAIL'].apply(troca_erro_string)
    df_clean['CD_SITUACAO_CANDIDATURA'] = df['CD_SITUACAO_CANDIDATURA'].apply(troca_erro)
    df_clean['DS_SITUACAO_CANDIDATURA'] = df['DS_SITUACAO_CANDIDATURA'].apply(troca_erro_string)
    df_clean['CD_DETALHE_SITUACAO_CAND'] = df['CD_DETALHE_SITUACAO_CAND'].apply(troca_erro)
    df_clean['DS_DETALHE_SITUACAO_CAND'] = df['DS_DETALHE_SITUACAO_CAND'].apply(troca_erro_string)
    df_clean['TP_AGREMIACAO'] = df['TP_AGREMIACAO'].apply(troca_erro_string)
    df_clean['NR_PARTIDO'] = df['NR_PARTIDO'].apply(troca_erro)
    df_clean['SG_PARTIDO'] = df['SG_PARTIDO'].apply(troca_erro_string)
    df_clean['NM_PARTIDO'] = df['NM_PARTIDO'].apply(troca_erro_string)
    df_clean['SQ_COLIGACAO'] = df['SQ_COLIGACAO'].apply(troca_erro)
    df_clean['NM_COLIGACAO'] = df['NM_COLIGACAO'].apply(troca_erro_string)
    df_clean['DS_COMPOSICAO_COLIGACAO'] = df['DS_COMPOSICAO_COLIGACAO'].apply(troca_erro_string)
    df_clean['CD_NACIONALIDADE'] = df['CD_NACIONALIDADE'].apply(troca_erro)
    df_clean['DS_NACIONALIDADE'] = df['DS_NACIONALIDADE'].apply(troca_erro_string)
    df_clean['SG_UF_NASCIMENTO'] = df['SG_UF_NASCIMENTO'].apply(troca_erro_string)
    df_clean['CD_MUNICIPIO_NASCIMENTO'] = df['CD_MUNICIPIO_NASCIMENTO'].apply(troca_erro)
    df_clean['NM_MUNICIPIO_NASCIMENTO'] = df['NM_MUNICIPIO_NASCIMENTO'].apply(troca_erro_string)
    df_clean['DT_NASCIMENTO'] = df['DT_NASCIMENTO'].apply(troca_erro_data)
    df_clean['NR_IDADE_DATA_POSSE'] = df['NR_IDADE_DATA_POSSE'].apply(troca_erro)
    df_clean['NR_TITULO_ELEITORAL_CANDIDATO'] = df['NR_TITULO_ELEITORAL_CANDIDATO'].apply(troca_erro_string)
    df_clean['CD_GENERO'] = df['CD_GENERO'].apply(troca_erro)
    df_clean['DS_GENERO'] = df['DS_GENERO'].apply(troca_erro_string)
    df_clean['CD_GRAU_INSTRUCAO'] = df['CD_GRAU_INSTRUCAO'].apply(troca_erro)
    df_clean['DS_GRAU_INSTRUCAO'] = df['DS_GRAU_INSTRUCAO'].apply(troca_erro_string)
    df_clean['CD_ESTADO_CIVIL'] = df['CD_ESTADO_CIVIL'].apply(troca_erro)
    df_clean['DS_ESTADO_CIVIL'] = df['DS_ESTADO_CIVIL'].apply(troca_erro_string)
    df_clean['CD_COR_RACA'] = df['CD_COR_RACA'].apply(troca_erro)
    df_clean['DS_COR_RACA'] = df['DS_COR_RACA'].apply(troca_erro_string)
    df_clean['CD_OCUPACAO'] = df['CD_OCUPACAO'].apply(troca_erro)
    df_clean['DS_OCUPACAO'] = df['DS_OCUPACAO'].apply(troca_erro_string)
    df_clean['VR_DESPESA_MAX_CAMPANHA'] = df['VR_DESPESA_MAX_CAMPANHA'].apply(troca_erro_valores)
    df_clean['CD_SIT_TOT_TURNO'] = df['CD_SIT_TOT_TURNO'].apply(troca_erro)
    df_clean['DS_SIT_TOT_TURNO'] = df['DS_SIT_TOT_TURNO'].apply(troca_erro_string)
    df_clean['ST_REELEICAO'] = df['ST_REELEICAO'].apply(troca_erro_string) #? conferir aplicabilidade ?
    df_clean['ST_DECLARAR_BENS'] = df['ST_DECLARAR_BENS'].apply(troca_erro_string)
    df_clean['NR_PROTOCOLO_CANDIDATURA'] = df['NR_PROTOCOLO_CANDIDATURA'].apply(troca_erro_string) #int tratado como str para fins de id
    df_clean['NR_PROCESSO'] = df['NR_PROCESSO'].apply(troca_erro_string) #int tratado como str para fins de id
    df_clean['CD_SITUACAO_CANDIDATO_PLEITO'] = df['CD_SITUACAO_CANDIDATO_PLEITO'].apply(troca_erro)
    df_clean['DS_SITUACAO_CANDIDATO_PLEITO'] = df['DS_SITUACAO_CANDIDATO_PLEITO'].apply(troca_erro_string)
    df_clean['CD_SITUACAO_CANDIDATO_URNA'] = df['CD_SITUACAO_CANDIDATO_URNA'].apply(troca_erro)
    df_clean['DS_SITUACAO_CANDIDATO_URNA'] = df['DS_SITUACAO_CANDIDATO_URNA'].apply(troca_erro_string)
    df_clean['ST_CANDIDATO_INSERIDO_URNA'] = df['ST_CANDIDATO_INSERIDO_URNA'].apply(troca_erro_string)

    #*Corrige erros das colunas que não são comuns a todos os dataframes
    if 'NM_TIPO_DESTINACAO_VOTOS' in df.columns:
        df_clean['NM_TIPO_DESTINACAO_VOTOS'] = df['NM_TIPO_DESTINACAO_VOTOS'].apply(troca_erro_string)
    else:
        df_clean['NM_TIPO_DESTINACAO_VOTOS'] = None

    if 'CD_SITUACAO_CANDIDATO_TOT' in df.columns:
        df_clean['CD_SITUACAO_CANDIDATO_TOT'] = df['CD_SITUACAO_CANDIDATO_TOTS'].apply(troca_erro)
    else:
        df_clean['CD_SITUACAO_CANDIDATO_TOT'] = None
    
    if 'DS_SITUACAO_CANDIDATO_TOT' in df.columns:
        df_clean['DS_SITUACAO_CANDIDATO_TOT'] = df['DS_SITUACAO_CANDIDATO_TOTS'].apply(troca_erro_string)
    else:
        df_clean['DS_SITUACAO_CANDIDATO_TOT'] = None

    if 'ST_PREST_CONTAS' in df.columns:
        df_clean['ST_PREST_CONTAS'] = df['ST_PREST_CONTAS'].apply(troca_erro_string)
    else:
        df_clean['ST_PREST_CONTAS'] = None

    if 'ST_SUBSTITUIDO' in df.columns:
        df_clean['ST_SUBSTITUIDO'] = df['ST_SUBSTITUIDO'].apply(troca_erro_string)
    else:
        df_clean['ST_SUBSTITUIDO'] = None

    if 'ST_SUBSTITUIDO' in df.columns:
        df_clean['SQ_SUBSTITUIDO'] = df['SQ_SUBSTITUIDO'].apply(troca_erro_string)
    else:
        df_clean['SQ_SUBSTITUIDO'] = None

    if 'SQ_ORDEM_SUPLENCIA' in df.columns:
        df_clean['SQ_ORDEM_SUPLENCIA'] = df['SQ_ORDEM_SUPLENCIA'].apply(troca_erro_string)
    else:
        df_clean['SQ_ORDEM_SUPLENCIA'] = None

    if 'DT_ACEITE_CANDIDATURA' in df.columns:
        df_clean['DT_ACEITE_CANDIDATURA'] = df['DT_ACEITE_CANDIDATURA'].apply(troca_erro_string)
    else:
        df_clean['DT_ACEITE_CANDIDATURA'] = None
    
    projetos = Projetos()
    getattr(projetos, "insert_df")("tb_projetos_candidatos_clean", df_clean)

    return 

def reune_tabelas():
#**FUNÇÃO COLETA PLANILHAS NA PASTA DE ORIGEM E CHAMA INSCRIÇÃO NA DB**#

    path = r".\\repositorio\\consulta_cand\\"

    for filename in os.listdir(path):
        if filename.endswith(".csv"):
            filename_fullpath = os.path.join(path, filename)
            excel_to_projetosdb(filename_fullpath)

def main():
    reune_tabelas()
    #fuzzy_names()

if __name__ == "__main__":
    main()
