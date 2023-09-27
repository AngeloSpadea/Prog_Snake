import unittest
from funzioni_gioco import calcola_mossa, converti_mosse, mangia, muovi, scontro_coda

class test(unittest.TestCase):
    # Nel Modificare i test tenere conto che nella rappresentazione dei punti [i,j]
    #  i rappresente la colonna mentre j rappresenta la riga

    def test_verifico_calcola_mossa(self):
        """
        Verifica che la funzione calcola_mossa funzioni correttamente restituendo la nuova posizione.
        ----------
        Parametri: corpo, mossa, righe, colonne.
        Risultato atteso: nuova posizione. 

        """
        result = calcola_mossa([[2,0]], [0,1], 4, 6)
        self.assertEqual(result, [2, 1])


    def test_verifico_calcola_mossa_con_uscita_dal_bordo(self):
        """
        Verifica che la funzione calcola_mossa gestisca correttamente l'uscita dal bordo,
        facendo ricomparire la testa del serpente dal bordo opposto.
        ----------
        Parametri: corpo, mossa, righe, colonne.
        Risultato atteso: nuova_posizione.

        """
        result = calcola_mossa([[3,5]], [1,1], 4, 6)
        self.assertEqual(result, [0, 0])

    def test_corverti_mosse(self):
        """
        Verifica che la funzione converti_mosse converta correttamente la direzione verticale Nord (N).
        ----------
        Parametri: 
            mosse: Nord (N) in punto cardinale.
        Risultato atteso:
            mosse_convertite: mossa Nord in forma vettoriale.

        """
        result = converti_mosse('N')
        self.assertEqual(result, [[-1, 0]])
    
    def test_corverti_mosse_oblique(self):
        """
        Verifica che la funzione converti_mosse converta correttamente la direzione obliqua Nord-Ovest (NW).
        ----------
        Parametri: 
            mosse: Nord-Ovest (NW) in punto cardinale.
        Risultato atteso:
            mosse_convertite: mossa Nord-Ovest in forma vettoriale.

        """
        result = converti_mosse('NW')
        self.assertEqual(result, [[-1, -1]])

    def test_mangia(self):
        """
        Verifica che la funzione mangia gestisca correttamente il caso in cui posizione_nuova sia occupata da un cipo.
        La funzione aggiunge la nuova posizione (dove il cibo è stato mangiato) due volte all'inizio del corpo del serpente,
        facendo crescere il corpo del serpente.
        ----------
        Parametri: 
            corpo: un solo elemento.
            scia_serpente: vuota.
            posizone_nuova.
            food.
        Risultati attesi: corpo, scia_serpente.
        
        """
        result = mangia([[1,1]],[],[1,2],[[1, 2], [2, 2], [3, 2]])
        self.assertEqual(result[0],[[1,2],[1,1]])
        self.assertEqual(result[1],[[1,1]])

    
    def test_muovi_start(self):
        """
        Verifica che la funzione muovi gestisca correttamente il movimento di partenza quando la nuova posizione è vuota.
        ----------
        Parametri:
            corpo: un solo elemento.
            scia_serpente: vuota.
            posizione_nuova.
        Risultati attesi: corpo, scia_serpente.
        
        """
        result = muovi([[3,4]], [], [2,4])
        self.assertEqual(result[0], [[2,4]])
        self.assertEqual(result[1], [[3,4]])

    def test_muovi(self):
        """
        Verifica che la funzione muovi gestisca correttamente il movimento generale.
        ----------
        Parametri:
            corpo: un solo elemento.
            scia_serpente: non vuota.
            posizione_nuova.
        Risultati attesi: corpo, scia_serpente.
        
        """
        result = muovi([[2,4]], [[3,4]], [2,3])
        self.assertEqual(result[0], [[2,3]])
        self.assertEqual(result[1], [[2,4], [3,4]]) 
   
    def test_muovi_da_cresciuto(self):
        """
        Verifica che la funzione muovi gestisca correttamente il movimento quando il serpente è cresciuto.
        ----------
        Parametri:
            corpo: più elementi.
            scia_serpente: non vuota.
            posizione_nuova.
        Risultati attesi: corpo, scia_serpente.
        
        """
        result = muovi([[5,1], [5,2]], [[5,3]], [4,1])
        self.assertEqual(result[0], [[4,1], [5,1]])
        self.assertEqual(result[1], [[5,2], [5,3]]) 
    
    
    
