from enum import Enum

class AufgabenTyp(str, Enum):
    FREITEXT = "freitext"
    ZUORDNUNG = "zuordnung"
    FORMEL_ZAHL = "formel_zahl"
    BEISPIELE = "beispiele"
    RECHENAUFGABE = "rechenaufgabe"
    FACHBEGRIFF = "fachbegriff"


kriterien_pro_aufgabe = {
    AufgabenTyp.FREITEXT: [
        "Inhaltliche Korrektheit", "Vollständigkeit", "Struktur", "Nachvollziehbarkeit"
    ],
    AufgabenTyp.ZUORDNUNG: [
        "Korrektheit der Zuordnung", "Vollständigkeit"
    ],
    AufgabenTyp.FORMEL_ZAHL: [
        "Numerische Genauigkeit", "Einheiten", "Formel wird in LaTeX Form angegeben"
    ],
    AufgabenTyp.BEISPIELE: [
        "Anzahl und Richtigkeit der Beispiele", "thematische Relevanz"
    ],
    AufgabenTyp.RECHENAUFGABE: [
        "Richtiges Ergebnis", "korrekter Rechenweg", "Einheiten"
    ]
}

kategorien_pro_aufgabe = {
    AufgabenTyp.FREITEXT: ["korrekt", "teilweise inkorrekt", "inkorrekt"],
    AufgabenTyp.ZUORDNUNG: ["korrekt", "teilweise inkorrekt", "inkorrekt"],
    AufgabenTyp.FORMEL_ZAHL: ["korrekt", "inkorrekt"],
    AufgabenTyp.BEISPIELE: ["korrekt", "teilweise inkorrekt", "inkorrekt"],
    AufgabenTyp.RECHENAUFGABE: ["korrekt", "teilweise inkorrekt", "inkorrekt"]
}

rubriken_pro_aufgabe = {
    AufgabenTyp.FREITEXT: ["Korrekt: Die Antwort ist inhaltlich richtig, vollständig, gut strukturiert und nachvollziehbar.",
                        "Teilweise inkorrekt: Die Antwort enthält kleinere Fehler oder Auslassungen, ist aberüberwiegend korrekt. Struktur und Nachvollziehbarkeit sind teilweise gegeben.",
                        "Inkorrekt: Die Antwort enthält gravierende inhaltliche Fehler oder lässt zentrale Punkte aus. Struktur und Nachvollziehbarkeit sind stark beeinträchtigt."
                        ],
    AufgabenTyp.ZUORDNUNG: ["Korrekt: Alle Zuordnungen sind vollständig und fehlerfrei richtig vorgenommen.",
                        "Teilweise inkorrekt: Ein Teil der Zuordnungen ist richtig, jedoch sind einige Elemente falsch oder nicht zugeordnet. Mindestens eine richtige Zuordnung ist vorhanden.",
                        "Inkorrekt: Die meisten Zuordnungen sind falsch oder es wurde keine sinnvolle Zuordnung vorgenommen."
                        ],
    AufgabenTyp.FORMEL_ZAHL: ["Korrekt: Die Formel ist korrekt angegeben, die Zahl ist genau und die Einheiten sind richtig.",
                           "Inkorrekt: Die Formel ist falsch, die Zahl ist ungenau oder die Einheiten sind falsch."
                          ],
    AufgabenTyp.BEISPIELE: ["Korrekt: Alle geforderten Beispiele sind korrekt, relevant und vollständig.",
                        "Teilweise inkorrekt: Einige Beispiele sind korrekt und relevant, aber es fehlen wichtige oder einige sind falsch.",
                        "Inkorrekt: Die Beispiele sind größtenteils falsch, irrelevant oder es wurden keine sinnvollen Beispiele gegeben."
                        ],  

    AufgabenTyp.RECHENAUFGABE: ["Korrekt: Das Ergebnis ist richtig, der Rechenweg ist vollständig und korrekt dargestellt, und die Einheiten sind korrekt angegeben.",
                             "Teilweise inkorrekt: Das Ergebnis ist teilweise richtig, der Rechenweg enthält kleinere Fehler oder Auslassungen, oder die Einheiten sind teilweise falsch.",     
                             "Inkorrekt: Das Ergebnis ist falsch, der Rechenweg ist fehlerhaft oder unvollständig, und die Einheiten sind größtenteils falsch."
                            ]


}

