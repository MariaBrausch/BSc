from textwrap import dedent
import json
from pathlib import Path
from PromptType import PromptType
from Instructions import Instructions
from TaskType import TaskType
from TaskType import task_criteria, task_categories, task_rubrics
from openai import OpenAI
from datetime import datetime


class PromptBuilder:

    def __init__(self):
        pass
    
    def build_prompt(self, prompt_type: PromptType, task_type: TaskType, aufgabenstellung: str, musterlösung: str = None, fewShotBeispiele: str = None, studentischeantwort: str = None) -> str:
        """
        Erstellt einen Prompt basierend auf dem Typ und den übergebenen Parametern.

        :param prompt_type: Der Typ des Prompts (z. B. BEISPIELANTWORTEN, STRATEGIEA, STRATEGIEB, STRATEGIEC)
        :param task_type: Der Typ der Aufgabe
        :param aufgabenstellung: Die Aufgabenstellung
        :param musterlösung: Optional, die Musterlösung
        :param fewShotBeispiele: Optional, Beispiele für Few-Shot-Learning
        :param studentischeantwort: Optional, eine studentische Antwort
        :return: Der vollständige Prompt als String
        """
        rubrics = task_rubrics.get(task_type, [])
        rubrics_str = "\n".join(f"- {item}" for item in rubrics)

        criteria_list = task_criteria.get(task_type, [])
        criteria_str = "\n".join(f"- {item}" for item in criteria_list)

        categories = task_categories.get(task_type, [])
        categories_str = ", ".join(categories)

        print(f"Debug: Received prompt_type = {prompt_type}")

        if prompt_type == PromptType.BEISPIELANTWORTEN:
            return dedent(f"""
Anweisung:
{Instructions.BEISPIELANTWORTEN.value}
Aufgabenstellung:
{aufgabenstellung}
Bewertungskategorien:
{categories_str}
Bewertungskriterien
Folgende Kriterien werden bewertet:
{criteria_str}
Musterlösung:
{musterlösung}
            """).strip()

        elif prompt_type == PromptType.STRATEGIEA:
            return dedent(f"""
Anweisung:
{Instructions.STRATEGIEA.value}
Aufgabenstellung:
{aufgabenstellung}
Bewertungsrubrik:
{rubrics_str}
Studentische Antwort:
{studentischeantwort}
            """).strip()

        elif prompt_type == PromptType.STRATEGIEB:
            return dedent(f"""
Rollenbeschreibung:
{Instructions.STRATEGIEB.value}
Aufgabenstellung:
{aufgabenstellung}
Beispiele:
{fewShotBeispiele }
Bewertungsrubrik:
{rubrics_str}
Studentische Antwort:
{studentischeantwort }
        """).strip()

        elif prompt_type == PromptType.STRATEGIEC:
            return dedent(f"""
Rollenbeschreibung:
{Instructions.STRATEGIEC.value}
Aufgabenstellung:
{aufgabenstellung}
Beispiele:
{fewShotBeispiele }
Bewertungsrubrik:
{rubrics_str}
Studentische Antwort:
{studentischeantwort}
            """).strip()

        else:
            raise ValueError("Unbekannter Prompt-Typ")
        
    def call_model_responses(self, prompt_text: str, model: str = "gpt-4o") -> str:
        client = OpenAI()
        resp = client.responses.create(
            model=model,
            input=prompt_text,
        )
        return resp.output_text 

    def choose_studentanswer(self, pfad: str, kategorie: str, nummer: int) -> str:
        antwort_lines = []
        try:
            #print(f"Öffne Datei: {pfad}")
            with open(pfad, "r", encoding="utf-8") as f:
                lines = f.readlines()

            inside_category = False
            inside_answer = False

            for line in lines:
                line_stripped = line.strip()

                # Kategorie erkannt (unabhängig von Groß-/Kleinschreibung)
                if line_stripped.lower().startswith("### bewertungskategorie:") and kategorie.lower() in line_stripped.lower():
                    #print(f"Kategorie gefunden: {kategorie}")
                    inside_category = True
                    continue

                # Falls neue Kategorie kommt -> rausgehen
                if line_stripped.lower().startswith("### bewertungskategorie:") and inside_category:
                    break

                # Antwort erkannt (unabhängig von Groß-/Kleinschreibung)
                if inside_category and line_stripped.lower().startswith(f"**antwort {nummer}:**".lower()):
                    #print(f"Antwort {nummer} gefunden in Kategorie {kategorie}")
                    inside_answer = True
                    continue

                # Text sammeln, solange wir in der richtigen Antwort sind
                if inside_answer:
                    if line_stripped.lower().startswith("**antwort") or line_stripped.lower().startswith("### bewertungskategorie:"):
                        break
                    antwort_lines.append(line_stripped)

            if not antwort_lines:
                print(f"Keine Antwort gefunden für Kategorie: {kategorie}, Nummer: {nummer}")
                return "Keine Antwort gefunden."

            return " ".join(antwort_lines).strip()

        except FileNotFoundError:
            print(f"Datei nicht gefunden: {pfad}")
            return "Datei nicht gefunden."
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return "Ein Fehler ist aufgetreten."


