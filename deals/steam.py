import requests

API_URL = "https://www.cheapshark.com/api/1.0/deals"


def ottieni_offerte():

    risposta = requests.get(
        API_URL,
        params={
            "storeID": 1,
            "pageSize": 30,
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

        if float(offerta["salePrice"]) > 10:
            continue

        if float(offerta["savings"]) < 90:
            continue

        if int(offerta["steamRatingPercent"]) < 80:
            continue

        if int(offerta["steamRatingCount"]) < 100:
            continue

        offerte_filtrate.append(offerta)

    return offerte_filtrate