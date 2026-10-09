# Antrag auf Nutzung von Scientific Use Files (Destatis FDZ)
## Forschungsdatenzentren der Statistischen Ämter des Bundes und der Länder
**Statistisches Bundesamt (Destatis) – FDZ**  
Gustav-Stresemann-Ring 11  
65189 Wiesbaden, Deutschland  
E-Mail: forschungsdatenzentrum@destatis.de | Web: https://www.forschungsdatenzentrum.de

---

### 1. Angaben zur antragstellenden Person und Institution

* **Name des Antragstellers:** Cristhian David Cáceres Mateus
* **Matrikelnummer:** `93515346`
* **Status:** Wissenschaftlicher Forscher / Projektmitarbeiter (M.Sc. Data Science)
* **Wissenschaftliche Institution:** University of Europe for Applied Sciences (UE Germany)
* **Campus:** Potsdam Campus (Think Campus, Konrad-Zuse-Ring 11, 14469 Potsdam, Deutschland)
* **Wissenschaftliche Projektleitung:** Prof. Dr. Talha Ali Khan (Department of Business)
* **E-Mail der Projektleitung:** talhaali.khan@ue-germany.de
* **Zweck der Nutzung:** Wissenschaftliches Forschungsprojekt / Institutsinterne universitäre Forschung.

---

### 2. Beantragter Datensatz und Erhebungsjahre

* **Datensatz:**  
  1. **Mikrozensus – Scientific Use File (SUF)** (Erhebungsjahre 2019, 2020, 2021, 2022 / 2023)  
     *Zweck:* Repräsentative Bevölkerungsgewichtung, Erwerbsquoten, Bildungsstrukturen und Zuwanderungsmerkmale.  
  2. *Ergänzend / Sekundär:* **Einkommens- und Verbrauchsstichprobe (EVS) – SUF** (Erhebungsjahre 2018 / 2023)  
     *Zweck:* Analyse privater Konsum- und Wohnkostenbudgets zur Kalibrierung von Alterssicherungs-Bedarfen.
* **Nutzungsform:** **Scientific Use File (SUF)** zur dezentralen Auswertung auf gesicherten Systemen der Hochschule.

---

### 3. Projekttitel und Wissenschaftliche Zielsetzung

* **Projekttitel (Deutsch):**  
  *Einkommensverteilung, Erwerbsmuster und Altersarmutsrisiken von Zuwanderer- und Geflüchtetenhaushalten in Deutschland: Mikrozensus- und EVS-basierte Analysen für dynamische Mikrosimulationsmodelle*
* **Project Title (English):**  
  *Income Distribution, Labor Market Patterns, and Old-Age Poverty Risks Among Immigrant and Refugee Households in Germany: Microcensus and EVS Empirical Foundations*

#### Kurzbeschreibung des Vorhabens (Abstract):
Das vorliegende wissenschaftliche Forschungsprojekt untersucht die sozioökonomischen Determinanten von Alterseinkommensrisiken bei zugewanderten Bevölkerungsgruppen in Deutschland. Während amtliche Aggregatstatistiken auf ein erhöhtes Armutsrisiko von Personen mit Migrationshintergrund hinweisen, bedarf es repräsentativer Individual- und Haushaltsmikrodaten, um die Heterogenität zwischen Arbeitsmigration, EU-Binnenmigration und humanitärer Zuwanderung (Geflüchtete) differenziert nach Bildungsstand, Erwerbsform (Vollzeit, Teilzeit, Minijobs) und Haushaltskontext abzubilden.

Die amtlichen Mikrodaten sollen genutzt werden, um:
1. Repräsentative soziometrische Profile (Alter, Geschlecht, Bildung nach ISCED, Haushaltsgröße, Wohneigentumsquote) für Zuwanderer- und Inländerkohorten zu erstellen.
2. Die Verteilung von Erwerbseinkommen und Haushaltsnettoeinkommen über Lebenszyklus-Alterskohorten hinweg ökonometrisch zu analysieren.
3. Repräsentative Gewichtungs- und Kalibrierungsmomente für eine dynamische Mikrosimulationsplattform bereitzustellen, die den Übergang in den Ruhestand und die Interaktion mit dem Grundsicherungsniveau (SGB XII, 4. Kapitel) prognostiziert.

