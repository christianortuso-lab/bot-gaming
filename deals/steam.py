import requests

API_URL = "https://www.cheapshark.com/api/1.0/deals"


def ottieni_offerte():

    risposta = requests.get(
        API_URL,
        params={
            "storeID": 1,
            "pageSize": 50,
            "sortBy": "Savings"
        },
        headers={
            "User-Agent": "GamingScontiItaliaBot/1.0"
        },
        timeout=15
    )

    risposta.raise_for_status()

    offerte = risposta.json()

    offerte_filtrate = []

    for offerta in offerte:

        titolo = offerta["title"]
        prezzo = float(offerta["salePrice"])
        sconto = float(offerta["savings"])
        voto = int(offerta["steamRatingPercent"])
        recensioni = int(offerta["steamRatingCount"])

        print(
            f"{titolo} | "
            f"{prezzo}€ | "
            f"{sconto:.1f}% | "
            f"{voto}% | "
            f"{recensioni} recensioni"
        )

        if prezzo > 20:
            print(" -> Scartato: prezzo troppo alto")
            continue

        if sconto < 85:
            print(" -> Scartato: sconto sotto il 85%")
            continue

        if voto < 75:
            print(" -> Scartato: voto Steam sotto il 75 %")
            continue

        if recensioni < 20:
            print(" -> Scartato: meno di 20 recensioni")
            continue

        print(" -> ACCETTATO\n")
        offerte_filtrate.append(offerta)

    print(f"\nTotale offerte filtrate: {len(offerte_filtrate)}")

    return offerte_filtrate