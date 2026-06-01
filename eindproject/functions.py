def toon_woord(gevonden):
    print("Het woord:", " ".join(gevonden))

def vraag_input():
    return input("Voer een woord in: ").lower()

def valideer_input(gok):
    if len(gok) != 5:
        return False
    return True

def controleer_woord(gok, het_woord, gevonden):
    feedback = ["⬜"] * 5
    # Woord omzetten naar lijst
    resterende_letters = list(het_woord)
    # Eerst groene letters controleren
    for i in range(5):
        if gok[i] == het_woord[i]:
            feedback[i] = "🟩"
            gevonden[i] = gok[i]
            # Letter verwijderen zodat hij niet dubbel telt
            resterende_letters[i] = None
    # Daarna gele letters controleren
    for i in range(5):
        # Alleen als niet al groen
        if feedback[i] == "⬜":
            if gok[i] in resterende_letters:
                feedback[i] = "🟨"
                # Verwijderen zodat hij niet opnieuw gebruikt wordt
                resterende_letters[
                    resterende_letters.index(gok[i])
                ] = None
    return feedback

def toon_feedback(feedback):
    print("Feedback:", "".join(feedback))

def opnieuw_spelen():
    opnieuw = input("\nNog een keer spelen? (ja/nee): ").lower()
    if opnieuw != "ja":
        print("Bedankt voor het spelen!")
        return False
    return True
        