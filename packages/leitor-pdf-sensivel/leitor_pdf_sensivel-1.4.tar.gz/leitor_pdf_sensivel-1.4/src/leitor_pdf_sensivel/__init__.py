# __init__.py
from .le_arquivo_sem_dados_sensiveis import le_arquivo_sem_dados_sensiveis

import subprocess
import spacy

def install_model():
    subprocess.check_call(['python', '-m', 'spacy', 'download', 'pt_core_news_lg'])

# Tente instalar o modelo ao importar o pacote
try:
    nlp = spacy.load('pt_core_news_lg')
except OSError:
    install_model()
    nlp = spacy.load('pt_core_news_lg')
