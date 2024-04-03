#1))Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
#Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo.


# a = int(input("Inserisci il primo numero: "))
# b = int(input("Inserisci il secondo numero: "))

# if a == b:
#     print("I numeri sono identici")
# elif a > b:
#     print("Il numero più grande tra i due è " + str(a))
# else:
#     print("Il numero più grande tra i due è " + str(b))

#2))Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.

# a = int(input("inserisci il numero: "))
# b = int(input("inserisci il numero: "))
# c = int(input("inserisci il numero: "))


# if a == b == c:
#     print("tutte e tre i numeri sono uguali")
# elif a >= b & a >= c:
#     print("il numero più grande è :" + str(a))
# elif b >= c & b >= a:
#     print("il numero più grande è :" + str(b))
# elif c >= b & c >= a:
#     print("il numero più grande è :" + str(c))


# 3))Scrivi un programma che, data una lista di numeri, fornisca in output il maggiore tra tutti gli elementi della lista.

# lista_numeri = [18, 36, 4, 8, 11, 88, 45, 33]

# numero_maggiore = lista_numeri[6]

# for numero in lista_numeri:
#     if numero > numero_maggiore:
#         numero_maggiore = numero
# print("Il numero maggiore tra tutti è:", numero_maggiore)

#4)) Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.

# lettera = input("inserisci una lettera: ").lower()
# vocali = "aeiou"
# if lettera in vocali :
#     o
# if lettera in ["a", "e", "i", "o", "u"] :
#     print((lettera) + " è una vocale")
# else :
#     print((lettera) + " è una consonante")


#5)) Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.

# Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

# lista_numeri = [10, 15, 20, 30, 25, 35, 40]

# somma_finale = 0

# for numero in lista_numeri :
#     somma_finale += numero
# print("il risultato finale è : " + str(somma_finale))

# 6))Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.

# lista_numeri = [2, 5, 4, 3]

# moltiplicazione = 1

# for numero in lista_numeri :
#     moltiplicazione *= numero
# print(str(moltiplicazione) + " questo è il risultato")

# 7))Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.
# Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.

# elemento = "cane"

# lista_elementi = ["gatto", "pappagallo", "coccodrillo", "ornitorinco", "pino"]

# for nome in lista_elementi :
#     if elemento == nome :
#         print("l'elemento " + (elemento) + " è presente nella lista")
#         break
#     else :
#         print("l'elemento non è presente")
    
        # molto più giusto V (quello sotto)

# lista = ['Marco', 'Luigi', 'Paolo', 'Giuseppe', 'Maria']
# el = input("Inserisci un nome da cercare: ").lower()
# trovato = False
# for nome in lista:
#     if nome.lower() == el:
#         trovato = True
#         break
# if trovato:
#     print((el) + " è presente nella lista " )
# else:
#     print(f"{el} non è presente nella lista.")


# 8))Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
# Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
# ***
# *******
# *********
# *****

# def istogramma(lista):
#     for numero in lista:
#         print("*" * numero)


# 9)) Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!

# def lunghezza():
#     parola = input("inserisci la parola che desideri: ")
#     lunghezza_parola = len(parola)
#     print(f"la lunghezza della parola digitata è {lunghezza} lettere")

# lunghezza()

# def lunghezza(array, parola):
#     lunghezza_array = len(array)
#     lunghezza_parola = len(parola)
#     print(lunghezza_array, lunghezza_parola)

# lunghezza(["tu", "noi", "voi", 3, 3.5, True], "ciao")    

# def lunghezza():
#     parola = "ciao"
#     lenght = 0
#     for lettera in parola :
#         lenght += 1
#     print(lenght)

# lunghezza()

# def my_len(lst_or_str):
#     length = 0
#     for unit in lst_or_str:
#         length += 1
#     return length
#     print(length)

# my_len("canee")

# 10))Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
# Questo esercizio può essere risolto anche usando una list comprehension.
                
