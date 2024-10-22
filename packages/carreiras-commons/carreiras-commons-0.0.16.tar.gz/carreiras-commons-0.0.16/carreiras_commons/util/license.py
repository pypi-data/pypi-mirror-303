import os
import json
import tempfile
from collections import namedtuple

class License():    

    def __init__(self) -> None:      
        self.type = os.getenv('TYPE')
        self.project_id = os.getenv('PROJECT_ID')
        self.private_key_id = os.getenv('PRIVATE_KEY_ID')
        self.private_key = os.getenv('PRIVATE_KEY')
        self.client_email = os.getenv('CLIENT_EMAIL')
        self.client_id = os.getenv('CLIENT_ID')
        self.auth_uri = os.getenv('AUTH_URI')
        self.token_uri = os.getenv('TOKEN_URI')
        self.auth_provider_x509_cert_url = os.getenv('AUTH_PROVIDER_X509_CERT_URL')
        self.client_x509_cert_url = os.getenv('CLIENT_X509_CERT_URL')
        self.universe_domain= 'googleapis.com'
        
        # Criando um arquivo temporário
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.json')
        self.to_json()
        self.to_object()

    def to_json(self)->str:       
      data_dict = self.__dict__.copy()  # Faz uma cópia para não alterar o original
      if 'temp_file' in data_dict:
        del data_dict['temp_file']  

        self.temp_file.write(json.dumps(data_dict).replace('\\\\n','\\n'))
        self.temp_file.seek(0)  # Retorna ao início do arquivo para leitura posterior
        self.temp_file.close()
     
           


    def to_object(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.temp_file.name
        print('self',self.temp_file.name)

        with open(os.environ['GOOGLE_APPLICATION_CREDENTIALS']) as file:
            data = json.load(file)
            return namedtuple("License", data.keys())(*data.values())
        
