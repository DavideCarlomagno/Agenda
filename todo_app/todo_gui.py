#INTERFACCIA UTENTE DEL MIO PROGRAMMINO. Programmata tramite la libreria built-in di python "tkinter".
#la gui sostituisce interamente il main vecchio, che pertanto risulterà superfuluo.

#Importo il package di TKINTER:
import tkinter as tk
from tkinter import messagebox
#Importo tutta la logica del mio programma:
import task_manager
from datetime import datetime
#------------------------------------------

#FINESTRA E TITOLO-------------------------
root = tk.Tk() #creo la finestra principale
root.title("ToDo App") #la chiamo ToDo App
#------------------------------------------

#AREA DI VISUALIZZAZIONE ELENCO TASK-------
tasksList = tk.Listbox(root, width = 50, height = 15) #creo lo spazio dove andranno le task
tasksList.pack(padx = 10, pady = 10) #impongo dei margini


#FUNZIONI DELLA GUI------------------------
def aggiorna_lista(): #Funzione che mi aggiorna la lita nella sua area di visualizzazione ogni volta che la chiamo
    tasksList.delete(0, tk.END)  # Pulisce la lista
    tasks = task_manager.todo_read("todo.csv")   # Legge le task dal file
    for task in tasks:
        tasksList.insert(tk.END, f"{task['Data'].strftime('%Y-%m-%d')} | {task['Descrizione']}")  # Inserisce in lista

def aggiungi_task(): # Funzione chiamata quando si clicca su "Aggiungi Task"
    data_str = entry_data.get().strip()
    descrizione = entry_descrizione.get().strip()

    # Validazione base
    if not data_str or not descrizione:
        messagebox.showwarning("Campi mancanti", "Inserisci sia la data che la descrizione.")
        return

    try:
        nuova_data = datetime.strptime(data_str, "%Y-%m-%d").date()
        if nuova_data < datetime.today().date():
            messagebox.showerror("Data non valida", "Inserisci una data futura o di oggi.")
            return
    except ValueError:
        messagebox.showerror("Formato errato", "La data deve essere nel formato YYYY-MM-DD.")
        return

    # Se tutto va bene, aggiungi la task
    task_manager.todo_append("todo.csv", nuova_data, descrizione)
    entry_data.delete(0, tk.END)
    entry_descrizione.delete(0, tk.END)
    aggiorna_lista()

def remove_task(): #funzione che permette di rimuovere le task dalla lista
    # Ottieni la selezione (una tupla, anche se selezioni una sola riga)
    selected = tasksList.curselection()

    if not selected:
        messagebox.showwarning("Attenzione", "Seleziona prima una task da rimuovere.")
        return

    # Indice della task da rimuovere
    index = selected[0]

    # Conferma con l’utente (facoltativo ma utile)
    conferma = messagebox.askyesno("Conferma", "Sei sicuro di voler rimuovere questa task?")
    if not conferma:
        return

    # Rimuovi la riga dal file
    task_manager.todo_remove("todo.csv", index)

    # Aggiorna la listbox
    aggiorna_lista()

# Bottone per aggiornare manualmente la lista
aggiorna_btn = tk.Button(root, text="Aggiorna lista", command=aggiorna_lista)
aggiorna_btn.pack(pady=5)

#CAMPI PER L'INSERIMENTO DI UNA NUOVA DATA:
# Etichetta e campo per la data
label_data = tk.Label(root, text="Data (YYYY-MM-DD):")
label_data.pack()
entry_data = tk.Entry(root)
entry_data.pack()
# Etichetta e campo per la descrizione
label_descrizione = tk.Label(root, text="Descrizione:")
label_descrizione.pack()
entry_descrizione = tk.Entry(root, width=50)
entry_descrizione.pack()


#BOTTONI:----------------------------------
# Bottone per aggiungere la task
btn_aggiungi = tk.Button(root, text="Aggiungi task", command=aggiungi_task)
btn_aggiungi.pack(pady=10)

remove_button = tk.Button(root, text="Rimuovi Task", command=remove_task)
remove_button.pack(pady=5)
#------------------------------------------

# Carichiamo subito la lista all'avvio
aggiorna_lista()
root.mainloop() # comando da posizionare alla fine del foglio SEMPRE. fa si che venga aperta la finestra finche l'utente non la chiude.