# lista_a = ["ciao", "hello", "HEJ", "privet"]
# lista_b = []
# for parola in lista_a:
#         lista_b.append(len(parola))
# print(lista_b)

# def char_counter(lista_a):
#     lista_b = []
#     for parola in lista_a:
#         lista_b.append(len(parola))
#     return lista_b
# risultato = char_counter(["ciao", "hello", "HEJ", "privet"])
# print(risultato)

# 11))Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
# Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}

# def freguenza(parola):
#         comparsa = {}
#         for lettera in parola :
#                 if lettera in comparsa :
#                         comparsa[lettera] += 1
#                 else :
#                         comparsa [lettera] = 1
#         return comparsa

# risultato = freguenza("aabbbcdeaca")
# print(risultato)

# 12))Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici. Come risolverai questo esercizio?

# def converti (metri) :
#         miglia = metri * 0.0006
#         iarde = metri * 1.09361296
#         piedi = metri * 3.2808388799999997
#         pollici = metri * 39.370066559999997935

#         frase_finale = print(f"{metri} corrispondono a :\n {miglia} miglia \n {iarde} iarde \n {piedi} piedi \n {pollici} pollici")
#         return frase_finale

# print(converti(35000))


# 13))Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.

# def converti(giorni, ore, minuti) :
#         giorni_secondi = giorni * 86400
#         ore_secondi = ore * 3600
#         minuti_secondi = minuti * 60
#         secondi = (giorni_secondi + ore_secondi + minuti_secondi)
#         return secondi

# risultato = converti(int(input("inserisci giorni: ")), int(input("inserisci ore: ")), int(input("inserisci minuti: ")))
# print(risultato)


# 14))Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
        # un cerchio
        # un quadrato
        # un rettangolo
        # un triangolo
        # Sentitevi liberi di estendere le potenzialità della funzione quanto meglio credete!


# import math
# def calcolo(figura):
        
#         if figura == "cerchio" :
#                 raggio = float(input("definisci il raggio del tuo cerchio : "))
#                 area = ((raggio ** 2) * math.pi)
#         elif figura == "quadrato" :
#                 lato = float(input("definisci il lato del quadrato: "))
#                 area= (lato ** 2)
#         elif figura == "rettangolo" :
#                 base = float(input("definisci l'altezza del rettangolo: "))
#                 altezza = float(input("gefinisci la base del rettangolo: "))
#                 area = (base * altezza)
#         elif figura == "triangolo" :
#                 base = float(input("definisci l'altezza del triangolo: "))
#                 altezza = float(input("definisci la base del triangolo: "))
#                 area = ((base * altezza)/2)
#         else :
#                area = print("possiamo calcolare l'area solamente delle seguenti figure : \n cerchio \n quadrato \n triangolo \n rettangolo ") 

#         return area
        

# print(calcolo(input("seleziona una figura di cui vuoi calcolare l'area tra : \n cerchio \n quadrato \n rettangolo \n triangolo \n\n ---")))


# 15))Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.
# Un esempio di MAC è 02:FF:A5:F2:55:12.
# Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.


# import random

# def genera_mac():
#     char_set = "ABCDEF0123456789"
#     mac_addr = ""
#     due_punti = 0

#     for _ in range(6):
#         for _ in range(2):
#             mac_addr += random.choice(char_set)
#         if due_punti < 5:
#           mac_addr += ":"
#           due_punti += 1
#     print(mac_addr)   
#     return mac_addr
    

# genera_mac()

# 16)) Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.
# Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria! ;)

# import platform

# def sys_info():
#     print("Il Sistema attualmente in uso è: " + platform.system())
#     print("Info Release: " + platform.release())
# sys_info()


# 17)) Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.
# Anche in questo caso, usare una libreria potrebbe facilitare la risoluzione dell'esercizio!

# def converti_ascii(carattere):
#         conversione = ord(carattere)
#         print(conversione)
# converti_ascii("A")


# 18))Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, escluso sé stesso. Scrivi una funzione che verifichi se un numero è perfetto oppure no.

