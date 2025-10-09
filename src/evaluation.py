from pathlib import Path
import pandas as pd


class Evaluation:
    """Klasse zur Auswertung und Erstellung von Matrizen """

    def __init__(self):
        pass

    def klassifiziere_antwort(self, pfad: str) -> str:
        """Liest eine Datei und gibt die Kategorie zurück: 'korrekt', 'teilweise inkorrekt' oder 'inkorrekt'
        :param pfad: Pfad zur Datei
        :return: Kategorie als String oder 'unbekannt', wenn nicht gefunden
        """
        try:
            with open(pfad, "r", encoding="utf-8") as f:
                for zeile in f:
                    zeile_clean = zeile.strip().lower()
                    if zeile_clean.startswith("### bewertungskategorie:"):
                        if "teilweise inkorrekt" in zeile_clean:
                            return "teilweise inkorrekt"
                        elif "inkorrekt" in zeile_clean:
                            return "inkorrekt"
                        elif "korrekt" in zeile_clean:
                            return "korrekt"
        except Exception as e:
            print(f"Fehler beim Lesen von {pfad}: {e}")
        return "unbekannt"

    def eingabe_kategorie(self, dateiname: str) -> str:
        """
        Zieht die Eingabe-Kategorie aus dem Dateinamen.
        Akzeptiert Varianten mit Leer-/Unterstrichen etc.
        Beispielnamen: ...-korrekt.txt, ...-teilweise_inkorrekt.txt, ...-inkorrekt.txt
        :param dateiname: Der Dateiname als String
        :return: Die Kategorie als String oder 'unbekannt', wenn nicht gefunden
        """
        s = dateiname.lower().replace("_", "-").replace(" ", "-")
        if "teilweise-inkorrekt" in s:
            return "teilweise inkorrekt"
        elif "inkorrekt" in s:
            return "inkorrekt"
        elif "korrekt" in s:
            return "korrekt"
        return "unbekannt"

    def erstelle_matrix(self, ordner: str):
        """
        Erstellt eine Matrix der Eingabe- und Ausgabe-Kategorien aus den Dateien in einem Ordner.
        :param ordner: Der Pfad zum Ordner mit den Antwortdateien
        :return: Eine Matrix (Dictionary), Liste unbekannter Eingaben, Liste unbekannter Ausgaben
        """
        kategorien = ["korrekt", "teilweise inkorrekt", "inkorrekt"]
        matrix = {eingabe: {ausgabe: 0 for ausgabe in kategorien} for eingabe in kategorien}
        unbekannte_eingaben = []
        unbekannte_ausgaben = []

        for datei in Path(ordner).glob("antwort*.txt"):
            eingabe = self.eingabe_kategorie(datei.name)
            ausgabe = self.klassifiziere_antwort(datei)

            if eingabe not in matrix:
                unbekannte_eingaben.append(str(datei))
                continue

            if ausgabe in matrix[eingabe]:
                matrix[eingabe][ausgabe] += 1
            else:
                unbekannte_ausgaben.append(str(datei))

        return matrix, unbekannte_eingaben, unbekannte_ausgaben

    def erstelle_auswertung(self, ordner: str, strategie_name: str, kategorie_eingabe: str | None = None) -> pd.DataFrame:
        """
        Erstellt eine Auswertungstabelle für die gegebene Strategie.
        :param ordner: Der Pfad zum Ordner mit den Antwortdateien
        :param strategie_name: Der Name der Strategie (für die Tabelle)
        :param kategorie_eingabe: Optional eine spezifische Eingabekategorie (z.B. "korrekt"), sonst alle 
        :return: Ein Pandas DataFrame mit der Auswertung  
        """
        matrix, unbekannte_eingaben, unbekannte_ausgaben = self.erstelle_matrix(ordner)

        # Falls nur eine bestimmte Eingabezeile erfolgen soll
        eingaben = [kategorie_eingabe] if kategorie_eingabe else ["korrekt", "teilweise inkorrekt", "inkorrekt"]

        zeilen = []
        for eingabe in eingaben:
            counts = matrix.get(eingabe, {"korrekt": 0, "teilweise inkorrekt": 0, "inkorrekt": 0})
            zeilen.append([
                strategie_name,
                eingabe,
                counts["korrekt"],
                counts["teilweise inkorrekt"],
                counts["inkorrekt"]
            ])

        df = pd.DataFrame(
            zeilen,
            columns=["Strategie", "Eingabe", "Ausgabe korrekt", "Ausgabe teilweise inkorrekt", "Ausgabe inkorrekt"]
        )

        # zur Kontrolle unbekannte Dateien melden
        if unbekannte_eingaben:
            print("Unbekannte Eingaben (Dateiname enthält keine Kategorie):")
            for f in unbekannte_eingaben:
                print(" -", f)
        if unbekannte_ausgaben:
            print("Unbekannte Ausgaben (Dateiinhalt ohne Kategoriezeile):")
            for f in unbekannte_ausgaben:
                print(" -", f)

        return df
