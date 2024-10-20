TinyDataFlow é uma biblioteca Python simples e extensível que facilita a criação e execução de pipelines de transformação de dados e automação de processos. Com suporte para conectores de dados e transformadores que vão desde a leitura de arquivos, processamento de linhas, gravação de arquivos CSV até envio de e-mails. O TinyFlow é projetado para ser flexível e modular, permitindo que você defina e execute fluxos de dados personalizados de maneira eficiente.

Recursos:

Conectores de dados : Integre várias fontes de dados, como arquivos TXT, CSV, bancos de dados, XML, e mais.
Transformadores de dados : Crie transformações personalizadas para processar seus dados.
Extensível : Adicione seus próprios conectores e transformadores de maneira simples.

Instalação:

Você pode instalar o TinyDataFlow diretamente do repositório ou clonar o projeto para desenvolvimento local:

# Clonando o repositório
git clone https://github.com/ismaelnjr/tinydataflow_project.git
cd tinydataflow

# Instalando dependências
pip install tinydataflow -r requirements.txt

Dependências

O TinyDataFlow utiliza as seguintes bibliotecas:

Python 3.8+
smtplib- Envio de e-mails via SMTP.
cryptography- Para criptografia de credenciais (opcional).
python-dotenv- Para carregar variáveis ​​de ambiente de arquivos .env.
csv- Para leitura e manipulação de arquivos CSV.

Uso:

Em test_case_email_sender.py é um exemplo de como usar o TinyFlow para processar um arquivo CSV e enviar e-mails com templates.