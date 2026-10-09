# Antrag auf wissenschaftliche Datennutzung (FDZ-RV)
## Forschungsdatenzentrum der Rentenversicherung (FDZ-RV)
**Deutsche Rentenversicherung Bund**  
Bereich 0420 – Forschungsdatenzentrum  
10709 Berlin, Deutschland  
E-Mail: fdz@drv-bund.de | Web: https://www.fdz-rv.de

---

### 1. Angaben zum Antragsteller und zur Forschungseinrichtung

* **Name des Forschers / Antragstellers:** Cristhian David Cáceres Mateus
* **Matrikelnummer:** `93515346`
* **Status:** Wissenschaftlicher Forscher / Projektmitarbeiter (M.Sc. Data Science)
* **Wissenschaftliche Einrichtung:** University of Europe for Applied Sciences (UE Germany)
* **Campus:** Potsdam Campus (Think Campus, Konrad-Zuse-Ring 11, 14469 Potsdam, Deutschland)
* **Fachbereich:** Fachbereich Wirtschaft / Department of Business
* **Wissenschaftliche Projektleitung:** Prof. Dr. Talha Ali Khan (Department of Business)
* **E-Mail der Projektleitung:** talhaali.khan@ue-germany.de
* **Zweck der Datennutzung:** Wissenschaftliches Forschungsprojekt / Institutsinterne universitäre Forschung an der University of Europe for Applied Sciences.

---

### 2. Angaben zum beantragten Datensatz und Zugangsweg

* **Beantragter Datensatz:**  
  **VSKT – Versichertenkontenstichprobe** (Scientific Use File – SUF)  
  *Ergänzend / Bei Bedarf:* **Remote Data Execution (Fernrechnen)** gemäß den Standards des FDZ-RV, falls detaillierte Zuwanderungs- bzw. Staatsangehörigkeitsmerkmale dies erfordern.
* **Berichtsjahrgänge / Wellen:** Neueste regulär freigegebene Fassung der Versichertenkontenstichprobe (z. B. VSKT 2022 / 2023).
* **Zielpopulation:** Aktiv versicherte und rentennahe Kohorten im erwerbsfähigen Alter (20–67 Jahre) zur Analyse von Beitragsverläufen nach Staatsangehörigkeit und Geschlecht.

---

### 3. Projekttitel und Zusammenfassung

* **Projekttitel (Deutsch):**  
  *Vermögen, Migration und Alterssicherung in Deutschland: Dynamische Mikrosimulation und ökonometrische Analyse von Rentenanwartschaften und Altersarmutsrisiken (2025–2070)*
* **Project Title (English):**  
  *Wealth, Migration & Retirement Sustainability in Germany: Dynamic Microsimulation and Econometric Policy Analysis (2025–2070)*

#### Zusammenfassung des Forschungsvorhabens (Abstract):
Die demografische Alterung Deutschlands stellt das umlagefinanzierte System der Gesetzlichen Rentenversicherung (GRV, SGB VI) vor fundamentale Herausforderungen. Nach der 16. koordinierten Bevölkerungsvorausberechnung des Statistischen Bundesamtes steigt der Altenquotient in den kommenden Jahrzehnten drastisch an. Gleichzeitig hängt die finanzielle und arbeitsmarktpolitische Stabilisierung des Systems wesentlich von der Arbeitsmarkt- und Beitragsintegration zugewanderter Erwerbstätiger ab.

Dieses Forschungsvorhaben untersucht anhand eines mehrstufigen mikroökonometrischen Modells und einer dynamischen Mikrosimulationsplattform die Rentenanwartschaften, Beitragsbiografien und Alterseinkommensrisiken verschiedener Bevölkerungsgruppen in Deutschland. Die VSKT fungiert dabei als zentrale empirische Säule für die Abbildung realer Versicherungsverläufe, beitragsrelevanter Erwerbseinkommen und der Entgeltpunkteakkumulation. Ergänzt wird die Analyse durch mikrodatenbasierte Arbeitsmarktmuster (IAB-BAMF-SOEP) und Haushaltsvermögensdaten (Bundesbank PHF) in einem methodisch harmonisierten Kalibrierungsansatz (ohne direkten Personenlinkage). Ziel ist es, zu analysieren, wie Zuwanderungszeitpunkt, Beitragsunterbrechungen und Ausgleichselemente (Kindererziehungszeiten nach § 56 SGB VI, Grundrente nach § 76g SGB VI) die spätere Rentenhöhe determinieren und in welchem Maße Lücken zur Grundsicherung im Alter (SGB XII, 4. Kapitel) entstehen.

