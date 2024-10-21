"""
Sistema de Abertura e Sanitização de PDFs

Este sistema processa arquivos PDF, removendo informações sensíveis de seu conteúdo.
O objetivo é garantir a proteção de dados confidenciais, atendendo a requisitos de segurança e privacidade.

Funcionalidades:
    - Abertura de arquivos PDF.
    - Extração de texto dos PDFs.
    - Identificação de dados sensíveis como nomes, CPFs, senhas, entre outros.
    - Substituição ou remoção de dados confidenciais das strings extraídas.
    - Salvamento do conteúdo sanitizado em novos arquivos PDF ou formatos alternativos.

Requisitos:
    - Bibliotecas necessárias: PyPDF2 ou outras para manipulação de PDFs.
    - Regex ou métodos de identificação de dados sensíveis.
    - Tratamento de erros para arquivos corrompidos ou com permissões restritas.
"""

# =============================================================================
# Pacotes
# =============================================================================
import re
import spacy
import unicodedata
import pandas as pd
from pypdf import PdfReader

# =============================================================================
# Função
# =============================================================================
#-----------------------------------------------------------------------------#
# Função 1
def load_pdf_interval(file_path, start_page=None, end_page=None):
    """
    Reads the text content from a range of pages in a PDF file and returns it as a single string.
    
    Parameters:
    - file_path (str): The file path to the PDF file.
    - start_page (int, optional): The starting page number of the range (inclusive). If None, starts from the first page.
    - end_page (int, optional): The ending page number of the range (inclusive). If None, ends at the last page.
    
    Returns:
    - str: The concatenated text content of the specified range of pages in the PDF.
    
    Raises:
    - FileNotFoundError: If the specified file_path does not exist.
    - PyPDF2.utils.PdfReadError: If the PDF file is encrypted or malformed.
    - IndexError: If the start_page or end_page is out of range or if start_page is greater than end_page.
    """
    try:
        reader = PdfReader(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the PDF file: {e}")
    
    text = ""
    
    total_pages = len(reader.pages)
    
    if start_page is not None and (start_page < 1 or start_page > total_pages):
        raise IndexError("Start page number is out of range")
    
    if end_page is not None and (end_page < 1 or end_page > total_pages):
        raise IndexError("End page number is out of range")
    
    if start_page is not None and end_page is not None:
        if start_page > end_page:
            raise IndexError("Start page number cannot be greater than end page number")
        
        for i in range(start_page - 1, end_page):
            try:
                text += reader.pages[i].extract_text() or ""
            except Exception as e:
                print(f"An error occurred while extracting text from page {i + 1}: {e}")
    
    else:
        for i in range(total_pages):
            try:
                text += reader.pages[i].extract_text() or ""
            except Exception as e:
                print(f"An error occurred while extracting text from page {i + 1}: {e}")
    
    return text

#-----------------------------------------------------------------------------#
# Função 2
def busca_nomes_pessoas(string_exame):
    """
    Extrai nomes de pessoas e localizações de um texto usando reconhecimento de entidades nomeadas (NER) com Spacy.

    A função processa o texto fornecido em `string_exame`, utilizando o modelo de linguagem Spacy em português 
    (`pt_core_news_lg`), e busca por entidades do tipo pessoa ('PER') e localizações ('LOC'). 
    As entidades reconhecidas são retornadas em duas listas separadas: uma contendo os nomes de pessoas e outra contendo
    as localizações.

    Parâmetros:
    -----------
    string_exame : str
        O texto que será processado para extração de entidades nomeadas.

    Retorna:
    --------
    tuple : (list, list)
        Uma tupla contendo duas listas:
        - lista_pessoa: lista de nomes de pessoas encontrados no texto.
        - lista_localizacao: lista de localizações encontrados no texto.

    Exceção:
    --------
    Em caso de erro durante o processamento, a função captura a exceção e imprime uma mensagem de erro,
    retornando `None`.

    Exemplo de uso:
    ---------------
    >>> texto = "Maria foi a São Paulo visitar João."
    >>> busca_nomes_pessoas(texto)
    (['maria', 'joão'], ['são paulo'])
    """
    try:
        # Inicializa uma lista vazia para armazenar as entidades
        lista_pessoa = []
        lista_localizacao = []
        # Carrega Spacy
        nlp = spacy.load("pt_core_news_lg")
        # Coloca texto em minúscula
        text = string_exame.lower()
        # Processa o texto
        doc = nlp(text)
        # Itera sobre as entidades reconhecidas e adiciona à lista
        for ent in doc.ents:
            if ent.label_ == 'PER':
                lista_pessoa.append(ent.text)
            elif ent.label_ == 'LOC':
                lista_localizacao.append(ent.text)
            else:
                pass
        return lista_pessoa, lista_localizacao
    except Exception as e:
        print(f"Ocorreu um erro na função encontra_dados_sensiveis: {e}")
        return None

#-----------------------------------------------------------------------------#    
# Função 3
def encontrar_cpfs(texto):
    """
    Encontra todos os CPFs no formato ###.###.###-## ou 11 dígitos contínuos em uma string e retorna uma lista.
    
    Args:
        texto (str): A string onde serão procurados os CPFs.
    
    Returns:
        list: Lista de CPFs encontrados.
    """
    # Expressão regular para CPF (###.###.###-## ou 11 dígitos contínuos)
    padrao_cpf = r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b'
    
    # Encontra todos os CPFs no texto
    cpfs_encontrados = re.findall(padrao_cpf, texto)
    
    return cpfs_encontrados

#-----------------------------------------------------------------------------#    
# Função 4
def encontrar_rgs(texto):
    """
    Encontra todos os RGs no formato XX.XXX.XXX-X ou 8 a 9 dígitos contínuos em uma string e retorna uma lista.
    
    Args:
        texto (str): A string onde serão procurados os RGs.
    
    Returns:
        list: Lista de RGs encontrados.
    """
    # Expressão regular para RG (XX.XXX.XXX-X ou 8 a 9 dígitos contínuos)
    padrao_rg = r'\b\d{2}\.?\d{3}\.?\d{3}-?\d?\b'
    
    # Encontra todos os RGs no texto
    rgs_encontrados = re.findall(padrao_rg, texto)
    
    return rgs_encontrados

#-----------------------------------------------------------------------------#    
# Função 5
def encontrar_datas(texto):
    """
    Encontra e retorna todas as datas no formato dd/mm/yyyy, dd-mm-yyyy, dd.mm.yyyy ou 
    no formato textual como '5 de maio de 2021' dentro de uma string fornecida.

    Parâmetros:
    texto (str): O texto em que as datas serão procuradas.

    Retorna:
    list: Uma lista de strings contendo todas as datas encontradas no texto.
    """
    # Padrão regex para datas (dd/mm/yyyy, dd-mm-yyyy, dd.mm.yyyy, "5 de maio de 2021")
    padrao_datas = r"\b(?:\d{1,2}[\/\-.]\d{1,2}[\/\-.]\d{4}|\d{1,2}\sde\s[a-zA-Z]+\sde\s\d{4})\b"
    
    # Encontrar todas as datas no texto
    datas_encontradas = re.findall(padrao_datas, texto)
    
    return datas_encontradas

#-----------------------------------------------------------------------------#    
# Função 6
def encontrar_generos(texto):
    """
    Encontra e retorna as palavras 'masculino' e 'feminino' em uma string, 
    independentemente de estarem em caixa alta ou baixa.

    Parâmetros:
    texto (str): O texto em que as palavras serão procuradas.

    Retorna:
    list: Uma lista contendo as palavras 'masculino' e 'feminino' encontradas no texto.
    """
    # Padrão regex para encontrar 'masculino' ou 'feminino' (case insensitive)
    padrao_generos = r"\b(masculino|feminino)\b"
    
    # Encontrar todas as ocorrências no texto (case insensitive)
    generos_encontrados = re.findall(padrao_generos, texto, re.IGNORECASE)
    
    return generos_encontrados

#-----------------------------------------------------------------------------#  
# Função 7
def gera_lista_dados_sensiveis(file,end_page):
    """
    Gera uma lista de dados sensíveis extraídos de um arquivo PDF, incluindo nomes, RGs, CPFs, e outros dados, usando modelos de NER e QA.
    
    Esta função carrega a primeira página de um PDF, identifica nomes de pessoas, e busca outros dados sensíveis como RG, CPF,
    número de protocolo e outras informações. Os resultados são concatenados em uma lista.
    
    Args:
        file (str): Caminho do arquivo PDF de onde serão extraídos os dados sensíveis.
        diretorio_modelo_ner (str): Caminho para o modelo de reconhecimento de entidades nomeadas (NER) usado para identificar nomes de pessoas.
        diretorio_modelo (str): Caminho para o modelo de question-answering (QA) usado para buscar outros dados sensíveis.
        text (str): Texto extraído da primeira página do PDF.
        processamento (int): ID do dispositivo de processamento (ex.: `-1` para CPU, `0` para GPU).
        temperatura (float): Valor de temperatura para ajustar o modelo de QA.
    
    Returns:
        list: Lista contendo os nomes, dados sensíveis encontrados (CPF, RG, etc.) e informações extraídas do PDF.
    
    Raises:
        Exception: Captura qualquer exceção que ocorra durante o processamento e retorna uma mensagem de erro, mantendo a função robusta.
    """
    try:
        # Carrega a primeira página
        text = load_pdf_interval(file_path=file, start_page=1, end_page=end_page)
        # Converte em minúscula
        text = text.lower()
        # Busca nomes
        lista_pessoa, lista_localizacao = busca_nomes_pessoas(text)
        # Encontra RG
        rgs = encontrar_rgs(text)
        # Encontra CPF
        cpfs = encontrar_cpfs(text)
        # Encontra genero
        genero = encontrar_generos(text)
        # Encontra CPF
        data = encontrar_datas(text)
        # Encontra nomes de estados
        estados_br = detectar_estados(text)
        # Encontra CRM ou OAB
        crm_oab = detectar_crm_oab(text)
        # Números de telefone
        phone = detectar_numeros_telefone(text)
        # Concatena resultado
        resultado = lista_pessoa+lista_localizacao+rgs+cpfs+genero+data+estados_br+crm_oab+phone
        # Guarda texto
        texto = text
        
        return resultado, texto
    
    except Exception as e:
        print(f"Ocorreu um erro na função gera_lista_dados_sensiveis: {e}")
        return None
    
#-----------------------------------------------------------------------------#  
# Função 8
def count_pdf_pages(file_path):
    """
    Counts the number of pages in a PDF file.

    Parameters:
    - file_path (str): The file path to the PDF file.

    Returns:
    - int: The number of pages in the PDF.

    Raises:
    - FileNotFoundError: If the specified file_path does not exist.
    - PyPDF2.utils.PdfReadError: If the PDF file is encrypted or malformed.

    Example:
    >>> num_pages = count_pdf_pages("example.pdf")
    >>> print(num_pages)
    10
    """
    reader = PdfReader(file_path)
    return len(reader.pages)

#-----------------------------------------------------------------------------#  
# Função 9
def remover_strings(texto, lista_strings):
    """
    Remove todas as strings especificadas em uma lista de um texto.

    Args:
        texto (str): O texto do qual as strings serão removidas.
        lista_strings (list): Uma lista de strings a serem removidas do texto.

    Returns:
        str: O texto resultante após a remoção das strings da lista.
    
    Example:
        >>> texto = "Este é um exemplo de texto com algumas palavras."
        >>> lista_strings = ["exemplo", "palavras"]
        >>> resultado = remover_strings(texto, lista_strings)
        >>> print(resultado)
        "Este é um  de texto com algumas ."
    """
    for string in lista_strings:
        texto = texto.replace(string, "")
    return texto

#-----------------------------------------------------------------------------#  
# Função 10
def detectar_estados(texto):
    """
    Detecta os nomes dos estados brasileiros em uma string, ignorando acentos.

    Esta função busca por nomes completos de estados brasileiros em um texto fornecido,
    ignora a presença de acentos e retorna uma lista de estados encontrados, sem duplicatas
    e em letras minúsculas.
    
    Parâmetros:
    texto (str): Uma string contendo o texto onde os nomes dos estados serão procurados.
    
    Retorna:
    list: Uma lista com os nomes dos estados brasileiros encontrados no texto.
          A lista não contém duplicatas e os nomes são retornados em letras minúsculas.

    Exemplo:
    >>> detectar_estados("Eu já visitei São Paulo, Rio de Janeiro e Bahia.")
    ['sao paulo', 'rio de janeiro', 'bahia']
    """
    
    # Lista com os nomes dos estados brasileiros em minúsculas e sem acentos
    estados_brasileiros = [
        "acre", "alagoas", "amapa", "amazonas", "bahia", "ceara", "distrito federal", "espirito santo",
        "goias", "maranhao", "mato grosso", "mato grosso do sul", "minas gerais", "para", "paraiba", 
        "parana", "pernambuco", "piaui", "rio de janeiro", "rio grande do norte", "rio grande do sul", 
        "rondonia", "roraima", "santa catarina", "sao paulo", "sergipe", "tocantins"
    ]
    
    # Remove acentos do texto
    texto_normalizado = ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower()) if unicodedata.category(c) != 'Mn'
    )
    
    # Cria um padrão regex que encontra qualquer nome de estado
    padrao = r'\b(?:' + '|'.join(estados_brasileiros) + r')\b'
    
    # Usa o re.findall para encontrar todos os estados no texto normalizado
    estados_encontrados = re.findall(padrao, texto_normalizado)
    
    # Remove duplicatas
    return list(set(estados_encontrados))

