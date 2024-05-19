from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository

# TESTE DE UNITARIO - SIMULANDO UMA SESSION
class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)], #query
                    [PetsTable(name="dog", type="dog"), PetsTable(name="cat", type="cat")] #results
                )
            ]
        )
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_value, trace): pass

def test_list_pets():
    # 1 - Testando a session
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    # 2 - Testando Metodos de List Pets
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
