import os
import sqlite3

DATABASE = os.path.join(os.path.dirname(__file__), "..", "database.db")


def crea_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS offerte(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        codice TEXT UNIQUE,

        titolo TEXT,

        prezzo REAL

    )
    """)

    conn.commit()

    conn.close()

    print("Database pronto!")


def offerta_esiste(codice):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT codice FROM offerte WHERE codice=?",
        (codice,)
    )

    risultato = cursor.fetchone()

    conn.close()

    return risultato is not None


def salva_offerta(codice, titolo, prezzo):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO offerte(codice, titolo, prezzo)
        VALUES (?, ?, ?)
        """,
        (codice, titolo, prezzo)
    )

    conn.commit()
    conn.close()