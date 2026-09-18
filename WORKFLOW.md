# Engineering Paper Writing Project (v1.1.0)
# Shared Engine (v1.1.0)
# Target: IEEE Transactions (TIE / TIM / TMECH / TAC / TRO / RAL)
#         Elsevier (Automatica / Mechatronics / CEP / AESCTE / AerospaceJ)

This file contains the runtime-independent workflow for **engineering journal papers**.
Read `docs/harness_guide.md` for manifest-based draft/revision/submission checks.
Human approvals must reflect an actual decision; never generate an approval to bypass a gate.
Use a separate **private** repository for manuscript work — do not commit unpublished work to a public repo.

---

## Phase 0: Research Intake and Source Review

Before creating or changing the Research Configuration, follow `docs/research_input_protocol.md`.

The user may provide one or more input modes:

- `NOTION_LINK`: Notion page, database, or export link
- `PPT_OR_PDF_UPLOAD`: uploaded presentation or PDF
- `LOCAL_DOCUMENT`: Markdown, TXT, DOCX, CSV, or workspace files
- `DIRECT_INPUT`: research description pasted into chat
- `MULTI_SOURCE`: any combination of the above

Record the selected modes and every source in `knowledge/source_manifest.md`. Extract and trace the candidate title, topic, objective, method, assumptions, results, contributions, and missing information. Present an integrated summary to the user for review. If a Notion page requires login, mark it `BLOCKED` and request an export or pasted content; never claim that inaccessible content was analyzed.

The following gates are mandatory before manuscript drafting:

1. Source intake is complete.
2. The integrated research summary has been reviewed by the user.
3. Conflicts and missing information have been disclosed.
4. The user explicitly approves generation of the Research Configuration.
5. The user separately approves `drafts/draft_plan.md`.

No Research Configuration or manuscript draft may be treated as final before these approvals.

---

## Research Configuration

```
  Paper Title  : Communication-Aware Decentralized Artificial Potential Field Control for Multi-UAV Formation and Collision Avoidance
  Topic        : Decentralized swarm control of quadrotor UAVs under communication delay, packet loss, and limited connectivity
  Target Journal: IEEE/ASME Transactions on Mechatronics (IEEE TMECH, provisional)
  Journal Family: IEEE     ← drives citation format & LaTeX class
  Paper Type   : Algorithm and experimental validation
    Research Input: [NOTION_LINK / PPT_OR_PDF_UPLOAD / LOCAL_DOCUMENT / DIRECT_INPUT / MULTI_SOURCE]
  Contribution :
     1. A decentralized artificial potential field framework for multi-UAV formation control,
         obstacle avoidance, and inter-UAV collision avoidance using local position information.
     2. A communication-aware swarm simulation model that incorporates communication range,
         neighbor limits, packet-loss probability, transmission period, and stochastic delay.
     3. A delay-dependent velocity-suppression mechanism and connectivity-aware repulsion strategy,
         evaluated in simulation and indoor quadrotor experiments for formation and obstacle avoidance.
```


> ⚠️ **Update this section for each new paper project before any other step.**

---

## Project Structure

