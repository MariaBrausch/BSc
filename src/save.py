import json
from pathlib import Path
from datetime import datetime

def speichere_beispielantworten(aufgabe_id, aufgabe_text, aufgabe_titel, musterloesung, bewertungskriterien, beispiele, ordner="beispielantworten"):
    """
    Speichert generierte Beispielantworten in einer JSON-Datei.

    :param aufgabe_id: Eindeutige ID oder Name der Aufgabe (z. B. "aufgabe1")
    :param aufgabe_text: Aufgabenstellung als String
    :param aufgabe_titel: Titel der Aufgabenstellung
    :param musterloesung: Musterlösung als String
    :param bewertungskriterien: Liste mit Kriterien
    :param beispiele: Liste von Dictionaries mit "kategorie" und "antwort"
    :param ordner: Zielordner für die JSON-Dateien
    """
    
    daten = {
        "aufgabe_id": aufgabe_id,
        "timestamp": datetime.now().isoformat(),
        "aufgabe_titel": aufgabe_titel,
        "aufgabe": aufgabe_text,
        "musterloesung": musterloesung,
        "bewertungskriterien": bewertungskriterien,
        "beispiele": beispiele
    }

    # Ordner erstellen, falls er nicht existiert
    Path(ordner).mkdir(parents=True, exist_ok=True)

    # Datei speichern
    dateiname = Path(ordner) / f"{aufgabe_id}.json"
    with open(dateiname, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)

    print(f"Beispielantworten gespeichert in: {dateiname}")


# Beispielaufruf
if __name__ == "__main__":
    aufgabe_titel = "Parallelität b)"
    aufgabe_text = "Fassen Sie die Aussage(n) von Amdahls Gesetz in eigenen Worten zusammen!"
    musterloesung = "Amdahls Gesetz besagt, dass der serielle Anteil eines Programms die durch Parallelisierung maximal erreichbare Beschleunigung begrenzt. Zwar steigt der Speedup mit dem Anteil parallelisierbarer Programmteile, jedoch wird selbst bei unendlich hoher Anzahl verfügbarer Prozessoren mindestens die Zeit benötigt, die der serielle Anteil erfordert. Da in der Praxis Parallelisierungskosten (durch Kommunikations- und Synchronisationsaufwand) entstehen, steigt ab einer gewissen Anzahl von Prozessoren der Zeitbedarf zur Bearbeitung der Aufgabe sogar wieder."
    bewertungskriterien = [" inhaltliche Korrektheit, Vollständigkeit, Struktur, Nachvollziehbarkeit"]

    beispiele = [
        {"kategorie": "korrekt", "antwort": "Amdahls Gesetz sagt aus, dass ein Programm nur so schnell wird, wie es sein serieller Anteil erlaubt. Selbst wenn man unendlich viele Prozessoren einsetzt, bleibt ein Teil des Programms, der nicht parallelisiert werden kann, und dieser begrenzt die Gesamtbeschleunigung. Ab einem bestimmten Punkt lohnt es sich also nicht mehr, weitere Prozessoren hinzuzufügen, da der Kommunikations- und Verwaltungsaufwand sogar mehr Zeit kosten kann."},
        {"kategorie": "korrekt", "antwort": "Nach Amdahls Gesetz hängt die maximale Beschleunigung durch Parallelisierung vom Anteil der seriellen Programmbestandteile ab. Je größer der parallelisierbare Teil ist, desto mehr Speedup ist möglich. Aber sobald ein gewisser Prozentsatz seriell bleiben muss, ist die Beschleunigung nach oben begrenzt – selbst mit beliebig vielen Prozessoren. Praktisch verschlechtern Synchronisations- und Kommunikationskosten die Effizienz zusätzlich."},
        {"kategorie": "teilweise inkorrekt", "antwort": "Amdahls Gesetz besagt, dass Programme immer beliebig beschleunigt werden können, wenn man nur genügend Prozessoren verwendet. Der Speedup wächst zwar langsamer, je mehr Prozessoren man einsetzt, aber ein Limit gibt es nicht."},
        {"kategorie": "teilweise inkorrekt", "antwort": "Das Gesetz von Amdahl bedeutet, dass sich Programme perfekt parallelisieren lassen, wenn man die richtigen Algorithmen verwendet. Der serielle Anteil spielt dabei nur eine kleine Rolle, aber in der Praxis ist es trotzdem schwer, mehr als eine bestimmte Anzahl Prozessoren effektiv zu nutzen."},
        {"kategorie": "inkorrekt", "antwort": "Amdahls Gesetz beschreibt, dass man ein Programm durch Hinzufügen von mehr Prozessoren immer verdoppeln kann, also doppelte Prozessorzahl bedeutet doppelte Geschwindigkeit, unabhängig vom Aufbau des Programms."},
        {"kategorie": "inkorrekt", "antwort": "Nach Amdahl geht es darum, wie viel Strom ein Prozessor beim Parallelisieren verbraucht und wie man dadurch die Laufzeit verlängert. Das Gesetz behandelt also vor allem Energieeffizienz in Mehrprozessorsystemen."}
    ]

    speichere_beispielantworten("EA1 Parallelität b)", aufgabe_text, aufgabe_titel, musterloesung, bewertungskriterien, beispiele)