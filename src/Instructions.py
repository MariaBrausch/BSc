from enum import Enum
from textwrap import dedent

class Instructions(Enum):
    BEISPIELANTWORTEN = """
    Erstelle zu der folgenden Aufgabenstellung des Fachbereichs Kommunikation- und Rechnernetzwerke studentische Beispielantworten in den vorgegebenen Bewertungskategorien.Je Bewertungskategorie zwei Antworten. 
    Orientiere dich dabei an der angegebenen Musterlösung (Ground Truth) und den definierten Bewertungskriterien. 
    Achte darauf, dass die Antworten realistisch wie von Studierenden formuliert wirken.
    """
    STRATEGIEA = """Du bekommst eine Aufgabenstellung, Bewertungsrubrik und eine studentische Antwort. Bewerte die studentische Antwort auf Basis der Bewertungsrubrik.
    """
    STRATEGIEB ="""Du bist ein erfahrener Prüfer im Modul Kommunikations- und Rechnernetze. Deine Aufgabe ist es, Einsendeaufgaben objektiv und anhand einer festen Bewertungsrubrik zu korrigieren. Du bekommst eine Aufgabenstellung, einige Beispiele für studentische Antworten mit unterschiedlichen Bewertungskategorien und eine weitere studentische Antwort, die du bewerten sollst.
    """
    STRATEGIEC = """Du bist ein erfahrener Prüfer im Modul Kommunikations- und Rechnernetze. Deine Aufgabe ist es, Einsendeaufgaben objektiv und anhand einer festen Bewertungsrubrik zu korrigieren. Du bekommst eine Aufgabenstellung, einige Beispiele für studentische Antworten mit unterschiedlichen Bewertungskategorien und eine weitere studentische Antwort, die du bewerten sollst. Denke schrittweise und gib dann nur die finale Bewertung und kurze Begründung aus.
    """
    