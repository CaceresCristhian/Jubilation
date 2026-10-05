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
* **Betreuender Hochschullehrer:** Prof. Dr. Talha Ali Khan (Department of Business)
* **E-Mail des Betreuers:** talhaali.khan@ue-germany.de
* **Art des wissenschaftlichen Projekts:** Masterarbeit im Studiengang M.Sc. Data Science
* **Beantragte Datenform:** **Scientific Use File (SUF)** zur dezentralen wissenschaftlichen Auswertung an der Hochschule.

---

### 2. Beantragter Datensatz und Wellen

* **Datensatzbezeichnung:**  
  1. **IAB-BAMF-SOEP Befragung von Geflüchteten** (Stichproben M3–M5, Scientific Use File, Längsschnitt ab 2016)  
     *Zweck:* Untersuchung von Geflüchteten (Asylzuwanderung 2015/16 sowie ukrainische Geflüchtete unter § 24 AufenthG).  
  2. **IAB-SOEP Migrationsstichproben** (Stichproben M1/M2, Scientific Use File)  
     *Zweck:* Untersuchung regulärer Arbeits- und Vorkriegszuwanderer zur methodischen Abgrenzung.
* **Zielgruppe:** Erwerbsfähige zugewanderte und geflüchtete Personen im erwerbsfähigen Alter (18–65 Jahre).

---

### 3. Projekttitel und Exposé

* **Projekttitel (Deutsch):**  
  *Arbeitsmarktintegration, Qualifikationsanerkennung und Rücküberweisungen von Geflüchteten und Zuwanderern in Deutschland: Ökonometrische Modellierung langfristiger Alterssicherungsbiografien*
* **Project Title (English):**  
  *Labor Market Integration, Qualification Deskilling, and Remittance Dynamics Among Refugees and Migrants in Germany: Econometric Foundations for Long-Term Retirement Microsimulation*

#### Wissenschaftliche Problemstellung (Abstract):
Die langfristige Alterssicherung von Zuwanderern und Geflüchteten in Deutschland hängt maßgeblich von der Geschwindigkeit und Qualität ihrer Arbeitsmarktintegration in den ersten Dekaden nach dem Zuzug ab. Viele Neuzuwanderer – insbesondere aus der Ukraine und den Hauptherkunftsländern der humanitären Zuwanderung – verfügen über ein beachtliches formales Bildungsniveau (u. a. über 65% tertiäre Abschlüsse unter ukrainischen Geflüchteten), stehen jedoch initial vor Herausforderungen durch verzögerte Berufs- und Bildungsanerkennung (*Deskilling*) und Spracherwerb.

Dieses Forschungsvorhaben nutzt die Mikrodaten der IAB-BAMF-SOEP Befragung von Geflüchteten und der IAB-SOEP Migrationsstichproben, um:
1. Den Zeithorizont und die Determinanten des Übergangs in sozialversicherungspflichtige Vollzeit- und Teilzeitbeschäftigung über die Aufenthaltsdauer ökonometrisch zu analysieren.
2. Den empirischen Zusammenhang zwischen formaler Qualifikationsanerkennung, Sprachkompetenzen (GER-Stufen A1 bis C2) und realisierten Bruttolöhnen zu untersuchen.
3. Die empirische Relevanz privater monatlicher Rücküberweisungen ins Ausland (*Remittances*) als potentielle Restriktion für die private Altersvorsorge zu prüfen (sekundäres Modul).
4. Die resultierenden Erwerbs- und Lohntrajektorien zur empirischen Kalibrierung einer dynamischen Mikrosimulationsplattform zu nutzen, die Rentenanwartschaften im deutschen Alterssicherungssystem bis zum 67. Lebensjahr abbildet.

---

### 4. Forschungsfragen und ökonometrische Hypothesen

* **Forschungsfrage 1 (Integrationskurve & Aufenthaltsdauer):** Wie entwickelt sich die Wahrscheinlichkeit einer sozialversicherungspflichtigen Beschäftigung über die Aufenthaltsdauer, und welche Unterschiede zeigen sich zwischen humanitärer und regulärer Arbeitsmigration?
* **Forschungsfrage 2 (Qualifikationsanerkennung & Lohnabstand):** Welcher Zusammenhang besteht zwischen dem formalen Abschluss eines Anerkennungsverfahrens für ausländische Bildungsabschlüsse und der Entwicklung des Erwerbseinkommens?
* **Forschungsfrage 3 (Sprachkapital):** Welcher statistische Zusammenhang zeigt sich zwischen fortgeschrittenen Deutschkenntnissen (B2/C1 nach GER) und dem monatlichen Bruttoerwerbseinkommen?
* **Forschungsfrage 4 (Rücküberweisungsverhalten - Optional):** Zeigen sich in den Daten systematische monatliche Rücküberweisungen ins Herkunftsland, die die private Sparfähigkeit für Altersvorsorgevermögen einschränken?

---

### 5. Methodik

1. **Mincer'sche Lohnfunktionen:**  
   Schätzung erweiterter Lohn- und Erwerbsprofile:
   $$\ln(\text{Wage}_{it}) = \alpha + \beta_1 \text{Duration}_{it} + \beta_2 \text{Duration}_{it}^2 + \beta_3 \text{Tertiary}_i + \beta_4 \text{German\_B2C2}_{it} - \beta_5 \text{Deskilling}_{it} + \mathbf{X}_{it}'\boldsymbol{\gamma} + \varepsilon_{it}$$
2. **Panel-Ökonometrie:**  
   Nutzung von Längsschnittmodellen (Fixed Effects und Random Effects, soweit durch die Within-Variation und Panelwellen gestützt) mit robusten Standardfehlern. Explorative Prüfung von Selektionsmodellen (Heckman), sofern valide Ausschlussrestriktionen vorliegen.
3. **Mikrosimulationskalibrierung:**  
   Die geschätzten empirischen Parameter und Verteilungen fließen als empirische Eingangsmomente in das Simulationsmodell ein, um alternative Reformpfade (z. B. beschleunigte Anerkennungsverfahren) zu evaluieren.

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
