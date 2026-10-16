
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

# Permite localizar o código dentro da pasta src
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / 'src'))

import controle_estoque as estoque


class TestTotalItem(unittest.TestCase):

    def test_calculo_valor_estoque_Diporona(self):
        medicamento = {
            'nome': 'Dipirona 500mg',
            'preço': 8.90,
            'quantidade': 5,
            'fabricante': 'Medley',
            'lote': 'abc123',
            'validade': '12/2027'
        }

        with patch('builtins.print'):
            resultado = estoque.total_item(medicamento)

        self.assertAlmostEqual(resultado, 44.50)

    def test_calculo_valor_estoque_total(self):
        valor_esperado = 0
        for medicamento in estoque.medicamentos:
            valor_esperado += medicamento['preço'] * medicamento['quantidade']

        with patch('builtins.print'):
            resultado = estoque.total_estoques_produtos()

        self.assertAlmostEqual(resultado, valor_esperado)

if __name__ == '__main__':
    unittest.main()




from datetime import date

hoje = date.today()

validade = '12/2027'
partes = validade.split('/')

mes_validade = int(partes[0])
ano_validade = int(partes[1])

print('Mês atual:', hoje.month)
print('Ano atual:', hoje.year)
print('Mês de validade:', mes_validade)
print('Ano de validade:', ano_validade)

if ano_validade < hoje.year or (ano_validade == hoje.year and mes_validade < hoje.month):
    print('Data invalida!')
    