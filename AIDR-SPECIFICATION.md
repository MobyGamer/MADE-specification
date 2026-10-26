# AIDR: Artificial Intelligence Disclosure Rating, Specification v1.0

**Version:** 1.0  
**Status:** Canonical Specification  
**Author:** Jim Leonard (<mobygamer@gmail.com>)  
**Date:** October 2026  
**Specification License:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)  
**Templates, Badges & Header Tags License:** [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/)

---

## 1. Purpose & Philosophy

**AIDR (Artificial Intelligence Disclosure Rating)** is a voluntary, author-declared rating framework that enables creators of software, creative writing, graphical art, music composition, and other public works to transparently communicate how artificial intelligence was used in their projects.

### Why Single-Number Scales Fail
Existing linear disclosure scales, such as the REAL Rating (0 to 5), the AI Assessment Scale (1 to 5), and the GAIT Framework, collapse all AI usage onto a single numeric spectrum. Worse, linear scales routinely place *AI brainstorming and ideation* at a lower number than *AI mechanical implementation*.

Under a single-number scale:
1. A creator with no original ideas who prompts an AI model to invent a plot, composition structure, or software design, and then manually types or illustrates the result, receives a low AI rating.
2. An author, artist, composer, or programmer who conceives a 100% original design, hand-crafts the primary work, and uses AI strictly to handle repetitive mechanical tasks (such as generating file-conversion utilities from a strict specification, cleaning up room reverb on a live recording, or generating flat color fills) is penalized with a high AI rating. This lumps original human creation together with unreviewed, end-to-end AI output.

### The AIDR Solution: Separating Ideation from Execution
AIDR resolves this problem by evaluating a project across two distinct rating categories, each scored from `0` to `4`:
- **Ideation (`I0` to `I4`)** measures who conceived the ideas, concepts, structure, composition, or algorithms.
- **Execution (`E0` to `E4`)** measures how the tangible work (code, prose, visual art, or music/audio) was mechanically produced.

Both categories share five symmetrical, whole-number level titles:
- **`0`: Unassisted**
- **`1`: Assisted**
- **`2`: Collaborative**
- **`3`: Directed**
- **`4`: Autonomous**

---

## 2. Category 1: Ideation Levels (`I0` to `I4`)

The **Ideation** level measures the intellectual and creative origin of the work, including its core concepts, narrative themes, visual design, musical composition, or software algorithms.

| Level | Title | Definition | Examples Across Creative & Technical Fields |
| :--- | :--- | :--- | :--- |
| **`I0`** | **Unassisted** | All concepts, designs, compositions, narratives, and algorithms are 100% human-originated, with zero AI consultation even for background research. | **Programming:** Designing an algorithm or system architecture solely from personal knowledge and non-AI documentation.<br>**Writing:** Conceiving a novel's plot, characters, and chapter structure independently.<br>**Art:** Designing characters, layouts, and color palettes entirely from imagination and traditional references.<br>**Music:** Composing melodies, harmonies, and arrangements without querying any AI tool. |
| **`I1`** | **Assisted** | All core concepts, designs, and primary structures are human-originated. AI was used only for background research (explaining theory, summarizing reference material) or as a sounding board that suggested minor local refinements which the human evaluated and selectively adopted. | **Programming:** Inventing an original algorithm while using an LLM to review mathematical formulas and test minor edge-case tweaks.<br>**Writing:** Plotting an original historical novel while using AI to summarize archival documents or verify period timelines.<br>**Art:** Designing an original illustration while using AI to search for historical costume references.<br>**Music:** Composing an original piece while asking an AI tutor about modal music theory or instrumentation ranges. |
| **`I2`** | **Collaborative** | The human established the overarching creative vision and goals, and actively partnered with AI to co-brainstorm sub-components, solve structural problems, or develop outlines together. | **Programming:** Designing an application architecture through an iterative dialogue where human and AI jointly propose subsystem designs.<br>**Writing:** Co-developing worldbuilding lore or secondary subplot beats in a back-and-forth brainstorming session.<br>**Art:** Iterating on rough composition thumbnails and visual motifs in collaboration with an AI tool before illustrating.<br>**Music:** Composing a main theme by hand and collaborating with an AI tool to explore alternate chord progressions or counter-melodies. |
| **`I3`** | **Directed** | The human provided a broad problem statement, theme, or high-level prompt, and AI generated the primary structure, outline, or design choices, which the human then curated, evaluated, and refined. | **Programming:** Prompting an AI with desired input/output goals and allowing the AI to select the underlying data structures and architecture for human approval.<br>**Writing:** Prompting an AI to generate several chapter outlines from a one-paragraph premise and curating the best outline.<br>**Art:** Generating multiple concept layouts from a text prompt and selecting one as the blueprint for production.<br>**Music:** Prompting an AI for song structures and harmonic progressions in a specific genre and curating the arrangement. |
| **`I4`** | **Autonomous** | AI conceived the project concept, design, and creative direction with minimal or no human conceptual input. | **All Fields:** Prompting an autonomous system to invent a software project, story concept, visual theme, or musical composition from a minimal, open-ended request. |

