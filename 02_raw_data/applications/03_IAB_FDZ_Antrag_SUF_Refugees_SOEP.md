# Antrag auf Bereitstellung eines Scientific Use Files (IAB FDZ)
## Forschungsdatenzentrum der Bundesagentur für Arbeit
**im Institut für Arbeitsmarkt- und Berufsforschung (FDZ des IAB)**  
Regensburger Straße 104  
90478 Nürnberg, Deutschland  
E-Mail: iab.fdz@iab.de | Web: https://fdz.iab.de

---

### 1. Stammdaten des Antragstellers und der Forschungsinstitution

* **Name des Forschenden / Antragstellers:** Cristhian David Cáceres Mateus
* **Matrikelnummer:** `93515346`
* **Status:** Masterand (M.Sc. Data Science)
* **Hochschule / Forschungseinrichtung:** University of Europe for Applied Sciences (UE Germany)
* **Campus-Adresse:** Dessauer Str. 3–5, 10963 Berlin
* **Betreuender Hochschullehrer:** Prof. Dr. Talha Ali Khan (Faculty of Tech and Software / Data Science)
* **E-Mail des Betreuers:** talhaali.khan@ue-germany.de
* **Art des wissenschaftlichen Projekts:** Masterarbeit im Studiengang M.Sc. Data Science
* **Beantragte Datenform:** **Scientific Use File (SUF)** zur dezentralen wissenschaftlichen Auswertung an der Hochschule.

---

### 2. Beantragter Datensatz und Wellen

* **Datensatzbezeichnung:**  
  1. **IAB-BAMF-SOEP Befragung von Geflüchteten** (Stichproben M3–M5, aktuelle Welle / Längsschnitt 2016–2023/2024).  
  2. **IAB-SOEP Migrationsstichproben** (Stichproben M1/M2 für historische und Vorkriegs-Zuwanderer).
* **Zielgruppe:** Erwerbsfähige geflüchtete Personen (insb. Asylzuwanderung 2015/16 sowie ukrainische Geflüchtete unter § 24 AufenthG) und Arbeitsmigranten im erwerbsfähigen Alter (18–65 Jahre).

---

### 3. Projekttitel und Exposé

* **Projekttitel (Deutsch):**  
  *Arbeitsmarktintegration, Qualifikationsanerkennung und Rücküberweisungen von Geflüchteten und Zuwanderern in Deutschland: Ökonometrische Modellierung langfristiger Alterssicherungsbiografien*
* **Project Title (English):**  
  *Labor Market Integration, Qualification Deskilling, and Remittance Dynamics Among Refugees and Migrants in Germany: Econometric Foundations for Long-Term Retirement Microsimulation*

#### Wissenschaftliche Problemstellung (Abstract):
Die langfristige Alterssicherung von Zuwanderern und Geflüchteten in Deutschland hängt maßgeblich von der Geschwindigkeit und Qualität ihrer Arbeitsmarktintegration in den ersten Dekaden nach dem Zuzug ab. Viele Geflüchtete und Neuzuwanderer – insbesondere aus der Ukraine und den Hauptherkunftsländern der Fluchtmigration 2015/16 – weisen ein hohes formales Bildungsniveau auf (über 65% tertiäre Abschlüsse unter ukrainischen Geflüchteten), sind jedoch in den ersten Jahren mit erheblichen Lohnabschlägen und Beschäftigung unterhalb ihres Qualifikationsniveaus konfrontiert (*Deskilling*). Gleichzeitig mindern regelmäßige Rücküberweisungen an Familienangehörige im Herkunftsland (*Remittances*) das für die private Altersvorsorge und Vermögensbildung verfügbare Nettoeinkommen.

Dieses Forschungsvorhaben nutzt die Mikrodaten der IAB-BAMF-SOEP Befragung von Geflüchteten, um:
1. Den Zeithorizont und die Determinanten des Übergangs von informeller / geringqualifizierter Tätigkeit in qualifikationsadäquate sozialversicherungspflichtige Beschäftigung ökonometrisch zu schätzen.
2. Den kausalen Lohnabschlag durch fehlende bzw. verzögerte Berufs- und Bildungsanerkennung unter Berücksichtigung von Sprachkompetenzen (GER-Stufen A1 bis C2) zu isolieren.
3. Die Höhe und Persistenz privater monatlicher Rücküberweisungen ins Ausland zu quantifizieren.
4. Die resultierenden Beitragsbiografien als empirische Eingangsparameter in eine dynamische Mikrosimulationsplattform zu überführen, die Rentenlücken bis zum 67. Lebensjahr und die Entlastungswirkung beschleunigter Anerkennungsverfahren evaluiert.

---

### 4. Forschungsfragen und ökonometrische Hypothesen

