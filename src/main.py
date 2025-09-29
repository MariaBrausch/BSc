import json
from pathlib import Path
from promptTyp import PromptTyp
from aufgabenTyp import AufgabenTyp
from datetime import datetime
from promptErsteller import PromptErsteller
from evaluation import Evaluation


promptErsteller = PromptErsteller()

# Aufgaben aus JSON-Datei laden
with open("aufgaben.json", "r", encoding="utf-8") as f:
    daten = json.load(f)

# Ausgabeordner vorbereiten
ausgabe_ordner = Path("prompts_und_antworten")
ausgabe_ordner.mkdir(exist_ok=True)

ordner_A = Path("strategie_A")
ordner_A.mkdir(exist_ok=True)

ordner_B = Path("strategie_B")
ordner_B.mkdir(exist_ok=True)

ordner_C = Path("strategie_C")
ordner_C.mkdir(exist_ok=True)

eingaben = [
    "korrekt",
    "teilweise inkorrekt",
    "inkorrekt"
]

# Beispielantworten erstellen
# for eintrag in daten:
#     prompt_typ = PromptTyp.BEISPIELANTWORTEN
#     aufgaben_typ = AufgabenTyp[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#     musterloesung = eintrag["musterloesung"]
#
#     prompt_text = promptErsteller.erstelle_prompt(prompt_typ, aufgaben_typ, aufgabe, musterloesung, None, None)
#
#     prompt_pfad = ausgabe_ordner / f"prompt_{eintrag['id']}.txt"
#     prompt_pfad.write_text(prompt_text, encoding="utf-8")
#
#     antwort_text = promptErsteller.rufe_modellantworten_ab(prompt_text)
#
#     zeitstempel = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
#     antwort_text = f"[Antwort generiert am {zeitstempel}]\n\n{antwort_text}"
#
#     antwort_pfad = ausgabe_ordner / f"antwort_{eintrag['id']}.txt"
#     antwort_pfad.write_text(antwort_text, encoding="utf-8")
#
#     print(f"Prompt {eintrag['id']} erstellt und Antwort gespeichert -> {antwort_pfad.name}")

# Beispiel für STRATEGIE A   
# for eintrag in daten: 
#     prompt_typ = PromptTyp.STRATEGIEA
#     aufgaben_typ = AufgabenTyp[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#     zeitstempel = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
#
#     for eingabe in eingaben:
#         # Studentische Antwort auswählen
#         studentenantwort = promptErsteller.waehle_studentenantwort(
#             f"prompts_und_antworten/antwort_{eintrag['id']}.txt", 
#             eingabe, 
#             1
#         )
#
#         # Prompt bauen
#         prompt_text = promptErsteller.erstelle_prompt(
#             prompt_typ,
#             aufgaben_typ,
#             aufgabe,
#             None,
#             None,
#             studentenantwort
#         )
#
#         # Antwort generieren
#         antwort_text = promptErsteller.rufe_modellantworten_ab(prompt_text)
#         antwort_text = f"[Antwort generiert am {zeitstempel}]\n\n{antwort_text}"
#
#         # Dateien speichern
#         antwort_pfad = ordner_A / f"antwort_{eintrag['id']}_{eingabe}.txt"
#         prompt_pfad = ordner_A / f"prompt_strategieA_{eintrag['id']}_{eingabe}.txt"
#
#         antwort_pfad.write_text(antwort_text, encoding="utf-8")
#         prompt_pfad.write_text(prompt_text, encoding="utf-8")
#
#         print(f"Prompt {eintrag['id']} ({eingabe}) erstellt und Antwort gespeichert -> {antwort_pfad.name}")

