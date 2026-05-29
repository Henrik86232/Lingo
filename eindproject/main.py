import woorden
import random
import functions

# Random woord kiezen
het_woord = random.choice(woorden.woorden)

# Aantal pogingen
pogingen = 5

# Eerste letter tonen
gevonden = [het_woord[0], "_", "_", "_", "_"]

print("Welkom bij Lingo!")
while pogingen > 0:
    # Woord tonen
    functions.toon_woord(gevonden)
    # Input vragen
    gok = functions.vraag_input()
    # Input controleren
    if not functions.valideer_input(gok):
        print("Ongeldige invoer, probeer opnieuw.")
        continue
    # Woord controleren
    feedback = functions.controleer_woord(
        gok,
        het_woord,
        gevonden
    )
    # Feedback tonen
    functions.toon_feedback(feedback)

    # Win check
    if gok == het_woord:
        print("Goed geraden!")
        break
    else:
        pogingen -= 1
        print(f"Fout! Je hebt nog {pogingen} pogingen over.")
else:
    print(f"Jammer, het woord was: {het_woord}")