---

### 4. Detaillierte wissenschaftliche Problemstellung und Forschungsfragen

Die zentrale wissenschaftliche Fragestellung lautet:
> **In welchem Ausmaß determinieren Zuwanderungsalter, Erwerbsbiografien und geschlechtsspezifische Faktoren die realisierten Entgeltpunkte in der GRV, und wie interagieren diese Rentenanwartschaften mit dem soziokulturellen Existenzminimum (SGB XII) im Alter?**

#### Spezifische Forschungsfragen:
1. **Erwerbs- und Beitragsdynamik (H1):** Wie unterscheiden sich die kumulierten Beitragsjahre und Entgeltpunkte zwischen Zuwanderergruppen mit unterschiedlicher Aufenthaltsdauer und der inländischen Referenzbevölkerung?
2. **Erwerbsverläufe & Entgeltpunkteentwicklung (H2):** Welche Zusammenhänge zeigen sich zwischen Zuwanderungsbiografien, beobachteten beitragspflichtigen Erwerbseinkommen und der jährlichen Entgeltpunkteakkumulation in der VSKT?
3. **Geschlechterdimension & Kindererziehungszeiten (H3):** In welchem Umfang kompensieren Kindererziehungszeiten (§ 56 SGB VI) den geschlechtsspezifischen Rentenabstand (*Gender Pension Gap*) bei zugewanderten Frauen im Vergleich zu Männern?
4. **Grundsicherungsinteraktion & Grundrente (H4):** Wie hoch ist der Anteil der Versicherten in den jeweiligen Kohorten, deren autonome GRV-Rente unter dem jeweiligen existenzsichernden Grundsicherungsniveau (SGB XII, 4. Kapitel) verbleibt, und wie wirkt der Grundrentenzuschlag (§ 76g SGB VI) als Puffer?

---

### 5. Methodischer Ansatz und Modellarchitektur

Das Vorhaben nutzt eine mehrstufige mikroökonometrische und versicherungsmathematische Methodik:
1. **Längsschnittanalyse von Versicherungskonten:** Deskriptive und multivariate Analyse der realen Beitragsverläufe (Pflichtbeitragszeiten, Anrechnungszeiten, Kindererziehungszeiten) aus der VSKT.
2. **Mincer'sche Lohn- und Entgeltpunkteregressionen:** Schätzung von Panel- und OLS-Modellen mit robusten Standardfehlern (HC1/HC3) zur Modellierung der jährlichen Entgeltpunkteentwicklung in Abhängigkeit von Alter, Aufenthaltsdauer, Bildungsniveau und Geschlecht.
3. **Dynamische Mikrosimulation (2025–2070):** Fortschreibung individueller Erwerbs- und Rentenbiografien bis zum gesetzlichen Renteneintrittsalter von 67 Jahren (§ 35 SGB VI) unter flexibler Parametrisierung der gesetzlichen Rechengrößen (wie Aktueller Rentenwert, Durchschnittsentgelt und Beitragsbemessungsgrenzen gemäß den jeweiligen Verordnungsjahren).
4. **Kopplung an SGB XII & Vermögensabbau:** Simulation des potentiellen Leistungsanspruchs auf Grundsicherung im Alter unter Beachtung der jeweils geltenden Vermögensschonbeträge (§ 90 SGB XII) und Grundrentenfreibeträge (§ 82a SGB XII).

---

### 6. Spezifikation der benötigten Merkmale / Variablenliste (VSKT)