---

## 3. Category 2: Execution Levels (`E0` to `E4`)

The **Execution** level measures how the final deliverables of the work (source code, text, visual artwork, or audio recordings) were mechanically constructed and verified.

| Level | Title | Definition | Examples Across Creative & Technical Fields |
| :--- | :--- | :--- | :--- |
| **`E0`** | **Unassisted** | Every line of code, word of prose, brushstroke, or musical note was manually authored or performed by the human with zero AI involvement. | **Programming:** Writing source code or assembly routines completely by hand.<br>**Writing:** Typing and editing a manuscript manually without generative text tools.<br>**Art:** Drawing, painting, or modeling artwork entirely by hand.<br>**Music:** Performing, sequencing, mixing, and mastering audio manually without AI plugins. |
| **`E1`** | **Assisted** | The delivered work is human-authored. AI or machine-learning tools were used only for read-only diagnostics (bug-finding, grammar checking), reference lookups (phrase thesaurus, syntax lookup), non-generative signal cleanup (audio denoising, upscaling), or minor inline autocomplete and boilerplate. | **Programming:** Writing code manually and using an LLM to scan for off-by-one bugs or syntax errors.<br>**Writing:** Writing prose by hand while using AI as an interactive phrase thesaurus or proofreader.<br>**Art:** Hand-painting digital art and using a machine-learning filter for final noise reduction or resolution upscaling.<br>**Music:** Recording live instruments and using a neural audio filter to remove room reverb or microphone hum. |
| **`E2`** | **Collaborative** | Human and AI each produced substantial portions of the delivered work, such as a human creating the core work while AI generated supporting utilities, background elements, or data visualizations. | **Programming:** Hand-coding the core application engine while using AI to generate test harnesses, build scripts, or CLI parsers.<br>**Writing:** Writing the primary text of a book or article while using AI to generate summary tables, indexes, or data charts.<br>**Art:** Hand-drawing all characters and foregrounds while using AI to assist with repetitive background textures or in-between tween frames.<br>**Music:** Performing lead vocals and primary instruments by hand while using AI to generate secondary accompaniment stems or drum fills. |
| **`E3`** | **Directed** | Generative AI produced the vast majority of the component's output, operating strictly as an implementation engine under human direction, detailed multi-paragraph specifications, explicit constraints, and human verification or editing. | **Programming:** Providing an LLM with a detailed, human-authored specification and algorithm so it writes a companion utility in a secondary language, followed by human testing.<br>**Writing:** Translating a human-authored book into another language using AI under strict glossary constraints, followed by human review.<br>**Art:** Generating rendered assets using a workflow tightly constrained by human-drawn control maps, depth maps, and manual paint-overs.<br>**Music:** Synthesizing a vocal or orchestral performance from a human-written score and lyric sheet, followed by manual mixing. |
| **`E4`** | **Autonomous** | The delivered output was generated end-to-end by AI from minimal prompts with little or no human specification, review, or manual modification. | **All Fields:** Accepting bulk AI-generated code without reviewing the logic ("vibe-coding"), or publishing raw AI-generated text, images, or music directly from a prompt. |

---

## 4. Disclosure Format & Syntax

AIDR supports a **two-tier disclosure format** so hybrid projects (such as a project where the core work is hand-crafted at `E0` and a secondary component is AI-generated from specifications at `E3`) can represent both the overall release and its individual components accurately.

### 4.1 Tier 1: Compact Shorthand Notation

