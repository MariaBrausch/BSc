import json
from pathlib import Path
from PromptType import PromptType
from TaskType import TaskType
from datetime import datetime
from prompt_builder import PromptBuilder
from evaluation import Evaluation
import pandas as pd

promptBuilder = PromptBuilder()


with open("aufgaben.json", "r", encoding="utf-8") as f:
    data = json.load(f)

out_dir = Path("prompts_und_antworten")
out_dir.mkdir(exist_ok=True)

out_dir_A = Path("strategie_A")
out_dir_A.mkdir(exist_ok=True)

out_dir_B = Path("strategie_B")
out_dir_B.mkdir(exist_ok=True)

out_dir_C = Path("strategie_C")
out_dir_C.mkdir(exist_ok=True)

#Beispielantworten erstellen
# for eintrag in data:
#     prompt_type = PromptType.BEISPIELANTWORTEN
#     task_type = TaskType[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#     musterlsg = eintrag["musterloesung"]


#     prompt_text = promptBuilder.build_prompt(prompt_type, task_type, aufgabe, musterlsg, None, None)

#     prompt_path = out_dir / f"prompt_{eintrag['id']}.txt"
#     prompt_path.write_text(prompt_text, encoding="utf-8")

    
#     antwort_text = promptBuilder.call_model_responses(prompt_text)

#     timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
#     antwort_text = f"[Antwort generiert am {timestamp}]\n\n{antwort_text}"

       
#     answer_path = out_dir / f"antwort_{eintrag['id']}.txt"
#     answer_path.write_text(antwort_text, encoding="utf-8")

#     print(f"Prompt {eintrag['id']} erstellt und Antwort gespeichert -> {answer_path.name}")

# #Beispiel für STRATEGIEA      
for eintrag in data: 
    prompt_type = PromptType.STRATEGIEA
    task_type = TaskType[eintrag["task_type"]]
    aufgabe = eintrag["aufgabenstellung"]

    eingabe_korrekt = "korrekt"
    eingabe_teilweise = "teilweise inkorrekt"
    eingabe_inkorrekt = "inkorrekt"

    studentischeantwort_korrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}_{eingabe_korrekt}.txt", eingabe_korrekt, 1)
    prompt_text = promptBuilder.build_prompt(prompt_type,task_type,aufgabe,None,None,studentischeantwort_korrekt)

    


    prompt_path = out_dir_A / f"prompt_strategieA_{eintrag['id']}.txt"
    prompt_path.write_text(prompt_text, encoding="utf-8")

    antwort_text = promptBuilder.call_model_responses(prompt_text)

    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    antwort_text = f"[Antwort generiert am {timestamp}]\n\n{antwort_text}"

       
    answer_path = out_dir_A / f"antwort_{eintrag['id']}.txt"
    answer_path.write_text(antwort_text, encoding="utf-8")

    print(f"Prompt {eintrag['id']} erstellt und Antwort gespeichert -> {answer_path.name}")

# #Beispiel für STRATEGIEB
# for eintrag in data:
#     prompt_type = PromptType.STRATEGIEB
#     task_type = TaskType[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#     musterlsg = eintrag["musterloesung"]
#     teilweiseInkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "teilweise inkorrekt", 2)
#     inkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "inkorrekt", 2)
#     fewShotBeispiele = "Musterlösung: " + musterlsg + "\n\nTeilweise inkorrekte Antwort: " + teilweiseInkorrekt + "\n\nInkorrekte Antwort: " + inkorrekt    
#     studentischeantwort = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "korrekt", 1)
#     prompt_text = promptBuilder.build_prompt(prompt_type,task_type,aufgabe,musterlsg,fewShotBeispiele,studentischeantwort)

#     prompt_path = out_dir_B / f"prompt_strategieB_{eintrag['id']}.txt"
#     prompt_path.write_text(prompt_text, encoding="utf-8")

#     antwort_text = promptBuilder.call_model_responses(prompt_text)

#     answer_path = out_dir_B/ f"antwort_strategieB_{eintrag['id']}.txt"
#     answer_path.write_text(antwort_text, encoding="utf-8")

# #Beispiel für STRATEGIEC
# for eintrag in data:    
#     prompt_type = PromptType.STRATEGIEC
#     task_type = TaskType[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#     musterlsg = eintrag["musterloesung"]
#     teilweiseInkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "teilweise inkorrekt", 2)
#     inkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "inkorrekt", 2)
#     fewShotBeispiele = "Musterlösung: " + musterlsg + "\n\nTeilweise inkorrekte Antwort: " + teilweiseInkorrekt + "\n\nInkorrekte Antwort: " + inkorrekt    
#     studentischeantwort = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "korrekt", 1)
#     prompt_text = promptBuilder.build_prompt(prompt_type,task_type,aufgabe,musterlsg,fewShotBeispiele,studentischeantwort)

#     prompt_path = out_dir_C / f"prompt_strategieC_{eintrag['id']}.txt"
#     prompt_path.write_text(prompt_text, encoding="utf-8")

#     antwort_text = promptBuilder.call_model_responses(prompt_text)

#     answer_path = out_dir_C/ f"antwort_strategieC_{eintrag['id']}.txt"
#     answer_path.write_text(antwort_text, encoding="utf-8")


#Auswertung der Antworten
evaluator = Evaluation()

ergebnisse = evaluator.count_all_answers(f"strategie_A")
print(f"Ergebnisse für Strategie A: {ergebnisse}")
darstellung = evaluator.collect_answers_table(f"strategie_A", "Strategie A", "korrekt")
print(darstellung)