```
project/
├── WORKFLOW.md              # This file — shared core rules (Claude/Codex/Gemini)
├── CLAUDE.md                # Claude Code bootstrap; imports via @WORKFLOW.md
├── AGENTS.md                # Codex/agent bootstrap; points to WORKFLOW.md
├── GEMINI.md                # Gemini bootstrap; points to WORKFLOW.md
├── .gitattributes           # text=auto eol=lf (prevents CRLF churn)
│
├── docs/                    # Reference guides (read when needed)
│   ├── writing_guide.md         # IEEE section-by-section writing guide
│   ├── drafting_protocol.md     # Mandatory drafting sequence
│   ├── section_templates.md     # Section-specific paragraph patterns
│   ├── expert_roles.md          # Expert team roles & responsibilities
│   ├── qc_guide.md              # QC & consistency verification
│   ├── verification_protocol.md # Gate definitions, Verifier charter
│   ├── revision_guide.md        # Reviewer response guide
│   ├── figure_guide.md          # Figure/plot generation (MATLAB/Python)
│   ├── latex_guide.md           # IEEEtran LaTeX rules & style
│   ├── draft_plan_template.md   # Draft plan template (Phase 3)
│   ├── math_notation_guide.md   # Notation consistency (vectors, matrices, operators)
│   ├── algorithm_guide.md       # Pseudocode & algorithm block style
│   └── citation_guide.md        # IEEE citation format & tools
│
├── knowledge/               # Reference materials
│   ├── evidence.md              # Literature summary registry [EVID:id]
│   ├── pdf/                     # Original PDFs (gitignored)
│   │   └── author_year_keyword.pdf
│   └── summaries/               # Detailed MD summaries of key papers
│       └── author_year_keyword.md
│
├── method/                  # Core technical content
│   ├── problem_formulation.md   # Mathematical problem statement
│   ├── proposed_method.md       # Algorithm / controller / system design
│   ├── stability_proof.md       # Stability / convergence proof (if required)
│   └── notation.md              # Symbol & notation table
│
├── simulation/              # Simulation validation
│   ├── sim_plan.md              # Simulation plan (required before running)
│   ├── matlab/                  # MATLAB/Simulink scripts & models
│   │   └── main_sim.m
│   ├── python/                  # Python simulation scripts
│   │   └── sim_main.py
│   └── results/                 # Simulation output data & figures
│       ├── sim_data.mat / .csv
│       └── figures/
│
├── experiment/              # Hardware experimental validation
│   ├── exp_plan.md              # Experimental plan (required before running)
│   ├── setup/                   # Hardware setup description & photos
│   │   └── setup_description.md
│   ├── data/                    # Raw experimental data (CSV/MAT)
│   │   └── exp_raw_YYMMDD.csv
│   ├── scripts/                 # Data processing scripts
│   │   └── process_exp.py
│   └── results/                 # Processed results & figures
│       ├── exp_results.csv
│       └── figures/
│
├── comparison/              # Baseline comparison
│   ├── baselines.md             # List of comparison methods & references
│   ├── metrics.md               # Performance metrics definition
│   └── results/                 # Comparison data & plots
│
├── drafts/                  # Manuscript sections
│   ├── draft_plan.md            # Draft plan (required before drafting)
│   ├── 00_cover_letter.md
│   ├── 01_title.md
│   ├── 02_abstract.md
│   ├── 03_introduction.md       # Background → Gap → Contributions → Paper org
│   ├── 04_related_work.md       # Literature review (optional — journal dependent)
│   ├── 05_problem_formulation.md
│   ├── 06_proposed_method.md    # Core technical section
│   ├── 07_simulation.md         # Simulation results & analysis
│   ├── 08_experiment.md         # Experimental results & analysis
│   ├── 09_discussion.md         # Comparison, limitations, future work
│   ├── 10_conclusion.md
│   ├── table_*.md               # Tables (from results CSV)
│   └── figures/                 # Final manuscript figures
│
├── scripts/                 # Automation & QC scripts
│   ├── check_citations.py       # [EVID:id] citation gate
│   ├── check_numbers.py         # Manuscript numbers ↔ results CSV gate
│   ├── check_gate.py            # Phase gate ledger check
│   ├── check_notation.py        # Symbol/notation consistency (method.md ↔ drafts/)
│   ├── check_claims.py          # Novelty claim ↔ results alignment
│   ├── check_revision_claims.py # Revision response gate
│   ├── lint_manuscript.py       # IEEE style lint (terminology, notation)
│   ├── search_ieee.py           # IEEE Xplore search (E-utilities)
│   ├── format_references.py     # [EVID:id] → IEEE bibliography format
│   ├── compile_latex.py         # LaTeX compilation & error check
│   ├── verify_all.py            # citation + numbers + gate batch verify
│   └── hooks/                   # Pre/post tool hooks
│
├── tests/                   # pytest suite for verification scripts
│   └── test_*.py
│
├── review/                  # Review & QC documents
│   ├── qc_log.md
│   ├── gates/                   # Gate ledger (phase_NN_*.GATE.md)
│   └── critical/                # Multi-model adversarial review reports
│
└── output/                  # Final compiled manuscript
    ├── manuscript_YYMMDD.pdf
    ├── manuscript_YYMMDD.tex
    └── figures/                 # High-res figures for submission
```

### Multi-Paper Project
When writing multiple papers from the same experimental setup, create per-paper subfolders under `drafts/`, `simulation/results/`, `experiment/results/`, `comparison/`, `review/`, and `output/`. Name them `paper{N}_{keyword}`. Shared assets (`knowledge/`, `scripts/`, `method/`) remain at the root.

### Revision Structure
After receiving reviewer comments, create `revision/REV{N}/` inside each paper's draft and output folders. Modified sections get `_REV{N}` suffix. The response letter lives in the revision folder.

---

## File Roles

| File/Folder | Purpose | When to Use |
|---|---|---|
| `WORKFLOW.md` | Core rules, config, writing style (shared by every runtime) | Auto-loaded via `@WORKFLOW.md` in `CLAUDE.md` |
| `docs/writing_guide.md` | IEEE section-by-section guidelines | When drafting specific sections |
| `docs/drafting_protocol.md` | Mandatory outline → evidence-bound draft → QC workflow | Before drafting any section |
| `docs/latex_guide.md` | IEEEtran LaTeX rules, figure/table formatting | Phase 4–7 |
| `docs/math_notation_guide.md` | Notation consistency rules | Phase 3–6 |
| `docs/algorithm_guide.md` | Pseudocode format (IEEE Algorithm2e) | Phase 4 |
| `docs/expert_roles.md` | Expert team descriptions | Phase 4–5 |
| `docs/verification_protocol.md` | Gate definitions, 4 Verifier charter | Phase 3–6, 8 |
| `docs/revision_guide.md` | Reviewer response guide | Phase 8 |
| `docs/figure_guide.md` | Figure DPI, palette, MATLAB/Python templates | Phase 2–4 |
| `docs/citation_guide.md` | IEEE citation style, [EVID:id] workflow | Phase 1, 4 |
| `knowledge/evidence.md` | Literature registry (EVID:id, summaries, BibTeX key) | Phase 1 + citation |
| `method/proposed_method.md` | Technical core — equations, algorithm, architecture | Phase 2–4 |
| `method/notation.md` | Master symbol table | Phase 3–8 (notation gate) |
| `simulation/sim_plan.md` | Simulation plan (gate-gated) | Phase 2 |
| `experiment/exp_plan.md` | Experimental plan (gate-gated) | Phase 2–3 |
| `comparison/baselines.md` | Comparison methods & metrics | Phase 2–5 |
| `drafts/draft_plan.md` | Manuscript structure plan (gate-gated) | Phase 3 |
| `review/gates/` | Gate ledger (PASS/FAIL records) | All phases |
| `output/` | Final LaTeX + PDF + figures | Phase 7 |

---

## Critical Rules (MUST FOLLOW)

### 1. Citation Integrity

