from textwrap import dedent
from pathlib import Path
from openai import OpenAI
from promptTyp import PromptTyp
from anweisungen import Anweisungen
from aufgabenTyp import AufgabenTyp
from aufgabenTyp import kriterien_pro_aufgabe, kategorien_pro_aufgabe, rubriken_pro_aufgabe
from datetime import datetime


class PromptErsteller:
    """Klasse zum Erstellen von Prompts basierend auf verschiedenen Typen und Parametern."""

    def __init__(self):
        pass

    def erstelle_prompt(
        self,
        prompt_typ: PromptTyp,
        aufgaben_typ: AufgabenTyp,
        aufgabenstellung: str,
        musterloesung: str = None,
        beispiele: str = None,
        studenten_antwort: str = None,
    ) -> str:
        """
        Erstellt einen Prompt basierend auf dem Typ und den übergebenen Parametern.

        :param prompt_typ: Der Typ des Prompts (z. B. BEISPIELANTWORTEN, STRATEGIEA, STRATEGIEB, STRATEGIEC)
        :param aufgaben_typ: Der Typ der Aufgabe
        :param aufgabenstellung: Die Aufgabenstellung
        :param musterloesung: Optional, die Musterlösung
        :param beispiele: Optional, Beispiele für Few-Shot-Learning
        :param studenten_antwort: Optional, eine studentische Antwort
        :return: Der vollständige Prompt als String
        """
        rubriken = rubriken_pro_aufgabe.get(aufgaben_typ, [])
        rubriken_str = "\n".join(f"- {item}" for item in rubriken)

        kriterien = kriterien_pro_aufgabe.get(aufgaben_typ, [])
        kriterien_str = "\n".join(f"- {item}" for item in kriterien)

        kategorien = kategorien_pro_aufgabe.get(aufgaben_typ, [])
        kategorien_str = ", ".join(kategorien)

        print(f"Debug: Eingehender prompt_typ = {prompt_typ}")

        if prompt_typ == PromptTyp.BEISPIELANTWORTEN:
            return dedent(f"""
Anweisung:
{Anweisungen.BEISPIELANTWORTEN.value}
Aufgabenstellung:
{aufgabenstellung}
Bewertungskategorien:
{kategorien_str}
Bewertungskriterien
Folgende Kriterien werden bewertet:
{kriterien_str}
Musterlösung:
{musterloesung}
            """).strip()

        elif prompt_typ == PromptTyp.STRATEGIEA:
            return dedent(f"""
Anweisung:
{Anweisungen.STRATEGIEA.value}
Aufgabenstellung:
{aufgabenstellung}
Bewertungsrubrik:
{rubriken_str}
Studentische Antwort:
{studenten_antwort}
            """).strip()

        elif prompt_typ == PromptTyp.STRATEGIEB:
            return dedent(f"""
Rollenbeschreibung:
{Anweisungen.STRATEGIEB.value}
Aufgabenstellung:
{aufgabenstellung}
Beispiele:
{beispiele}
Bewertungsrubrik:
{rubriken_str}
Studentische Antwort:
{studenten_antwort}
            """).strip()

        elif prompt_typ == PromptTyp.STRATEGIEC:
            return dedent(f"""
Rollenbeschreibung:
{Anweisungen.STRATEGIEC.value}
Aufgabenstellung:
{aufgabenstellung}
Beispiele:
{beispiele}
Bewertungsrubrik:
{rubriken_str}
Studentische Antwort:
{studenten_antwort}
            """).strip()

        else:
            raise ValueError("Unbekannter Prompt-Typ")

    def rufe_modellantworten_ab(self, prompt_text: str, modell: str = "gpt-4o") -> str:
        """
        Ruft das OpenAI-Modell auf und gibt die Antwort zurück.

        :param prompt_text: Der zu sendende Prompt
        :param modell: Das zu verwendende Modell (Standard: gpt-4o)
        :return: Die Antwort des Modells als String
        """
        client = OpenAI()
        resp = client.responses.create(
            model=modell,
            input=prompt_text,
        )
        return resp.output_text

    def waehle_studentenantwort(self, pfad: str, kategorie: str, nummer: int) -> str:
        """
        Wählt eine studentische Antwort aus einer Datei basierend auf der Kategorie und der Nummer aus.

        :param pfad: Der Pfad zur Datei mit den Antworten
        :param kategorie: Die Kategorie der Antwort (z. B. "korrekt", "teilweise inkorrekt", "inkorrekt")
        :param nummer: Die Nummer der Antwort in der Kategorie (1 oder 2)
        :return: Die ausgewählte studentische Antwort als String
        """
        antwort_zeilen = []
        try:
            print(f"Öffne Datei: {pfad}")
            with open(pfad, "r", encoding="utf-8") as f:
                zeilen = f.readlines()

            in_kategorie = False
            in_antwort = False

            for zeile in zeilen:
                zeile_clean = zeile.strip()

                if zeile_clean.lower().startswith("### bewertungskategorie:") and kategorie.lower() in zeile_clean.lower():
                    print(f"Kategorie gefunden: {kategorie}")
                    in_kategorie = True
                    continue

                if zeile_clean.lower().startswith("### bewertungskategorie:") and in_kategorie:
                    break

                if in_kategorie and zeile_clean.lower().startswith(f"**antwort {nummer}**".lower()):
                    print(f"Antwort {nummer} gefunden in Kategorie {kategorie}")
                    in_antwort = True
                    continue

                if in_antwort:
                    if zeile_clean.lower().startswith("**antwort") or zeile_clean.lower().startswith("### bewertungskategorie:"):
                        break
                    antwort_zeilen.append(zeile_clean)

            if not antwort_zeilen:
                print(f"Keine Antwort gefunden für Kategorie: {kategorie}, Nummer: {nummer}")
                return "Keine Antwort gefunden."

            return " ".join(antwort_zeilen).strip()

        except FileNotFoundError:
            print(f"Datei nicht gefunden: {pfad}")
            return "Datei nicht gefunden."
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return "Ein Fehler ist aufgetreten."




