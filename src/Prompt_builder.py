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
    
    def build_prompt(prompt_type: PromptType, task_type: TaskType, aufgabenstellung: str, musterlösung: str) -> str:

        criteria_list = task_criteria.get(task_type, [])
        criteria_str = "\n".join(f"- {item}" for item in criteria_list)

        categories = task_categories.get(task_type, [])
        categories_str  = ", ".join(categories)


        if prompt_type == PromptType.BEISPIELANTWORTEN:
            return dedent(f"""\
    Anweisung
    {Instructions.BEISPIELANTWORTEN.value}
Aufgabenstellung
{aufgabenstellung}
Bewertungskategorien
{categories_str}
Bewertungskriterien
Folgende Kriterien werden bewertet:
{criteria_str}
Musterlösung
{musterlösung}
    """).strip()
        
        else:
            raise ValueError("Unbekannter Prompt-Typ")
        
def prompt_builder_strategieA(prompt_type: PromptType, task_type: TaskType, aufgabenstellung: str, studentischeantwort: str) -> str:  
        rubrics = task_rubrics.get(task_type, [])       
        rubrics_str = "\n".join(f"- {item}" for item in rubrics)  

        if prompt_type == PromptType.STRATEGIEA:
            return dedent(f"""\
    Anweisung
    {Instructions.STRATEGIEA.value}
Aufgabenstellung 
{aufgabenstellung}
Bewertungsrubrik
{rubrics_str}
Studentische Antwort
{studentischeantwort}
    """).strip()

        
        
def call_model_responses(prompt_text: str, model: str = "gpt-4o") -> str:
    client = OpenAI()
    resp = client.responses.create(
        model=model,
        input=prompt_text,
    )
    return resp.output_text 

def choose_studentanswer(pfad: str, kategorie: str, nummer: int) -> str:
    antwort_lines = []
    try:
        print(f"Öffne Datei: {pfad}")
        with open(pfad, "r", encoding="utf-8") as f:
            lines = f.readlines()

        inside_category = False
        inside_answer = False

        for line in lines:
            line_stripped = line.strip()

            # Kategorie erkannt
            if line_stripped.startswith("### Bewertungskategorie:") and kategorie in line_stripped:
                print(f"Kategorie gefunden: {kategorie}")
                inside_category = True
                continue

            # Falls neue Kategorie kommt -> rausgehen
            if line_stripped.startswith("### Bewertungskategorie:") and inside_category:
                break

            # Antwort erkannt
            if inside_category and line_stripped.startswith(f"**Antwort {nummer}:**"):
                print(f"Antwort {nummer} gefunden in Kategorie {kategorie}")
                inside_answer = True
                continue

            # Text sammeln, solange wir in der richtigen Antwort sind
            if inside_answer:
                if line_stripped.startswith("**Antwort") or line_stripped.startswith("### Bewertungskategorie:"):
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
        
if __name__ == "__main__":

    with open("aufgaben.json", "r", encoding="utf-8") as f:
        data = json.load(f)


    out_dir = Path("prompts_und_antworten")
    out_dir.mkdir(exist_ok=True)

    out_dir_A = Path("strategie_A")
    out_dir_A.mkdir(exist_ok=True)

    #Beispielantworten erstellen
    # for eintrag in data:
    #     prompt_type = PromptType[eintrag["prompt_type"]]
    #     task_type = TaskType[eintrag["task_type"]]
    #     aufgabe = eintrag["aufgabenstellung"]
    #     musterlsg = eintrag["musterloesung"]


    #     prompt_text = PromptBuilder.build_prompt(prompt_type, task_type, aufgabe, musterlsg)

    #     prompt_path = out_dir / f"prompt_{eintrag['id']}.txt"
    #     prompt_path.write_text(prompt_text, encoding="utf-8")

    
    #     antwort_text = call_model_responses(prompt_text)

       
    #     answer_path = out_dir / f"antwort_{eintrag['id']}.txt"
    #     answer_path.write_text(antwort_text, encoding="utf-8")

    #     print(f"Prompt {eintrag['id']} erstellt und Antwort gespeichert -> {answer_path.name}")

    #Beispiel für STRATEGIEA
      
    for eintrag in data: 
        prompt_type = PromptType.STRATEGIEA
        task_type = TaskType[eintrag["task_type"]]
        aufgabe = eintrag["aufgabenstellung"]
        musterlsg = eintrag["musterloesung"]
        studentischeantwort = choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "korrekt", 1)
        prompt_text = prompt_builder_strategieA(prompt_type, task_type, aufgabe, studentischeantwort)

        prompt_path = out_dir_A / f"prompt_strategieA_{eintrag['id']}.txt"
        prompt_path.write_text(prompt_text, encoding="utf-8")

        antwort_text = call_model_responses(prompt_text)

        answer_path = out_dir_A/ f"antwort_strategieA_{eintrag['id']}.txt"
        answer_path.write_text(antwort_text, encoding="utf-8")


