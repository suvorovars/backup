import speech_recognition as sr


def recognize_wake(rec, mic, timeout=1):
    with mic as source:
        audio = rec.listen(source, phrase_time_limit=timeout)
    try:
        return rec.recognize_google(audio, language="ru-RU").lower()
    except:
        return ""


def recognize_command(rec, mic, timeout=3):
    with mic as source:
        audio = rec.listen(source, phrase_time_limit=timeout)
    try:
        return rec.recognize_google(audio, language="ru-RU").lower()
    except:
        return ""