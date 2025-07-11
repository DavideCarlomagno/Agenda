#FUNZIONI DI MANIPOLAZIONE DELLE TASK
from datetime import datetime, date
#------------------------IMPORT DEL MIO PACKAGE MYINPUT---------------------------------------
import sys
import os

# Aggiunta della cartella madre 'PYTHON' al path per poter importare il package 'myinput'
cartella_madre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if cartella_madre not in sys.path:
    sys.path.append(cartella_madre)

# Import delle funzioni di validazione dell'input dal modulo 'validate input'
from myinput.validate_input import int_input
#---------------------------------------------------------------------------------------------

def todo_printer(todoFile):
    #funzione che prende l'agenda e la stampa a video.
    with open(todoFile) as todo: #apro il file csv per sola lettura
        tasks = todo_read(todoFile) #creo una lista dove gli elementi sono le righe della todo App PRESI COME DIZIONARI

    print("." * 40, "\n")
    print("--DAILY TASKS--".center(40), "\n")
    for i in range(len(tasks)):
        print(f"{i+1} --> {tasks[i]['Data'].strftime('%Y-%m-%d')} | {tasks[i]['Descrizione']}") #faccio dei print di tutte le task.
    print("\n")
    print("." * 40)

def todo_append(todoFile, newDate: datetime, newTask: str):
    # Apre il file in modalità append e aggiunge una riga correttamente formattata
    with open(todoFile, "a") as todo:
        # Aggiunge "\n" solo se il file non è vuoto
        if os.path.getsize(todoFile) > 0:
            todo.write("\n")
        todo.write(f"{newDate.strftime('%Y-%m-%d')},{newTask}")

    # Riordina l'agenda dopo l'aggiunta
    todo_sort(todoFile)

    print(f"Impegno inserito correttamente in agenda per il giorno: {newDate.strftime('%Y-%m-%d')}.")


def todo_read(todoFile) -> list:
    tasks = []
    with open(todoFile) as todo:
        for row in todo:
            row = row.strip()
            if not row: #se trova una riga vuota la salta
                continue
            parts = row.split(",", 1)
            raw_date = parts[0].split()[0]  # prendi solo la data senza orario
            dataTask = datetime.strptime(raw_date, "%Y-%m-%d")
            tasks.append({"Data": dataTask, "Descrizione": parts[1].strip()})
    return tasks



def todo_write(todoFile, rows: list):
    with open(todoFile, "w") as todo:
        for i, row in enumerate(rows):
            formatted_date = row['Data'].strftime("%Y-%m-%d")  # <-- conversione sicura
            line = f"{formatted_date},{row['Descrizione']}"
            if i != 0:
                todo.write("\n")  # Vai a capo solo da seconda riga in poi
            todo.write(line)


def todo_sort(todoFile):
    tasks = todo_read(todoFile) #leggo il file e creo la lista di dizionari
    tasks.sort(key = lambda x : x["Data"]) # tramite la lambda function, ordino la lista seguendo l'ordine cronologico della "data"
    todo_write(todoFile, tasks)

def todo_remove(todoFile, row : int):
    #funzione che permette all'utente di rimuovere un vecchio impegno in agenda.
    tasks = todo_read(todoFile) #Leggo le righe
    removed = tasks.pop(row) #Cancello la riga che vuole l'utente
    todo_write(todoFile, tasks) #riscrivo il file senza la riga omessa
    print(f"{removed} --> RIMOSSO CON SUCCESSO")

    
