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
* **Status:** Masterstudent (M.Sc. Data Science)
* **Wissenschaftliche Einrichtung:** University of Europe for Applied Sciences (UE Germany)
* **Campus:** Dessauer Str. 3–5, 10963 Berlin, Deutschland
* **Fachbereich:** Fachbereich Wirtschaft / Department of Business
* **Wissenschaftliche Betreuung:** Prof. Dr. Talha Ali Khan (Department of Business)
* **E-Mail des Betreuers:** talhaali.khan@ue-germany.de
* **Zweck der Datennutzung:** Masterarbeit / Wissenschaftliches Forschungsprojekt im Rahmen des Masterstudiengangs M.Sc. Data Science.

---

### 2. Angaben zum beantragten Datensatz und Zugangsweg

* **Beantragter Datensatz:**  
  **VSKT – Versichertenkontenstichprobe** (Scientific Use File – SUF)  
  *Alternativ / Ergänzend:* **Fernrechnen via JoSuA** (für detailliertere Variablenmerkmale).
* **Berichtsjahrgänge / Wellen:** Neueste verfügbare Welle (VSKT 2020–2024).
* **Zielpopulation:** Aktiv versicherte und rentennahe Kohorten im erwerbsfähigen Alter (20–67 Jahre) mit Differenzierung nach Staatsangehörigkeit, Zuwanderungsstatus und Geschlecht.

---

### 3. Projekttitel und Zusammenfassung

* **Projekttitel (Deutsch):**  
  *Vermögen, Migration und Alterssicherung in Deutschland: Dynamische Mikrosimulation und ökonometrische Analyse von Rentenanwartschaften und Altersarmutsrisiken (2025–2070)*
* **Project Title (English):**  
  *Wealth, Migration & Retirement Sustainability in Germany: Dynamic Microsimulation and Econometric Policy Analysis (2025–2070)*

#### Zusammenfassung des Forschungsvorhabens (Abstract):
Die demografische Alterung Deutschlands stellt das umlagefinanzierte System der Gesetzlichen Rentenversicherung (GRV, SGB VI) vor fundamentale Herausforderungen. Nach der 16. koordinierten Bevölkerungsvorausberechnung des Statistischen Bundesamtes steigt der Altenquotient bis 2070 drastisch an. Gleichzeitig hängt die finanzielle und arbeitsmarktpolitische Stabilisierung des Systems zunehmend von der Integration zugewanderter Arbeitskräfte und Geflüchteter ab.

Dieses Forschungsvorhaben untersucht anhand einer dynamischen Mikrosimulationsplattform die langfristigen Rentenanwartschaften, Lohnbiografien und Alterseinkommenslücken von fünf komparativen Bevölkerungsgruppen in Deutschland: (1) deutsche Referenzbevölkerung, (2) Arbeitsmigranten der 1. Generation, (3) Geflüchtete der Asylzuwanderung 2015/16, (4) ukrainische Kriegsflüchtlinge (§ 24 AufenthG) und (5) ukrainische Vorkriegsmigranten. Ziel der Arbeit ist es, auf Basis der realen Erwerbs- und Versicherungskonten der VSKT zu quantifizieren, in welchem Umfang unterbrochene Erwerbsverläufe, späte Zuwanderungszeitpunkte und Qualifikationsentwertungen (Deskilling) zu Rentenlücken führen und wie kompensatorische Mechanismen (Kindererziehungszeiten nach § 56 SGB VI, Grundrente nach § 76g SGB VI sowie private Vermögensakkumulation) die Inanspruchnahme von Grundsicherung im Alter (SGB XII, 4. Kapitel) beeinflussen.

---

### 4. Detaillierte wissenschaftliche Problemstellung und Forschungsfragen

Die zentrale wissenschaftliche Fragestellung lautet:
> **In welchem Ausmaß determinieren Zuwanderungsalter, Erwerbsbiografien und geschlechtsspezifische Faktoren die realisierten Entgeltpunkte in der GRV, und welche zusätzlichen monatlichen Sparleistungen ($S^*$) sind erforderlich, um das soziokulturelle Existenzminimum (SGB XII) bzw. eine adäquate Nettoersatzquote von 60% im Ruhestand zu gewährleisten?**

#### Spezifische Forschungsfragen:
1. **Erwerbs- und Beitragsdynamik (H1):** Wie unterscheiden sich die kumulierten Beitragsjahre und Entgeltpunkte zwischen Zuwanderergruppen mit unterschiedlicher Aufenthaltsdauer und der inländischen Referenzbevölkerung?
2. **Qualifikationsentwertung & Lohnregression (H2):** Welcher Anteil des Beitragsrückstands bei tertiär gebildeten Migranten ist auf initiale Lohnabschläge durch fehlende formale Berufs- und Bildungsanerkennung zurückzuführen?
3. **Geschlechterdimension & Kindererziehungszeiten (H3):** In welchem Umfang kompensieren Kindererziehungszeiten (§ 56 SGB VI) den geschlechtsspezifischen Rentenabstand (*Gender Pension Gap*) bei zugewanderten Frauen im Vergleich zu Männern?
4. **Grundsicherungsrisiko & Grundrente (H4):** Wie hoch ist der Anteil der jeweiligen Zuwanderungskohorten, deren autonome GRV-Rente unter dem Grundsicherungsniveau von ca. €1.113/Monat verbleibt, und wie wirkt der Grundrentenzuschlag (§ 76g SGB VI) als Armutspuffer?

---

### 5. Methodischer Ansatz und Modellarchitektur

