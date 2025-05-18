from functions.jarvis import *

def time_day(mc):
    mc.command("time set day")
    print("Day!")


def time_night(mc):
    mc.command("time set night")
    print("Теперь ночь!")


def apocalypse(mc):
    mc.command("weather thunder")
    mc.command("time set midnight")
    mc.command("summon lightning_bolt")


def say_about_Vanko(mc):
    mc.command("say Я Ваня!")
    play_sound("sound/story_vanko.wav")

commands = {
    "сделать день": time_day,
    "сделать ночь": time_night,
    "включи апокалипсис": apocalypse,
    "расскажи про Ивана Ванко": say_about_Vanko,
}