#-----------------------------------------------------------------------------#  
# Função 11
def detectar_crm_oab(texto):
    """
    Detecta números de CRM e OAB em uma string, retornando exatamente como aparecem no texto original.

    Formatos suportados:
    - CRM: "CRM 12345 SP", "CRM-12345-SP", "crm-sp-70776"
    - OAB: "OAB 12345 SP", "OAB-12345-SP", "OAB/67890/RJ"

    Parâmetros:
    texto (str): A string contendo o texto onde os números de CRM e OAB serão procurados.
    
    Retorna:
    list: Uma lista de strings contendo os números de CRM ou OAB encontrados.

    Exemplo:
    >>> detectar_crm_oab("O médico tem CRM 12345 SP, e o advogado tem OAB 67890-RJ.")
    ['CRM 12345 SP', 'OAB 67890-RJ']
    """
    
    # Padrão regex para detectar CRM
    padrao_crm = r'\b(?:crm|CRM)[-\s]?([a-z]{2})[-]?(\d{4,6})\b|crm[-]?(\w{1,2})[-]?(\d{5})\b'
    
    # Padrão regex para detectar OAB
    padrao_oab = r'\b(?:oab|OAB)[-\s]?(\d{5})[-]?([A-Z]{2})\b|OAB[-]?(\d{5})[-]?([A-Z]{2})\b'
    
    # Encontrar todos os números de CRM no texto
    crms = re.findall(padrao_crm, texto)
    crms = ['crm-' + match[0] + '-' + match[1] if match[0] and match[1] else 'crm-' + match[2] + '-' + match[3] for match in crms]

    # Encontrar todos os números de OAB no texto
    oabs = re.findall(padrao_oab, texto)
    oabs = ['OAB-' + match[0] + '-' + match[1] if match[0] and match[1] else 'OAB-' + match[2] + '-' + match[3] for match in oabs]

    # Combinar ambos os resultados (CRM e OAB) preservando a formatação original
    total = crms + oabs
    
    return total

#-----------------------------------------------------------------------------#  
# Função 12
def detectar_numeros_telefone(texto):
    """
    Detecta números de telefone em uma string.

    Esta função utiliza expressões regulares para identificar números de telefone
    no formato brasileiro, que podem incluir:
    - Código de área entre parênteses (opcional).
    - Números com 4 ou 5 dígitos antes do hífen e 4 dígitos após o hífen.
    - Possibilidade de espaços ou hífens entre os números.

    Args:
        texto (str): A string onde os números de telefone serão buscados.

    Returns:
        list: Uma lista contendo todos os números de telefone encontrados na string.
    """
    # Expressão regular para detectar números de telefone
    padrao = r'\(?\b\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}\b'
    numeros_telefone = re.findall(padrao, texto)
    return numeros_telefone
#-----------------------------------------------------------------------------#  