# Research Input Protocol

## Purpose

Collect research material through one or more selectable input channels, normalize the material into a source manifest, and obtain user approval of the integrated summary before creating `WORKFLOW.md` Research Configuration or drafting a manuscript.

## Selectable Input Modes

Choose one or more modes for each paper project.

| Mode | User provides | Processing rule |
|---|---|---|
| `NOTION_LINK` | A Notion page, database, or export link | Fetch the page when accessible. If login-restricted, request Markdown/CSV export or pasted content. |
| `PPT_OR_PDF_UPLOAD` | PPTX, PPT, or PDF file | Extract slide/page text and inspect images, equations, tables, and captions. |
| `LOCAL_DOCUMENT` | Markdown, TXT, DOCX, CSV, or files already in the workspace | Read the selected files and record their workspace-relative paths. |
| `DIRECT_INPUT` | Research description pasted into chat | Ask for missing title, objective, method, data, and validation details. |
| `MULTI_SOURCE` | Any combination of the modes above | Keep each source separate, then create a conflict-aware integrated summary. |

The user may select multiple modes. No mode is mandatory except that at least one usable source must be available.

## Intake Sequence

1. Ask the user which input mode(s) to use.
2. Create or update `knowledge/source_manifest.md`.
3. Record each source, access status, extraction status, and provenance.
4. Extract research facts without adding unsupported claims.
5. Produce an integrated research summary covering:
   - candidate title;
   - research topic;
   - application and system;
   - research problem and motivation;
   - proposed method or algorithm;
   - assumptions and constraints;
   - simulation and experimental evidence;
   - quantitative results, if available;
   - candidate contributions;
   - missing information and contradictions;
   - possible target journals;
   - simulation and experimental results explicitly reported in the sources.
6. Show the summary to the user for review.
7. Revise the summary only from user corrections or source evidence.
8. Record approval in `knowledge/source_manifest.md`.
9. Only after approval, update `WORKFLOW.md` Research Configuration.
10. Only after `Research Configuration` and `drafts/draft_plan.md` are approved, start manuscript drafting.

## Provenance Rules

- Every extracted fact must be traceable to a source ID in `knowledge/source_manifest.md`.
- A source that cannot be accessed is recorded as `BLOCKED`; it must not be treated as evidence.
- Do not infer numerical results from plots unless the source explicitly provides the values.
- When a source explicitly provides numerical simulation or experimental results, reflect those results in the draft as source-reported findings, tables, or figure plans. Mark them as source-reported when raw logs, trial counts, or uncertainty estimates are unavailable.
- Do not omit an explicitly reported result merely because raw data are unavailable; distinguish presentation-level evidence from reproducible validated evidence.
- Do not convert a candidate contribution into a final claim before it is linked to literature and result data.
- Conflicting sources must be reported to the user rather than silently merged.
- Login credentials and private tokens must never be requested or stored in project files.

## Review Gate

The following approval is required before the project proceeds from intake to configuration:

```markdown
- [ ] Source intake complete
- [ ] Integrated research summary reviewed by user
- [ ] Conflicts and missing information reviewed by user
- [ ] User approved Research Configuration generation
```

Valid approval messages include:

- `연구 요약 승인. Research Configuration 작성해줘.`
- `Summary approved. Create the Research Configuration.`

Without explicit approval, the assistant may analyze sources and propose a summary but must not begin the paper draft.
