from src.utils import eleva_quadrado, requires_role
import pytest
from unittest.mock import Mock, patch
from http import HTTPStatus


@pytest.mark.parametrize("test_input,expected", [(2, 4), (10, 100), (3, 9)])
def test_eleva_quarado_sucesso(test_input, expected):
    resultado = eleva_quadrado(test_input)
    assert resultado == expected


# @pytest.mark.parametrize("test_input,expected", [(2, 4), (10, 100), (3, 9)])
# def test_eleva_quadrado_falha():
#     with pytest.raises(TypeError) as exc:
#         eleva_quadrado("a")
#     assert (
#         str(exc.value) == "unsupported operand type(s) for ** or pow(): 'str' "
#         "and 'int'"
#     )


def test_requires_role():
    mock_user = Mock()
    mock_user.role.name = "normal"

    mock_get_jwt_identity = patch("src.utils.get_jwt_identity")
    mock_db_get_or_404 = patch("src.utils.db.get_or_404", return_value=mock_user)

    mock_db_get_or_404.start()
    mock_get_jwt_identity.start()

    decorated_function = requires_role("admin")(lambda: "success")

    result = decorated_function()

    assert result == ({"message": "User dont have access."}, HTTPStatus.FORBIDDEN)

    mock_db_get_or_404.stop()
    mock_get_jwt_identity.stop()
