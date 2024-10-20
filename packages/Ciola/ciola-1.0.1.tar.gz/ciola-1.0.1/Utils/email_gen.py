import random

class MailGen:
    def __init__(self):
        pass
    
    def gen_mail(self):
        nomi = [
    "Alessandro", "Giovanni", "Lorenzo", "Mattia", "Gabriele",
    "Riccardo", "Nicola", "Leonardo", "Andrea", "Francesco",
    "Davide", "Simone", "Marco", "Stefano", "Giulio",
    "Luca", "Matteo", "Daniele", "Alessio", "Angelo",
    "Carlo", "Vincenzo", "Federico", "Emanuele", "Giuseppe",
    "Antonio", "Salvatore", "Pietro", "Roberto", "Filippo",
    "Diego", "Cristiano", "Raffaele", "Sebastiano", "Fabio",
    "Elia", "Leonardo", "Tommaso", "Aldo", "Giordano",
    "Alberto", "Umberto", "Giorgio", "Salvatore", "Nicolò",
    "Gianluca", "Piero", "Ernesto", "Martino", "Riccardo",
    "Lucio", "Gianni", "Ruggero", "Giulio", "Tiziano",
    "Dario", "Rinaldo", "Renato", "Alfredo", "Ettore",
    "Edoardo", "Vittorio", "Maurizio", "Claudio", "Sergio",
    "Nerino", "Emilio", "Alberto", "Benedetto", "Orazio",
    "Leone", "Luciano", "Adriano", "Graziano", "Giuseppe",
    "Carmine", "Agostino", "Bartolomeo", "Beppe", "Domenico",
    "Ferdinando", "Guido", "Ignazio", "Lazzaro", "Michele",
    "Onofrio", "Quinto", "Silvano", "Umberto", "Virgilio",
    "Zeno", "Sisto", "Ascanio", "Corrado", "Clemente",
    "Dante", "Sandro", "Nazzareno", "Teodoro", "Rocco",
    "Marcello", "Alessandro", "Claudio", "Giorgio", "Ivo",
    "Livio", "Mauro", "Osvaldo", "Rinaldo", "Savino",
    "Taddeo", "Ulisse", "Zefiro"
        ]

        cognomi = [
    "Rossi", "Ferrari", "Russo", "Colombo", "Ricci",
    "Marino", "Greco", "Bruno", "Gallo", "Conti",
    "Daniele", "Rizzo", "Lombardi", "Moretti", "Barbieri",
    "Fabbri", "Fontana", "Cattaneo", "Giordano",
    "Costa", "Romano", "Sartori", "Valenti", "Riva",
    "Sorrentino", "Palmieri", "Mancini", "Martini", "Vitali",
    "Testa", "Miele", "Ruggeri", "Farina",
    "Carbone", "Mariani", "Pugliese", "Ferri", "Caputo",
    "Rinaldi", "Giorgi", "Pereira", "Barbato", "Silvestri",
    "Corsi", "D'Angelo", "Cipriani", "Ventura", "Fusco",
    "Battaglia", "Cavalli", "Marta","Savino",
    "Mancuso", "Pagano", "Giuliani", "Schiavone",
    "Fiore", "Giustino", "Palmieri", "Luciano",
    "Marchetti", "Lucarelli", "Bianchi", "Gatti", "Longo",
    "Ricciardi", "Bianco", "Rossi", "Calabrese",
    "Monti", "Rinaldi", "Battisti", "Serra", "Tedesco",
    "Montalto", "Bertolini", "Alessi", "Ruggeri",
    "Fiorentino", "Fioravanti", "Palumbo", "Salvatori", "Martelli",
    "Giuliano", "Palmieri", "Rocca", "Serafini", "Giannini",
    "Petrucci", "Lombardo", "Sgro", "Giorgetti", "Ventura"
        ]
    
        domains = [
    "gmail.com",
    "libero.it",
    "hotmail.com",
    "yahoo.it",
    "alice.it",
    "outlook.com",
        ]   
    
        rnd_number = random.randint(1, 999)
        rnd_name = random.choice(nomi)
        rnd_cognome = random.choice(cognomi)
        rnd_domain = random.choice(domains)
    
        formats = (
        f"{rnd_name}.{rnd_cognome}{rnd_number}@{rnd_domain}",
        f"{rnd_name}.{rnd_cognome}@{rnd_domain}",
        f"{rnd_name}_{rnd_cognome}{rnd_number}@{rnd_domain}",
        f"{rnd_name}_{rnd_cognome}@{rnd_domain}",
        f"{rnd_name}.{rnd_cognome}_{rnd_number}@{rnd_domain}",
        f"{rnd_name}_{rnd_cognome}.{rnd_number}@{rnd_domain}"
        )
        return random.choice(formats)