# def numero_perfetto(numero) :
#         numeri_divisori = []
#         lista_possibili = list(range(1, (numero - 1) +1))
#         for n in lista_possibili :
#                 if numero % n == 0 :
#                         numeri_divisori.append(n)
#         somma_divisori = 0
#         for n in numeri_divisori :
#                 somma_divisori += n
#         if somma_divisori == numero :
#                 print(f"il tuo numero : {numero} è un numero primo")
#         else :
#                 print("il numero che hai selezionato "  + str(numero) + " non è un numero primo \n ASINO")
        
#         print("può essere anche usata la funzione sum() per sommare l'interno dell'array")




# numero_perfetto(28)

# 19)) Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output solo i colori nella lista che iniziano con quella lettera.
# Suggerimento: potresti usare la funzione range e il metodo startswith().


# def scelta_colori():
        
#         print("gentile utente sei pregato di inserire 10 colori a tua scelta")
#         tutti_colori =  input("inserisci i colori separati da spazi : ")
#         colori_inseriti = tutti_colori.split()
#         input_iniziale = input("inserire una lettera per stampare i colori che iniziano per quella lettera : ")
#         for colore in colori_inseriti :
#                 iniziale = colore[0]
#                 if iniziale == input_iniziale :
#                   print(colore)
# scelta_colori()


# 20))Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while e li stampi con la funzione print senza andare a capo. 
# Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.


# def print_senza_andare_a_capo():
#     input_utente = input("Inserisci una stringa: ")
#     while input_utente != "":
#         print(input_utente, end=" ")
#         input_utente = input("Inserisci una stringa: ")

# print_senza_andare_a_capo()

# 21)) Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola.
# ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti. 
# La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.

# lista_studenti = [
#         {"nome": "luca", "cognome": "rossi", "classe": "1° A", "voti": [7, 5, 10, 8, 4, 9, 6]},
#         {"nome": "maria", "cognome": "bianchi", "classe": "1° B", "voti": [6, 5, 4, 8, 7, 3, 8]},
#         {"nome": "Luigi", "cognome": "verdi", "classe": "1° C", "voti": [8, 9, 10, 8, 7, 9, 7]},
#         {"nome": "Mario", "cognome": "gila", "classe": "1° A", "voti": [3, 5, 6, 5, 4, 6, 2]},
#         {"nome": "franco", "cognome": "verga", "classe": "1° A", "voti": [6, 4, 5, 10, 9, 9, 1]},
# ]
# # print(lista_studenti[0]["nome"])
# for studente in lista_studenti :
#         media = (sum(studente["voti"])) / len(studente["voti"])
#         studente["media"] = media
#         print("lo studente : " + (studente["nome"]) + " ha la media di : " + str(studente ["media"]))


# 22)) Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati degli utenti registrati su un sito web. 
# I dati richiesti per ogni utente sono: username, password, email e data di registrazione. Il programma deve permettere di salvare le informazioni nel file, leggere i dati e stamparli a schermo.


# import csv

# def crea_file_csv(dizionario, nome_file):
#     with open(nome_file, 'w', newline='') as file_csv:
#         writer = csv.writer(file_csv)
#         writer.writerow(['username', 'password', 'email', 'data_registrazione'])
#         for utente in dizionario.values():
#             writer.writerow([utente['username'], utente['password'], utente['email'], utente['data_registrazione']])

# def leggi_file_csv(nome_file):
#     with open(nome_file, 'r') as file_csv:
#         reader = csv.reader(file_csv)
#         for row in reader:
#             print(row)

# # Dizionario degli utenti
# utenti = {
#     1: {'username': 'piero', 'password': 'p4ssw0rd', 'email': 'mario@gmail.com', 'data_registrazione': '2023-01-01'},
#     2: {'username': 'lisa', 'password': 's3cr3t', 'email': 'luigi@yahoo.com', 'data_registrazione': '2023-01-02'},
#     3: {'username': 'rita', 'password': 'p3ach', 'email': 'princess@castle.com', 'data_registrazione': '2023-01-03'}
# }

