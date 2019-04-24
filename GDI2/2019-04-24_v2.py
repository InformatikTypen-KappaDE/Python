score=0.0

def getAnswer(eingabe, richtige, punkte):
    if eingabe==richtige:
        print("Richtig, gut gemacht!")
        return punkte
    else:
        print("Falsch")
        return 0.0

def getAnswer2(eingabe, richtige, punkte, score):
    tempScore=0.0
    if eingabe==richtige:
        print("Richtig, gut gemacht!")
        tempScore=punkte
    else:
        print("Falsch")
        tempScore=0.0

    score += tempScore
         
    
def platzhalter():
    print()
    print("Aktueller Punktestand: " + str(score))
    print()

    

#FRAGE 1
print("Was bedeutet Kirmes?")
print("a) Spielplatz")
print("b) Spelunke")
print("c) Meyenburg, Schwanewede, Niedersachen, DE")
print("d) Freimarkt")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
getAnswer2(eingabe=input(), richtige="d", punkte=1.0, score=score)
platzhalter()


#FRAGE 2
print("Wer ist die fleißigste Person im EU-Parlament?")
print("a) Elmar Brocken")
print("b) Martin Sonneborn")
print("c) Manfred Streber")
print("d) Axel Voss (The Vozz)")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
getAnswer2(eingabe=input(), richtige="b", punkte=5.0, score=score)
platzhalter()


#FRAAGE 3
print("Wo sind wir?")
print("a) Universität Bremen")
print("b) Bayern")
print("c) Meyenburg, Schwanewede, Niedersachen, DE")
print("d) Weiß ich doch nicht! (sicher?)")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
getAnswer2(eingabe=input(), richtige="a", punkte=2.5, score=score)
platzhalter()


#FRAGE 4
print("Was bedeutet kommod?")
print("a) groß")
print("b) breit")
print("c) klein")
print("d) bequem")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
getAnswer2(eingabe=input(), richtige="d", punkte=0.5, score=score)
platzhalter()


#Frage 5
print("Kranbauplätze müssen...")
print("a) ...tief sein.")
print("b) ...weich sein.")
print("c) ...lecker sein.")
print("d) ...verdichtet sein.")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
getAnswer2(eingabe=input(), richtige="d", punkte=3.5, score=score)
platzhalter()


print("Fertig. Ihre Punkte: " + str(score) + ".")

if score==0:
    print("WASTED...")