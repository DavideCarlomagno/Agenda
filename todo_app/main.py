#--------------PREAMBOLO---CON---GLI---IMPORT--------------------------------------------------------

import sys
import os

# Aggiunta della cartella madre 'PYTHON' al path per poter importare il package 'myinput'
cartella_madre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if cartella_madre not in sys.path:
    sys.path.append(cartella_madre)

# Import delle funzioni di validazione dell'input dal modulo 'validate input'
from myinput.validate_input import int_input, date_input
import task_manager


#---------------CORPO---DEL---PROGRAMMINO------------------------------------------------------------

while True:

    print("." * 40, "\n")
    print("--TASKS MANAGER--".center(40),"\n")
    print("0 -> Leggi l'agenda \n"
          "1 -> Aggiungi un impegno in agenda \n"
          "2 -> Rimuovi un impegno dall'agenda \n"
          "3 -> Esci dal programma \n")
    print("." * 40, "\n")

    choice = int_input("Scegli cosa fare : ",0,3) #Funzione di controllo dell'input. Forza l'inserimento di un intero tra 0 e 3.

    if choice == 0:
        task_manager.todo_printer("todo.csv") #funzione di printing

    elif choice == 1:
        #CODICE PER AGGIUNGERE UN IMPEGNO IN AGENDA
        newDate = date_input("Inserisci una data: ", onlyFuture = True) #l'utente può inserire solo una data futura
        newTask = input("Inserisci una descrizione: ")

        task_manager.todo_append("todo.csv", newDate, newTask)


    elif choice == 2:
        #CODICE PER RIMUOVERE UNA RIGA DALL'AGENDA
        tasks = task_manager.todo_read("todo.csv") #leggo l'agenda e la salvo in una lista di dizionari.
        
        task_manager.todo_printer("todo.csv")
        cancelThisLine = int_input("Scegli l'impegno da cancellare digitando il suo numero di riga: ", 1, len(tasks)) #input validato
        
        task_manager.todo_remove("todo.csv", cancelThisLine - 1)

        print(f"Riga {cancelThisLine} rimossa con successo!")
    else:
        break

print("\n Fine. Arrivederci.")
