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
    
    def collect_answers_table(self, ordner: str, strategie_name: str, kategorie_eingabe:str) -> pd.DataFrame:
        rows = []
        #rows.append(["Strategie", "Kategorie Eingabe", "Ausgabe Kategorie korrekt", "Ausgabe Kategorie teilweise inkorrekt", "Ausgabe Kategorie inkorrekt"])
        #for datei in Path(ordner).glob("antwort*.txt"):
        kategorie_ausgabe = self.count_all_answers(ordner)
        rows.append([strategie_name, kategorie_eingabe, kategorie_ausgabe.get("korrekt", "fehler"), kategorie_ausgabe.get("teilweise inkorrekt", "fehler"), kategorie_ausgabe.get("inkorrekt", "fehler")])        
        
        df = pd.DataFrame(
        rows,
        columns=["Strategie", "Eingabe", "Ausgabe korrekt", "Ausgabe teilweise inkorrekt", "Ausgabe inkorrekt"]
        )
        return df
