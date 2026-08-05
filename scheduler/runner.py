import time
import schedule


def avvia(funzione):

    schedule.every(1).minutes.do(funzione)

    print("Scheduler avviato.")
    print("Controllo ogni 1 minuto.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)