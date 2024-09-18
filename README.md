# MarketCapETLforTopBanks

Este projeto consiste em um sistema **ETL** que realiza a captura de informações atualizadas sobre a capitalização de mercado dos maiores bancos do mundo por meio de *web scraping*. Os dados coletados são convertidos de dólares para euros, rúpias indianas e libras esterlinas. As informações são então acessadas via consultas *SQL* em um banco de dados dedicado.

## Pré-requisitos

Antes de começar, você precisa ter o Python instalado em sua máquina. Este projeto é compatível com o Python 3.6 ou superior.

### Instalando o Python

#### No Windows

1. Baixe o instalador do Python no [site oficial do Python](https://www.python.org/downloads/).
2. Execute o instalador e certifique-se de marcar a opção "Add Python to PATH" antes de clicar em "Install Now".

#### No macOS

1. Você pode instalar o Python usando o Homebrew. Se você ainda não tem o Homebrew instalado, siga as instruções em [brew.sh](https://brew.sh).

2. Execute o seguinte comando no Terminal:

   ```
   brew install python
   ```

#### No Linux

  Use o gerenciador de pacotes de sua distribuição. Por exemplo, no Ubuntu, execute:

    sudo apt update

### Instalação das Dependências

Depois de instalar o Python, você precisa instalar as dependências do projeto. Crie um ambiente virtual e instale as dependências usando pip:

Criar um Ambiente Virtual

    python -m venv venv

Ativar o Ambiente Virtual

No Windows:

    venv\Scripts\activate

No macOS/Linux:

    source venv/bin/activate

Instalar Dependências

    pip install -r requirements.txt

Executando o Projeto

Depois de instalar todas as dependências, você pode executar o projeto com o seguinte comando:

```
python banks_project.py
```
