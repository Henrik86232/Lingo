import woorden
import random
import functions

spelen = True
streak = 0
wins = 0
losses = 0
potjes = 0
print("Welkom bij Lingo!")
while spelen:
# Random woord kiezen
    het_woord = random.choice(woorden.woorden)

# Aantal pogingen
    pogingen = 5

# Eerste letter tonen
    gevonden = [het_woord[0], "_", "_", "_", "_"]

    
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
            wins += 1
            streak += 1
            break
        else:
            pogingen -= 1
            print(f"Fout! Je hebt nog {pogingen} pogingen over.")
    else:
        print(f"Jammer, het woord was: {het_woord}")
        losses =+ 1  
        streak = 0
    potjes += 1
        # Opnieuw spelen?
    opnieuw = functions.opnieuw_spelen()
    if not opnieuw:
            spelen = False
            print(f"\nEindstand: {wins} wins, {losses} losses, {potjes} potjes gespeeld, huidige streak: {streak}") 