import json
from pathlib import Path
from promptType import PromptType
from taskType import TaskType
from datetime import datetime
from prompt_builder import PromptBuilder
from evaluation import Evaluation


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
eingaben = [
    "korrekt",
    "teilweise inkorrekt",
    "inkorrekt"
]  
# #Beispiel für STRATEGIEA   
 
# for eintrag in data: 
#     prompt_type = PromptType.STRATEGIEA
#     task_type = TaskType[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#     timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

#     for eingabe in eingaben:
#         # Studentische Antwort auswählen
#         studentische_antwort = promptBuilder.choose_studentanswer(
#             f"prompts_und_antworten/antwort_{eintrag['id']}.txt", 
#             eingabe, 
#             1
#         )

#         # Prompt bauen
#         prompt_text = promptBuilder.build_prompt(
#             prompt_type,
#             task_type,
#             aufgabe,
#             None,
#             None,
#             studentische_antwort
#         )

#         # Antwort generieren
#         antwort_text = promptBuilder.call_model_responses(prompt_text)
#         antwort_text = f"[Antwort generiert am {timestamp}]\n\n{antwort_text}"

#         # Dateien speichern
#         answer_path = out_dir_A / f"antwort_{eintrag['id']}_{eingabe}.txt"
#         prompt_path = out_dir_A / f"prompt_strategieA_{eintrag['id']}_{eingabe}.txt"

#         answer_path.write_text(antwort_text, encoding="utf-8")
#         prompt_path.write_text(prompt_text, encoding="utf-8")

#         print(f"Prompt {eintrag['id']} ({eingabe}) erstellt und Antwort gespeichert -> {answer_path.name}")

# #Beispiel für STRATEGIEB
# for eintrag in data:
#     prompt_type = PromptType.STRATEGIEB
#     task_type = TaskType[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#     # Few Shot Beispiele
#     musterlsg = eintrag["musterloesung"]
#     teilweiseInkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "teilweise inkorrekt", 2)
#     inkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "inkorrekt", 2)
#     fewShotBeispiele = "Musterlösung: " + musterlsg + "\n\nTeilweise inkorrekte Antwort: " + teilweiseInkorrekt + "\n\nInkorrekte Antwort: " + inkorrekt    
#     # Studentische Antwort einfügen 
#     for eingabe in eingaben:
#         # Studentische Antwort auswählen
#         studentische_antwort = promptBuilder.choose_studentanswer(
#             f"prompts_und_antworten/antwort_{eintrag['id']}.txt", 
#             eingabe, 
#             1
#         )
#         # Prompt bauen
#         prompt_text = promptBuilder.build_prompt(
#             prompt_type,
#             task_type,
#             aufgabe,
#             musterlsg,
#             fewShotBeispiele,
#             studentische_antwort)

#         prompt_path = out_dir_B / f"prompt_strategieB_{eintrag['id']}_{eingabe}.txt"
#         prompt_path.write_text(prompt_text, encoding="utf-8")

#         antwort_text = promptBuilder.call_model_responses(prompt_text)

#         answer_path = out_dir_B/ f"antwort_strategieB_{eintrag['id']}_{eingabe}.txt"
#         answer_path.write_text(antwort_text, encoding="utf-8")

#         print(f"Prompt {eintrag['id']} ({eingabe}) erstellt und Antwort gespeichert -> {answer_path.name}")


#Beispiel für STRATEGIEC
for eintrag in data:    
    prompt_type = PromptType.STRATEGIEC
    task_type = TaskType[eintrag["task_type"]]
    aufgabe = eintrag["aufgabenstellung"]
    # Few Shot Beispiele
    musterlsg = eintrag["musterloesung"]
    teilweiseInkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "teilweise inkorrekt", 2)
    inkorrekt = promptBuilder.choose_studentanswer(f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "inkorrekt", 2)
    fewShotBeispiele = "Musterlösung: " + musterlsg + "\n\nTeilweise inkorrekte Antwort: " + teilweiseInkorrekt + "\n\nInkorrekte Antwort: " + inkorrekt    
    # Studentische Antwort einfügen
    for eingabe in eingaben:
        # Studentische Antwort auswählen
        studentische_antwort = promptBuilder.choose_studentanswer(
            f"prompts_und_antworten/antwort_{eintrag['id']}.txt", 
            eingabe, 
            1
        )
        # Prompt bauen
        prompt_text = promptBuilder.build_prompt(
            prompt_type,
            task_type,
            aufgabe,
            musterlsg,
            fewShotBeispiele,
            studentische_antwort)

        prompt_path = out_dir_C / f"prompt_strategieC_{eintrag['id']}_{eingabe}.txt"
        prompt_path.write_text(prompt_text, encoding="utf-8")

        antwort_text = promptBuilder.call_model_responses(prompt_text)

        answer_path = out_dir_C/ f"antwort_strategieC_{eintrag['id']}_{eingabe}.txt"
        answer_path.write_text(antwort_text, encoding="utf-8")

        print(f"Prompt {eintrag['id']} ({eingabe}) erstellt und Antwort gespeichert -> {answer_path.name}")
   

#Auswertung der Antworten
evaluator = Evaluation()

# A
# darstellung = evaluator.collect_answers_table("strategie_A", "Strategie A", None)
# print(darstellung)


# B
# darstellung = evaluator.collect_answers_table("strategie_B", "Strategie B", None)
# print(darstellung)

# C
darstellung = evaluator.collect_answers_table("strategie_C", "Strategie C", None)
print(darstellung)