- **NEVER** fabricate or hallucinate references.
- **ALWAYS** check `knowledge/evidence.md` before searching — avoid duplicate work.
- Every citation in the draft uses `[EVID:author_year]` tag (converted to IEEE `[N]` in Phase 7).
- IEEE Xplore, ScienceDirect, and arXiv are discovery tools only — register any paper in `knowledge/evidence.md` (verify DOI/IEEE ID and publisher metadata) before citing.
- Reference PDFs are local only: store under `knowledge/pdf/`; never commit copyrighted PDFs.
- Use the three-layer search defined in `docs/reference_research_protocol.md`: IEEE Xplore, Elsevier ScienceDirect, and a separate target-journal (TMECH) corpus survey.

**New reference workflow:**
1. Read `docs/reference_research_protocol.md` and check `knowledge/evidence.md`.
2. Search IEEE Xplore using query families Q1--Q7.
3. Search Elsevier ScienceDirect with the same query families.
4. Repeat the relevant queries with a target-journal filter for IEEE/ASME TMECH.
5. Record candidates separately; do not cite discovery results.
6. Verify the publisher page plus DOI or IEEE document number.
7. Save legally accessible PDFs to `knowledge/pdf/author_year_keyword.pdf`.
8. Register verified papers in `knowledge/evidence.md` with a summary, score, BibTeX key, and claim mapping.
9. Add only verified records to `drafts/references.bib`.
10. Summarize key papers in `knowledge/summaries/` and cite them in the manuscript.

### 2. Novelty & Claim Integrity

Engineering papers live or die by their novelty claims. Before writing, define 2–4 specific, falsifiable claims in `drafts/draft_plan.md` under **Contributions**. Each claim must:

- Be **traceable** to a specific result in `simulation/results/` or `experiment/results/`
- Be **comparable** to a baseline method listed in `comparison/baselines.md`
- Be **quantified** (e.g., "reduces tracking error by 23% vs. PID under [EVID:smith_2021]")

**Forbidden claim patterns:**
| ❌ Vague | ✅ Specific |
|---|---|
| "proposed method is superior" | "proposed RPC reduces RMS error by 18% vs. LQR (Table II, Fig. 5)" |
| "novel approach" | "first to apply preview control to 6-DOF SMP with proof of stability (Theorem 1)" |
| "comprehensive validation" | "validated on hardware platform at 10 kHz, 3 operating conditions (Section V-B)" |

### 3. Notation Consistency

- All mathematical symbols are defined in `method/notation.md` **before** drafting.
- Vectors: **bold lowercase** (e.g., **x**, **u**); Matrices: **bold uppercase** (**A**, **B**); Scalars: italic (*t*, *n*).
- `check_notation.py` verifies that every symbol in drafts matches `method/notation.md`.
- Never introduce a symbol in the manuscript that is not in the notation table.

### 4. Number & Data Integrity

- Every numerical result in the manuscript must trace to `simulation/results/*.csv` or `experiment/results/*.csv`.
- `check_numbers.py` gates this before any section advance.
- Never round results inconsistently (Table: 0.23 m/s → Text: 0.2 m/s is **forbidden**).
- Performance tables must include all comparison methods and all metrics defined in `comparison/metrics.md`.

### 5. Redundancy Prevention

| Section | Contains | Does NOT Contain |
|---|---|---|
| Introduction | Background, gap, contributions (bulleted), paper organization | Your results |
| Related Work | Prior art, comparison to proposed approach | Methodology details |
| Problem Formulation | System model, assumptions, objective | Solution method |
| Proposed Method | Algorithm, control law, stability proof | Raw results |
| Simulation / Experiment | Results with reference to figures/tables | Re-derivation of method |
| Discussion | Comparative analysis, limitations, future work | New results not shown above |
| Conclusion | Summary of contributions + takeaways | New claims not in the paper |

**Table vs. Figure rule:** Ask before creating.
- Exact values required → **Table**
- Trends, trajectories, time responses → **Figure**
- Never duplicate the same data in both Table and Figure.

**IEEE Table limit:** Aim for ≤ 5 tables. Move detailed parameter tables to Appendix.

### 6. Simulation Plan Mandatory

**NEVER** run simulations without first creating `simulation/sim_plan.md` and receiving approval.

`sim_plan.md` must include:
- Simulation scenario description (plant model, disturbance, initial conditions)
- Performance metrics and expected ranges
- Comparison baselines and parameter settings
- Approval checkbox: `- [ ] 사용자 승인 완료`

### 7. Experimental Plan Mandatory

**NEVER** run hardware experiments without `experiment/exp_plan.md` approval.

`exp_plan.md` must include:
- Hardware platform description (sensors, actuators, sampling rate)
- Test conditions and safety envelope
- Data recording format and post-processing plan
- Correspondence with simulation scenarios
- Approval checkbox: `- [ ] 사용자 승인 완료`

### 8. Draft Plan Mandatory

**NEVER** draft sections without `drafts/draft_plan.md` approval.

**NEVER** begin the draft plan or manuscript from unreviewed source material. Complete Phase 0 source intake and obtain explicit approval of the integrated research summary first.

`draft_plan.md` must include:
- **Key message** (1–2 sentences)
- **Contributions** (2–4 specific, quantified novelty claims)
- **Claim → Result mapping** (each claim traced to simulation/experiment result)
- **Related work scope** (which baselines, which papers)
- **Table/Figure plan** (how many, what content)
- **Section outline** (Introduction → Conclusion flow)
- **Target word/page count** (journal page limit)
- Approval checkbox: `- [ ] 사용자 승인 완료`

### 9. Verification Gates Mandatory

Each output stage requires a gate PASS before advancing. See `docs/verification_protocol.md`.

**Verifier types for engineering papers:**

