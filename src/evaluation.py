from textwrap import dedent
import json
from pathlib import Path

from PromptType import PromptType
from Instructions import Instructions
from TaskType import TaskType
from TaskType import task_criteria, task_categories, task_rubrics
import pandas as pd



class Evaluation:

    def __init__(self):
        pass

    def classify_answer(self, pfad: str) -> str:
        """Liest eine Datei und gibt die Kategorie zurück: 'korrekt', 'teilweise inkorrekt' oder 'inkorrekt'"""
        try:
            with open(pfad, "r", encoding="utf-8") as f:
                for line in f:
                    line_stripped = line.strip().lower()
                    if line_stripped.startswith("### bewertungskategorie:"):
                        if "teilweise inkorrekt" in line_stripped:
                            return "teilweise inkorrekt"
                        elif "inkorrekt" in line_stripped:   
                            return "inkorrekt"
                        elif "korrekt" in line_stripped:
                            return "korrekt"
        except Exception as e:
            print(f"Fehler beim Lesen von {pfad}: {e}")
        return "unbekannt"
    
    def input_category(self, filename: str) -> str:
        """
        Zieht die EINGABE-Kategorie aus dem Dateinamen.
        Akzeptiert Varianten mit Leer-/Unterstrichen etc.
        Beispielnamen: ...-korrekt.txt, ...-teilweise_inkorrekt.txt, ...-inkorrekt.txt
        """
        s = filename.lower().replace("_", "-").replace(" ", "-")
        if "teilweise-inkorrekt" in s:
            return "teilweise inkorrekt"
        elif "inkorrekt" in s:     
            return "inkorrekt"
        elif "korrekt" in s:
            return "korrekt"
        return "unbekannt"
    

    def count_by_input_category(self, ordner: str):
            kategorien = ["korrekt", "teilweise inkorrekt", "inkorrekt"]
            matrix = {input: {output: 0 for output in kategorien} for input in kategorien}
            unknown_input_files = []
            unknown_output_files = []

            for datei in Path(ordner).glob("antwort*.txt"):
                input = self.input_category(datei.name)   # EINGABE aus Dateiname
                output = self.classify_answer(datei)             # AUSGABE aus Inhalt

                if input not in matrix:
                    unknown_input_files.append(str(datei))
                    continue

                if output in matrix[input]:
                    matrix[input][output] += 1
                else:
                    unknown_output_files.append(str(datei))

            return matrix, unknown_input_files, unknown_output_files


    def collect_answers_table(self, ordner: str, strategie_name: str, kategorie_eingabe: str | None = None) -> pd.DataFrame:
        matrix, unk_inp, unk_out = self.count_by_input_category(ordner)

        # Falls nur eine bestimmte Eingabezeile gewünscht ist
        inputs = [kategorie_eingabe] if kategorie_eingabe else ["korrekt", "teilweise inkorrekt", "inkorrekt"]

        rows = []
        for inp in inputs:
            counts = matrix.get(inp, {"korrekt": 0, "teilweise inkorrekt": 0, "inkorrekt": 0})
            rows.append([
                strategie_name,
                inp,
                counts["korrekt"],
                counts["teilweise inkorrekt"],
                counts["inkorrekt"]
            ])

        df = pd.DataFrame(
            rows,
            columns=["Strategie", "Eingabe", "Ausgabe korrekt", "Ausgabe teilweise inkorrekt", "Ausgabe inkorrekt"]
        )

        # Optional: zur Kontrolle unbekannte Dateien melden
        if unk_inp:
            print("Unbekannte EINGABE (Dateiname enthält keine Kategorie):")
            for f in unk_inp: print(" -", f)
        if unk_out:
            print("Unbekannte AUSGABE (Dateiinhalt ohne Kategoriezeile):")
            for f in unk_out: print(" -", f)

        return df