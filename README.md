# Sistema Bancário

Um sistema de fluxo de caixa bancário simples para gerenciar depósitos, saques e verificar extratos, com controle de limites diários e histórico de transações.

# Instalação

Instruções sobre como instalar e configurar o projeto localmente.

- Pré-requisitos: conhecimento básico em python, env (ambiente virtual) e trabalhar com terminal (opcional);
- Passo a passo de como clocar o repositório:

1 - Clonar o repositório
git clone https://github.com/GuiReisSilva/Sistema_Banc-rio.git

2 - Entrar na pasta do projeto
cd projeto

3 - Criar um ambiente virtual (opcional)
python -m venv venv

4 - Ativar o ambiente virtual (opcional)
source venv/bin/activate # Para Linux/Mac
.\venv\Scripts\activate # Para Windows

5 - Instalar dependências
pip install -r requirements.txt

6 - Rodar o projeto
python main.py

# Uso

Execute o arquivo principal do sistema (python main.py);
Use os botões Depositar, Sacar e Extrato para interagir com o sistema;
O saldo e o histórico de transações serão exibidos na tela.

# Funcionalidades

Depósitos e saques com validação de saldo e limites.
Histórico de transações (extrato).
Controle de limite diário de saques.

# Tecnologias Utilizadas

- Python: linguagem principal;
- Tkinter: para a interface gráfica;
- Pandas: para manipulação de dados (é possível utilizar o pandas ou criar um sqlite para brincar com os dados de forma opcional).

# Contribuição

Contribuam para a melhoria do código :), segue abaixo o passo a passo para criar uma branch:

- 1 - Faça um fork deste repositório;
- 2 - Crie uma branch com a nova funcionalidade: git checkout -b minha-feature;
- 3 - Commit suas mudanças: git commit -m 'Adiciona nova feature';
- 4 - Faça o push para a branch: git push origin minha-feature;
- 5 - Abra um Pull Request.

# Autores

Nome: Guilherme dos Reis  
GitHub: GuiReisSilva  
LinkedIn: https://www.linkedin.com/in/guilhermedosreissilva/

# Rodapé / Contato

Contato: guilhermedosreissilva3@gmail.com
