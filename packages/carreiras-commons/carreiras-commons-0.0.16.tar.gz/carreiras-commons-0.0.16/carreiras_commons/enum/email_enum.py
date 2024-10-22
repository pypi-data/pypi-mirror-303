from enum import Enum

class TipoEmailEnum(Enum):

    NOTIFICACAO = 1
    CONFIRMACAO_EMAIL = 2
    ESQUECI_SENHA = 3

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)