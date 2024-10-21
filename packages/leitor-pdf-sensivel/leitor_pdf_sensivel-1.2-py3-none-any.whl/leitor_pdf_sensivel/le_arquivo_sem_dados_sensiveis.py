# =============================================================================
# Pacotes
# =============================================================================
import os
import sys
import numpy as np
import pandas as pd
from .elimina_dados_sensiveis import gera_lista_dados_sensiveis,busca_nomes_pessoas,load_pdf_interval,remover_strings,count_pdf_pages

# =============================================================================
# Função Principal
# =============================================================================
def le_arquivo_sem_dados_sensiveis(pdf_path):
    """
    Lê um arquivo PDF, remove informações sensíveis com base em uma lista fornecida e retorna o texto sem esses dados.
    
    Parâmetros:
    -----------
    pdf_path : str
        Caminho para o arquivo PDF a ser processado.

    Retorna:
    --------
    texto_sem_dados_sensiveis : str
        Texto do PDF com as informações sensíveis removidas.

    Exceções:
    ---------
    O código trata exceções relacionadas a:
        - Arquivo PDF não encontrado ou inválido.
        - Problemas ao ler o arquivo Excel 'exames.xlsx'.
        - Erros ao gerar a lista de dados sensíveis ou ao filtrar os dados.
    """
    try:
        # Obter o diretório atual de execução
        current_dir = os.path.dirname(__file__)
    
        # Definir o caminho para o arquivo Excel na pasta 'data'
        local_excel = os.path.join(current_dir, 'data', 'exames.xlsx')
        
        # Contagem do número de páginas no PDF
        num_pdf_pages = count_pdf_pages(pdf_path)
        
        # Geração da lista de dados sensíveis e extração do texto
        lista_dados_sensiveis, texto = gera_lista_dados_sensiveis(pdf_path, num_pdf_pages)
        
        # Leitura do arquivo Excel que contém a lista de exames
        df = pd.read_excel(local_excel, header=0)
        exames = df['Exames'].tolist()
        
        # Filtra a lista de exames, removendo valores nulos
        exames = [valor for valor in exames if valor and not (isinstance(valor, float) and np.isnan(valor))]
        exames = [valor.lower() for valor in exames]
        
        # Filtra a lista de dados sensíveis para remover os exames
        lista_filtrada = [valor for valor in lista_dados_sensiveis if valor not in exames]
        
        # Remove as strings sensíveis do texto
        texto_sem_dados_sensiveis = remover_strings(texto, lista_filtrada)

        # Abrindo (ou criando) o arquivo .txt e escrevendo o conteúdo
        with open("texto_sem_dados_sensiveis.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_sem_dados_sensiveis)

        return texto_sem_dados_sensiveis

    except FileNotFoundError as fnf_error:
        print(f"Erro: Arquivo não encontrado - {fnf_error}")
    except pd.errors.EmptyDataError as ede_error:
        print(f"Erro: O arquivo Excel está vazio ou corrompido - {ede_error}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

#-----------------------------------------------------------------------------#


