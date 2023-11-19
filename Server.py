import socket
import mysql.connector

PASSWORD = "cogoleto"

connes = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Scuola",
    port=3306
)
cur = connes.cursor()

def setCRUD(parametri):
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    return clausole

def db_get_dipendenti(parametri):
    query = f"SELECT * FROM dipendenti where 1=1 {setCRUD(parametri)}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_get_zone(parametri):
    query = f"SELECT * FROM zone_di_lavoro where 1=1 {setCRUD(parametri)}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_elimina_dipendente(parametri):
    query = f"DELETE FROM dipendenti where 1=1 {setCRUD(parametri)}"
    cur.execute(query)
    connes.commit()

def db_elimina_zona(parametri):
    query = f"DELETE FROM zone_di_lavoro where 1=1 {setCRUD(parametri)}"
    cur.execute(query)
    connes.commit()

def db_inserisci_dipendente(parametri):
    query = f"INSERT INTO dipendenti (nome, cognome, posizione_lavorativa, data_assunzione, stipendio) VALUES ('{nome}','{cognome}','{posizione_lavorativa}','{data_assunzione}','{stipendio}')"
    cur.execute(query)
    connes.commit()

def db_inserisci_zona(parametri):
    query = f"INSERT INTO zone_di_lavoro (nome, n_clienti, Piano) VALUES ('{nome}','{n_clienti}','{Piano}')"
    cur.execute(query)
    connes.commit()

def db_modifica_dipendente(par):
    query = f"UPDATE dipendenti SET nome = '{nome}', cognome = '{cognome}', posizione_lavorativa = '{posizione_lavorativa}', data_assunzione = '{data_assunzione}', stipendio = '{stipendio}' WHERE ID = '{id_modifica}'"
    cur.execute(query)
    connes.commit()

def db_modifica_zona(par):
    query = f"UPDATE zone_di_lavoro SET nome = '{nome}', n_clienti = '{n_clienti}', Piano = '{Piano}' WHERE IDZ = '{id_modifica}'"
    cur.execute(query)
    connes.commit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50017))
s.listen()

print("In attesa di connessioni...")

conn, addr = s.accept()
print('Connected by', addr)
if __name__ == '__main__':
    for i in range(3):
        password = conn.recv(1024).decode()
        if password == PASSWORD:
            conn.send("Password corretta.".encode())
            break
        else:
            if i < 3:
                conn.send(f"Password errata.\n".encode())
            else:
                conn.send("Tentativi finiti, connessione chiusa.".encode())
                conn.close()
                exit()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break  
        if data == "5":
            break  

        if data == "1":
            
            scelta = conn.recv(1024).decode()
            if scelta == "1":
                nome = conn.recv(1024).decode()
                par = {"nome": nome}
                result = db_get_dipendenti(par)
                conn.send(str(result).encode())
            
            else:
                nome = conn.recv(1024).decode()
                par = {"nome": nome}
                result = db_get_zone(par)
                conn.send(str(result).encode())
        
        elif data == "2":

            scelta = conn.recv(1024).decode()
            if scelta == "1":
                id_elimina = conn.recv(1024).decode()
                par = {"ID": id_elimina}
                db_elimina_dipendente(par)
            
            else:
                id_elimina = conn.recv(1024).decode()
                par = {"IDZ": id_elimina}
                db_elimina_zona(par)
        
        elif data == "3":

            scelta = conn.recv(1024).decode()
            if scelta == "1":
                nome = conn.recv(1024).decode()
                cognome = conn.recv(1024).decode()
                posizione_lavorativa = conn.recv(1024).decode()
                data_assunzione = conn.recv(1024).decode()
                stipendio = conn.recv(1024).decode()
                par = {"nome": nome, "cognome": cognome, "posizione_lavorativa": posizione_lavorativa, "data_assunzione": data_assunzione, "stipendio": stipendio}
                db_inserisci_dipendente(par)
            else:
                nome = conn.recv(1024).decode()
                n_clienti = conn.recv(1024).decode()
                Piano = conn.recv(1024).decode()
                par = {"nome": nome, "n_clienti": n_clienti, "Piano": Piano}
                db_inserisci_zona(par)

        elif data == "4":

            scelta = conn.recv(1024).decode()
            if scelta == "1":
                id_modifica = conn.recv(1024).decode()
                nome = conn.recv(1024).decode()
                cognome = conn.recv(1024).decode()
                posizione_lavorativa = conn.recv(1024).decode()
                data_assunzione = conn.recv(1024).decode()
                stipendio = conn.recv(1024).decode()
                par = {"ID": id_modifica, "nome": nome, "cognome": cognome, "posizione_lavorativa": posizione_lavorativa, "data_assunzione": data_assunzione, "stipendio": stipendio}
                db_modifica_dipendente(par)
            else:
                id_modifica = conn.recv(1024).decode()
                nome = conn.recv(1024).decode()
                n_clienti = conn.recv(1024).decode()
                Piano = conn.recv(1024).decode()
                par = {"IDZ": id_modifica, "nome": nome, "n_clienti": n_clienti, "Piano": Piano}
                db_modifica_zona(par)

    conn.close()
