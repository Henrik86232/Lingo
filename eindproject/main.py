import woorden, random, math

het_woord = "baard"
pogingen = 5

print("Welkom bij Lingo!")
while pogingen > 0:
    gok = input("Voer een woord in: ")
    if len(gok) != 5:
        print("Ongeldige invoer, probeer opnieuw.")
        continue

    feedback = []
    for i in range(5):
        if gok[i] == het_woord[i]:
            feedback.append("🟩")
        elif gok[i] in het_woord:
            feedback.append("🟨")
        else:
            feedback.append("⬜")

    print("Feedback:", feedback)

    if gok == het_woord:
        print("Goed geraden!")
        break

    else:
        pogingen -= 1
        print(f"Fout! Je hebt nog {pogingen} pogingen over.")
else:
    print(f"Jammer, het woord was: {het_woord}")