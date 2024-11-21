import random


def juokelis():
    klausimai = [
        "Kodėl programuotojai nemėgsta gamtos?",
        "Ką pasakė kodas, kai jam buvo liūdna?",
        "Kodėl Python programuotojas visada laimi?",
        "Ką pasakė bitas kitam bitui per vakarėlį?"
    ]

    atsakymai = [
        "Nes ten per daug klaidų (bugs).",
        "Man reikia daugiau 'debug'.",
        "Nes jie visada žino, kaip apeiti klaidas.",
        "Leisk pasukti tau galvą (bit)."
    ]

    pasirinkimas = random.randint(0, len(klausimai) - 1)
    return klausimai[pasirinkimas] + " " + atsakymai[pasirinkimas]

print(juokelis())