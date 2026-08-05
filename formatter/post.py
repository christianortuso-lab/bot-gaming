def crea_post(offerta):

    prezzo = float(offerta["salePrice"])
    normale = float(offerta["normalPrice"])
    sconto = round(float(offerta["savings"]))

    return (
        f"🎮 <b>{offerta['title']}</b>\n\n"
        f"💰 <b>{prezzo:.2f} $</b>\n"
        f"🏷️ <s>{normale:.2f} $</s>\n"
        f"🔥 <b>-{sconto}%</b>\n\n"
        f"👇 <i>Acquista dal pulsante qui sotto</i>"
    )