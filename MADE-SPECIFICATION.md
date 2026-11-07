# MADE: Measure of AI in Design & Execution, Specification v0.1

**Version:** 0.1  
**Status:** Draft Specification  
**Homepage:** https://example.com  
**Specification License:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)  
**Date:** November 2026  
**Author:** Jim Leonard (<mobygamer@gmail.com>)  
**Templates, Badges, & Header Tags License:** [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/)

---

## 1. Purpose & Philosophy

**MADE (Measure of AI in Design & Execution)** is a voluntary, author-declared rating framework that enables creators of software, writing, art, music, and other public works to transparently communicate how generative AI was used in their projects. What sets MADE apart from previous AI disclosure scales is that it rates **original human ideas** separately from *mechanical implementation*, rather than reducing an entire project to a single number.

### Why Single-Number Scales Fail
Existing disclosure scales and labels, such as the [REAL Rating](https://www.realgoodai.org/real-rating), the [AI Assessment Scale](https://aiassessmentscale.com/), the [GAIT Framework](https://hypervisor.studio/gait/#levels), and [Responsible AI Disclosure (RAID)](https://responsibleaidisclosure.com/), collapse all AI usage onto a single numeric spectrum or a single category label. Such scales routinely place *brainstorming and ideation* at a lower number than *mechanical implementation*.  This incentivizes the wrong signals:
1. A creator with no original ideas who prompts an AI model for all creative inspiration, *and then manually types or illustrates the result*, receives a "low" AI rating, despite the completed work lacking human creativity and originality.
2. A creator who conceives a 100% original design, hand-crafts the primary work, and uses AI strictly to handle repetitive procedural tasks (such as writing file-conversion utilities from a specification, cleaning up reverb on a live recording, or generating textured fills) is *penalized* with a "high" AI rating, despite only using AI for mechanical tasks.

### MADE's Balanced Alternative: Separating Ideation from Execution
MADE resolves this problem by evaluating a project across two distinct rating categories, each scored from `0` to `4`:
- **Ideation (`I0` to `I4`)** measures who conceived the ideas, concepts, structure, design, composition, or algorithms.
- **Execution (`E0` to `E4`)** measures how the tangible work (code, prose, visual art, music, etc.) was mechanically produced.

Both categories use the same five symmetrical, whole-number level titles:
- **`0`: Unassisted**
- **`1`: Assisted**
- **`2`: Collaborative**
- **`3`: Directed**
- **`4`: Autonomous**

Example Usage:  Assume a creative project was 100% conceived of and designed by a human, who then used AI to automate 50% of the work needed to deliver said project.  The project's author could then self-disclose the following MADE score:

> MADE: I0 / E2
> Ideation: I0 (Unassisted); Execution: E2 (Collaborative)

---

## 2. Category 1: Ideation Levels (`I0` to `I4`)

The **Ideation** level measures the intellectual and creative origin of the work, including its core concepts, narrative themes, visual design, musical composition, or software algorithms.

| Level | Title | Definition | Examples Across Creative & Technical Fields |
| :--- | :--- | :--- | :--- |
| **`I0`** | **Unassisted** | 100% human-originated concepts, designs, compositions, and algorithms.  Zero AI consultation. | **Programming:** Designing an algorithm or system architecture solely from personal knowledge and non-AI documentation.<br>**Writing:** Conceiving a novel's plot, characters, and chapter structure independently.<br>**Art:** Designing characters, layouts, and color palettes entirely from imagination and traditional references.<br>**Music:** Composing melodies, harmonies, and arrangements without querying any AI tool. |
| **`I1`** | **Assisted** | Core concepts and designs are human-originated.  AI used only for background research or minor tested refinements. | **Programming:** Inventing an original algorithm while using an LLM to review mathematical formulas and test minor edge-case tweaks.<br>**Writing:** Plotting an original historical novel while using AI to summarize archival documents or verify period timelines.<br>**Art:** Designing an original illustration while using AI to search for historical costume references.<br>**Music:** Composing an original piece while asking an AI tutor about modal music theory or instrumentation ranges. |
| **`I2`** | **Collaborative** | A human set the creative vision and partnered with AI to co-brainstorm subcomponents or outlines. | **Programming:** Designing an application architecture through an iterative dialogue where human and AI jointly propose subsystem designs.<br>**Writing:** Co-developing worldbuilding lore or secondary subplot beats in a back-and-forth brainstorming session.<br>**Art:** Iterating on rough composition thumbnails and visual motifs in collaboration with an AI tool before illustrating.<br>**Music:** Composing a main theme by hand and collaborating with an AI tool to explore alternate chord progressions or counter-melodies. |
| **`I3`** | **Directed** | A human provided a high-level goal; AI proposed the primary structure or design choices, curated by the human. | **Programming:** Prompting an AI with desired input/output goals and allowing the AI to select the underlying data structures and architecture for human approval.<br>**Writing:** Prompting an AI to generate several chapter outlines from a one-paragraph premise and curating the best outline.<br>**Art:** Generating multiple concept layouts from a text prompt and selecting one as the blueprint for production.<br>**Music:** Prompting an AI for song structures and harmonic progressions in a specific genre and curating the arrangement. |
| **`I4`** | **Autonomous** | AI conceived the project concept, design, and creative direction with minimal or no human conceptual input. | **All Fields:** Prompting an autonomous system to invent a software project, story concept, visual theme, or musical composition from a minimal, open-ended request. |

---

## 3. Category 2: Execution Levels (`E0` to `E4`)

The **Execution** level measures how the final deliverables of the work (source code, text, visual artwork, or audio recordings) were mechanically constructed and verified.

| Level | Title | Definition | Examples Across Creative & Technical Fields |
| :--- | :--- | :--- | :--- |
| **`E0`** | **Unassisted** | 100% hand-crafted code, prose, illustration, or musical performance by the human creator. | **Programming:** Writing source code or assembly routines completely by hand.<br>**Writing:** Typing and editing a manuscript manually without generative text tools.<br>**Art:** Drawing, painting, or modeling artwork entirely by hand.<br>**Music:** Performing, sequencing, mixing, and mastering audio manually without AI plugins. |
| **`E1`** | **Assisted** | Human-authored output.  AI used only for read-only diagnostics, phrase lookup, signal cleanup, or minor boilerplate. | **Programming:** Writing code manually and using an LLM to scan for off-by-one bugs or syntax errors.<br>**Writing:** Writing prose by hand while using AI as an interactive phrase thesaurus or proofreader.<br>**Art:** Hand-painting digital art and using a machine-learning filter for final noise reduction or resolution upscaling.<br>**Music:** Recording live instruments and using a neural audio filter to remove room reverb or microphone hum. |
| **`E2`** | **Collaborative** | Shared human-AI production, such as human-created core work paired with AI-generated helper scripts or background textures. | **Programming:** Hand-coding the core application engine while using AI to generate test harnesses, build scripts, or CLI parsers.<br>**Writing:** Writing the primary text of a book or article while using AI to generate summary tables, indexes, or data charts.<br>**Art:** Hand-drawing all characters and foregrounds while using AI to assist with repetitive background textures or in-between tween frames.<br>**Music:** Performing lead vocals and primary instruments by hand while using AI to generate secondary accompaniment stems or drum fills. |
| **`E3`** | **Directed** | AI produced the component's output strictly from detailed human specifications and constraints, verified by the creator. | **Programming:** Providing an LLM with a detailed, human-authored specification and algorithm so it writes a companion utility in a secondary language, followed by human testing.<br>**Writing:** Translating a human-authored book into another language using AI under strict glossary constraints, followed by human review.<br>**Art:** Generating rendered assets using a workflow tightly constrained by human-drawn control maps, depth maps, and manual paint-overs.<br>**Music:** Synthesizing a vocal or orchestral performance from a human-written score and lyric sheet, followed by manual mixing. |
| **`E4`** | **Autonomous** | Generated end-to-end by AI from minimal prompts with little or no human specification or review. | **All Fields:** Accepting bulk AI-generated code without reviewing the logic ("vibe-coding"), or publishing raw AI-generated text, images, or music directly from a prompt. |

---

## 4. Disclosure Format & Syntax

MADE supports a **two-tier disclosure format** so hybrid projects (such as a project where the core work is hand-crafted at `E0` and a secondary component is AI-generated from specifications at `E3`) can represent both the overall release and its individual components accurately.

### 4.1 Tier 1: Compact Shorthand Notation

1. **Separating Ideation and Execution (Always Use a Slash):**
   Ideation (`I`) and Execution (`E`) are always separated by a forward slash (`/`).
   - Example: `MADE: I1 / E0`

2. **Expanded Human-Readable Format (Use a Comma):**
   When writing out the full rating in prose, separate the Ideation and Execution clauses with a semicolon:
   - `MADE: Ideation 1 (Assisted); Execution 0 (Unassisted)`

3. **Multi-Component Projects: Discrete Levels (`E0,E3`) vs. Contiguous Ranges (`I0-I1`, `E0-E3`):**
   When a project contains multiple components with different AI involvement levels, MADE distinguishes between discrete selections and continuous ranges:
   - **Discrete Levels (Comma-Separated):** If a project uses non-contiguous levels (such as `E0` for hand-crafted work and `E3` for a spec-driven utility, with no `E1` or `E2` components), list the exact levels separated by a comma:
     `MADE: I1 / E0,E3` (or `MADE: I1 / E0, E3`)
   - **Contiguous Ranges (Hyphen-Separated with Repeated Letter Prefix):** If a project spans two or more consecutive levels (for example, components covering `I0` and `I1`, or `E0`, `E1`, `E2`, and `E3`), express the span using a hyphen and repeat the letter prefix (`I` or `E`) on both numbers:
     `MADE: I0-I1 / E0,E3` or `MADE: I1 / E0-E3` (Never write `E0-3`, which is visually ambiguous.)

### 4.2 Tier 2: Component-Level Breakdown

Whenever a project includes multiple components with different ratings, authors are encouraged to include a brief component breakdown where **each component declares both its Ideation level and its Execution level**:

```markdown
**AI Disclosure ([MADE](MADE-SPECIFICATION.md)): `I0-I1 / E0,E3`**
- **Core Application Engine (`I0 / E0`, Unassisted Ideation, Unassisted Execution):** Designed and hand-coded 100% by the human author with zero AI involvement.
- **Data Import & Conversion Utilities (`I1 / E3`, Assisted Ideation, Directed Execution):** Algorithms designed by the author (`I1`), with code generated by an LLM from detailed human specifications and verified by hand (`E3`).
```

### 4.3 Per-File Source Code & Asset Metadata Headers

To prevent individual hand-crafted files from being misattributed to AI (or vice versa) when viewed in isolation, authors may place a `MADE-Usage` line tag in file headers or asset metadata comments:

**Assembly (`.asm`, `.inc`, `.s`):**
```nasm
; MADE-Usage: I0/E0 (Ideation: Unassisted; Execution: Unassisted)
```

**C / C++ / Rust / Go / JavaScript / C#:**
```c
// MADE-Usage: I1/E3 (Ideation: Assisted; Execution: Directed)
```

**Python / Shell / YAML / Makefile / Markdown / Text Metadata:**
```python
# MADE-Usage: I1/E1 (Ideation: Assisted; Execution: Assisted)
```

---

## 5. Licensing & Governance

To protect the canonical definitions of the scale from fragmentation while ensuring zero-friction adoption for all creators, MADE uses a two-part licensing structure:

1. **Using MADE Ratings, Badges, and Templates in Your Works (`CC0 1.0 Public Domain`):**
   Declaring a MADE rating on your project, embedding MADE badges, copying disclosure templates, or placing `MADE-Usage` tags in your files is completely free of restrictions under [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/).
2. **Republishing the Specification Document (`CC BY-ND 4.0`):**
   This specification document itself (`MADE-SPECIFICATION.md`) is licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/). This ensures that if someone republishes the specification document itself, the initial authorship remains recorded in the specification text and third parties cannot alter the definitions of `I0` through `I4` or `E0` through `E4` while still calling the modified scale "MADE."

---

## 6. Authorship & Provenance

The MADE standard was created by Jim Leonard (<mobygamer@gmail.com>) to provide programmers, writers, visual artists, musicians, and independent creators with an honest, human-readable self-disclosure standard that distinguishes human conceptual originality from mechanical AI assistance.
