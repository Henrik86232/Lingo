def toon_woord(gevonden):
    print("Het woord:", " ".join(gevonden))


def vraag_input():
    return input("Voer een woord in: ").lower()


def valideer_input(gok):

    if len(gok) != 5:
        return False

    return True


def controleer_woord(gok, het_woord, gevonden):

    feedback = []

    for i in range(5):

        # Goede plek
        if gok[i] == het_woord[i]:

            feedback.append("🟩")

            gevonden[i] = gok[i]

        # Letter bestaat wel
        elif gok[i] in het_woord:

            feedback.append("🟨")

        # Letter bestaat niet
        else:

            feedback.append("⬜")

    return feedback


def toon_feedback(feedback):
    print("Feedback:", "".join(feedback))