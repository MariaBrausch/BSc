from enum import Enum

class TaskType(str, Enum):
    FREITEXT = "freitext"
    ZUORDNUNG = "zuordnung"
    FORMEL_ZAHL = "formel_zahl"
    BEISPIELE = "beispiele"
    RECHENAUFGABE = "rechenaufgabe"
    FACHBEGRIFF = "fachbegriff"


task_criteria = {
    TaskType.FREITEXT: [
        "Inhaltliche Korrektheit", "Vollständigkeit", "Struktur", "Nachvollziehbarkeit"
    ],
    TaskType.ZUORDNUNG: [
        "Korrektheit der Zuordnung", "Vollständigkeit"
    ],
    TaskType.FORMEL_ZAHL: [
        "Numerische Genauigkeit", "Einheiten", "Formel wird in LaTeX Form angegeben"
    ],
    TaskType.BEISPIELE: [
        "Anzahl und Richtigkeit der Beispiele", "thematische Relevanz"
    ],
    TaskType.RECHENAUFGABE: [
        "Richtiges Ergebnis", "korrekter Rechenweg", "Einheiten"
    ]
}

task_categories = {
    TaskType.FREITEXT: ["korrekt", "teilweise inkorrekt", "inkorrekt"],
    TaskType.ZUORDNUNG: ["korrekt", "teilweise inkorrekt", "inkorrekt"],
    TaskType.FORMEL_ZAHL: ["korrekt", "inkorrekt"],
    TaskType.BEISPIELE: ["korrekt", "teilweise inkorrekt", "inkorrekt"],
    TaskType.RECHENAUFGABE: ["korrekt", "teilweise inkorrekt", "inkorrekt"]
}

task_rubrics = {
    TaskType.FREITEXT: ["Korrekt: Die Antwort ist inhaltlich richtig, vollständig, gut strukturiert und nachvollziehbar.",
                        "Teilweise inkorrekt: Die Antwort enthält kleinere Fehler oder Auslassungen, ist aberüberwiegend korrekt. Struktur und Nachvollziehbarkeit sind teilweise gegeben.",
                        "Inkorrekt: Die Antwort enthält gravierende inhaltliche Fehler oder lässt zentrale Punkte aus. Struktur und Nachvollziehbarkeit sind stark beeinträchtigt."
                        ],
    TaskType.ZUORDNUNG: ["Korrekt: Alle Zuordnungen sind vollständig und fehlerfrei richtig vorgenommen.",
                        "Teilweise inkorrekt: Ein Teil der Zuordnungen ist richtig, jedoch sind einige Elemente falsch oder nicht zugeordnet. Mindestens eine richtige Zuordnung ist vorhanden.",
                        "Inkorrekt: Die meisten Zuordnungen sind falsch oder es wurde keine sinnvolle Zuordnung vorgenommen."
                        ],
    TaskType.FORMEL_ZAHL: ["Korrekt: Die Formel ist korrekt angegeben, die Zahl ist genau und die Einheiten sind richtig.",
                           "Inkorrekt: Die Formel ist falsch, die Zahl ist ungenau oder die Einheiten sind falsch."
                          ],
    TaskType.BEISPIELE: ["Korrekt: Alle geforderten Beispiele sind korrekt, relevant und vollständig.",
                        "Teilweise inkorrekt: Einige Beispiele sind korrekt und relevant, aber es fehlen wichtige oder einige sind falsch.",
                        "Inkorrekt: Die Beispiele sind größtenteils falsch, irrelevant oder es wurden keine sinnvollen Beispiele gegeben."
                        ],  

    TaskType.RECHENAUFGABE: ["Korrekt: Das Ergebnis ist richtig, der Rechenweg ist vollständig und korrekt dargestellt, und die Einheiten sind korrekt angegeben.",
                             "Teilweise inkorrekt: Das Ergebnis ist teilweise richtig, der Rechenweg enthält kleinere Fehler oder Auslassungen, oder die Einheiten sind teilweise falsch.",     
                             "Inkorrekt: Das Ergebnis ist falsch, der Rechenweg ist fehlerhaft oder unvollständig, und die Einheiten sind größtenteils falsch."
                            ]


}