1. **Separating Ideation and Execution (Always Use a Slash):**
   Ideation (`I`) and Execution (`E`) are always separated by a forward slash (`/`). Never use a hyphen between `I` and `E`, as a hyphen implies a range.
   - Correct: `AIDR: I1 / E0`
   - Incorrect: `AIDR: I1-E0`

2. **Expanded Human-Readable Format (Use a Comma):**
   When writing out the full rating in prose, separate the Ideation and Execution clauses with a comma rather than a pipe symbol:
   - `AIDR: Ideation 1 (Assisted), Execution 0 (Unassisted)`

3. **Multi-Component Projects: Discrete Levels (`E0,E3`) vs. Contiguous Ranges (`E0-E3`):**
   When a project contains multiple components with different AI involvement levels, AIDR distinguishes between discrete selections and continuous ranges:
   - **Discrete Levels (Comma-Separated):** If a project uses only specific, non-contiguous levels (or just two distinct levels, such as `E0` for hand-crafted work and `E3` for a spec-driven utility, with no `E1` or `E2` components), list the exact levels separated by a comma:
     `AIDR: I1 / E0,E3` (or `AIDR: I1 / E0, E3`)
   - **Contiguous Ranges (Hyphen-Separated with Repeated Letter Prefix):** If a project spans three or more consecutive levels (for example, components covering `E0`, `E1`, `E2`, and `E3`), express the span using a hyphen and repeat the letter prefix (`I` or `E`) on both numbers:
     `AIDR: I1 / E0-E3` (Never write `E0-3`, which is visually ambiguous.)

### 4.2 Tier 2: Component-Level Breakdown

Whenever a project includes multiple components with different ratings, authors are encouraged to include a brief component breakdown where **each component declares both its Ideation level and its Execution level**:

```markdown
**AI Disclosure ([AIDR v1.0](AIDR-SPECIFICATION.md)): `I0,I1 / E0,E3`**
- **Core Application Engine (`I0 / E0`, Unassisted Ideation, Unassisted Execution):** Designed and hand-coded 100% by the human author with zero AI involvement.
- **Data Import & Conversion Utilities (`I1 / E3`, Assisted Ideation, Directed Execution):** Algorithms designed by the author (`I1`), with code generated by an LLM from detailed human specifications and verified by hand (`E3`).
```

### 4.3 Per-File Source Code & Asset Metadata Headers

To prevent individual hand-crafted files from being misattributed to AI (or vice versa) when viewed in isolation, authors may place an `AIDR-Usage` line tag in file headers or asset metadata comments:

**Assembly (`.asm`, `.inc`, `.s`):**
```nasm
; AIDR-Usage: I0/E0 (Ideation: Unassisted, Execution: Unassisted)
```

**C / C++ / Rust / Go / JavaScript / C#:**
```c
// AIDR-Usage: I1/E3 (Ideation: Assisted, Execution: Directed)
```

**Python / Shell / YAML / Makefile / Markdown / Text Metadata:**
```python
# AIDR-Usage: I1/E1 (Ideation: Assisted, Execution: Assisted)
```

---

## 5. Licensing & Governance

To protect the canonical definitions of the scale from fragmentation while ensuring zero-friction adoption for all creators, AIDR uses a two-part licensing structure:

1. **Using AIDR Ratings, Badges, and Templates in Your Works (`CC0 1.0 Public Domain`):**
   Declaring an AIDR rating on your project, embedding AIDR badges, copying disclosure templates, or placing `AIDR-Usage` tags in your files is completely free of restrictions under [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/).
2. **Republishing the Specification Document (`CC BY-ND 4.0`):**
   This specification document itself (`AIDR-SPECIFICATION.md`) is licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/). This ensures that if someone republishes the specification document itself, the initial authorship remains recorded in the specification text and third parties cannot alter the definitions of `I0` through `I4` or `E0` through `E4` while still calling the modified scale "AIDR."

---

## 6. Authorship & Provenance

- **Initial Author:** Jim Leonard (<mobygamer@gmail.com>)
- **Version:** 1.0 (October 2026)
- **Origin & Intent:** Created to provide programmers, writers, visual artists, musicians, and independent creators with an honest, human-readable self-disclosure standard that distinguishes human conceptual originality from mechanical AI assistance.
