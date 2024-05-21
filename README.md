# renovacao-politica

INTRODUÇÃO

Módulos em python que calculam o número e a proporção de candidatos novos, candidatos que já disputaram uma eleição e candidatos à reeleição para cada uma das eleições (municipais e geral) realizadas no Brasil. Para isso, os scripts compõem um banco de dados de candidatos e eleitos a partir dos dados abertos disponibilizados pelo TSE.

Os dados são extraídos manualmente do Portal de Dados Abertos do TSE, tratados por meio de um script Python e inscritos em um gerenciador de banco de dados PostgreSQL previamente configurado para armazenamento e análise.

O objetivo é avaliar a taxa de sucesso de políticos segundo demografias observáveis de gênero, etnia, idade e um parâmetro não-observável de experiência eleitoral - avaliado por meio de proxies de números de eleições disputadas e mandatos. 

Uma vez que a coleta dos dados eleitorais é feita de forma descentralizada - por meio dos Tribunais Regionais Eleitorais (TREs) ou em algumas ocasiões por cartórios eleitorais - a maior parte do tempo de processamento é destinada à limpeza e tratamento dos dados. Especificamente, à padronização dos missings values (NAs) e à substituição de caracteres inválidos. Ao todo, os dados consolidados ocupam 1,7 GB de memória.

Este levantamento deu origem a diversas reportagens e matérias publicadas na impresa pelo Broadcast+, serviço de notícias em tempo real da Agência Estado. As principais contribuições e relatórios podem ser encontrados neste git no diretório ".//repercussao//"

ORIENTAÇÕES

Os arquivos com sufixo [ANO]_BRASIL.csv já reúnem os dados de todos os Estados em um repositório nacional. Caso prefira, é possível fazer a importação estadualizada de cada um dos outros arquivos, entretanto o processo é ainda mais demorado.

O gerenciador de banco de dados foi previamente configurado. As informações de acesso utilizadas para acesso à database podem ser substituídas no arquivo config.json.

Alguns arquivos de exemplo - referentes às Eleições Gerais a partir de 2000 - foram disponibilizados por serem mais leves. Os arquivos referentes às Eleições Municipais podem ser de 20 a 30 vezes maiores do que os das Eleições Gerais.

COMO FUNCIONA

1. O script ".//csv_to_eleicoesdb.py" lê cada um dos arquivos em formato .csv disponíveis no caminho ".//repositorio//consulta_cand//" que foram previamente baixados do Portal de Dados Abertos do TSE.

2. Para cara coluna da tabela selecionada, o script aplica o tratamento adequado e a concatena ao dataframe limpo.

3. O script apensa o dataframe limpo ao servidor local para consulta e queries.

4. A função fuzzy_names lê os dados inseridos e trata possíveis individuos igauis a partir da semelhança entre nome, CPF, data e local de nascimento.
