import woorden
import random
import functions
import config

spelen = True
streak = 0
wins = 0
losses = 0
potjes = 0

print(config.WELKOM_BERICHT)

while spelen:
    het_woord = random.choice(woorden.woorden)

    pogingen = config.AANTAL_POGINGEN

    gevonden = [het_woord[0]] + ["_"] * (config.WOORD_LENGTE - 1)

    while pogingen > 0:
        functions.toon_woord(gevonden)

        gok = functions.vraag_input()

        if not functions.valideer_input(gok):
            print(config.ONGELDIGE_INVOER_BERICHT)
            continue

        feedback = functions.controleer_woord(
            gok,
            het_woord,
            gevonden
        )

        functions.toon_feedback(feedback)

        if gok == het_woord:
            print(config.GOED_GERADEN_BERICHT)
            wins += 1
            streak += 1
            break
        else:
            pogingen -= 1
            print(f"Fout! Je hebt nog {pogingen} pogingen over.")
    else:
        print(f"Jammer, het woord was: {het_woord}")
        losses += 1
        streak = 0

    potjes += 1

    opnieuw = functions.opnieuw_spelen()
    if not opnieuw:
        spelen = False
        print(
            f"\nEindstand: {wins} wins, {losses} losses, "
            f"{potjes} potjes gespeeld, huidige streak: {streak}"
        )