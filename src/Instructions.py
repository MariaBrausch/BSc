from enum import Enum
from textwrap import dedent

class Instructions(Enum):
    BEISPIELANTWORTEN = dedent("""
        Erstelle zu der folgenden Aufgabenstellung des Fachbereichs Kommunikation- und Rechnernetzwerke studentische Beispielantworten in den vorgegebenen Bewertungskategorien.Je Bewertungskategorie zwei Antworten. 
        Orientiere dich dabei an der angegebenen Musterlösung (Ground Truth) und den definierten Bewertungskriterien. 
        Achte darauf, dass die Antworten realistisch wie von Studierenden formuliert wirken.
    """)
    STRATEGIEA = dedent("""
        Du bekommst eine Aufgabenstellung, Bewertungsrubrik und eine studentische Antwort. Bewerte die studentische Antwort auf Basis der Bewertungsrubrik.
    """)