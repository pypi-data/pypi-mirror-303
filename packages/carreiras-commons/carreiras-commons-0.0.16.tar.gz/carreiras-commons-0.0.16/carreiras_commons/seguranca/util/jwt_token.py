from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta
from carreiras_commons.config import SECRET_KEY, HOST
from carreiras_commons.util.exceptions import Exception409
import jwt
import uuid

class JwtToken():
    
    def generate_token(self,user_profile):
        tokens ={'user_name':user_profile.user.username,
                 'picture':user_profile.picture,
                'full_name': user_profile.user.get_full_name(),
                'user_id': user_profile.user.id,
                 }
        tokens['access_token'] = self.get_access_token(user_profile)
        tokens['refresh_token'] = self.get_refresh_token(user_profile)


        return tokens
    
    def renew_token(self,refresh_token:str, callback):
        payload = self.decode_token(refresh_token)
        user_profile = callback(payload['id'])

        return self.generate_token(user_profile)

    def get_access_token(self,user_profile):
        now = datetime.now().replace(microsecond=0)
        exp = now + timedelta(days=1)
        exp = int(exp.timestamp())
        now = int(now.timestamp())
        scope = ''

        for group in user_profile.user.groups.all():
            scope = f'{group} {scope}' 

        payload_data = {
            'exp': exp,
            'iat': now,
            'jti': str(uuid.uuid4()),
            'sub': 'carrers',
            'iss': HOST,
            'typ': 'Bearer',
            'id': user_profile.user.pk,
            'name': f'{user_profile.user.first_name} {user_profile.user.last_name}',
            'principal-email': user_profile.e_mail,
            'picture':user_profile.picture,
            'scope': scope.rstrip()
        }       

        private_key = open('./resources/carreiras', 'r').read()
        key = serialization.load_ssh_private_key(private_key.encode(), password= SECRET_KEY.encode('utf-8'))
        
        token = jwt.encode(payload=payload_data, key=key, algorithm='RS256')
        return token
    
    def get_refresh_token(self,user_profile):
        now = datetime.now().replace(microsecond=0)
        exp = now + timedelta(days=365)
        exp = int(exp.timestamp())
        now = int(now.timestamp())

        payload_data = {
            'exp': exp,
            'id': user_profile.user.pk,
            'principal-email': user_profile.e_mail,
        } 

        private_key = open('./resources/carreiras', 'r').read()
        key = serialization.load_ssh_private_key(private_key.encode(), password= SECRET_KEY.encode('utf-8'))
        
        token = jwt.encode(payload=payload_data, key=key, algorithm='RS256')
        return token
     
    def decode_token(self,token:str):
        try:
            token = token.replace('Bearer ', '')
            public_key = open('./resources/carreiras.pub', 'r').read()
            return jwt.decode(token,key=public_key,algorithms=['RS256'])
        except Exception:
            raise Exception409()

jwt_token = JwtToken()