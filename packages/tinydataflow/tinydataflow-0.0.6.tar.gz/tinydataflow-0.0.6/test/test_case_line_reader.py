import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from tinydataflow import TinyDataFlow
from tinydataflow.transformers.writers import LineWriter
from tinydataflow.connectors.readers import LineReader

class FileSelTest(unittest.TestCase):

    def test_file_selector(self):
        
        reader = LineReader('test_case_text.txt')
        writer = LineWriter('output.txt')

        try:
            app = TinyDataFlow(reader, [writer])
            #app.setup({'open_mode': 'w'})
            app.setup()
            app.run()    
            print(f"Resultados: {app.outputs}")
            
            self.assertEqual(len(app.outputs), 4)
        except TypeError as e:
            print(f"Erro de compatibilidade: {e}")
               
if __name__ == '__main__':
    unittest.main()