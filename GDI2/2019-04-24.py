


#variable für den score
score=0.0

#funktion um die frage und antwort zu verarbeiten
def getAnswer(richtige, punkte, bauerntipp="Kein Tipp, zu einfach!"):
    print("Mögliche Punkte in dieser Aufgabe: " + str(punkte) + ".")
    eingabe=input()
    if eingabe==richtige:
        print("Richtig, gut gemacht!")
        return punkte
    elif eingabe!="a" and eingabe !="b" and eingabe !="c" and eingabe !="d":
        print("Komische Eingabe...")
        print("Lieber zur nächsten Aufgabe, diese ist verloren.")
        return 0.0
    else:
        print("Falsch, versuchs noch mal, hier noch ein Tipp: ")
        print(str(bauerntipp))
        print()
        trys=0
        while trys<1:
            if richtige==input():
                print("Richtig! Immerhin noch geschafft... (aber nur halbe Punktzahl)")
                return punkte/2
            else:
                trys += 1
                print("Falsch, auch beim zweiten Versuch!")
                return 0.0
         
#funktion für ausgabe nachdem die antwort geprüft wurde
def platzhalter():
    print()
    print("Aktueller Punktestand: " + str(score))
    print()
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print()

#unterschiedliche "bewertungen" je nach erreichten punkten
def getBewertung(score, maxPunkte=12.5):
    percentage=score/maxPunkte

    if percentage>=0.8:
        return "Ja mei, das haben sie ja gut gemacht."
    elif percentage>=0.6:
        return "Joa, dat is schon jut gegangen."
    elif percentage>=0.4:
        return "Knappe Kiste, ganz knappe Kiste..."
    elif percentage>=0.2:
        return "Das hätte selbst der Ronny besser gemacht."
    else:
        return "... ich bin enttäuscht..."
    

#quizablauf

#überschrift
print("Allgemeinwissensprüfung in diversen Themen: Teil A")
print("--------------------------------------------------")
print()


#FRAGE 1
print("Was bedeutet Kirmes?")
print("a) Spielplatz")
print("b) Spelunke")
print("c) Meyenburg, Schwanewede, Niedersachen, DE")
print("d) Freimarkt")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
score += getAnswer(richtige="d", punkte=1.0)
platzhalter()


#FRAGE 2
print("Wer ist die fleißigste Person im EU-Parlament?")
print("a) Elmar Brocken")
print("b) Martin Sonneborn")
print("c) Manfred Streber")
print("d) Axel Voss (The Vozz)")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
score += getAnswer(richtige="b", punkte=5.0, bauerntipp="Nicht a, c und d! (Allgemeinwissen)")
platzhalter()


#FRAAGE 3
print("Wo sind wir?")
print("a) Universität Bremen")
print("b) Bayern")
print("c) Meyenburg, Schwanewede, Niedersachen, DE")
print("d) Weiß ich doch nicht! (sicher?)")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
score += getAnswer(richtige="a", punkte=2.5)
platzhalter()


#FRAGE 4
print("Was bedeutet kommod?")
print("a) groß")
print("b) breit")
print("c) klein")
print("d) bequem")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
score += getAnswer(richtige="d", punkte=0.5)
platzhalter()


#Frage 5
print("Kranbauplätze müssen...")
print("a) ...tief sein.")
print("b) ...weich sein.")
print("c) ...lecker sein.")
print("d) ...verdichtet sein.")
print("Welche Antwort ist korrekt? Schreiben Sie den Buchstaben der Antwort.")
score += getAnswer(richtige="d", punkte=3.5, bauerntipp="Kranfahrer Ronny hats den Norwegern schon erklärt.")
platzhalter()


#abschlussausgabe
print("Fertig. Ihre Punkte: " + str(score) + ". " + "Das Resultiert in folgender Bewertung: ")
print(getBewertung(score=score))
print("____________________________________________________________________________________________________________")
print()