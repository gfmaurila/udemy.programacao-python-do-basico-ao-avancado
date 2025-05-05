
# 8. Testes: Teste unitário simples
def dobrar(n):
    return n * 2

def test_dobrar():
    assert dobrar(2) == 4
    assert dobrar(5) == 10

test_dobrar()
print("Todos os testes passaram.")
