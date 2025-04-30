
# Exemplo de teste com Pytest

def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

# Para rodar: pytest exemplo_pytest.py
