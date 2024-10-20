import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from tinydataflow import TinyDataFlow
from tinydataflow import EmailSender, ListToDictTransformer
from tinydataflow import CSVLineReader


class EmailSenderTest(unittest.TestCase):

    def test_email_sender(self):
        
        csvReader = CSVLineReader('email_list.txt')
        csv2dict = ListToDictTransformer(k_names=['recipient_name', 'recipient_email', 'order_id', 'tracking_code', 'attachment_path']) 

        # Transformador que converte TXT para Excel
        email_sender = EmailSender(
            emailsender_email=os.getenv('EMAIL_SENDER'),
            emailsender_password=os.getenv('EMAIL_PASSWORD'),
            emailsender_smtp_port=587,
            emailsender_smtp_server='smtp.gmail.com'
        )

        config = {
            'emailbody_template': """
            <html>
            <body>
            <h1>Olá, ${recipient_name}!</h1>
            <p>Este é um e-mail enviado automaticamente pelo sistema TinyFlow.</p>
            <p>Seu código de rastreamento é: ${tracking_code}</p>
            </body>
            </html>
            """,
            'subject_template': "Status do pedido: ${order_id}"
        }

        try:
            app = TinyDataFlow(csvReader, [csv2dict, email_sender])
            app.setup(config)
            app.run()
            print(f"Resultados: {app.outputs}")
            self.assertEqual(app.outputs[1], 0)
        except TypeError as e:
            print(f"Erro de compatibilidade: {e}")
               
if __name__ == '__main__':
    unittest.main()