Für die Durchführung der empirischen Analysen werden folgende Merkmalsbereiche aus der VSKT benötigt:

| Merkmalskategorie | Benötigte VSKT-Variablen | Wissenschaftliche Begründung |
|:---|:---|:---|
| **Demografie** | Geburtsjahr, Geschlecht, Wohnort/Bundesland (Ost/West) | Alterskohortenabgrenzung, Lebenszeitberechnung, Gender Pension Gap. |
| **Staatsangehörigkeit / Herkunft** | Staatsangehörigkeitsschlüssel (deutsch, EU, Drittstaat, wichtige Herkunftsländer) | Unterscheidung von Zuwanderungs- und Inländergruppen im Rahmen der Datenverfügbarkeit. |
| **Versicherungsbiografie** | Versicherungsmonate gesamt, Pflichtbeitragszeiten, beitragsfreie Zeiten, Anrechnungszeiten | Berechnung von Wartezeiten (5 Jahre Regelaltersrente, 35/45 Jahre für langjährig Versicherte). |
| **Entgeltpunkte (EP)** | Entgeltpunkte gesamt, EP aus Beitragszeiten, EP aus beitragsfreien Zeiten, EP Ost/West | Kernvariable für gesetzliche Bruttomonatsrente ($Rente = EP \times ZF \times AR$). |
| **Kindererziehungszeiten** | Anzahl der Monate mit Kindererziehungszeiten (§ 56 SGB VI), Berücksichtigungszeiten | Quantifizierung des ausgleichenden Effekts von Kindererziehungszeiten für Frauen. |
| **Grundrentenzeiten** | Grundrentenzeiten (§ 76g SGB VI), Zuschlags-EP | Evaluierung des Anspruchs auf Grundrentenzuschlag und Freibetrag nach § 82a SGB XII. |
| **Entgelt / Beitragsbemessung** | Gemeldete beitragspflichtige Bruttoarbeitsentgelte pro Kalenderjahr | Kalibrierung von Erwerbsprofilen und jährlichen Entgeltpunktezuwächsen. |

---

### 7. Datenschutz, Datensicherheit und Löschungsverpflichtung

Der Antragsteller und die betreuende Hochschule verpflichten sich zur strikten Einhaltung der Bestimmungen des Bundesdatenschutzgesetzes (BDSG), der DSGVO sowie des § 16 Bundesstatistikgesetz (BStatG) / Sozialgesetzbuch X (SGB X):
1. **Vertraulichkeit:** Die Daten werden ausschließlich für den in diesem Antrag spezifizierten wissenschaftlichen Forschungszweck verwendet. Eine Weitergabe an Dritte oder eine kommerzielle Nutzung ist ausgeschlossen.
2. **Re-Identifikationsverbot:** Es werden keinerlei Versuche unternommen, anonymisierte Einzeldatensätze mit realen Personen zu verknüpfen. Ergebnisse werden ausschließlich in hochaggregierter Form (Tabellen, Kennzahlen, Grafiken) veröffentlicht, die keine Rückschlüsse auf Einzelfälle zulassen (Mindestfallzahl $N \ge 5$).
3. **Speicherung & Zugriff:** Die Datenhaltung erfolgt auf einem passwortgeschützten, verschlüsselten Forschungsspeicher der University of Europe for Applied Sciences.
4. **Löschung:** Nach Abschluss des Forschungsprojekts und der wissenschaftlichen Publikation der Ergebnisse (spätestens zum 31. Dezember 2027) werden alle Rohdatensätze und Zwischendateien nachweislich und unwiderruflich gelöscht.

---

### 8. Unterschriften und Bestätigung

**Ort, Datum:** Potsdam, den ________________________

\
____________________________________________________  
**Cristhian David Cáceres Mateus**  
(Antragsteller / Forschender, Matr.-Nr. 93515346)

\
____________________________________________________  
**Prof. Dr. Talha Ali Khan**  
(Wissenschaftliche Projektleitung / Professor, University of Europe for Applied Sciences)
