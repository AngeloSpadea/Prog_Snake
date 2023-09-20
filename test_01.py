import unittest
from funzioni_gioco import calcola_mossa, converti_mosse, mangia, muovi
#from gestione_input import carico_dati

class test(unittest.TestCase):
    # Nel Modificare i test tenere conto che nella rappresentazione dei punti [i,j]
    #  i rappresente la colonna mentre j rappresenta la riga

    def test_verifico_calcola_mossa(self):
        result = calcola_mossa([[2,0]], [0,1], 4, 6)
        self.assertEqual(result, [2, 1])

    def test_verifico_calcola_mossa_con_uscita_dal_bordo(self):
        result = calcola_mossa([[5,3]], [1,1], 4, 6)
        self.assertEqual(result, [0, 0])

    def test_corverti_mosse(self):
        result = converti_mosse('N')
        self.assertEqual(result, [[-1, 0]])
    
    def test_corverti_mosse_oblique(self):
        result = converti_mosse('NW')
        self.assertEqual(result, [[-1, -1]])

    def test_mangia(self):
        result = mangia([[1,1]],[],[1,2],[[1, 2], [2, 2], [3, 2]])
        self.assertEqual(result[0],[[1,2],[1,2]])
        self.assertEqual(result[1],[[1,1]])

    
    def test_muovi_start(self):
        result = muovi([[3,4]], [], [2,4])
        self.assertEqual(result[0], [[2,4]])
        self.assertEqual(result[1], [[3,4]])

    def test_muovi(self):
        result = muovi([[2,4]], [[3,4]], [2,3])
        self.assertEqual(result[0], [[2,3]])
        self.assertEqual(result[1], [[2,4], [3,4]]) 
   
    def test_muovi_da_cresciuto(self):
        result = muovi([[5,1], [5,2]], [[5,3]], [4,1])
        self.assertEqual(result[0], [[4,1], [5,1]])
        self.assertEqual(result[1], [[5,2], [5,3]]) 