| Verifier | Checks | When |
|---|---|---|
| **Constraint** | Scope, tone, forbidden patterns, IEEE style | Phase 4 each section |
| **Citation** | [EVID:id] ↔ evidence.md, IEEE format | Phase 4, 6 |
| **Data/Numerical** | Numbers ↔ results CSV, table consistency | Phase 4, 6 |
| **Notation** | Symbols ↔ notation.md, LaTeX rendering | Phase 4, 6 |
| **Claim** | Novelty claims ↔ results (no overclaiming) | Phase 3 gate, Phase 6 |
| **Revision** | Response claims ↔ revised manuscript diff | Phase 8 |

FAIL → autonomous fix loop (max 2 iterations) → escalate to user.
Gate record stored in `review/gates/`.

### 10. LaTeX Style — IEEE vs. Elsevier

Set `Journal Family` in Research Configuration first. Rules diverge between families.

#### IEEE Journals (TIE, TIM, TMECH, TAC, TRO, RAL)

| Rule | Detail |
|---|---|
| Document class | `\documentclass[journal]{IEEEtran}` |
| Citation format | Numeric `[1]`, `[2]–[5]` — **never** author-year |
| Equation reference | `(\ref{eq:N})` — not "Eq. (N)" |
| Section headers | `\section{INTRODUCTION}` — ALL CAPS |
| Figure DPI | ≥ 300 DPI; 600 DPI for halftones |
| Page limit | Typically 8–14 pages double-column |
| Algorithms | `algorithm2e` or `algorithmicx` |
| Bold math | `\boldsymbol{}` for Greek; `\mathbf{}` for Latin |
| Author block | IEEEtran author/affiliation macros |
| Biography | Short paragraph + photo required for full Transactions papers |

**Key Elsevier journals for control/UAM/mechatronics:**

| Journal | Scope |
|---|---|
| **Automatica** | Control theory, systems, optimization (IFAC flagship) |
| **Mechatronics** | Mechatronics systems, motion control, robotics |
| **Control Engineering Practice (CEP)** | Applied control, industrial systems |
| **Aerospace Science and Technology (AESCTE)** | Aerospace systems, UAM, flight control |
| **Aerospace (MDPI)** | Open-access; UAM, drone systems, UAV control |
| **Applied Sciences (MDPI)** | Open-access; broad engineering applications |
| **Actuators (MDPI)** | Actuator systems, motion platforms, motors |

#### Elsevier Journals (Automatica, Mechatronics, CEP, AESCTE, etc.)

