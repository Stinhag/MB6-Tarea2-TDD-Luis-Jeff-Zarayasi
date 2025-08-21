import unittest
from validar_usuario import validar_username

class TestValidarUsername(unittest.TestCase):
    def test_valido(self):
        self.assertTrue(validar_username("user_01"))

    def test_invalido_corto(self):
        self.assertFalse(validar_username("us"))

    def test_invalido_largo(self):
        self.assertFalse(validar_username("super_long_username_2025"))

    def test_invalido_caracteres(self):
        self.assertFalse(validar_username("user@01"))

if __name__ == "__main__":
    unittest.main()
