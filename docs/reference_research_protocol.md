# Reference Research Protocol

## Scope

This protocol is for the paper on communication-aware decentralized artificial potential field control for multi-UAV formation and collision avoidance.

Target journal: IEEE/ASME Transactions on Mechatronics (TMECH, provisional).

The search uses three evidence layers:

1. **IEEE Xplore:** primary search for TMECH, IEEE robotics, control, and mechatronics papers.
2. **Elsevier ScienceDirect:** cross-publisher search for Automatica, Mechatronics, Control Engineering Practice, and related multi-agent control papers.
3. **Target-journal corpus:** papers published in IEEE/ASME TMECH are searched separately to learn the journal's scope, contribution style, validation depth, and citation patterns.

Discovery results are not citable until bibliographic metadata and DOI/IEEE document information are verified.

## Selected Keywords

Core concepts:

- multi-UAV formation control
- decentralized multi-UAV control
- swarm robotics
- artificial potential field
- collision avoidance
- obstacle avoidance
- communication delay
- packet loss
- connectivity-aware control
- quadrotor formation
- distributed consensus

## Search Query Families

Run each query family in IEEE Xplore and ScienceDirect, then repeat the most relevant terms with a TMECH venue filter.

| ID | Query |
|---|---|
| Q1 | `("multi-UAV" OR "multi-quadrotor") AND ("formation control" OR swarm)` |
| Q2 | `("artificial potential field" OR APF) AND (UAV OR quadrotor) AND formation` |
| Q3 | `(decentralized OR distributed) AND (UAV OR multi-agent) AND collision avoidance` |
| Q4 | `(UAV OR multi-agent) AND (communication delay OR packet loss) AND formation control` |
| Q5 | `(connectivity OR communication graph) AND (multi-UAV OR swarm) AND collision avoidance` |
| Q6 | `("artificial potential field") AND (communication OR delay OR packet loss)` |
| Q7 | `("multi-UAV") AND ("IEEE/ASME Transactions on Mechatronics" OR TMECH)` |

Search variants should also use spelling variants: `multi-UAV`, `multi UAV`, `multi-robot`, `quadrotor`, `quadcopter`, `distributed`, and `decentralized`.

## Search Order

For each query:

1. Check `knowledge/evidence.md` for an existing record and duplicate DOI.
2. Search IEEE Xplore.
3. Record candidate title, authors, year, venue, DOI/IEEE document number, abstract, and URL.
4. Search ScienceDirect using the same query and record candidates separately.
5. Apply the target-journal filter for TMECH.
6. Remove duplicates by DOI, then by normalized title.
7. Verify the final metadata using the publisher page, DOI resolver, or Crossref.
8. Download only legally accessible full text to `knowledge/pdf/` when permitted.
9. Read the abstract and relevant method/results sections.
10. Register the verified paper in `knowledge/evidence.md`.
11. Add the BibTeX record to `drafts/references.bib` only after registration.

## Selection Criteria

Score each candidate from 0 to 2 for each criterion:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Topic match | unrelated | adjacent | directly addresses the paper problem |
| Method match | unrelated method | partially transferable | APF/distributed/formation method directly relevant |
| Communication relevance | absent | mentions communication | models delay, loss, range, or connectivity |
| Validation relevance | no validation | simulation only | simulation plus hardware/flight validation |
| Target-journal relevance | unrelated venue | related venue | TMECH paper or close TMECH-style paper |
| Metadata confidence | unverified | partial metadata | DOI/IEEE ID and publisher metadata verified |

Priority rules:

- **Priority A:** score 9--12 and metadata confidence = 2. Candidate for direct Related Work citation.
- **Priority B:** score 6--8 and metadata confidence = 2. Use for context or comparison.
- **Priority C:** score below 6 or unverified metadata. Do not cite until rechecked.

Do not select papers solely because they are highly cited. A paper must support a specific sentence in the manuscript.

## Literature-Matrix Fields

Every selected paper must answer:

- What problem is solved?
- What control architecture is used?
- Is the method centralized, leader--follower, or decentralized?
- Is APF used? If so, how are attractive and repulsive terms defined?
- What communication assumptions are made?
- Are delay, packet loss, communication range, or connectivity modeled?
- What collision and formation metrics are reported?
- Is there simulation, hardware, or flight validation?
- What limitation remains relative to the present paper?
- Which exact manuscript claim does this paper support?

## Target-Journal Survey

For at least 8--12 recent TMECH papers, record:

- problem domain and application;
- number and type of experiments;
- baseline methods;
- quantitative metrics;
- theoretical analysis, if any;
- figure/table density and page usage;
- how novelty is stated;
- whether communication/network assumptions are explicit.

This target-journal survey is separate from the technical evidence used to support claims.

## Required Outputs

- `knowledge/evidence.md`: verified literature registry and claim mapping.
- `knowledge/summaries/<key>.md`: detailed summaries for the most important papers.
- `drafts/references.bib`: verified BibTeX records only.
- `comparison/baselines.md`: selected baseline methods.
- `review/gates/phase_01_literature.PASS.md`: completion report after the minimum evidence set is complete.

## Minimum Completion Gate

Before drafting a final Related Work section:

- [ ] At least 15 verified papers collected.
- [ ] At least 3 APF or potential-field papers collected.
- [ ] At least 3 decentralized/distributed formation-control papers collected.
- [ ] At least 3 communication-aware multi-agent-control papers collected.
- [ ] At least 3 TMECH papers surveyed.
- [ ] At least 2 papers with hardware or flight validation collected.
- [ ] Every paper has verified DOI or IEEE document number.
- [ ] Every major literature claim maps to one or more evidence IDs.
- [ ] No placeholder or fabricated BibTeX entry remains.
