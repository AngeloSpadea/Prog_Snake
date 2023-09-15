import unittest
from funzioni_gioco import calcola_mossa, converti_mosse, mangia

campo_da_gioco={'rows': 4,
                    'cols': 6,
                    'food': [[1, 2], [2, 2], [3, 2]],
                    'blocks': [[0, 2], [1, 1], [3, 1]]}

class test(unittest.TestCase):
    

    def test_verifico_calcola_mossa(self):
        result = calcola_mossa([[2,0]], [0,1], 4, 6)
        self.assertEqual(result, [2, 1])

    def test_verifico_calcola_mossa_con_uscita_dal_bordo(self):
        result = calcola_mossa([[3,5]], [1,1], 4, 6)
        self.assertEqual(result, [0, 0])

    def test_corverti_mosse(self):
        result = converti_mosse(['N'])
        self.assertEqual(result, [[-1, 0]])
    
    def test_corverti_mosse_oblique(self):
        result = converti_mosse(['NW'])
        self.assertEqual(result, [[-1, -1]])

    def test_mangia(self):
        result = mangia([[1,1]],[],[1,2],campo_da_gioco)
        self.assertEqual(result[0],[[1,2],[1,2]])
        self.assertEqual(result[1],[[1,1]])