# Beispiel für STRATEGIE B
# for eintrag in daten:
#     prompt_typ = PromptTyp.STRATEGIEB
#     aufgaben_typ = AufgabenTyp[eintrag["task_type"]]
#     aufgabe = eintrag["aufgabenstellung"]
#
#     # Few-Shot-Beispiele vorbereiten
#     musterloesung = eintrag["musterloesung"]
#     teilweise_inkorrekt = promptErsteller.waehle_studentenantwort(
#         f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "teilweise inkorrekt", 2
#     )
#     inkorrekt = promptErsteller.waehle_studentenantwort(
#         f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "inkorrekt", 2
#     )
#     few_shot_beispiele = (
#         "Musterlösung: " + musterloesung
#         + "\n\nTeilweise inkorrekte Antwort: " + teilweise_inkorrekt
#         + "\n\nInkorrekte Antwort: " + inkorrekt
#     )
#
#     # Studentische Antworten einfügen 
#     for eingabe in eingaben:
#         studentenantwort = promptErsteller.waehle_studentenantwort(
#             f"prompts_und_antworten/antwort_{eintrag['id']}.txt", 
#             eingabe, 
#             1
#         )
#
#         # Prompt bauen
#         prompt_text = promptErsteller.erstelle_prompt(
#             prompt_typ,
#             aufgaben_typ,
#             aufgabe,
#             musterloesung,
#             few_shot_beispiele,
#             studentenantwort
#         )
#
#         prompt_pfad = ordner_B / f"prompt_strategieB_{eintrag['id']}_{eingabe}.txt"
#         prompt_pfad.write_text(prompt_text, encoding="utf-8")
#
#         antwort_text = promptErsteller.rufe_modellantworten_ab(prompt_text)
#
#         antwort_pfad = ordner_B / f"antwort_strategieB_{eintrag['id']}_{eingabe}.txt"
#         antwort_pfad.write_text(antwort_text, encoding="utf-8")
#
#         print(f"Prompt {eintrag['id']} ({eingabe}) erstellt und Antwort gespeichert -> {antwort_pfad.name}")

# Beispiel für STRATEGIE C
for eintrag in daten:    
    prompt_typ = PromptTyp.STRATEGIEC
    aufgaben_typ = AufgabenTyp[eintrag["task_type"]]
    aufgabe = eintrag["aufgabenstellung"]

    # Few-Shot-Beispiele vorbereiten
    musterloesung = eintrag["musterloesung"]
    teilweise_inkorrekt = promptErsteller.waehle_studentenantwort(
        f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "teilweise inkorrekt", 2
    )
    inkorrekt = promptErsteller.waehle_studentenantwort(
        f"prompts_und_antworten/antwort_{eintrag['id']}.txt", "inkorrekt", 2
    )
    few_shot_beispiele = (
        "Musterlösung: " + musterloesung
        + "\n\nTeilweise inkorrekte Antwort: " + teilweise_inkorrekt
        + "\n\nInkorrekte Antwort: " + inkorrekt
    )

    # Studentische Antworten einfügen
    for eingabe in eingaben:
        studentenantwort = promptErsteller.waehle_studentenantwort(
            f"prompts_und_antworten/antwort_{eintrag['id']}.txt", 
            eingabe, 
            1
        )

        # Prompt bauen
        prompt_text = promptErsteller.erstelle_prompt(
            prompt_typ,
            aufgaben_typ,
            aufgabe,
            musterloesung,
            few_shot_beispiele,
            studentenantwort
        )

        prompt_pfad = ordner_C / f"prompt_strategieC_{eintrag['id']}_{eingabe}.txt"
        prompt_pfad.write_text(prompt_text, encoding="utf-8")

        antwort_text = promptErsteller.rufe_modellantworten_ab(prompt_text)

        antwort_pfad = ordner_C / f"antwort_strategieC_{eintrag['id']}_{eingabe}.txt"
        antwort_pfad.write_text(antwort_text, encoding="utf-8")

        print(f"Prompt {eintrag['id']} ({eingabe}) erstellt und Antwort gespeichert -> {antwort_pfad.name}")

# Auswertung der Antworten
auswerter = Evaluation()

# Strategie A
# darstellung = auswerter.erstelle_auswertung("strategie_A", "Strategie A", None)
# print(darstellung)

# Strategie B
# darstellung = auswerter.erstelle_auswertung("strategie_B", "Strategie B", None)
# print(darstellung)

# Strategie C
darstellung = auswerter.erstelle_auswertung("strategie_C", "Strategie C", None)
print(darstellung)

