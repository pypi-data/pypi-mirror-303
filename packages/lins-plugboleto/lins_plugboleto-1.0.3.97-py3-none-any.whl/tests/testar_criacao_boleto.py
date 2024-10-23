from unittest import TestCase
from unittest.mock import patch, Mock

from lins_plugboleto.request.criar_boleto import CriarBoleto
from lins_plugboleto.plugBoleto import PlugBoleto
from tests.mocks import (
    mock_falha_insercao_boleto,
    mock_sucesso_insercao_boleto,
    mock_sucesso_insercao_boleto_sem_id_impressao,
)
from tests.utils import criar_e_configurar_plugboleto


class CriacaoBoletoOfflineCasoTeste(TestCase):
    __EXCEPTION_ERRO_PADRAO: str = "Aplicando erro Genérico controlado no teste!"

    def setUp(self) -> None:
        self.__plugboleto: PlugBoleto = criar_e_configurar_plugboleto()

    @patch.object(CriarBoleto, "send_request", new=mock_sucesso_insercao_boleto)
    def testar_criacao_boleto_id_impressao(self) -> None:
        objeto_mock_boleto: Mock = Mock()

        objeto_mock_boleto.update_return.side_effect = lambda resposta, _: resposta[
            "_dados"
        ]["_sucesso"][0]["idImpressao"]

        self.__plugboleto.criar_boleto(objeto_mock_boleto)

        objeto_mock_boleto.update_return.assert_called_once()

    @patch.object(CriarBoleto, "send_request", new=mock_falha_insercao_boleto)
    def testar_criacao_boleto_com_falha_requisicao(self) -> None:
        objeto_boleto: Mock = Mock()

        self.__plugboleto.criar_boleto(objeto_boleto)

        objeto_boleto.update_return.assert_not_called()

    @patch.object(
        CriarBoleto,
        "send_request",
        new=Mock(side_effect=Exception(__EXCEPTION_ERRO_PADRAO)),
    )
    def testar_criacao_boleto_com_disparo_erro_generico_na_requisicao(self) -> None:
        objeto_boleto: Mock = Mock()

        with self.assertRaisesRegex(
            expected_exception=Exception,
            expected_regex=rf"Problema no retorno da plugboleto: {CriacaoBoletoOfflineCasoTeste.__EXCEPTION_ERRO_PADRAO} - Response: None",
        ):
            self.__plugboleto.criar_boleto(objeto_boleto)

        objeto_boleto.update_return.assert_not_called()

    @patch.object(
        CriarBoleto, "send_request", new=mock_sucesso_insercao_boleto_sem_id_impressao
    )
    def testar_criacao_boleto_sem_id_impressao(self) -> None:
        objeto_boleto: Mock = Mock()

        objeto_boleto.update_return.side_effect = lambda resposta, _: resposta[
            "_dados"
        ]["_sucesso"][0]["idImpressao"]

        with self.assertRaises(Exception):
            self.__plugboleto.criar_boleto(objeto_boleto)

        objeto_boleto.update_return.assert_called_once()
