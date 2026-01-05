from src.utils import eleva_quadrado


def test_eleva_quarado_sucesso():
    resultado = eleva_quadrado(2)
    assert resultado == 4
