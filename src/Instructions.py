from enum import Enum
from textwrap import dedent

class Instructions(Enum):
    BEISPIELANTWORTEN = """
    Erstelle zu der folgenden Aufgabenstellung des Fachbereichs Kommunikation- und Rechnernetzwerke studentische Beispielantworten in den vorgegebenen Bewertungskategorien.
    Orientiere dich dabei an der angegebenen Musterlösung (Ground Truth) und den definierten Bewertungskriterien. 
    Strikte Regeln:
    Gib in jeder Kategorie genau zwei Antworten.
    Du bist Student und weißt nicht was du falsch machst.
    Keine Erklärungen, keine Kommentare, keine Hinweise auf Fehler oder Richtigkeit.
    Keine Selbstreflexion.
    In der Kategorie inkorrekt und teilweise inkorrekt sollst du das falsche Ergebnis so begründen, als würdest du denken es wäre richtig.



    Ausgabeformat: 
    ### bewertungskategorie: korrekt 
    **antwort 1**
    **antwort 2**
    ### bewertungskategorie: teilweise inkorrekt 
    **antwort 1**
    **antwort 2**
    ### bewertungskategorie: inkorrekt 
    **antwort 1**   
    **antwort 2**
    """
    STRATEGIEA = """
    Du bekommst eine Aufgabenstellung, Bewertungsrubrik und eine studentische Antwort. Bewerte die studentische Antwort auf Basis der Bewertungsrubrik.
    Ausgabeformat:
    ### bewertungskategorie: <korrekt/teilweise inkorrekt/inkorrekt>
    """
    STRATEGIEB ="""Du bist ein erfahrener Prüfer im Modul Kommunikations- und Rechnernetze. Deine Aufgabe ist es, Einsendeaufgaben objektiv und anhand einer festen Bewertungsrubrik zu korrigieren. Du bekommst eine Aufgabenstellung, einige Beispiele für studentische Antworten mit unterschiedlichen Bewertungskategorien und eine weitere studentische Antwort, die du bewerten sollst.
    """
    STRATEGIEC = """Du bist ein erfahrener Prüfer im Modul Kommunikations- und Rechnernetze. Deine Aufgabe ist es, Einsendeaufgaben objektiv und anhand einer festen Bewertungsrubrik zu korrigieren. Du bekommst eine Aufgabenstellung, einige Beispiele für studentische Antworten mit unterschiedlichen Bewertungskategorien und eine weitere studentische Antwort, die du bewerten sollst. Denke schrittweise und gib dann nur die finale Bewertung und kurze Begründung aus.
    """
    