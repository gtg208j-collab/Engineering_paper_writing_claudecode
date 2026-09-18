# Usage Guide — Engineering Paper Writing Workflow

> Version 1.1.0 | Target: IEEE Transactions + Elsevier Journals

---

## Table of Contents

1. [Quick Start](#1-quick-start)
2. [Setting Up a New Paper Project](#2-setting-up-a-new-paper-project)
3. [Choosing Your Journal (IEEE vs. Elsevier)](#3-choosing-your-journal)
4. [Phase-by-Phase Walkthrough](#4-phase-by-phase-walkthrough)
5. [Verification Gates](#5-verification-gates)
6. [Scripts Reference](#6-scripts-reference)
7. [LaTeX Setup](#7-latex-setup)
8. [Common Workflows](#8-common-workflows)
9. [FAQ](#9-faq)

---

## 1. Quick Start

### Step 1 — Prepare the terminal

Choose the command set for your operating system.

**Windows PowerShell**

```powershell
Set-Location $HOME
git clone https://github.com/gtg208j-collab/Engineering_paper_writing_claudecode.git
Set-Location .\Engineering_paper_writing_claudecode
```

**Windows Command Prompt (cmd.exe)**

```cmd
cd %USERPROFILE%
git clone https://github.com/gtg208j-collab/Engineering_paper_writing_claudecode.git
cd Engineering_paper_writing_claudecode
```

**Linux or macOS Bash**

```bash
git clone https://github.com/gtg208j-collab/Engineering_paper_writing_claudecode.git
cd Engineering_paper_writing_claudecode
```

If the repository already exists, skip `git clone` and change into its directory instead.

Confirm that the project root is correct:

```text
The directory should contain CLAUDE.md and WORKFLOW.md.
```

### Step 2 — Open with Claude Code

```text
claude
```

Run `claude` from the project root. Claude Code will automatically load `CLAUDE.md`, which imports `@WORKFLOW.md`.

If `claude` is not recognized, install Claude Code first, then reopen the terminal and run the command again. Do not put API keys or passwords in this project documentation.

### Step 0 — Choose Research Input Sources

Before filling in Research Configuration, select one or more ways to provide the research material:

```text
Start Phase 0.
Input mode: MULTI_SOURCE
Sources:
- Notion link: [paste link]
- PPT/PDF: [upload file]
- Local documents: [workspace-relative paths]
- Direct research notes: [paste notes]

Extract the sources, create an integrated research summary, list conflicts and missing information,
and wait for my approval before writing WORKFLOW.md Research Configuration.
```

Available modes are `NOTION_LINK`, `PPT_OR_PDF_UPLOAD`, `LOCAL_DOCUMENT`, `DIRECT_INPUT`, and `MULTI_SOURCE`.
Record sources in `knowledge/source_manifest.md`. A login-restricted Notion page must be marked `BLOCKED`; provide a Markdown/CSV export or pasted content instead.

The required sequence is:

```text
source selection
-> source extraction
-> integrated research summary
-> user review and approval
-> Research Configuration
-> draft_plan.md review and approval
-> manuscript drafting
```

### Step 3 — Fill in your Research Configuration

Open `WORKFLOW.md` and find the **Research Configuration** block at the top. Fill in every field:

```
Paper Title  : Robust Preview Control for a 6-DOF Motion Platform
Topic        : Preview-based disturbance rejection in motion simulation
Target Journal: IEEE TIM
Journal Family: IEEE          ← THIS IS THE MOST IMPORTANT SETTING
Paper Type   : Method proposal
Contribution :
  1. Novel preview horizon optimization for motion cueing
  2. Real-time implementation on embedded hardware
  3. Validated on human-in-the-loop experiment
```

### Step 4 — Approve the Summary and Start Phase 1

After reviewing the integrated summary and approving Research Configuration, say `Phase 1` to Claude. Claude will then guide you through Phase 1 → Phase 8.

---

## 2. Setting Up a New Paper Project

### Directory Structure

```
Engineering_paper_writing_claudecode/
├── WORKFLOW.md          ← Main workflow (READ THIS FIRST)
├── CLAUDE.md            ← Claude Code bootstrap
├── AGENTS.md            ← Codex/OpenAI agent bootstrap
├── .gitattributes
│
├── method/              ← Mathematical derivations
│   └── notation.md      ← Master symbol table (fill before writing!)
│
├── simulation/
│   ├── matlab/          ← MATLAB simulation scripts
│   └── python/          ← Python simulation scripts
│
├── experiment/          ← Experimental data and analysis
├── comparison/          ← Baseline comparison CSVs
├── drafts/              ← LaTeX source files (.tex, .bib)
├── scripts/             ← Utility scripts
│   ├── check_notation.py
│   └── format_references.py
├── review/
│   └── gates/           ← Gate verification reports
├── docs/                ← Reference guides (this folder)
├── knowledge/           ← Literature, domain notes
└── output/              ← Final PDF and submission package
```

### Starting Fresh vs. Using an Existing Project

**Fresh paper (new research):**
1. Create a new branch: `git checkout -b paper/your-paper-name`
2. Fill in `WORKFLOW.md` Research Configuration
3. Start from Phase 1

**Revision of existing paper:**
1. Skip to Phase 8 (Revision) in `WORKFLOW.md`
2. Place reviewer comments in `review/reviewer_comments.md`
3. Claude will guide you through responding to each comment

---

## 3. Choosing Your Journal

The single most important decision is setting `Journal Family` in the Research Configuration block. This one field controls everything: LaTeX class, citation format, reference style, and submission checklist.

### Journal Selection Reference

| Journal | Abbrev. | Family | Impact Factor | Type |
|---------|---------|--------|--------------|------|
| IEEE Trans. Industrial Electronics | TIE | IEEE | ~7.5 | Applications |
| IEEE Trans. Instrumentation & Measurement | TIM | IEEE | ~5.6 | Measurement |
| IEEE/ASME Trans. Mechatronics | TMECH | IEEE | ~6.4 | Systems |
| IEEE Trans. Automatic Control | TAC | IEEE | ~6.2 | Theory |
| IEEE Trans. Robotics | TRO | IEEE | ~9.4 | Robotics |
| IEEE Robotics & Automation Letters | RAL | IEEE | ~4.6 | Short papers |
| Automatica | — | Elsevier | ~6.4 | Control theory |
| Mechatronics | — | Elsevier | ~3.5 | Systems |
| Control Engineering Practice | CEP | Elsevier | ~4.0 | Applied control |
| Aerospace Science & Tech. | AESCTE | Elsevier | ~5.6 | Aerospace |

### IEEE vs. Elsevier: Key Differences

| | IEEE | Elsevier |
|--|------|---------|
| LaTeX class | `\documentclass{IEEEtran}` | `\documentclass{elsarticle}` |
| Citation format | Numeric `[1], [2]` | Numeric `[1]` or Author-year `(Smith, 2021)` |
| Reference script | `format_references.py --style ieee` | `format_references.py --style elsevier` |
| Section headers | ALL CAPS | Title Case |
| Column layout | Double column | Single column (draft) |
| Highlights file | Not required | **Required** (4–5 bullets, ≤85 chars each) |
| Graphical abstract | Optional | **Required** |
| CRediT authorship | Not required | **Required** |

---

## 4. Phase-by-Phase Walkthrough

### Phase 1 — Setup & Literature (Week 1)

**Goal:** Establish the gap in existing work and finalize novelty claims.

**Key actions:**
- Collect 30–50 references; store PDFs in `knowledge/`
- Write `knowledge/literature_gap.md` — what is missing that your paper addresses?
- Define 2–3 specific, verifiable novelty claims
- Complete `method/notation.md` with ALL symbols you plan to use

**Command to start:**
> "Start Phase 1. My paper is about [topic]. The gap I see is [gap]."

**Gate to pass before Phase 2:**
- [ ] At least 15 high-quality references collected
- [ ] 2–3 novelty claims written and agreed upon
- [ ] `method/notation.md` has all core symbols

---

### Phase 2 — Method Development & Validation (Weeks 2–4)

**Goal:** Develop your method, run simulations, run experiments, compare against baselines.

**Sub-phases:**
1. **Method design** — derive equations, prove stability/convergence, document in `method/`
2. **Simulation plan** — write `simulation/simulation_plan.md` before running ANY simulation (**mandatory gate**)
3. **Run simulations** — save results as CSV in `simulation/`
4. **Experimental plan** — write `experiment/experimental_plan.md` before running ANY experiment (**mandatory gate**)
5. **Run experiments** — save raw data in `experiment/`
6. **Comparison** — benchmark against 2–3 baselines, save as `comparison/baseline_comparison.csv`

**Key rule:** Novelty claims must be traceable to specific rows in `comparison/baseline_comparison.csv`. Claims without data are rejected by the workflow.

---

### Phase 3 — Draft Plan (1 day)

**Goal:** Plan the paper structure before writing any prose.

**Action:**
> "Create a draft plan for my paper. Target journal: [journal]."

Claude will create `drafts/draft_plan.md` with:
- Section breakdown (Introduction, Related Work, Method, Simulation, Experiment, Conclusion)
- Key figures list with captions
- Key tables list
- Word count targets per section

**Gate:** Draft plan must be reviewed and approved before any LaTeX writing begins.

---

### Phase 4 — Draft Sections (Weeks 5–7)

**Goal:** Write all sections in LaTeX.

**Section order (recommended):**
1. Method / Proposed Approach (write first — this is your contribution)
2. Simulation Results
3. Experimental Results
4. Introduction (write last — after you know what you proved)
5. Related Work
6. Conclusion

**File:** `drafts/<JOURNAL>_draft.tex`

**Command:**
> "Write the Method section. Here are my equations: [paste equations from method/]"

---

### Phase 5 — Style Polish (1–2 days)

**Goal:** Apply journal-specific formatting.

For **IEEE:**
- Section headers → ALL CAPS
- Figures → `\begin{figure}[htbp]` with `\caption{}` below
- Tables → `\begin{table}[htbp]` with `\caption{}` above
- Citations → `[1]`, `[1]–[3]` for ranges

For **Elsevier:**
- Create `drafts/highlights.txt` (4–5 bullets, ≤85 chars each)
- Create `drafts/graphical_abstract.pdf`
- Add CRediT contributions to the manuscript

---

### Phase 6 — QC Rounds (5 rounds, 2–3 days)

The workflow runs 5 verification passes. Each must PASS before moving to the next.

| Round | Checks |
|-------|--------|
| 1 | Constraint checker — equations numbered, proofs complete |
| 2 | Citation checker — every claim cites a reference |
| 3 | Data checker — every number in text matches source file |
| 4 | Notation checker — every symbol in `method/notation.md` |
| 5 | Claim integrity — every novelty claim supported by comparison data |

**Running QC:**
> "Run QC Round 1 on my draft."

Gate reports are saved in `review/gates/`.

---

### Phase 7 — Finalize & Compile (2–3 days)

**Goal:** Produce the submission-ready PDF and package.

```bash
# Compile LaTeX
pdflatex drafts/TIM_draft.tex
bibtex drafts/TIM_draft
pdflatex drafts/TIM_draft.tex
pdflatex drafts/TIM_draft.tex

# Validate references
python scripts/format_references.py --style ieee  # or --style elsevier

# Check notation
python scripts/check_notation.py
```

**Output:** `output/<journal>_submission.pdf` + cover letter + all supplementary files.

---

### Phase 8 — Revision

When reviewers return comments:

1. Place reviewer PDF in `review/`
2. Create `review/reviewer_comments.md` with each comment copied verbatim
3. Tell Claude: "Help me respond to Reviewer 2, Comment 3: [paste comment]"
4. All responses tracked in `review/response_to_reviewers.md`

---

## 5. Verification Gates

Gates are hard stops — you **cannot** skip them. When a gate fails, Claude will output a `[STOP]` signal.

| Gate | File created | When it runs |
|------|-------------|--------------|
| Simulation Plan | `simulation/simulation_plan.md` | Before first simulation |
| Experimental Plan | `experiment/experimental_plan.md` | Before first experiment |
| Draft Plan | `drafts/draft_plan.md` | Before any LaTeX writing |
| QC Round 1–5 | `review/gates/QC_R*.md` | Before finalization |
| Submission Checklist | `review/gates/submission_checklist.md` | Before upload |

### What to do when a gate fails

```
[STOP] QC Round 3 FAILED — Data Integrity
  Issue: "RMSE = 2.3 deg" in Section IV.B
         but experiment/results_exp1.csv shows RMSE = 2.31 deg
  Fix: Update the text to match the CSV value exactly.
```

Fix the issue, then re-run: `"Re-run QC Round 3."`

---

## 6. Scripts Reference

### `scripts/check_notation.py`

Checks that all symbols in your draft appear in `method/notation.md`.

```bash
# Check all .tex files in drafts/
python scripts/check_notation.py

# Check a specific file
python scripts/check_notation.py --draft drafts/TIM_draft.tex
```

### `scripts/format_references.py`

Validates `.bib` file fields and reports style-specific issues.

```bash
# Validate for IEEE
python scripts/format_references.py --style ieee

# Validate for Elsevier
python scripts/format_references.py --style elsevier

# Validate a specific .bib file
python scripts/format_references.py --style ieee --input drafts/references.bib
```

---

## 7. LaTeX Setup

### IEEE Template (IEEEtran)

```latex
\documentclass[journal]{IEEEtran}
\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{textcomp}

\begin{document}
\title{Your Paper Title}
\author{\IEEEauthorblockN{Hungsun Son}
\IEEEauthorblockA{UNIST, Ulsan, Korea\\
hson@unist.ac.kr}}

\maketitle
\begin{abstract}
...
\end{abstract}

\begin{IEEEkeywords}
keyword1, keyword2, keyword3
\end{IEEEkeywords}

\section{Introduction}
...
\bibliographystyle{IEEEtran}
\bibliography{references}
\end{document}
```

### Elsevier Template (elsarticle)

```latex
\documentclass[preprint,12pt]{elsarticle}
\usepackage{natbib}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}

\journal{Control Engineering Practice}

\begin{document}
\begin{frontmatter}
\title{Your Paper Title}
\author{Hungsun Son}
\address{UNIST, Ulsan, Korea}
\ead{hson@unist.ac.kr}

\begin{abstract}
...
\end{abstract}

\begin{keyword}
keyword1 \sep keyword2 \sep keyword3
\end{keyword}
\end{frontmatter}

\section{Introduction}
...
\bibliographystyle{elsarticle-num}
\bibliography{references}
\end{document}
```

---

## 8. Common Workflows

### "I want to start a new paper from scratch"

```
You: "새 논문 시작. 주제: UAM 경로 추적을 위한 예측 제어 알고리즘. 목표 저널: IEEE TAC."

Claude: [Begins Phase 1 — asks for literature gap, helps define novelty claims]
```

### "I have simulation results and want to write the paper"

```
You: "시뮬레이션 결과가 있어. RMSE: proposed 1.2 deg, baseline PID 3.5 deg.
      Phase 3부터 시작해줘."

Claude: [Skips to Phase 3 — creates draft plan, then moves to Phase 4 writing]
```

### "I need to respond to reviewer comments"

```
You: "Reviewer 1이 제안한 방법의 stability proof를 요구했어.
      response to reviewers 작성 도와줘."

Claude: [Phase 8 — drafts technical response + identifies where to add proof in the paper]
```

### "Check if my draft is ready to submit"

```
You: "제출 전에 QC 전부 돌려줘."

Claude: [Runs all 5 QC rounds sequentially, stops at first failure]
```

---

## 9. FAQ

**Q: Can I use this workflow without Claude Code?**
A: Yes — read `WORKFLOW.md` directly and follow it manually. The `CLAUDE.md` bootstrap only helps Claude Code automatically load the workflow.

**Q: What if my target journal isn't in the list?**
A: Set `Journal Family: IEEE` or `Journal Family: Elsevier` based on the publisher, then customize. The workflow adapts based on that one setting.

**Q: Can I start writing before finishing the simulation?**
A: No. This is Rule 7 (Experimental Plan Mandatory) and Rule 6 (Simulation Plan Mandatory). The workflow enforces a data-first approach — claims must be supported by results before prose is written.

**Q: How do I handle co-authors?**
A: Add their names to the LaTeX author block. For Elsevier, add CRediT contributions for each author at the end of Phase 5.

**Q: The notation checker says symbols are undefined but they're in notation.md — why?**
A: The checker uses regex matching. Make sure your symbols in `notation.md` use the same LaTeX command as in the `.tex` file (e.g., `\mathbf{x}` vs `\boldsymbol{x}` are treated as different symbols).

**Q: When should I create a new branch vs. use the same repo?**
A: Create a new branch (`git checkout -b paper/topic-name`) for each new paper. The `main` branch holds the workflow template only.

---

*Engineering Paper Writing Workflow v1.1.0 — Usage Guide*
