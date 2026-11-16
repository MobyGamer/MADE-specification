# MADE: Measure of AI in Design & Execution

MADE is a self-disclosure AI rating scale for creative and technical works that separates human conceptual authorship (Ideation / Design) from mechanical production (Execution).  For more information, as well as an interactive builder for MADE disclosures, visit https://madespec.org/

The canonical MADE specification is located in MADE-SPECIFICATION.md, which can be referenced as a "ground truth" document for MADE.

**This is a release candidate specification, currently in final review.** When the specification is finalized, this notice will be removed.

## AI Usage Disclosure

[![MADE: I0 / E0,E2-E3](docs/images/made-badge.svg)](https://madespec.org/)

The MADE Specification itself is, appropriately, self-disclosed under the **MADE (Measure of AI in Design & Execution)** standard:
- **Ideation (`I0`, Unassisted):** 100% human-originated concepts, designs, compositions, and algorithms.  Zero AI consultation.
- **Execution (`E0,E2-E3`, Unassisted, Collaborative, Directed):** Project components span multiple execution levels. See the component breakdown below for details.

### Component Breakdown

| Component / Deliverable | MADE&nbsp;Score | Classification | Details |
| :--- | :--- | :--- | :--- |
| **MADE Specification** | **<code>I0&nbsp;/&nbsp;E0</code>** | Ideation: Unassisted; Execution: Unassisted | Specification design, wording, and markdown "ground truth" document all written by a human. |
| **MADE Landing page** | **<code>I0&nbsp;/&nbsp;E2</code>** | Ideation: Unassisted; Execution: Collaborative | Landing page design, layout, and non-interactive elements were designed by a human, partially executed by AI. |
| **MADE Interactive Builder** | **<code>I0&nbsp;/&nbsp;E3</code>** | Ideation: Unassisted; Execution: Directed | Interactive builder, including purpose, colors, text, and behavior, was designed by a human; AI built most of the HTML/CSS/logic. |

## License

MADE uses a two-part licensing structure (see [`LICENSE`](LICENSE) for full legal text):
- **Ratings, Templates, Badges, Header Tags, and Software Code (`CC0 1.0 Universal`):** Public domain dedication with zero restrictions on declaring MADE ratings, copying templates/badges, or using/modifying `scripts/sync_spec.py`, `scripts/sync.bat`, and the builder code.
- **Specification Document (`CC BY-ND 4.0` with Express Permission Addendum):** Preserves canonical `I0` to `I4` and `E0` to `E4` definitions while permitting translations, UI/documentation quoting, and separate extension profiles.

