# =============================================================================
# Pacotes
# =============================================================================
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
import spacy

# =============================================================================
# Leitura de termos e requirements
# =============================================================================
def read_terms():
    """Função para exibir o termo de uso e verificar a concordância do usuário."""
    with open('TERMO_DE_USO.txt', 'r', encoding='utf-8') as f:
        terms = f.read()
    print(terms)

    response = 's'  # Simulação, altere conforme necessário
    
    if response in ['s', 'sim']:
        print("Você concordou com os termos.")
    elif response in ['n', 'não']:
        print("Instalação cancelada.")
        sys.exit(1)
    else:
        print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
        sys.exit(1)

def read_requirements():
    """Função para ler o arquivo requirements.txt."""
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def read_readme():
    """Função para ler o arquivo README.md."""
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

class CustomInstallCommand(install):
    """Customização do comando de instalação para baixar o modelo do spaCy."""

    def run(self):
        # Chama o método de instalação padrão
        install.run(self)
        
        # Baixa o modelo 'pt_core_news_lg' após a instalação
        print("Baixando dependência")
        os.system("python -m spacy download pt_core_news_lg")

# Lê e exibe os termos antes de continuar
read_terms()

# =============================================================================
# Setup
# =============================================================================
setup(
    name='leitor_pdf_sensivel',
    version='1.2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        'leitor_pdf_sensivel': [
            'data/*.xlsx',           # Inclui arquivos .xlsx da pasta data
        ],  
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
        'pypdf',
        'setuptools',
        'spacy'
    ],
    long_description=read_readme(),  # Lê o README para a descrição longa
    long_description_content_type='text/markdown',  # Especifica o formato do README
    cmdclass={
        'install': CustomInstallCommand,  # Usa a classe customizada para instalação
    },
)