# # Crea il file CSV
# crea_file_csv(utenti, 'utenti.csv')

# # Legge il file CSV e stampa i dati a schermo
# leggi_file_csv('utenti.csv')


# 23))Scrivi una funzione che permetta di inserire una canzone e salvarla in un file di testo. 
# Il programma deve chiedere all'utente di inserire il titolo e il testo della canzone, e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.
# Suggerimento: dovrai utilizzare l'istruzione with.



# def crea_canzone(titolo, testo):
#         nome_file = titolo + ".txt"
#         with open(nome_file, 'w') as file_testo:
#                 file_testo.write(testo)
#                 print(f"Il testo della canzone : {titolo} è inserito nel file : {nome_file}")
# titolo_canzone = input("insetrisci il titolo della canzone : ")
# testo_canzone = input("insetrisci il testo della canzone: ")

# crea_canzone(titolo_canzone, testo_canzone)


# con nano
# import subprocess
# def salva_testo_canzone(titolo):
#     nome_file = titolo + '.txt'
#     with open(nome_file, 'w') as file_testo:
#         subprocess.run(['nano', nome_file])
#     print(f"Testo della canzone '{titolo}' salvato in '{nome_file}'.")

# titolo_canzone = input("Inserisci il titolo della canzone: ")

# salva_testo_canzone(titolo_canzone)



# 24)) Scrivi una funzione che crei una tupla contenente i nomi dei pianeti del sistema solare, la loro tipologia (gassoso o roccioso) e il numero di satelliti naturali conosciuti. 
# Il programma deve quindi stampare a schermo il contenuto della tupla e il numero totale di satelliti.

# pianeti = (
#     ("Mercurio", "roccioso", 0),
#     ("Venere", "roccioso", 0),
#     ("Terra", "roccioso", 1),
#     ("Marte", "roccioso", 2),
#     ("Giove", "gassoso", 95),
#     ("Saturno", "gassoso", 83),
#     ("Urano", "gassoso", 27),
#     ("Nettuno", "gassoso", 14)
# )
# def info_pianeti():
#     # Stampa a schermo il contenuto della tupla
#     print("I pianeti del sistema solare sono:")
#     for pianeta in pianeti:
#         print(f"{pianeta[0]}: {pianeta[1]}, {pianeta[2]} satelliti")

#     # Calcola il numero totale di satelliti naturali
#     num_satelliti = sum(pianeta[2] for pianeta in pianeti)

#     # Stampa a schermo il numero totale di satelliti naturali
#     print(f"Il numero totale di satelliti naturali conosciuti nel sistema solare è di {num_satelliti}")

# info_pianeti()

# 25))Scrivi una funzione che prenda come argomento un set di sport preferiti dall'utente e stampi un messaggio di testo che indica se si tratta di uno sport di squadra o individuale.
# Suggerimento: per valutare la stringa inserita potrebbe essere utile utilizzare il metodo lower.

# def sport_preferito(sports) : 
#         sport_squadra = {"calcio", "basket", "rugby", "pallanuoto", "volley"}
#         sport_individuali = {"golf", "tennis", "freccette", "pugilato", "atletica", "surf"}

#         if sports.lower() in sport_squadra:
#                 print("lo sport selezionato è uno sport di squadra")
#         elif sports.lower() in sport_individuali:
#                 print("lo sport selezionato è uno sport individuale")
#         else:
#                 print("non lo so che sport è")

# seleziona_sport = input("seleziona il tuo sport preferito: ")
# sport_preferito(seleziona_sport)


# 1 I ))  In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto rövarspråket, che significa "linguaggio dei furfanti": 
# consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".
# Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in rövarspråket.
# Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente.


# def rovarspråket(parola):
#         vocali = ["a", "e", "i", "o", "u"]
#         nuova_parola = ""
        
