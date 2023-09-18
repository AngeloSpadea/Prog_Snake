import unittest
from funzioni_gioco import calcola_mossa, converti_mosse, mangia, muovi
from gestione_input import carico_dati

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
        self.assertEqual(campo_da_gioco["food"], [[2, 2], [3, 2]])
    
    def test_muovi_start(self):
        result = muovi([[3,4]], [], [2,4])
        self.assertEqual(result[0], [[2,4]])
        self.assertEqual(result[1], [[3,4]])

    def test_muovi(self):
        result = muovi([[2,4]], [[3,4]], [2,3])
        self.assertEqual(result[0], [[2,3]])
        self.assertEqual(result[1], [[2,4], [3,4]]) 
   
    def test_muovi_da_cresciuto(self):
        result = muovi([[1,5], [2,5]], [[3,5]], [1,4])
        self.assertEqual(result[0], [[1,5], [1,4]])
        self.assertEqual(result[1], [[2,5], [3,5]]) 
    
    def test_carico_dati(self):
        result=carico_dati('file_gioco.json')
        self.assertEqual(result[0], [5,3])
        self.assertEqual(result[1], "N N N E SE SE SE E E N N N W W W W W W W S S S S S S SW SW SW")
        self.assertEqual(result[2], [[0, 4],[2, 2],[3, 2]])
        self.assertEqual(result[3], [[0, 2],[1, 1],[3, 1]])
        self.assertEqual(result[4], 4)
        self.assertEqual(result[5], 6)
        self.assertEqual(result[6], 'field_out_01.json')