Das Vorhaben nutzt eine mehrstufige mikroökonometrische und versicherungsmathematische Methodik:
1. **Längsschnittanalyse von Versicherungskonten:** Deskriptive und multivariate Analyse der realen Beitragsverläufe (Pflichtbeitragszeiten, Anrechnungszeiten, Kindererziehungszeiten) aus der VSKT.
2. **Mincer'sche Lohn- und Entgeltpunkteregressionen:** Schätzung von Panel- und OLS-Modellen mit robusten Standardfehlern (HC1/HC3) zur Modellierung der jährlichen Entgeltpunkteentwicklung in Abhängigkeit von Alter, Aufenthaltsdauer, Bildungsniveau und Geschlecht.
3. **Dynamische Mikrosimulation (2025–2070):** Fortschreibung individueller Erwerbs- und Rentenbiografien bis zum gesetzlichen Renteneintrittsalter von 67 Jahren (§ 35 SGB VI) unter Zugrundelegung der aktuellen sozialrechtlichen Parameter (Aktueller Rentenwert $\text{AR}_{2026} = 42,52$ €, Durchschnittsentgelt $\text{DE}_{2026} = 51.944$ €, BBG $= 101.400$ €).
4. **Kopplung an SGB XII & Vermögensabbau:** Simulation des Leistungsanspruchs auf Grundsicherung im Alter unter Beachtung des Vermögensfreibetrags (§ 90 SGB XII, 10.000 €) und des Grundrentenfreibetrags (§ 82a SGB XII).

---

### 6. Spezifikation der benötigten Merkmale / Variablenliste (VSKT)

Für die Durchführung der empirischen Analysen werden folgende Merkmalsbereiche aus der VSKT benötigt:

| Merkmalskategorie | Benötigte VSKT-Variablen | Wissenschaftliche Begründung |
|:---|:---|:---|
| **Demografie** | Geburtsjahr, Geschlecht, Bundesland (Ost/West) | Alterskohortenabgrenzung, Lebenszeitberechnung, Gender Pension Gap. |
| **Staatsangehörigkeit / Herkunft** | Staatsangehörigkeitsschlüssel (deutsch, EU, Drittstaat, Asylherkunftsländer, Ukraine) | Differenzierung der 5 Untersuchungsgruppen. |
| **Versicherungsbiografie** | Versicherungsmonate gesamt, Beitragsmonate, beitragsfreie Zeiten, Anrechnungszeiten | Berechnung der Wartezeit (5 Jahre Regelaltersrente, 35/45 Jahre für langjährig Versicherte). |
| **Entgeltpunkte (EP)** | Entgeltpunkte gesamt, EP aus Beitragszeiten, EP aus beitragsfreien Zeiten, EP Ost/West | Kernvariable für Bruttomonatsrente ($Rente = EP \times ZF \times AR$). |
| **Kindererziehungszeiten** | Anzahl der Monate mit Kindererziehungszeiten (§ 56 SGB VI), Berücksichtigungszeiten | Quantifizierung des armutsmindernden Effekts von Erziehungsgutschriften für Frauen. |
| **Grundrentenzeiten** | Vorhandensein von Grundrentenzeiten (§ 76g SGB VI), Zuschlags-EP | Evaluierung des Anspruchs auf Grundrentenzuschlag und Freibetrag nach § 82a SGB XII. |
| **Entgelt / Beitragsbemessung** | Gemeldete beitragspflichtige Bruttoarbeitsentgelte pro Kalenderjahr | Kalibrierung der Mincer-Lohnprofile und jährlichen Entgeltpunktezuwächse. |

---

### 7. Datenschutz, Datensicherheit und Löschungsverpflichtung

Der Antragsteller und die betreuende Hochschule verpflichten sich zur strikten Einhaltung der Bestimmungen des Bundesdatenschutzgesetzes (BDSG), der DSGVO sowie des § 16 Bundesstatistikgesetz (BStatG) / Sozialgesetzbuch X (SGB X):
1. **Vertraulichkeit:** Die Daten werden ausschließlich für den in diesem Antrag spezifizierten wissenschaftlichen Forschungszweck verwendet. Eine Weitergabe an Dritte oder eine kommerzielle Nutzung ist ausgeschlossen.
2. **Re-Identifikationsverbot:** Es werden keinerlei Versuche unternommen, anonymisierte Einzeldatensätze mit realen Personen zu verknüpfen. Ergebnisse werden ausschließlich in hochaggregierter Form (Tabellen, Kennzahlen, Grafiken) veröffentlicht, die keine Rückschlüsse auf Einzelfälle zulassen (Mindestfallzahl $N \ge 5$).
3. **Speicherung & Zugriff:** Die Datenhaltung erfolgt auf einem passwortgeschützten, verschlüsselten Forschungsspeicher der University of Europe for Applied Sciences.
4. **Löschung:** Nach Abschluss des Forschungsprojekts und der Begutachtung der Masterarbeit (spätestens zum 31. Dezember 2027) werden alle Rohdatensätze und Zwischendateien nachweislich und unwiderruflich gelöscht.

---

### 8. Unterschriften und Bestätigung

**Ort, Datum:** Berlin, den ________________________

\
____________________________________________________  
**Cristhian David Cáceres Mateus**  
(Antragsteller / Masterstudent, Matr.-Nr. 93515346)

\
____________________________________________________  
**Prof. Dr. Talha Ali Khan**  
(Wissenschaftlicher Betreuer, University of Europe for Applied Sciences)
