from datetime import datetime

def log(messaggio):

    ora = datetime.now().strftime("%H:%M:%S")

    print(f"[{ora}] {messaggio}")