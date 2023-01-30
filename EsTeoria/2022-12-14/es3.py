
from datetime import date

class ResponsabileViaggio(object):
    def __init__(self, 
                 cognome: str = None,
                 nome: str = None):
        self.cognome = cognome
        self.nome = nome
        
    def __str__(self):
        return "%s %s" % (
            self.cognome.upper(),
            self.nome
        )
    
class Luogo(object):
    def __init__(self,
                 paese: str = None,
                 regione: str = None,
                 citta: str = None,
                 indirizzo: str = None):
        self.paese = paese
        self.regione = regione
        self.citta = citta
        self.indirizzo = indirizzo
        
    def __str__(self):
        return "%s, %s, %s (%s)" % (
            self.indirizzo,
            self.citta,
            self.regione,
            self.paese
        )
        
class Resort(Luogo):
    def __init__(self,
                 paese: str = None,
                 regione: str = None,
                 citta: str = None,
                 indirizzo: str = None,
                 
                 nome_resort: str = None
                 ):
        super().__init__(paese=paese, regione=regione, citta=citta, indirizzo=indirizzo)
        self.nome_resort = nome_resort
        
    def __str__(self):
        return "%s [%s]" % (
            self.nome_resort,
            super().__str__()
        )
        
class ImpiantoSciistico(object):
    def __init__(self,
                 nome: str = None
                 ):
        self.nome = nome
        
    def __str__(self):
        return "%2" % (self.nome)
        
class EscursioneMarina(object):
    def __init__(self,
                 nome: str = None
                 ):
        self.nome = nome
    
    def __str__(self):
        return "%2" % (self.nome)

class Vacanza(object):
    def __init__(self, 
                 nome_viaggio: str = None,
                 data_partenza: date = None,
                 data_ritorno: date = None,
                 localita: Luogo = None,
                 resort: Resort = None,
                 prezzo: float = None,
                 partecipanti: int = None,
                 responsabile_viaggio: ResponsabileViaggio = None
                 ):
        self.nome_viaggio = nome_viaggio
        self.data_partenza = data_partenza
        self.data_ritorno = data_ritorno
        self.localita = localita
        self.resort = resort
        self.prezzo = prezzo
        self.partecipanti = partecipanti
        self.responsabile_viaggio = responsabile_viaggio
        
    def __repr__(self):
        print("""Nome Viaggio = %s
Data Partenza = %s
Data Arrivo = %s
Località = %s
Resort = %s
Prezzo = %.2f
Partecipanti = %i
Responsabile Viaggio = %s""" % (
    self.nome_viaggio,
    self.data_partenza.strftime("%d / %M / %Y"),
    self.data_ritorno.strftime("%d / %M / %Y"),
    str(self.localita),
    str(self.resort),
    round(self.prezzo, 2),
    self.partecipanti,
    str(self.responsabile_viaggio)
))
        
    def __str__(self):
        return self.__repr__()
        
    def stampa(self):
        return self.__repr__()
        
class VacanzaInvernare(Vacanza):
    def __init__(self,
                 nome_viaggio: str = None,
                 data_partenza: date = None,
                 data_ritorno: date = None,
                 localita: Luogo = None,
                 resort: Resort = None,
                 prezzo: float = None,
                 partecipanti: int = None,
                 responsabile_viaggio: ResponsabileViaggio = None,
                 
                 skipass: int = None,
                 impianti_sciistici: list[ImpiantoSciistico] = []
                 ):
        super().__init__(
            nome_viaggio=nome_viaggio,
            data_partenza=data_partenza,
            data_ritorno=data_ritorno,
            localita=localita,
            resort=resort,
            prezzo=prezzo,
            partecipanti=partecipanti,
            responsabile_viaggio=responsabile_viaggio
        )
        self.skipass = skipass
        self.impianti_sciistici = impianti_sciistici
        
    def __repr__(self):
        super().__repr__()
        print("""Skiipass = %.2f
Impianti Sciistici = %s""" % (
    round(self.skipass, 2),
    ["\n\t%2" for item in str(self.impianti_sciistici)]
))
        
    def __str__(self):
        return self.__repr__()
        
class VacanzaEstiva(Vacanza):
    def __init__(self,
                 nome_viaggio: str = None,
                 data_partenza: date = None,
                 data_ritorno: date = None,
                 localita: Luogo = None,
                 resort: Resort = None,
                 prezzo: float = None,
                 partecipanti: int = None,
                 responsabile_viaggio: ResponsabileViaggio = None,
                 
                 distanza: int = None,
                 escursioni_marine: list[EscursioneMarina] = []
                 ):
        super().__init__(
            nome_viaggio=nome_viaggio,
            data_partenza=data_partenza,
            data_ritorno=data_ritorno,
            localita=localita,
            resort=resort,
            prezzo=prezzo,
            partecipanti=partecipanti,
            responsabile_viaggio=responsabile_viaggio
        )
        self.distanza = distanza
        self.escursioni_marine = escursioni_marine
        
    def __repr__(self):
        super().__repr__()
        print("""Distanza dal Mare = %.2f
Escursioni Marine = %s""" % (
    round(self.distanza, 2),
    ["\n\t%2" for item in str(self.escursioni_marine)]
))
        
    def __str__(self):
        return self.__repr__()