| Rule | Detail |
|---|---|
| Document class | `\documentclass{elsarticle}` (use journal's template) |
| Citation format | **Author-year** `(Smith, 2021)` or `Smith (2021)` — check specific journal |
| In-text citation | `\citep{}` (parenthetical) or `\citet{}` (textual) with `natbib` |
| Equation reference | `(\ref{eq:N})` or "Eq. (\ref{eq:N})" — journal style varies |
| Section headers | Title case (`\section{Introduction}`) |
| Figure DPI | ≥ 300 DPI; submit as EPS/PDF/TIFF |
| Page limit | Typically no hard limit; 10–25 pages single-column; check guide for authors |
| Layout | Single-column draft for submission; camera-ready formatted by journal |
| Algorithms | `algorithm2e` or inline pseudocode |
| Highlights | Required: 3–5 bullet highlights (85 chars each) submitted separately |
| Graphical abstract | Required or recommended by most Elsevier journals |
| Cover letter | More detailed than IEEE — explain novelty, suggest reviewers |
| Open access | Most have APC option; MDPI journals are fully open-access |

**Elsevier submission checklist (additional items vs. IEEE):**
```
✅ Highlights file (3–5 bullets, 85 chars max each)
✅ Graphical abstract (visual summary, 1 figure)
✅ Author contribution statement (CRediT taxonomy)
✅ Data availability statement
✅ Declaration of competing interests
✅ Funding / acknowledgment statement
✅ Suggested reviewers (3–5 names + emails + affiliation)
```

#### BibTeX format differences

| Item | IEEE | Elsevier |
|---|---|---|
| Citation key | `smith2021control` | `smith2021control` (same) |
| In-text tag | `[EVID:smith2021control]` → `[1]` | `[EVID:smith2021control]` → `(Smith, 2021)` |
| `format_references.py` flag | `--style ieee` | `--style elsevier` |

Set `--style` flag to match `Journal Family` in Research Configuration.

### 11. STOP Signals

| Inner thought (STOP) | Reality / Required action |
|---|---|
| "This number looks about right" | Trace to results CSV. Not there → do not write it. |
| "This reference is from memory" | Check `knowledge/evidence.md`. Not there → do not cite. |
| "The claim is obvious from the results" | Verify with `check_claims.py`. Overclaiming is a rejection trigger. |
| "Notation is obvious from context" | Check `method/notation.md`. Undefined symbol → forbidden. |
| "Simulation matches, no need for experiment" | IEEE Transactions requires hardware validation for most topics. |
| "PASS recorded, now safe" | If output changed, PASS is stale. Re-run with `--verify-hash`. |
| "Reviewer is wrong, I'll rebut" | Rebuttals need citations. Limit to 1–2 rebuttal points; concede the rest gracefully. |

---

## Recommended Workflow

### Phase 1: Setup & Literature

```
├── Complete Phase 0 source intake and user review
├── Define topic, journal, paper type in WORKFLOW.md Research Configuration
├── Check journal scope, page limit, LaTeX template (docs/latex_guide.md)
├── Follow docs/reference_research_protocol.md
├── Search IEEE Xplore and Elsevier ScienceDirect by Q1--Q7
├── Search the target TMECH corpus separately
├── Verify DOI/IEEE ID and publisher metadata
├── Save legally accessible PDFs to knowledge/pdf/
├── Summarize & register verified papers in knowledge/evidence.md
│   Fields: [EVID:id], title, authors, year, venue, DOI/IEEE ID,
│           BibTeX key, scores, contributions, relevance, claim mapping
├── Key papers → knowledge/summaries/ (detailed 2-3 page summary)
├── Define comparison baselines in comparison/baselines.md
│   (List 3–5 state-of-the-art methods you will compare against)
└── Define performance metrics in comparison/metrics.md
```

**Completion criteria:** Evidence supports 2–4 specific novelty claims; all baselines identified.

---

### Phase 2: Method Development & Validation

```
├── Read docs/math_notation_guide.md + docs/algorithm_guide.md
├── Define all symbols in method/notation.md (master table)
├── Write method/problem_formulation.md
│   └── System model, assumptions, objective function, constraints
├── Write method/proposed_method.md
│   └── Algorithm / control law / architecture — equations in LaTeX
├── Write method/stability_proof.md (if applicable)
│   └── Theorem + Proof; Lyapunov / Nyquist / etc.
│
├── SIMULATION
│   ├── Create simulation/sim_plan.md (MANDATORY, user approval required)
│   │   └── Scenario, metrics, baselines, initial conditions
│   ├── Write MATLAB/Python scripts in simulation/matlab/ or simulation/python/
│   ├── Run simulation → save to simulation/results/ (CSV + MAT)
│   ├── Generate figures → simulation/results/figures/ (docs/figure_guide.md)
│   └── 🔒 GATE: Numerical Verifier — sim results match expected from plan
│
├── EXPERIMENT (if applicable)
│   ├── Create experiment/exp_plan.md (MANDATORY, user approval required)
│   ├── Setup hardware (document in experiment/setup/)
│   ├── Run experiments → save raw data to experiment/data/
│   ├── Process data with experiment/scripts/process_exp.py
│   ├── Generate figures → experiment/results/figures/
│   └── 🔒 GATE: Numerical Verifier — exp results consistent with sim
│
└── COMPARISON
    ├── Implement baseline methods (comparison/baselines.md)
    ├── Run baselines under identical conditions
    ├── Compile comparison table → comparison/results/
    └── 🔒 GATE: Claim Verifier — novelty claims supported by comparison data
```

**Completion criteria:** `sim_plan.md` and `exp_plan.md` approved; all results in CSV; comparison table ready; novelty claims verified by data.

---

### Phase 3: Draft Plan

```
├── Confirm Phase 0 source-intake approval in knowledge/source_manifest.md
├── Step 0 (Socratic): Clarify key message with user — ask one question at a time
│   Q1: What is the single most important result?
│   Q2: Who is the target reader? (control theorist / systems engineer / practitioner)
│   Q3: What existing paper does this most closely compete with?
├── Copy docs/draft_plan_template.md → drafts/draft_plan.md
│   ├── Key message (1–2 sentences)
│   ├── Contributions (2–4 bulleted claims, each with → result pointer)
│   ├── Claim → Result mapping (~15–20 specific claims with [EVID:id] or result ref)
│   ├── Related work scope (which threads, which baselines, which papers)
│   ├── Table / Figure plan (number, content, Table vs. Figure decision)
│   ├── Section outline (subsection level)
│   ├── Notation table reference (method/notation.md)
│   ├── Target page count (check journal limit)
│   └── Tone & voice ("rigorous & concise IEEE style", "practical engineering focus", etc.)
├── 🔒 GATE: Claim → Citation pre-verification (Citation Verifier)
│   └── Each claim in draft_plan.md must map to [EVID:id] or results data
└── User approval → Phase 4
```

**Completion criteria:** `draft_plan.md` complete with all items; gate PASS recorded; user approved.

---

### Phase 4: Draft Sections (in order)

```
├── Read docs/drafting_protocol.md + docs/section_templates.md
├── Read docs/latex_guide.md for section formatting
│
├── 05_problem_formulation.md → mathematical setup
│   └── Expert: Dr. Systems Engineer (theoretical rigor)
├── 06_proposed_method.md → core algorithm/control law
│   └── Expert: Dr. Control Engineer (method clarity)
├── 07_simulation.md → simulation results narrative
│   └── Expert: Dr. Validation Engineer (result presentation)
├── 08_experiment.md → experimental results (if applicable)
│   └── Expert: Dr. Validation Engineer
├── 04_related_work.md → literature positioning
│   └── Expert: Dr. Control Engineer + Dr. Technical Editor
├── 03_introduction.md → background → gap → contributions → organization
│   └── Expert: Dr. Control Engineer (framing) + Dr. Technical Editor
├── 09_discussion.md → comparison, limitations, future work
│   └── Expert: Dr. Systems Engineer + Dr. Technical Editor
├── 10_conclusion.md → summary of contributions
├── 02_abstract.md → write LAST (summary of all sections, 150–250 words)
└── 01_title.md → finalize (concise, IEEE style, ≤12 words preferred)

🔒 GATE (per section): Constraint + Citation + Data + Notation Verifier
   → autonomous fix loop (max 2 iterations) → review/gates/ record
```

**Section drafting rules:**
- Write Introduction last among the narrative sections (after Methods & Results are solid)
- Abstract = last section drafted
- Every equation must be labeled and referenced in text
- Every figure and table must be cited in text before it appears
- Never start a sentence with a math symbol — precede with noun ("The error *e*...")

**Completion criteria:** All sections drafted; all per-section gates passed.

---

### Phase 5: Style Polish

```
├── Apply docs/writing_guide.md IEEE Style Reference
│   ├── Voice: mostly active ("We propose", "The results show")
│   ├── Tense: past for results, present for general facts & method description
│   ├── Avoid: "novel", "unique", "state-of-the-art" (overused — show, don't tell)
│   ├── Avoid: "It is worth noting", "It should be mentioned"
│   ├── Hedging: use appropriately ("may", "suggests") — not excessive
│   ├── Transition upgrades: "but" → "however"; "also" → "furthermore"
│   └── Verb upgrades: "show" → "demonstrate"; "use" → "employ"
├── Run scripts/lint_manuscript.py drafts/ --quiet → fix high-priority findings
├── Verify notation consistency: scripts/check_notation.py
├── Expert: Dr. Technical Editor (final language polish)
├── Check: all figures cited in text, all tables cited in text
├── Check: contribution bullets in Introduction match draft_plan.md exactly
└── Check: Abstract covers all 4 elements (context, gap, method, key result)
```

**IEEE Abstract template (4-sentence structure):**
1. **Context:** "Control of [system] is critical for [application]."
2. **Gap:** "Existing approaches suffer from [limitation]."
3. **Method:** "This paper proposes [method], which [mechanism]."
4. **Result:** "Experiments on [platform] demonstrate [quantified improvement] over [baseline]."

---

### Phase 6: QC (Minimum 3 rounds; 5 recommended)

```
├── Round 1: Notation & number consistency (check_notation.py, check_numbers.py)
│   └── Every symbol defined, every number traceable to results
├── Round 2: Citation verification (check_citations.py, check_coverage.py)
│   └── Every [EVID:id] in evidence.md; no fabricated references
├── Round 3: Claim integrity (check_claims.py)
│   └── Each contribution claim supported by specific data; no overclaiming
├── Round 4: LaTeX compilation & figure quality
│   └── compile_latex.py; all figures ≥ 300 DPI; algorithms render correctly
├── Round 5: Critical adversarial review (/critical-review)
│   └── External multi-model review — attack novelty, methodology, results
│   └── Common rejection triggers: weak comparison, missing ablation, unclear novelty
├── Document all rounds in review/qc_log.md
└── IEEE-specific checklist (docs/qc_guide.md):
    ✅ Title ≤ 12 words (preferred)
    ✅ Abstract 150–250 words
    ✅ All equations numbered and referenced
    ✅ All figures/tables cited in text
    ✅ Notation consistent throughout
    ✅ Page limit met
    ✅ Supplemental material separated (if any)
    ✅ Author information / IEEE biography section ready
```

**Completion criteria:** Minimum 3 QC rounds passed (5 recommended); all gate records in `review/gates/`.

---

### Phase 7: Finalize & Compile

```
├── Read docs/latex_guide.md (LaTeX compilation rules)
├── Compile final LaTeX → output/manuscript_YYMMDD.pdf
│   ├── output/manuscript_YYMMDD.tex    (main file)
│   ├── output/references.bib           (BibTeX, generated by format_references.py)
│   └── output/figures/                 (high-res, submission-ready)
│
├── [IEEE] Run: python scripts/format_references.py --style ieee
│           → converts [EVID:id] → [N] numbered bibliography
│           → LaTeX class: IEEEtran
│
├── [Elsevier] Run: python scripts/format_references.py --style elsevier
│           → converts [EVID:id] → (Author, Year) bibliography (natbib)
│           → LaTeX class: elsarticle
│           → Prepare: highlights.txt, graphical_abstract.pdf, CRediT statement
│           → Suggest 3–5 reviewers (name, email, affiliation) for cover letter
│
├── File naming (default: date-based):
│   manuscript_YYMMDD.pdf / .tex
│   manuscript_REV1_YYMMDD.pdf (revision)
│   manuscript_FINAL_YYMMDD.pdf (final submission)
├── Verify against journal submission checklist:
│   ✅ PDF/LaTeX source package
│   ✅ Individual high-res figure files (EPS/PDF/TIFF)
│   ✅ Cover letter (00_cover_letter.md → PDF)
│   ✅ Highlights / Graphical abstract (if required)
│   ✅ Author contribution statement (IEEE Author Contribution form)
│   ✅ Conflict of interest declaration
└── Co-author final review
```

**File versioning:**

| Format | Use | Example |
|---|---|---|
| `_YYMMDD` | Default (date-based) | `manuscript_260917.pdf` |
| `_v1`, `_v2` | When author prefers sequential | `manuscript_v1.pdf` |
| `_REV1`, `_REV2` | Revision submissions | `manuscript_REV1_260917.pdf` |
| `_FINAL` | Final accepted version | `manuscript_FINAL_260917.pdf` |

---

### Phase 8: Revision (After Reviewer Comments)

```
├── Read docs/revision_guide.md
├── Save reviewer comments: review/reviewer_comments_REV1.md
│   └── Parse into: Major (must address) / Minor (should address) / Optional
├── Create revision folders:
│   ├── drafts/revision/REV1/          (modified sections with _REV1 suffix)
│   └── output/revision/REV1/          (revised PDF, response letter)
│
├── Analyze each comment:
│   ├── Concede + fix: most comments (even if partially wrong — pragmatic)
│   ├── Rebuttal (max 2): supported by new results or strong existing evidence
│   └── Clarification: "We agree this was unclear; we have revised to..."
│
├── For each Major comment requiring new results:
│   ├── Update sim_plan.md or exp_plan.md
│   ├── Run additional simulation/experiment
│   └── Update relevant sections
│
├── Response letter (drafts/revision/REV1/response_letter_REV1.md):
│   ├── Respond to EVERY comment — no ghost revisions
│   ├── Format: "Comment: ... / Response: ... / Change: Section X, lines Y–Z"
│   └── Highlight all changes in revised manuscript (track changes or blue text)
│
├── 🔒 GATE: Revision Verifier
│   ├── check_revision_claims.py: response claims ↔ actual manuscript changes
│   └── check_response_coverage.py: every reviewer comment has a response
│
├── QC re-run (Rounds 1–3 mandatory)
├── Compile → output/revision/REV1/
│   ├── manuscript_REV1_YYMMDD.pdf + .tex
│   └── response_letter_REV1_YYMMDD.pdf
└── Second revision: repeat in REV2/ folder
```

**Response letter tone:**
- Open: "We thank the reviewers for their thorough and constructive comments."
- Per comment: respectful, specific, no defensiveness
- Concession formula: "The reviewer raises an important point. We have revised [section] to clarify [issue]."
- Rebuttal formula: "With respect, we would like to clarify that [point], as supported by [EVID:id] and our results in Table N."

---

## Phase Completion Criteria

| Phase | Move to Next When |
|---|---|
| 1 → 2 | Evidence supports 2–4 specific claims; baselines & metrics defined |
| 2 → 3 | `sim_plan.md` + `exp_plan.md` approved; all results in CSV; claims verified by data |
| 3 → 4 | `draft_plan.md` complete & approved; Claim→Citation gate PASS |
| 4 → 5 | All sections drafted; per-section gates PASS |
| 5 → 6 | IEEE style applied; Dr. Technical Editor reviewed |
| 6 → 7 | Minimum 3 QC rounds passed; all gates PASS |
| 7 → Submit | Co-author approved; journal requirements met; versioned files in `output/` |
| Submit → 8 | Reviewer comments received |
| 8 → Resubmit | Revised manuscript + response letter complete; QC re-run passed |

---

## Quick Commands

### Setup & Research

| Command | Action |
|---|---|
| `Setup project for [topic]` | Initialize folder structure |
| `/search-ieee [query]` | IEEE Xplore search → select → register in `evidence.md` |
| `/import-doi [doi]` | DOI → `evidence.md` registration |
| `Process new PDFs` | Scan `knowledge/pdf/`, register unprocessed PDFs |
| `Define baselines for [topic]` | Populate `comparison/baselines.md` |
| `Define metrics for [task]` | Populate `comparison/metrics.md` |

### Method Development

| Command | Action |
|---|---|
| `Write problem formulation` | Create `method/problem_formulation.md` |
| `Write proposed method` | Create `method/proposed_method.md` |
| `Write stability proof` | Create `method/stability_proof.md` (Theorem + Proof) |
| `Update notation table` | Add/modify symbols in `method/notation.md` |
| `Check notation consistency` | `python scripts/check_notation.py method/ drafts/` |

### Simulation & Experiment

| Command | Action |
|---|---|
| `Create simulation plan` | Create `simulation/sim_plan.md` (MANDATORY, approval required) |
| `Generate simulation script` | Create MATLAB/Python script in `simulation/matlab/` or `simulation/python/` |
| `Process simulation results` | Parse output → `simulation/results/*.csv` |
| `Create experiment plan` | Create `experiment/exp_plan.md` (MANDATORY, approval required) |
| `Process experimental data` | Run `experiment/scripts/process_exp.py` |
| `Generate comparison table` | Compile `comparison/results/` from all methods |

### Draft Plan & Drafting

| Command | Action |
|---|---|
| `Create draft plan` | Copy template → `drafts/draft_plan.md`, fill all items |
| `Draft [section]` | Write specific section (draft_plan.md–based) |
| `Draft [section] as Dr. [Expert]` | Write with specific expert perspective |
| `Review as Dr. [Expert]` | Expert feedback on current draft |

### Style & QC

| Command | Action |
|---|---|
| `Apply IEEE style to [section]` | Apply writing_guide.md rules |
| `Check notation` | `python scripts/check_notation.py drafts/` |
| `Check numbers` | `python scripts/check_numbers.py drafts/ --results simulation/results/ experiment/results/` |
| `Verify references` | `python scripts/check_citations.py drafts/ --evidence knowledge/evidence.md` |
| `Check claims` | `python scripts/check_claims.py drafts/ --plan drafts/draft_plan.md --results comparison/results/` |
| `/verify [artifacts]` | `python scripts/verify_all.py` — citation + numbers + gate batch check |
| `/critical-review [target]` | External multi-model adversarial review |
| `Run QC round [1-5]` | Execute specific QC round per `docs/qc_guide.md` |
| `Lint manuscript` | `python scripts/lint_manuscript.py drafts/ --quiet` |

### Finalize & LaTeX

| Command | Action |
|---|---|
| `Compile LaTeX` | `python scripts/compile_latex.py` — compile + error check |
| `Format references` | `python scripts/format_references.py --style ieee` |
| `Generate submission package` | Compile PDF + figures + cover letter |

### Revision

| Command | Action |
|---|---|
| `Analyze reviewer comments` | Classify Major/Minor, suggest response strategy |
| `Draft response to reviewer [N]` | Draft specific reviewer response |
| `Draft response letter` | Full response letter draft |
| `Check response completeness` | `python scripts/check_revision_claims.py drafts/revision/REV1/response_letter_REV1.md --strict` |
| `Check response coverage` | `python scripts/check_response_coverage.py ... --comments review/reviewer_comments_REV1.md` |

---

## Expert Team (docs/expert_roles.md)

| Expert | Role | Activates In |
|---|---|---|
| **Dr. Control Engineer** | Control theory, algorithm rigor, stability proofs | Phase 4: Method, Related Work, Introduction |
| **Dr. Systems Engineer** | System architecture, hardware integration, signal flow | Phase 4: Problem Formulation, Discussion |
| **Dr. Validation Engineer** | Experimental design, data analysis, figure quality | Phase 2–4: Simulation, Experiment sections |
| **Dr. Technical Editor** | IEEE language style, conciseness, clarity, transitions | Phase 5: Style Polish; Phase 4 review |
| **Dr. Reviewer (Adversarial)** | Attack novelty, methodology weaknesses, missing baselines | Phase 6: /critical-review |

**Invocation examples:**
- `Draft the Proposed Method section as Dr. Control Engineer`
- `Review this introduction as Dr. Technical Editor`
- `Attack this paper as Dr. Reviewer — find all weaknesses`

---

## IEEE Writing Style (Quick Reference)

**General (both IEEE and Elsevier):**
- Active voice: "We propose...", "The simulation shows...", "This paper presents..."
- Precise quantification: "18% reduction", "RMSE of 0.023 m", "settling time < 0.5 s"
- Verb upgrades: show → demonstrate, use → employ, get → obtain, check → verify
- Transitions: however, furthermore, consequently, in contrast, notably
- Cite when making any factual claim about prior work

**Avoid (both):**
- "novel", "unique", "state-of-the-art" (show it, don't say it)
- "It is worth noting that...", "It should be mentioned that..."
- Passive-only writing (mix appropriately)
- Starting sentences with symbols or numbers
- Hedging on your own results ("might", "possibly" — use "demonstrates", "achieves")
- Re-stating what a figure shows exhaustively — point to key trends only

**IEEE-specific style:**
- All main section headers in ALL CAPS (`INTRODUCTION`, `PROPOSED METHOD`)
- Numeric citations only: `[1]`, `[2]–[5]`
- Biographical note required at end (Transactions papers)
- Keep Abstract ≤ 200 words

**Elsevier-specific style:**
- Title-case section headers (`Introduction`, `Proposed Method`)
- Author-year citations: `(Smith, 2021)` or `Smith (2021)` per journal guide
- Highlights required: start with "•" — "• Proposes a preview control method for 6-DOF motion platforms"
- Graphical abstract: single clear image summarizing the whole paper
- Abstract typically 150–250 words; some journals have structured abstract (Background/Method/Results/Conclusion)
- Acknowledgments section required (funding, contributors)

**Section tense guide:**

| Section | Tense |
|---|---|
| Introduction (background) | Present ("Control of UAVs is critical...") |
| Related Work | Past ("Smith [1] proposed...", "Prior work showed...") |
| Problem Formulation | Present (definitions, assumptions) |
| Proposed Method | Present ("The controller computes...", "Algorithm 1 describes...") |
| Simulation / Experiment | Past ("The simulation demonstrated...", "Results showed...") |
| Discussion / Conclusion | Present + Past mix |

---

## Notes & Reminders

- **Detailed guides are in `docs/`** — read as needed to conserve context window.
- **Hardware validation is expected** by IEEE Transactions for method papers. Plan for it early.
- **Ablation study** (removing components of your method) significantly strengthens papers — plan in `sim_plan.md`.
- **Minimum 3 QC rounds mandatory** before submission.
- **Independent co-author review mandatory** before submission. If unavailable, record `BLOCKED` — self-review is useful but must not be recorded as independent.
- **Page charges:** IEEE charges per page over limit — write to the limit, not over it.
- **Conflict of interest disclosure:** required for all IEEE submissions.
- **ORCID:** required for all authors on IEEE submissions.
- **Open access:** check journal policy — some IEEE journals require APC for open access; others have free access after embargo.

---

---

## Journal Selection Guide

Use this table to pick the right journal before starting Phase 1.

| Journal | Family | IF (approx.) | Scope | Page Limit |
|---|---|---|---|---|
| **IEEE TIM** (Trans. Instrum. Meas.) | IEEE | ~5.6 | Measurement, sensors, instrumentation, control systems | ~10 pp |
| **IEEE TMECH** (Trans. Mechatronics) | IEEE | ~6.4 | Mechatronics, motion control, robotics, actuators | ~10 pp |
| **IEEE TIE** (Trans. Ind. Electronics) | IEEE | ~7.7 | Industrial electronics, drives, power, control | ~10 pp |
| **IEEE TAC** (Trans. Autom. Control) | IEEE | ~6.8 | Control theory (rigorous), systems | ~10 pp |
| **IEEE TRO** (Trans. Robotics) | IEEE | ~9.4 | Robotics, manipulation, autonomous systems | ~14 pp |
| **IEEE RAL** (Robotics Autom. Lett.) | IEEE | ~4.6 | Short letters, robotics — fast turnaround | 8 pp |
| **Automatica** | Elsevier | ~6.4 | Control theory & systems (IFAC) — theory-heavy | No strict limit |
| **Mechatronics** | Elsevier | ~3.7 | Mechatronics integration, motion systems | No strict limit |
| **CEP** (Control Eng. Practice) | Elsevier | ~4.0 | Applied control, industrial applications | No strict limit |
| **AESCTE** (Aerosp. Sci. Tech.) | Elsevier | ~5.6 | Aerospace engineering, UAM, flight systems | No strict limit |
| **Aerospace** | MDPI | ~2.6 | UAM, UAV, drone systems — open access | No strict limit |
| **Actuators** | MDPI | ~2.5 | Actuators, motion platforms, motors — open access | No strict limit |

> **Rule of thumb:** Control theory paper → Automatica / TAC. Experimental system paper → TMECH / TIM / CEP. UAM/UAV application → AESCTE / RAL / Aerospace.

---

*Engineering Paper Writing Workflow v1.1.0 — IEEE + Elsevier*
*Tailored for: Control Systems · UAM · Mechatronics · Motion Platforms · Spherical Motors*
*Adapt Research Configuration and Journal Family for each new paper project.*