#         for lettera in parola:
#                 if lettera not in vocali:
#                         nuova_parola += lettera + "o" + lettera
                        
#                 else:
#                         nuova_parola += lettera

#         print(f"la parola tradotta in rovarspråket è : \n {nuova_parola}" )
                
# nuova_parolaa = input("inserisci parola che vuoi tradurre in rövarspråket : ")
# rovarspråket(nuova_parolaa)


# def traduttore():
#     print("""
#     Ciao! questo programma traduce un testo passato in "rövarspråket".
#     Ció significa che raddoppia ogni consonante delle parole e ci mette una "o" in mezzo...
#     """)

#     vocali = "aeiou"

#     # volendo puoi ovviamente aggiungere ulteriori caratteri speciali alla lista...
#     specials = [" ", ",", ".", "?", "!", '"',"'"]

#     while True:
#         testo = input("\nInserisci il testo che desideri tradurre: ")
#         tradotta = ""
#         for x in testo:
#             if x in vocali or x in specials:
#                 tradotta += x
#             else:
#                 tradotta = tradotta + x + "o" + x

#         print(f"Ecco a te la traduzione! '{tradotta}'")

#         if input("\nDesidere tradurre un'altra frase? ") == "no":
#             break

# traduttore()


# 2 I))Scrivi una funzione a cui passerai come parametro una stringa, e che manderà in print una versione inversa (al contrario) della stessa stringa. Ad esempio "abcd" diventerà "dcba".
#      Suggerimento: per risolvere questo esercizio in modo compatto potresti usare lo slicing.

# def inverti(stringa):
#         stringa_invertita = stringa[::-1]
#         print(stringa_invertita)

# inverti("*cropoid")

# 3 I)) Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo (parole che si leggono uguali anche al contrario) oppure no.

# def palindromo(stringa):
#         stringa_invertita = stringa[::-1]
#         if stringa == stringa_invertita:
#                 print(f"la parola {stringa} è una parola palindroma")
#         else:
#                 print(f"la parola {stringa} non è una parola palindroma")

# nuova_parola = input("inserisci una parola per scoprire se palindroma : ").lower()
# palindromo(nuova_parola)


# 4 I))Scrivi una funzione generatrice di password.
# La funzione deve generare una stringa alfanumerica di 8 caratteri qualora l'utente voglia una password semplice, e di 20 caratteri ASCII qualora desideri una password più complicata.

# import string
# import random

# def password():

#         numeri_random = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#         lettere_random = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

#         lista_completa = [str(numero) for numero in numeri_random] + lettere_random

#         semplice_complicata = input("Generiamo delle password random \n se vuoi generare una password semplice digita S \n se vuoi generare una password più complicata digita C \n")
       
#         ascii_caratteri = string.digits + string.ascii_letters + string.punctuation

#         if semplice_complicata == "S":
#                 password_semplice =''.join(random.sample(lista_completa, 8))
#                 print(password_semplice)
#         elif semplice_complicata == "C":
#                 password_complicata =''.join(random.sample(ascii_caratteri, 20))
#                 print(password_complicata)


# password()


# 5 I))Scrivi una semplice funzione rimario, a cui viene passato un elenco di parole come parametro e che riceva una parola inserita dall'utente tramite la funzione input.
# La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle presenti nell'elenco passato, alla ricerca di rime, intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.
# Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.


# def rimario():
#         parola = input("inserisci una parola e vediamo se troviamo una rima ! : \n ")
#         with open('rocksyou.txt', 'r') as file:
#                 contenuto = file.readlines()
#         ultime_3_parola = parola[-3:]
#         for stringa in contenuto:
#                 ultime_3_stringa = stringa.strip()[-3:]
#                 if ultime_3_parola == ultime_3_stringa:
#                         print(f"questa parola fa rima con la parola : {parola} : {stringa}")
# rimario()

