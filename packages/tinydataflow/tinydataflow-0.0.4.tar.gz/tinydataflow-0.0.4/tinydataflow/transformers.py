from tinydataflow.core import DataTransformer, DataTransformerException
from typing import List, Type, Union
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import csv
import string


class EmailSender(DataTransformer):
    '''
    Classe que envia e-mails para um destinatário. Recebe do input_data um dicionário com as chaves:
    - recipient_email
    - subject (opcional, usa o template se não fornecido)
    - body (opcional, usa o template se não fornecido)
    - attachment_path (opcional)
    O método setup permite definir templates de e-mail (subject_template e emailbody_template).
    '''

    STATUS_OK = 0
    STATUS_ERROR = 1    

    def __init__(self, emailsender_email=None, emailsender_password=None, emailsender_smtp_server='smtp.gmail.com', emailsender_smtp_port=587):
        self.__sender_email = emailsender_email
        self.__sender_password = emailsender_password
        self.__smtp_server = emailsender_smtp_server
        self.__smtp_port = emailsender_smtp_port
        self.__subject_template = ""
        self.__emailbody_template = ""

    @property    
    def input_type(self) -> Type:
        return dict[str]
    
    @property
    def output_type(self) -> Type:
        return List[Union[str, int, str]]  # Retorna o endereço de e-mail do destinatário e o status do envio de e-mail (erro = 1, ok = 0)

    def transform(self, input_data) -> List[Union[str, int, str]]:
        '''
        Transforms a dictionary with the recipient's e-mail address, subject, body and attachment path into a tuple with the recipient's e-mail address, the status of the email sending and the error message.

        Args:
            input_data: A dictionary with the keys 'recipient_email', 'subject', 'body' and optionally 'attachment_path'.
        Returns:
            A list with the recipient's e-mail address, the status of the email sending (0 = ok, 1 = error) and the error message.
        '''

        recipient_email = input_data.get('recipient_email')
        subject = input_data.get('subject', self.render_template(self.__subject_template, input_data))
        body = input_data.get('body', self.render_template(self.__emailbody_template, input_data))
        attachment_path = input_data.get('attachment_path')

        try:
            self.send_email(
                self.__smtp_server, 
                self.__smtp_port, 
                self.__sender_email, 
                self.__sender_password,
                recipient_email, 
                subject, 
                body, 
                attachment_path
            )
            return [recipient_email, self.STATUS_OK, '']
        except Exception as e:
            return [recipient_email, self.STATUS_ERROR, str(e)] 

    @staticmethod
    def send_email(
        smtp_server, 
        smtp_port, 
        sender_email, 
        sender_password, 
        recipient_email, 
        subject, 
        body, 
        attachment_path=None
    ):
        # Criar mensagem
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Adicionar corpo ao e-mail
        msg.attach(MIMEText(body, 'html' if body.strip().startswith('<') else 'plain'))

        # Adicionar anexo, se fornecido
        if attachment_path:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
                msg.attach(part)

        try:
            # Iniciar conexão com o servidor SMTP
            servidor_smtp = smtplib.SMTP(smtp_server, smtp_port)
            servidor_smtp.starttls()

            # Fazer login
            servidor_smtp.login(sender_email, sender_password)

            # Enviar e-mail
            servidor_smtp.sendmail(sender_email, recipient_email, msg.as_string())

            # Fechar conexão
            servidor_smtp.quit()
        except Exception as e:
            raise DataTransformerException(e)
        
    def setup(self, config: dict):
        """
        Define os templates de e-mail para o corpo (emailbody_template) e o assunto (subject_template).
        """
        self.__emailbody_template = config.get('emailbody_template', '')
        self.__subject_template = config.get('subject_template', 'E-mail enviado pelo TinyFlow')

    @staticmethod
    def render_template(template: str, context: dict) -> str:
        """
        Renderiza o template usando variáveis presentes no dicionário 'context'.
        Substitui chaves no formato {{key}} pelo valor correspondente do dicionário.
        """
        template = string.Template(template)
        return template.safe_substitute(context)
        
        
class StrToCSVTransformer(DataTransformer):
    '''
    The StrToCSVTransformer transforms a list of strings into a CSV file and provides the path to the output CSV file as the result of the transformation.
    '''
    def __init__(self, output_file: str = 'output.csv'):
        self.__output_file = output_file
    
    @property
    def input_type(self) -> Type:        
        return list[str]  # Espera uma lista de strings, sendo cada string uma linha no arquivo CSV

    @property
    def output_type(self) -> Type:
        return str

    def transform(self, input_data: list) -> str:
        """
        Transforms a list of strings into a CSV file and returns the file path.

        Each string in the input list is written as a separate line in the CSV file.
        The CSV file is created at the specified output file path.

        Args:
            input_data: A list of strings, each representing a line to be written to the CSV file.

        Returns:
            The path to the output CSV file as a string.
        """
        with open(self.__output_file, 'w', newline='', encoding='utf-8') as csvfile:
            # Criando um objeto writer do módulo csv
            csvwriter = csv.writer(csvfile)

            # Escrevendo os dados na planilha, um item por linha
            for item in input_data:
                csvwriter.writerow([item])  # Escreve cada string como uma linha única no CSV
        
        return self.__output_file

class ListToDictTransformer(DataTransformer):
    '''
    The ListToDictTransformer transforms a list of strings into a dictionary with the specified keys in a order provided by the user.
    '''
    
    def __init__(self, k_names: list[str]):
        """
        Creates a ListToDictTransformer object.

        Args:
            k_names: The list of keys in the order they should be used to create the dictionary from a list of strings.
        """
        self.__k_names = k_names  
    
    @property
    def input_type(self) -> Type:
        return list[str]  # Espera uma lista de strings
    
    @property
    def output_type(self) -> Type:
        return dict[str]  # Converte em dicinário com valores em strings

    def transform(self, input_data: list[str]) -> dict[str]:
        """
        Transforms a list of strings into a dictionary with the specified keys in a order provided by the user.

        Args:
            input_data: A list of strings to be transformed into a dictionary.

        Returns:
            The dictionary with the specified keys and values from the input_data list.
        """
        return dict(zip(self.__k_names, input_data))

    def setup(self, config: dict):
        pass  # Nenhuma configuração necessária para este exemplo