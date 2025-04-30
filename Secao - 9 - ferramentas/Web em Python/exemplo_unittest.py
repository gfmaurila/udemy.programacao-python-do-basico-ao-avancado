
# Exemplo de teste com unittest

import unittest

def multiplica(a, b):
    return a * b

class TesteMultiplicacao(unittest.TestCase):
    def test_basico(self):
        self.assertEqual(multiplica(2, 3), 6)
        self.assertEqual(multiplica(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
