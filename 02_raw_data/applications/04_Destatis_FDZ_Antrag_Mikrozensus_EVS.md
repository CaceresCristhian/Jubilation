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
* **Status:** Masterstudent (M.Sc. Data Science)
* **Wissenschaftliche Institution:** University of Europe for Applied Sciences (UE Germany)
* **Campus:** Dessauer Str. 3–5, 10963 Berlin
* **Betreuende Dozentin / Erstprüferin:** Dr. Humera Noor (Faculty of Tech and Software)
* **E-Mail des Betreuers:** humera.noor@ue-germany.de
* **Zweck der Nutzung:** Wissenschaftliche Masterarbeit im Rahmen des Masterstudiengangs M.Sc. Data Science.

---

### 2. Beantragter Datensatz und Erhebungsjahre

* **Datensatz:**  
  1. **Mikrozensus – Scientific Use File (SUF)** (Erhebungsjahre 2019, 2020, 2021, 2022, 2023)  
  2. *Ergänzend / Alternativ:* **Einkommens- und Verbrauchsstichprobe (EVS) – SUF** (Erhebungsjahre 2018 / 2023).
* **Nutzungsform:** **Scientific Use File (SUF)** zur dezentralen Auswertung auf gesicherten Systemen der Hochschule.

---

### 3. Projekttitel und Wissenschaftliche Zielsetzung

* **Projekttitel (Deutsch):**  
  *Einkommensverteilung, Erwerbsmuster und Altersarmutsrisiken von Zuwanderer- und Geflüchtetenhaushalten in Deutschland: Mikrozensus- und EVS-basierte Analysen für dynamische Mikrosimulationsmodelle*
* **Project Title (English):**  
  *Income Distribution, Labor Market Patterns, and Old-Age Poverty Risks Among Immigrant and Refugee Households in Germany: Microcensus and EVS Empirical Foundations*

#### Kurzbeschreibung des Vorhabens (Abstract):
Die vorliegende Masterarbeit untersucht die sozioökonomischen Determinanten von Alterseinkommensrisiken bei zugewanderten Bevölkerungsgruppen in Deutschland. Während amtliche Aggregatstatistiken auf ein erhöhtes Armutsrisiko von Personen mit Migrationshintergrund hinweisen, bedarf es repräsentativer Individual- und Haushaltsmikrodaten, um die Heterogenität zwischen Arbeitsmigration, EU-Binnenmigration und humanitärer Zuwanderung (Geflüchtete) differenziert nach Bildungsstand, Erwerbsform (Vollzeit, Teilzeit, Minijobs) und Haushaltskontext abzubilden.

Die Mikrodaten des Mikrozensus und der EVS sollen genutzt werden, um:
1. Repräsentative soziometrische Profile (Alter, Geschlecht, Bildung nach ISCED, Haushaltsgröße, Wohneigentumsquote) für fünf distinkte Bevölkerungsgruppen zu erstellen.
2. Die Verteilung von Erwerbseinkommen und Haushaltsnettoeinkommen über Lebenszyklus-Alterskohorten hinweg ökonometrisch zu analysieren.
3. Die empirische Grundlage für eine dynamische Mikrosimulationsplattform zu schaffen, die den Übergang in den Ruhestand und die Lücke zur Grundsicherung im Alter (SGB XII, 4. Kapitel) prognostiziert.

---

### 4. Detaillierte Begründung des Datenbedarfs

Für die Kalibrierung des Simulationsmodells reichen publizierte Tabellenwerke der amtlichen Statistik nicht aus, da multivariate Kreuztabellierungen nach exakter Aufenthaltsdauer, Bildungsabschluss im Ausland, Erwerbsstatus und Renteneinkünften nicht in der erforderlichen Granularität frei verfügbar sind. Die Scientific Use Files des Mikrozensus ermöglichen die gleichzeitige statistische Kontrolle von:
* Differenzierter Zuwanderungsbiografie (Zuzugsjahr, eigene Zuwanderungserfahrung vs. 2. Generation).
* Erwerbsumfang (Stundenumfang, befristete Verträge, atypische Beschäftigung).
* Haushaltsstruktur und Einkommenspooling im Paar- und Familienkontext.

---

### 5. Benötigte Merkmale / Variablenübersicht (Mikrozensus & EVS)

| Merkmalskategorie | Spezifische Merkmale im Mikrozensus | Relevanz für das Forschungsvorhaben |
|:---|:---|:---|
| **Migrationsmerkmale** | Migrationsstatus im engeren und weiteren Sinn, Zuzugsjahr, Aufenthaltsdauer, Geburtsland, Staatsangehörigkeit | Trennung der 5 Untersuchungsgruppen (Deutsche, Migranten 1. Gen, Geflüchtete 2015/16, Ukrainer). |
| **Bildung & Ausbildung** | Höchster beruflicher und schulischer Abschluss (ISCED-1997 / ISCED-2011), im Ausland erworbener Abschluss | Abbildung des Qualifikationsniveaus und Messung von Bildungsabschlägen. |
| **Erwerbsleben** | Erwerbsstatus, sozioökonomischer Status, geleistete Arbeitsstunden, Vollzeit/Teilzeit/Geringfügigkeit | Modellierung von Beitragszeiten und Rentenanwartschaften (§§ 35, 56 SGB VI). |
| **Einkommensklassen** | Individuelles Nettoeinkommen, Haushaltsnettoeinkommen (Klassen und metrische Angaben) | Ermittlung der relativen Einkommensarmutsgrenze (60% Median) und Sparfähigkeit. |
| **Wohnen & Ausgaben** | Eigentümer vs. Mieter, Wohnfläche, Mietbelastung, Bruttokaltmiete | Schätzung der existenzsichernden Wohnkosten (KdU im Rahmen des SGB XII). |
| **Alterseinkünfte** | Gesetzliche Rente, Betriebsrente, private Vorsorge (bei Rentnern) | Validierung der simulierten Rentenauszahlungsprofile. |

---

### 6. Verpflichtung zur Geheimhaltung und Datensicherheit

1. **Datengeheimnis:** Der Antragsteller verpflichtet sich gemäß § 16 Abs. 1 Bundesstatistikgesetz (BStatG) zur uneingeschränkten Wahrung des statistischen Datengeheimnisses.
2. **Re-Identifikationsverbot:** Jede Handlung, die auf die Re-Identifikation einzelner Befragter oder wirtschaftlicher Einheiten abzielt, ist untersagt.
3. **Ergebniskontrolle:** Tabellen und Abbildungen, die publiziert werden, unterliegen den Geheimhaltungsregeln der Forschungsdatenzentren (Mindestfallzahl $N \ge 3$, bei sensiblen Merkmalen $N \ge 5$).
4. **Aufbewahrung & Löschung:** Die Daten werden ausschließlich auf dem verschlüsselten Forschungsserver der University of Europe for Applied Sciences abgelegt. Nach Abschluss der Masterarbeit werden sämtliche SUF-Dateien vollständig und unwiderruflich gelöscht.

---

### 7. Unterschriften

**Ort, Datum:** Berlin, den ________________________

\
____________________________________________________  
**Cristhian David Cáceres Mateus**  
(Antragsteller / Masterstudent, Matr.-Nr. 93515346)

\
____________________________________________________  
**Dr. Humera Noor**  
(Wissenschaftliche Betreuerin, University of Europe for Applied Sciences)