# 6 I))Scrivi una funzione vendi_libri(), che aiuti nella gestione della vendita di libri in una libreria:
# -Controlla se il libro richiesto è presente sugli scaffali della libreria
# -Qualora il libro sia presente, ne decrementa il numero di copie (eventualmente rimuovendo il titolo) e ci segnala che la vendita ha avuto successo
# -Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e ci viene comunicato che la vendita non ha avuto successo
# -La funzione deve restituire valore booleanoTrue o False in base all'esito della vendita.


# def vendi_libri():     
#         disponibili = [
#                 {'titolo': "il signore degli anellidi", 'N': 3},
#                 {'titolo': "harry fotter", 'N': 2},
#                 {'titolo': "cappuccetto rosso", 'N': 3},
#                 {'titolo': "topolino", 'N': 2},
#                 {'titolo': "one piece", 'N': 1},
#                 {'titolo': "le avventure di milena", 'N': 5},
#         ]
#         richiesta_libro = input("inserisci il libro che stai cercando: ")
#         trovato = False
#         darichiedere = []
#         for libro in disponibili:
#                 if richiesta_libro == libro['titolo']:
#                         print("il libro è disponibile in archivio desideri acquistarlo? ")
#                         trovato = True
#                         if input("S/N ") == "S":
#                                 libro['N'] -= 1
#                                 print(f"hai appena acquistato il libro : \n {libro['titolo']}  complimentoni deficente")
#                         else :
#                                 print(f"ci sono solo {libro['N']} copie disponibili affrettati cane")
#                         break
#         if trovato == False :
#                 print(f"il libro selezionato non è in archivio.\n Metteremo questo libro nella lista e proveremo a renderlo disponibile a breve")
#                 darichiedere.append(richiesta_libro)
#                 print(darichiedere)
                        
       
# vendi_libri()        


# 7 I))Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.
# Scrivi una semplice funzione in grado di criptare una stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.

# cifrario = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
#             'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
#             'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
#             'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
#             'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
#             'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
#             'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

# def cript():
#         frase=input("inserire la frase da criptare: ")
#         frase_criptata = ""
#         for carattere in frase:
#                 if carattere in cifrario:
#                         frase_criptata += cifrario[carattere]
#                 else:
#                         frase_criptata += carattere
#         print(frase_criptata)

# cript()


# 8 I))Scrivi una funzione che calcoli la somma (espressa in MB) delle dimensioni dei file presenti nella cartella di lavoro utilizzando il modulo os.


# import os

# directory_corrente = os.getcwd()
# files = os.listdir(directory_corrente)
# somma_file = []
# for file in files:
#         dimensioni_file = os.path.getsize(file)
#         somma_file.append(dimensioni_file)
# somma_file_mb = sum(somma_file)/ (1024 * 1024)
# print(somma_file_mb)



# 9 I)) Scrivi una funzione "postino" che sia in grado di spedire delle eMail tramite Gmail.
# Suggerimento: puoi usare il modulo smtplib.


# import smtplib

# def postino():
#     print("""
#     Questa è la funzione Postino: spedisce eMail utilizzando Gmail!
#     Server: smtp.gmail.com
#     Porta: 587
#     Si richiedono: Username, Password, Destinatario, Oggetto e Messaggio da inviare.
#     """)

#     username = input("Inserisci il tuo username: ")
#     password = input("Inserisci la tua password: ")
#     destinatario = input("Inserisci l'email del destinatario: ")
#     oggetto = input("Inserisci l'oggetto della mail: ")
#     messaggio = input("Ora puoi inserire il messaggio che vuoi inviare: ")
#     contenuto = f"Subject: {oggetto}\n\n{messaggio}"
#     print("Sto effettuando la connessione col Server...")
#     email = smtplib.SMTP("smtp.gmail.com",587)
#     email.ehlo()
#     email.starttls()
#     email.login(username,password)
#     print("Sto inviando...")
#     email.sendmail(username, destinatario, contenuto)
#     email.quit()
#     print("Messaggio Inviato!")
# postino()



