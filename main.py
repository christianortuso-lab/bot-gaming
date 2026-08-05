import time

from deals.steam import ottieni_offerte
from formatter.post import crea_post
from telegram_bot.sender import invia
from utils.database import (
    crea_database,
    offerta_esiste,
    salva_offerta
)


def controlla_offerte():

    from datetime import datetime
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Nuovo controllo...")

    crea_database()

    offerte = ottieni_offerte()

    if not offerte:
        print("Nessuna offerta trovata.")
        return

    pubblicati = 0

    for offerta in offerte:

        if pubblicati >= 3:
            print("Limite di 3 offerte raggiunto.")
            break

        print(f"Controllo: {offerta['title']}")

        codice = offerta["dealID"]

        if offerta_esiste(codice):
            print(f"Già pubblicata: {offerta['title']}")
            continue

        testo = crea_post(offerta)

        link = f"https://www.cheapshark.com/redirect?dealID={offerta['dealID']}"

        invia(
            testo,
            offerta["thumb"],
            link
        )

        salva_offerta(
            codice,
            offerta["title"],
            float(offerta["salePrice"])
        )

        pubblicati += 1

        print(f"Pubblicata: {offerta['title']}")

        time.sleep(5)


from scheduler.runner import avvia

if __name__ == "__main__":

    controlla_offerte()

    avvia(controlla_offerte)