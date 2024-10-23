from typing import Any, Tuple


def mock_sucesso_insercao_boleto(*args: Any, **kwargs: Any) -> Tuple:
    return (
        {
            "_status": "sucesso",
            "_dados": {
                "_sucesso": [
                    {
                        "idintegracao": "RE1WDW909",
                        "situacao": "SALVO",
                        "TituloNumeroDocumento": "1737",
                        "TituloNossoNumero": "1737",
                        "CedenteContaCodigoBanco": "001",
                        "CedenteContaNumero": "103500",
                        "CedenteConvenioNumero": "3145850",
                        "TituloCodigoReferencia": None,
                        "idImpressao": "1234",
                    }
                ],
                "_falha": [],
            },
        },
        {},
    )


def mock_sucesso_insercao_boleto_sem_id_impressao(*args: Any, **kwargs: Any) -> Tuple:
    return (
        {
            "_status": "sucesso",
            "_dados": {
                "_sucesso": [
                    {
                        "idintegracao": "RE1WDW909",
                        "situacao": "SALVO",
                        "TituloNumeroDocumento": "1737",
                        "TituloNossoNumero": "1737",
                        "CedenteContaCodigoBanco": "001",
                        "CedenteContaNumero": "103500",
                        "CedenteConvenioNumero": "3145850",
                        "TituloCodigoReferencia": None,
                    }
                ],
                "_falha": [],
            },
        },
        {},
    )


def mock_falha_insercao_boleto(*args, **kwargs):
    return (
        {
            "_status": "sucesso",
            "_dados": {"_sucesso": None, "_falha": [{"erro_de_teste": "TESTE"}]},
        },
        None,
    )
