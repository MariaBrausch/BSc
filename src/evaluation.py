from textwrap import dedent
import json
from pathlib import Path
from PromptType import PromptType
from Instructions import Instructions
from TaskType import TaskType
from TaskType import task_criteria, task_categories, task_rubrics



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
    

    def count_all_answers(self, ordner: str):
        korrekt = 0
        teilweise_inkorrekt = 0
        inkorrekt = 0
        unbekannt = 0

        for datei in Path(ordner).glob("antwort*.txt"):
            kategorie = self.classify_answer(datei)
            if kategorie == "korrekt":
                korrekt += 1
            elif kategorie == "teilweise inkorrekt":
                teilweise_inkorrekt += 1
            elif kategorie == "inkorrekt":
                inkorrekt += 1
            else:
                unbekannt += 1
                print(f"Unbekannt in Datei: {datei}")

        return {
            "korrekt": korrekt,
            "teilweise inkorrekt": teilweise_inkorrekt,
            "inkorrekt": inkorrekt,
            "unbekannt": unbekannt
        }
