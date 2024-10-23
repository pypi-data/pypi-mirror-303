import os

from lins_plugboleto.plugBoleto import PlugBoleto
from lins_plugboleto.environment import Environment
from lins_plugboleto.authorize import Authorize


CNPJ_CEDENTE: str = os.environ.get("CNPJ_CEDENTE", "01001001000113")

CNPJ_SH: str = os.environ.get("CNPJ_SH", "01001001000113")

TOKEN_SH: str = os.environ.get("TOKEN_SH", "f22b97c0c9a3d41ac0a3875aba69e5aa")


def criar_e_configurar_plugboleto(
    cnpjcedente: str = CNPJ_CEDENTE, cnpjsh: str = CNPJ_SH, tokensh: str = TOKEN_SH
) -> PlugBoleto:
    environment: Environment = Environment(sandbox=True)

    authorize: Authorize = Authorize(
        cnpjcedente=cnpjcedente, cnpjsh=cnpjsh, tokensh=tokensh
    )

    return PlugBoleto(authorize, environment)
