# Projeto de Remoção de Dados Sensíveis de PDF

Este projeto fornece uma solução para ler arquivos PDF e remover informações sensíveis, gerando um novo arquivo de texto com os dados filtrados.

O pacote é uma ferramenta desenvolvida para auxiliar na conformidade com a Lei Geral de Proteção de Dados (LGPD) no Brasil. 
Ele oferece funcionalidades para identificar e remover dados sensíveis, ajudando na tarefa de que informações pessoais identificáveis (PII) 
não sejam expostas ou utilizadas de maneira inadequada.

Este é um projeto da empresa Asi Tech. 
Soluções em Inteligência Artificial? Fale conosco: asitech.solucoesemia@gmail.com.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Funções](#funções)
- [Tratamento de Exceções](#tratamento-de-exceções)
- [Licença](#licença)

## Descrição do Projeto

O objetivo deste projeto é permitir que os usuários leiam arquivos PDF e removam informações sensíveis com base em uma lista de dados.

## Instalação

Para usar este projeto, você precisará ter o Python instalado em seu ambiente. 

```python

pip install leitor-pdf-sensivel

```

## Uso

Para utilizar a função principal, basta chamar `le_arquivo_sem_dados_sensiveis` com o caminho do arquivo PDF que você deseja processar.

### Exemplo de uso:

```python
from leitor_pdf_sensivel import le_arquivo_sem_dados_sensiveis

resultado = le_arquivo_sem_dados_sensiveis("caminho/para/seu/arquivo.pdf")
print(resultado)
```

O texto sem dados sensíveis será salvo em um arquivo chamado `texto_sem_dados_sensiveis.txt`.

## Funções

### `le_arquivo_sem_dados_sensiveis(pdf_path)`

Lê um arquivo PDF, remove informações sensíveis com base na LGPD e retorna o texto sem esses dados.
A acurácia da ferramenta é alta, mas não 100%.

**Parâmetros:**
- `pdf_path` (str): Caminho para o arquivo PDF a ser processado.

**Retorna:**
- `texto_sem_dados_sensiveis` (str): Texto do PDF com as informações sensíveis removidas.
- `arquivo texto` (arquivo): texto tratado sem as informações sensíveis encontradas.

## Tratamento de Exceções

O código inclui tratamento para as seguintes exceções:
- `FileNotFoundError`: Arquivo PDF não encontrado ou inválido.
- `pd.errors.EmptyDataError`: Problemas ao ler o arquivo Excel `exames.xlsx`.
- `Exception`: Outros erros durante a execução.

# Observação Importante
Este pacote é um projeto da Empresa Asi Tech. A Asi Tech não se responsabiliza pelo uso de informações sigilosas por seus usuários.
Ao instalar esse pacote, o usuário concorda que:

- Ele é unicamente responsável pelo processamento de informações sigilosas.
- A acurácia do pacote não é 100%, portanto pode haver informação sensível não removida.
- Todo o processamento do pacote é feito localmente na máquina do usuário. A Asi Tech não guarda nem processa dados processados com esse pacote.
- O objetivo desse pacote é unicamente ajudar na extração de informações sigilosas de um texto. Entretanto, dado que nem toda informação será necessáriamente retirada, o usuário é responsável por olhar o resultado e garantir que tudo tenha sido extraído.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
