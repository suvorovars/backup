import time
from mcrcon import MCRcon
from functions.recognize import *
from functions.synonimus import *
from functions.jarvis import *

# Настройки RCON и игрока
RCON_HOST, RCON_PORT, RCON_PASSWORD = "localhost", 25575, "admin"
PLAYER = "i_am_npc"

def main():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("слушаю шум")
        rec.adjust_for_ambient_noise(source, duration=2)
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        mcr.connect()
        print("Я готов к работе. Скажи 'майнкрафт' для начала диалога.")
        play_sound("sounds/start.wav")
        while True:
            wake = recognize_wake(rec, mic, 1)
            if "майнкрафт" in wake or "minecraft" in wake:
                mcr.command(f"say {PLAYER}, я слушаю...")
                play_sound("sounds/wake.wav")
                user_input = recognize_command(rec, mic)
                response, c = find_closest_command(user_input)
                if response:
                    response(mcr)
                    play_sound(f"sounds/response.wav")
            print(wake)

if __name__ == "__main__":
    main()