# 10 I))   Scrivi una funzione "cercatrice" che scansioni un dato percorso di sistema alla ricerca di file di tipo pdf tramite il modulo os. La funzione dovrà avere le seguenti caratteristiche:
# Il percorso fornito dovrà essere anzitutto validato, in quanto deve portare a una cartella esistente
# La funzione dovrà fornire un elenco dei file pdf (con/relativo/percorso) man mano che questi vengono trovati
# In fine la funzione dovrà fornire in output il totale dei file .pdf che sono stati trovati durante la scansione.

# import os
# def cercatrice(percorso):
#         contatore = 0
#         if not os.path.isdir(percorso):
#                 print(f"il percorso {percorso} non risulta esistere. riprova.")
       
#         for cartella, sottocartella, files in os.walk(percorso):
#                 for file in files:
#                         if file.endswith(".txt"):
#                                 pdf = os.path.join(cartella,file)
#                                 print(f"Trovato file pdf: {pdf}\n")
#                                 contatore += 1
#                 print(f"\nScansione Ultimata! Ho trovato {contatore} files con estensione txt.")

# cercatrice('../../SecLists/Passwords')


# 11 I)) Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:
# Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente tramite input
# Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito, e qualora questa non fosse presente dovrà crearla
# La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare che non esiste
# Suggerimento: potresti importare i moduli os e shutil.

# import shutil
# import os 

# def backup(percorso, tipo):
#         if not os.path.isdir(percorso):
#                 print(f"il percorso {percorso} non è disponibile. Riprova rimastino che non sei altro.")
#         file_percorso = os.listdir(percorso)
#         file_giusti = []
#         file_stringa = ", ".join(file_giusti)                

#         contatore = 0
#         for file in file_percorso:
#                 if file.endswith(tipo):
#                         file_giusti.append(file)
#         for file in file_giusti:                
#                 if "backup" in file_percorso:
#                         print(f"c'è una cartella backup vuoi copiare il file all'interno della cartella? :")
#                         if input("S/N : ")=="S":
#                                  shutil.copy(percorso + file, '../../backup')
#                 else:
#                         os.mkdir(percorso + "backup")
#                         print("è stata creata una nuova cartella chiamata backup vuoi copiare i file qui? ")

#                         if input("S/N : ")=="S":
#                                 shutil.copy(percorso + file, '../../backup')


# backup('../../', '.txt')                


# 13 I))  Nella Successione di Fibonacci, ciascun numero è la somma dei due numeri che lo precedono, ad esempio:
# 1, 1, 2, 3, 5, 8, 13 (...)
# Scrivi una funzione ricorsiva che restituisce in output i numeri della successione di Fibonacci, entro una soglia specifica impostata dall'utente.


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
   
# limite = int(input("Inserisci il numero di valori della serie che desideri vedere: "))

# for num in range(1, limite+1):
#     print(fibonacci(num))
# fibonacci(10)


# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     print(fib)
# fibonacci(10)


# 14 I))Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare ciascuna lettera di una certa quantità di posti nell'alfabeto. 
# Per utilizzarlo, si sceglie una chiave che rappresenta il numero di posti di cui ogni lettera dell'alfabeto verrà spostata: 
# ad esempio, se si sceglie una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
# Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero di posti corrispondente alla chiave.
# Scrivi una funzione che riceva come argomento una stringa e un numero e applichi il Cifrario di Cesare alla stringa spostandosi nell'alfabeto di tante posizioni quante dice il numero.


# def cifrario(chiave, stringa):
#     alfabeto = 'abcdefghijklmnopqrstuvwxyz'
#     cifrata = ''
#     for let in stringa:
#         if let in alfabeto:
#             indice = alfabeto.index(let)
#             cifrata += alfabeto[indice - chiave]
#     print(cifrata)
# cifrario(8, 'gesu')


