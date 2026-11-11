# MADE: Measure of AI in Design & Execution, Specification v0.1

**Version:** 0.1  
**Status:** Draft Specification  
**Canonical URI:** https://example.com
**Specification License:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)  
**Date:** November 2026  
**Author:** Jim Leonard (<mobygamer@gmail.com>)  
**Templates, Badges, & Header Tags License:** [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/)

---

## 1. Purpose & Philosophy

**MADE (Measure of AI in Design & Execution)** is a voluntary, author-declared rating framework that enables creators of software, writing, art, music, and other public works to transparently communicate how generative AI was used in their projects. What sets MADE apart from previous AI disclosure scales is that it rates *original human ideas* separately from *mechanical implementation*, rather than reducing an entire project to a single number.

### Why Single-Number Scales Fail
Existing disclosure scales and frameworks, such as the [REAL Rating](https://www.realgoodai.org/real-rating), the [AI Assessment Scale](https://aiassessmentscale.com/), [W3C's AI Content Disclosure for HTML](https://w3c-cg.github.io/ai-content-disclosure/#disclosure-values), the [AI Attribution Tooklit](https://aiattribution.github.io/), and [RAID - Responsible AI Disclosure](https://responsibleaidisclosure.com/), collapse all AI usage onto a single numeric spectrum or a single category label. Such scales routinely place *brainstorming and ideation* at a lower number than *mechanical implementation*. This distorts how AI usage is represented:
1. A creator who prompts an AI model for all creative inspiration, *and then manually types or illustrates the result*, receives a "low" AI rating, despite the core concepts originating entirely from AI.
2. A creator who conceives a 100% original design, hand-crafts the primary work, and uses AI strictly to handle repetitive procedural tasks (such as writing file-conversion utilities, or performing background research) is assigned a "high" AI rating, despite only using AI for mechanical tasks.

### MADE's Balanced Alternative: Separating Ideation from Execution
MADE resolves this problem by evaluating a project across two distinct rating categories, each scored from `0` to `4`:
- **Ideation (`I0` to `I4`)** measures who conceived the ideas, concepts, structure, design, composition, or algorithms.
- **Execution (`E0` to `E4`)** measures how the tangible work (code, prose, visual art, music, etc.) was mechanically produced.

Both categories use the same five symmetrical, whole-number levels:
- **`0`: Unassisted**
- **`1`: Assisted**
- **`2`: Collaborative**
- **`3`: Directed**
- **`4`: Autonomous**

Example Usage: Assume a creative project was 100% designed by a human, who then collaborated with AI to produce the supporting material. The project's author could then self-disclose the following MADE score:

```markdown
MADE: I0 / E2
(or:)
MADE: Ideation 0 (Unassisted); Execution 2 (Collaborative)
```

---

## 2. Ideation Levels (`I0` to `I4`)

The **Ideation** level measures the intellectual and creative origin of the work, including its core concepts, narrative themes, visual design, musical composition, or software algorithms.

| Level | Title | Definition | Examples Across Creative & Technical Fields |
| :--- | :--- | :--- | :--- |
| **`I0`** | **Unassisted** | 100% human-originated concepts, designs, compositions, and algorithms.  Zero AI consultation. | **Programming:** Designing an algorithm or system architecture solely from personal knowledge and non-AI documentation.<br>**Writing:** Conceiving a novel's plot, characters, and chapter structure independently.<br>**Art:** Designing characters, layouts, and color palettes entirely from imagination and traditional references.<br>**Music:** Composing melodies, harmonies, and arrangements without querying any AI tool. |
| **`I1`** | **Assisted** | Core concepts and designs are human-originated. AI used only for background research or minor conceptual refinements. | **Programming:** Inventing an original algorithm while using an LLM to review mathematical formulas and test minor edge-case tweaks.<br>**Writing:** Plotting an original historical novel while using AI to summarize archival documents or verify period timelines.<br>**Art:** Designing an original illustration while using AI to search for historical costume references.<br>**Music:** Composing an original piece while asking an AI tutor about modal music theory or instrumentation ranges. |
| **`I2`** | **Collaborative** | A human set the creative vision and partnered with AI to brainstorm specific elements, sections, or outlines. | **Programming:** Designing an application architecture through an iterative dialogue where human and AI jointly propose subsystem designs.<br>**Writing:** Co-developing worldbuilding lore or secondary subplot beats in a back-and-forth brainstorming session.<br>**Art:** Iterating on rough composition thumbnails and visual motifs in collaboration with an AI tool before illustrating.<br>**Music:** Composing a main theme by hand and collaborating with an AI tool to explore alternate chord progressions or counter-melodies. |
| **`I3`** | **Directed** | A human provided a high-level goal; AI proposed the primary structure or design choices, curated by the human. | **Programming:** Prompting an AI with desired input/output goals and allowing the AI to select the underlying data structures and architecture for human approval.<br>**Writing:** Prompting an AI to generate several chapter outlines from a one-paragraph premise and curating the best outline.<br>**Art:** Generating multiple concept layouts from a text prompt and selecting one as the blueprint for production.<br>**Music:** Prompting an AI for song structures and harmonic progressions in a specific genre and curating the arrangement. |
| **`I4`** | **Autonomous** | AI conceived the project concept, design, and creative direction with minimal or no human conceptual input. | **All Fields:** Prompting an autonomous system to invent a software project, story concept, visual theme, or musical composition from a minimal, open-ended request. |

---

## 3. Execution Levels (`E0` to `E4`)

The **Execution** level measures how the finished work (source code, prose, visual artwork, or audio recordings) was produced and reviewed.

| Level | Title | Definition | Examples Across Creative & Technical Fields |
| :--- | :--- | :--- | :--- |
| **`E0`** | **Unassisted** | 100% human-produced code, prose, illustration, or musical performance by the human creator. | **Programming:** Writing source code or assembly routines completely by hand.<br>**Writing:** Typing and editing a manuscript manually without generative text tools.<br>**Art:** Drawing, painting, or modeling artwork entirely by hand.<br>**Music:** Performing, sequencing, mixing, and mastering audio manually without AI plugins. |
| **`E1`** | **Assisted** | 100% human-authored output. AI is used strictly for read-only diagnostics, proofreading, syntax checking, or signal cleanup. | **Programming:** Writing code manually and using an LLM to scan for off-by-one bugs or syntax errors.<br>**Writing:** Writing prose by hand while using AI as an interactive phrase thesaurus or proofreader.<br>**Art:** Hand-painting digital art, then using generative spot-healing or margin bleed fill for print preparation.<br>**Music:** Recording live instruments and using an AI assistant for read-only mix diagnostics or to patch a clipped transient. |
| **`E2`** | **Collaborative** | Shared human-AI production, such as human-crafted primary work paired with AI-generated supporting assets, boilerplate, or utilities. | **Programming:** Hand-coding the core application engine while using AI to generate test harnesses, build scripts, or CLI parsers.<br>**Writing:** Writing the primary text of a book or article while using AI to generate summary tables, indexes, or data charts.<br>**Art:** Hand-drawing all characters and foregrounds while using AI to assist with repetitive background textures or in-between tween frames.<br>**Music:** Performing lead vocals and primary instruments by hand while using AI to generate secondary accompaniment stems or drum fills. |
| **`E3`** | **Directed** | AI produced the component's output strictly from detailed human specifications and constraints, verified by the creator. | **Programming:** Providing an LLM with a detailed, human-authored specification and algorithm so it writes a companion utility in a secondary language, followed by human testing.<br>**Writing:** Translating a human-authored book into another language using AI under strict glossary constraints, followed by human review.<br>**Art:** Generating rendered assets using a workflow tightly constrained by human-drawn control maps, depth maps, and manual paint-overs.<br>**Music:** Synthesizing a vocal or orchestral performance from a human-written score and lyric sheet, followed by manual mixing. |
| **`E4`** | **Autonomous** | Generated end-to-end by AI from minimal prompts with little or no human specification or review. | **All Fields:** Accepting bulk AI-generated code without reviewing the logic ("vibe-coding"), or publishing raw AI-generated text, images, or music directly from a prompt. |

---

## 4. Disclosure Format & Syntax

At its simplest, a MADE disclosure always begins with the `MADE:` prefix (including the colon), followed by a single Ideation level (`I0` to `I4`) and a single Execution level (`E0` to `E4`) separated by a forward slash (`/`), such as: `MADE: I1 / E0`. Ideation is always listed first, then Execution. For works with uniform AI usage throughout, this single rating is all that is necessary.

MADE also defines a **layered disclosure format** that can scale with project complexity. Hybrid projects (where there were multiple levels of human and AI involvement for various pieces) can summarize multiple levels in the overall score, while optionally documenting individual components and source files underneath.

> **Note:** You do not need to format complex disclosures by hand; the accompanying **Interactive Badge and Disclosure Builder** can automatically generate multi-level scores, badges, component breakdowns, and file header tags.

### 4.1 Single-Rating Formats

1. **Shorthand Format:**
   Start with the `MADE:` prefix, then separate the Ideation (`I`) and Execution (`E`) levels with a space, a forward slash (`/`), and a space.
   - Example: `MADE: I1 / E0`

2. **Expanded Human-Readable Format:**
   Start with the `MADE:` prefix and write out the Ideation and Execution level numbers and parenthesized titles, separating the two clauses with a **semicolon** (`;`). The expanded clause may also be placed in parentheses immediately after a shorthand rating:
   - Example: `MADE: Ideation 1 (Assisted); Execution 0 (Unassisted)`
   - Combined Example: `MADE: I1 / E0 (Ideation 1 (Assisted); Execution 0 (Unassisted))`

### 4.2 Multi-Component Projects

When a project contains multiple components with different AI involvement levels, combine all applicable levels within each category from lowest to highest (`0` to `4`). Always include the letter (`I` or `E`) before every number.

- **Discrete Levels:** When components use non-consecutive levels with nothing in between (such as hand-crafted primary work at `E0` and a spec-driven utility or translated appendix at `E3`), list only the levels used, separated by a **comma** without spaces:
  - Example: `MADE: I1 / E0,E3`
- **Contiguous Ranges:** When components span consecutive levels with no gaps (such as adjacent levels `I0` and `I1`, or every level from `E0` through `E2`), always join the first and last level with a **hyphen** rather than commas:
  - Examples: `MADE: I0-I1 / E0` or `MADE: I1 / E0-E2`
- **Combined Categories:** Ideation and Execution can apply commas and hyphens independently.  (Both can be combined within a category if needed, such as `E0-E1,E3`):
  - Example: `MADE: I0-I1 / E0,E3`

When writing multi-component ratings in the expanded format, level numbers follow the same comma and hyphen rules, followed by comma-separated titles, such as: `MADE: Ideation 0-1 (Unassisted, Assisted); Execution 0,3 (Unassisted, Directed)`.

### 4.3 Component-Level Breakdown

Whenever a project includes multiple components with different ratings, authors are encouraged to include a brief component breakdown where each component declares both its Ideation level and its Execution level:

```markdown
AI Disclosure ([MADE](MADE-SPECIFICATION.md)): `MADE: I0-I1 / E0,E3`
- **Core Application Engine (`I0 / E0`, Ideation: Unassisted; Execution: Unassisted):** Designed and hand-coded 100% by the human author with zero AI involvement.
- **Data Import & Conversion Utilities (`I1 / E3`, Ideation: Assisted; Execution: Directed):** Algorithms designed by the author (`I1`), with code generated by an LLM from detailed human specifications and verified by hand (`E3`).
```

Or for a creative publication or album:

```markdown
AI Disclosure ([MADE](MADE-SPECIFICATION.md)): `MADE: I0-I1 / E0,E2`
- **Novel Manuscript & Dialogue (`I1 / E0`, Ideation: Assisted; Execution: Unassisted):** Plot and prose written 100% by the author (`E0`), using AI only for historical period research (`I1`).
- **Chapter Header Illustrations (`I0 / E2`, Ideation: Unassisted; Execution: Collaborative):** Character line art drawn by hand (`I0`), paired with AI-assisted background textures (`E2`).
```

### 4.4 Per-File Source Code & Asset Metadata Headers

To prevent individual hand-crafted files, manuscripts, or digital assets from being misattributed to AI (or vice versa) when viewed in isolation, authors may place a `MADE:` line tag in source file headers, document frontmatter, or asset metadata comments. Because a header tag describes how a single file or asset was made, it specifies a single Ideation level and a single Execution level:

**Python / Shell / YAML / Makefile / Markdown / Text Metadata:**
```python
# MADE: I1 / E1 (Ideation: Assisted; Execution: Assisted)
```

**C / C++ / Rust / Go / JavaScript / C#:**
```c
// MADE: I1 / E3 (Ideation: Assisted; Execution: Directed)
```

**Assembly (`.asm`, `.inc`, `.s`):**
```nasm
; MADE: I0 / E0 (Ideation: Unassisted; Execution: Unassisted)
```

**HTML / XML / SVG Artwork / EPUB / XMP Metadata:**
```html
<!-- MADE: I0 / E0 (Ideation: Unassisted; Execution: Unassisted) -->
```

### 4.5 Optional Tool & Model Attribution

Creators who want to note which specific AI tools or models were used can optionally list them in square brackets at the end of any standalone rating or file header tag, separated by commas:

```markdown
# Example 1
MADE: I1 / E2 [Claude 3.5 Sonnet, Midjourney v6]
# Example 2
MADE: I1 / E3 (Ideation: Assisted; Execution: Directed) [GPT-4o]
```

For the complete formal syntax specification, see the RFC 5234 ABNF grammar in [`MADE-GRAMMAR.abnf`](MADE-GRAMMAR.abnf).

---

## 5. Licensing & Governance

To preserve a single canonical definition of the scale while ensuring frictionless adoption across all creators and licenses, MADE uses a two-part licensing structure:

1. **Using MADE Ratings, Badges, and Templates in Your Works:**
   Declaring a MADE rating on your project, embedding MADE badges, copying disclosure templates, or placing `MADE:` tags in your files is completely free of restrictions under [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/) (`CC0 1.0 Public Domain`).
2. **Republishing the Specification Document:**
   The specification document itself (`MADE-SPECIFICATION.md`), the HTML conversion of the specification, and the HTML Interactive Badge and Disclosure Builder, are licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/) (`CC BY-ND 4.0`). This ensures that if someone republishes the specification document itself, third parties cannot alter the definitions of `I0` through `I4` or `E0` through `E4` while still calling the modified scale "MADE".

> **Express Permission Addendum:** Notwithstanding the NoDerivatives restriction in Section 3(a)(4) of `CC BY-ND 4.0`, the Licensor grants all users the irrevocable, royalty-free, perpetual permission to: (1) translate the specification document into any natural language and publicly distribute such translation, provided the translation is accurate and preserves the canonical level definitions; (2) quote and display the unmodified level titles and definitions in user interfaces, tooltips, and documentation, and extract, modify, and redistribute all software code, scripts, regular expressions, and interactive builder logic; and (3) create and distribute domain-specific extension profiles that append auxiliary metadata fields without altering the definitions of `I0` through `I4` and `E0` through `E4`.

---

## 6. Authorship & Provenance

The MADE standard was created by Jim Leonard (<mobygamer@gmail.com>) to provide programmers, writers, visual artists, musicians, and independent creators with a human-readable self-disclosure standard that distinguishes human conceptual originality from mechanical AI assistance.
