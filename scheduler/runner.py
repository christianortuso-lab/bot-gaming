import time
import schedule


def avvia(funzione):

    schedule.every(10).minutes.do(funzione)

    print("Scheduler avviato.")
    print("Controllo ogni 10 minuti.\n")

    while True:
        schedule.run_pending()
        time.sleep(1)