* **Forschungsfrage 1 (Integrationskurve & Aufenthaltsdauer):** Wie entwickelt sich die Wahrscheinlichkeit einer sozialversicherungspflichtigen Vollzeitbeschäftigung über die Aufenthaltsdauer (1 bis 10 Jahre nach Zuzug), und welche Unterschiede bestehen zwischen humanitärer Zuwanderung (Geflüchtete) und regulärer Arbeitsmigration?
* **Forschungsfrage 2 (Qualifikationsanerkennung & Deskilling-Prämie):** Führt der erfolgreiche Abschluss eines formalen Anerkennungsverfahrens ausländischer Hochschulabschlüsse zu einem signifikanten Lohnsprung, der die jährliche Akkumulation von Entgeltpunkten in der GRV messbar beschleunigt?
* **Forschungsfrage 3 (Sprachkapital):** Welchen marginalen Ertrag generiert der Erwerb fortgeschrittener Deutschkenntnisse (B2/C1 nach GER) auf das monatliche Bruttoerwerbseinkommen?
* **Forschungsfrage 4 (Rücküberweisungsverhalten & Sparquote):** In welchem Umfang reduzieren monatliche Rücküberweisungen ins Herkunftsland die Sparfähigkeit der Haushalte für den Aufbau privaten Altersvorsorgevermögens?

---

### 5. Methodik

1. **Mincer'sche Lohnregressionen mit Selektionskorrektur:**  
   Schätzung erweiterter Lohnfunktionen (Heckman Two-Step zur Berücksichtigung der Erwerbsbeteiligungsselektion):
   $$\ln(\text{Wage}_{it}) = \alpha + \beta_1 \text{Duration}_{it} + \beta_2 \text{Duration}_{it}^2 + \beta_3 \text{Tertiary}_i + \beta_4 \text{German\_B2C2}_{it} - \beta_5 \text{Deskilling}_{it} + \mathbf{X}_{it}'\boldsymbol{\gamma} + \varepsilon_{it}$$
2. **Panel-Ökonometrie (Random / Fixed Effects):**  
   Analyse individueller Lohn- und Spracherwerbstrajektorien über mehrere Befragungswellen.
3. **Mikrosimulationskalibrierung:**  
   Die geschätzten Koeffizienten fließen direkt in das Open-Source-Simulationsmodell des Forschungsprojekts ein, um kontrafaktische Politikreformen (z. B. Fast-Track-Anerkennung ausländischer Abschlüsse) versicherungsmathematisch zu bewerten.

---

### 6. Liste der beantragten IAB-BAMF-SOEP Variablen

| Merkmalsbereich | Relevante Variablenkürzel (SOEP/IAB) | Verwendungszweck |
|:---|:---|:---|
| **Zuwanderungsbiografie** | `zuzug`, `zuzugsjahr`, `aufenthalt_status`, `asyl_entscheid` | Bestimmung der Aufenthaltsdauer und Rechtsstatus (§ 24 AufenthG vs. Asyl). |
| **Bildung im Herkunftsland** | `schule_ausl`, `beruf_ausl`, `hochschule_ausl`, `isced_ausl` | Erfassung des im Heimatland erworbenen Humankapitals. |
| **Anerkennungsverfahren** | `anerkennung_antrag`, `anerkennung_status`, `anerkennung_voll` | Zentrale Variable zur Messung des Deskilling- und Anerkennungseffekts. |
| **Erwerbstätigkeit & Arbeitsmarkt** | `erwstat`, `tatzeit`, `stib` (Stellung im Beruf), `vollzeit_teilzeit` | Unterscheidung von sozialversicherungspflichtiger Vollzeit, Teilzeit und Minijobs. |
| **Einkommen & Löhne** | `labgro`, `labnet` (Brutto-/Nettoerwerbseinkommen monatlich) | Abhängige Variable der Lohnregression und Basis für Rentenbeiträge. |
| **Sprachkompetenz** | `deutsch_sprechen`, `deutsch_schreiben`, `deutsch_lesen` (GER) | Quantifizierung des Sprachkapitals (A1 bis C2). |
| **Rücküberweisungen (Remittances)** | `ueberweis_ausl`, `ueberweis_betrag` (Betrag p.a. / monatlich) | Kalibrierung des Liquiditätsabflusses ins Herkunftsland. |
| **Soziodemografie & Familie** | `gebjahr`, `sex`, `familienstand`, `kinder_im_hh` | Kontrolle von Lebensalter, Geschlecht und Kindererziehungszeiten. |

---

### 7. Erklärung zu Datenschutz und Datensicherheit

Der Antragsteller versichert:
1. Die Daten werden ausschließlich für den wissenschaftlichen Zweck der Masterarbeit an der University of Europe for Applied Sciences verwendet.
2. Der Zugang zu den Daten erfolgt ausschließlich über passwortgeschützte, verschlüsselte IT-Infrastrukturen der Hochschule.
3. Die Bestimmungen des Bundesdatenschutzgesetzes (BDSG), der DSGVO und des IAB-FDZ-Nutzungsvertrages werden uneingeschränkt eingehalten.
4. Alle Veröffentlichungen erfolgen in aggregierter Form ohne Ausweisung von Einzelfalldaten (Fallzahlbeschränkung $N \ge 3$).

---

### 8. Unterschriften

**Ort, Datum:** Berlin, den ________________________

\
____________________________________________________  
**Cristhian David Cáceres Mateus**  
(Antragsteller / Masterstudent, Matr.-Nr. 93515346)

\
____________________________________________________  
**Prof. Dr. Talha Ali Khan**  
(Wissenschaftlicher Betreuer, University of Europe for Applied Sciences)