---

### 4. Detaillierte Begründung des Datenbedarfs

Für die Kalibrierung des Simulationsmodells reichen publizierte Tabellenwerke der amtlichen Statistik nicht aus, da multivariate Kreuztabellierungen nach Zuwanderungsjahr, Bildungsabschluss im Ausland, Erwerbsstatus und Haushaltskonstellation nicht in der erforderlichen Granularität frei verfügbar sind. Die Scientific Use Files des Mikrozensus ermöglichen die gleichzeitige statistische Kontrolle von:
* Differenzierter Zuwanderungsbiografie (Zuzugsjahr, eigene Zuwanderungserfahrung vs. 2. Generation).
* Erwerbsumfang (Stundenumfang, befristete Verträge, atypische Beschäftigung).
* Haushaltsstruktur und Einkommenspooling im Paar- und Familienkontext.

---

### 5. Benötigte Merkmale / Variablenübersicht (Mikrozensus & EVS)

| Merkmalskategorie | Spezifische Merkmale im Mikrozensus | Relevanz für das Forschungsvorhaben |
|:---|:---|:---|
| **Migrationsmerkmale** | Migrationsstatus, Zuzugsjahr, Aufenthaltsdauer, Geburtsland, Staatsangehörigkeit | Unterscheidung von Zuwanderungskohorten und inländischer Referenzbevölkerung. |
| **Bildung & Ausbildung** | Höchster beruflicher und schulischer Abschluss (ISCED), im Ausland erworbener Abschluss | Abbildung des Qualifikationsniveaus und Schätzung von Bildungsabschlägen. |
| **Erwerbsleben** | Erwerbsstatus, Stellung im Beruf, geleistete Arbeitsstunden, Vollzeit/Teilzeit | Modellierung von Erwerbsbeteiligungs- und Beitragsquoten im Lebenszyklus. |
| **Einkommensklassen** | Individuelles Nettoeinkommen, Haushaltsnettoeinkommen (Klassen und metrisch) | Ermittlung relativer Einkommensarmutsgrenzen (60% Median) und Sparpotenziale. |
| **Wohnen & Ausgaben** | Eigentümer vs. Mieter, Wohnfläche, Mietbelastung, Bruttokaltmiete | Empirischer Kontext für Wohnkostenbelastungen (zur Parametrisierung von KdU-Szenarien). |
| **Alterseinkünfte** | Gesetzliche Rente, Betriebsrente, private Vorsorge (bei Rentnern) | Externe Validierung und Kalibrierungsabgleich für simulierte Alterseinkünfte. |

---

### 6. Verpflichtung zur Geheimhaltung und Datensicherheit

1. **Datengeheimnis:** Der Antragsteller verpflichtet sich gemäß § 16 Abs. 1 Bundesstatistikgesetz (BStatG) zur uneingeschränkten Wahrung des statistischen Datengeheimnisses.
2. **Re-Identifikationsverbot:** Jede Handlung, die auf die Re-Identifikation einzelner Befragter oder wirtschaftlicher Einheiten abzielt, ist untersagt.
3. **Ergebniskontrolle:** Tabellen und Abbildungen, die publiziert werden, unterliegen den Geheimhaltungsregeln der Forschungsdatenzentren (Mindestfallzahl $N \ge 3$, bei sensiblen Merkmalen $N \ge 5$).
4. **Aufbewahrung & Löschung:** Die Daten werden ausschließlich auf dem verschlüsselten Forschungsserver der University of Europe for Applied Sciences abgelegt. Nach Abschluss des Forschungsprojekts und der wissenschaftlichen Publikation werden sämtliche SUF-Dateien vollständig und unwiderruflich gelöscht.

---

### 7. Unterschriften

**Ort, Datum:** Potsdam, den ________________________

\
____________________________________________________  
**Cristhian David Cáceres Mateus**  
(Antragsteller / Forschender, Matr.-Nr. 93515346)

\
____________________________________________________  
**Prof. Dr. Talha Ali Khan**  
(Wissenschaftliche Projektleitung / Professor, University of Europe for Applied Sciences)
