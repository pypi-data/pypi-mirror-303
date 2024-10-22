from functools import wraps
from carreiras_commons.util.exceptions import Exception403,Exception401
from carreiras_commons.seguranca.util.jwt_token import jwt_token

def get_scope(token):
    if not token:
        raise Exception401()
            
    token = token.replace('Bearer ', '')
    token_decode = jwt_token.decode_token(token)
    return token_decode['scope'].split()

def validator_request(permissions):
    def decorator_func(func):
        @wraps(func)
        def wrapper(self, request):            
            token = request.META.get('HTTP_AUTHORIZATION')            
            
            required = str(permissions).split()
            scope = get_scope(token)

            for r in required:
                if r in scope:
                    return func(self,request)
           
            raise Exception403()
    
        return wrapper

    return decorator_func


def validator_self_args_kwargs(permissions):
    def decorator_func(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            token = request.META.get('HTTP_AUTHORIZATION')            
            required = str(permissions).split()

            scope = get_scope(token)

            for r in required:
                if r in scope:
                    return func(self,request, *args, **kwargs)
           
            raise Exception403()
    
        return wrapper

    return decorator_func



def validator_pk_user_id():
    def decorator_func(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            token = request.META.get('HTTP_AUTHORIZATION')      
            usuario_id = jwt_token.decode_token(token)['id']    

            if int(usuario_id) != int(kwargs['pk']):
                raise Exception403()

            return func(self,request, *args, **kwargs)

    
        return wrapper

    return decorator_func

def validator_args_kwargs(permissions):
    def decorator_func(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            token = request.META.get('HTTP_AUTHORIZATION')            
            required = str(permissions).split()
            scope = get_scope(token)

            for r in required:
                if r in scope:
                    return func(request, *args, **kwargs)
           
            raise Exception403()
    
        return wrapper

    return decorator_func

def validator_self(permissions):
    def decorator_func(func):
        @wraps(func)
        def wrapper(self):
            token = self.request.META.get('HTTP_AUTHORIZATION')
            required = str(permissions).split()
            scope = get_scope(token)

            for r in required:
                if r in scope:
                    return func(self)
           
            raise Exception403()
    
        return wrapper

    return decorator_func
