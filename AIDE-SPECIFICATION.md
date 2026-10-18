# AIDE: AI Disclosure of Ideation & Execution — Specification v1.0

**Version:** 1.0  
**Status:** Canonical Specification  
**Specification License:** [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)  
**Templates, Badges & Header Tags License:** [CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/)

---

## 1. Purpose & Philosophy

**AIDE (AI Disclosure of Ideation & Execution)** is a voluntary, author-declared, two-dimensional rating framework that enables creators of software, utilities, source code, and creative works to transparently communicate how artificial intelligence was used in their projects.

### Why Single-Axis Scales Fail
Existing linear disclosure scales—such as the REAL Rating (0–5), the AI Assessment Scale (1–5), the GAIT Framework, and single-tag SPDX conventions—collapse all AI usage onto a single one-dimensional spectrum. Worse, linear scales routinely place *AI brainstorming and ideation* at a lower tier than *AI mechanical implementation*.

Under a single-axis scale:
1. An author with zero original ideas who prompts an LLM to invent a concept and outline, and then types the resulting work manually, receives a low AI rating.
2. An engineer or creator who spends years conceiving a novel algorithm or original design, hand-crafts the performance-critical core (such as assembly language routines), and uses an LLM strictly as an implementation workhorse to write companion utilities from a rigorous specification is penalized with a high AI rating—lumping original human engineering together with unreviewed "vibe-coded" output.

### The AIDE Solution: Separating Mind from Muscle
AIDE resolves this distortion by separating disclosure into two independent 0-to-4 axes:
- **Axis 1: Ideation (`I0`–`I4`)** measures who conceived the ideas, algorithms, system architecture, creative vision, and structural design.
- **Axis 2: Execution (`E0`–`E4`)** measures how the mechanical production, coding, drafting, or asset generation was performed.

Both axes share five symmetrical, whole-number levels:
- **`0` — Unassisted**
- **`1` — Assisted**
- **`2` — Collaborative**
- **`3` — Directed**
- **`4` — Autonomous**

---

## 2. Axis 1: Ideation (`I0`–`I4`)

The **Ideation** axis measures the intellectual and creative origin of the work: its concepts, algorithms, system architecture, problem-solving methodology, and structural design.

| Level | Title | Definition | Programming & Engineering Examples | Creative & Media Examples |
| :--- | :--- | :--- | :--- | :--- |
| **`I0`** | **Unassisted** | All concepts, algorithms, architecture, and creative designs are 100% human-originated, with zero AI consultation even for background research. | Designing a novel compression algorithm, protocol, or hardware routine entirely from personal knowledge, paper datasheets, and non-AI references. | Conceiving a story outline, documentary thesis, musical composition, or visual design completely independently without querying any AI tool. |
| **`I1`** | **Assisted** | All core concepts, architecture, and primary algorithms are human-originated. AI was used only for background research (explaining domain theory, summarizing documentation) or as a sounding board that suggested minor optimizations or edge-case tweaks which the human tested and selectively adopted. | Inventing a novel 8-bit PCM audio compression algorithm over years of thought, using an LLM as an interactive textbook to review DSP math, and testing minor edge-case refinements suggested by the model. | Designing an original essay or video script structure while using an LLM to summarize long archival transcripts or collate historical reference data. |
| **`I2`** | **Collaborative** | The human established the overarching vision and goals, and actively partnered with AI to brainstorm sub-algorithms, solve structural design problems, or develop outlines together. | Designing an application architecture in an iterative back-and-forth dialogue where the human and AI jointly propose and refine subsystem structures. | Co-developing a narrative world, chapter breakdown, or thematic structure through interactive brainstorming sessions with an LLM. |
| **`I3`** | **Directed** | The human provided a broad problem statement, theme, or high-level prompt, and AI generated the primary architecture, algorithm choices, or creative structure, which the human then curated, evaluated, and refined. | Prompting an AI with desired input/output goals and allowing the AI to select the underlying data structures, algorithms, and module architecture, which the human reviews and approves. | Asking an AI to propose several plot outlines, musical progressions, or visual layouts from a brief premise and selecting the strongest candidate for production. |
| **`I4`** | **Autonomous** | AI conceived the project concept, design, and direction with minimal or no human conceptual input. | Prompting an autonomous agent to invent and design a software project from a single open-ended request without human architectural guidance. | Generating an entire story concept, theme, and structural outline automatically from a minimal prompt. |

---

## 3. Axis 2: Execution (`E0`–`E4`)

The **Execution** axis measures how the tangible artifacts of the work—source code, binaries, prose, audio, video, or visual assets—were mechanically constructed and verified.

| Level | Title | Definition | Programming & Engineering Examples | Creative & Media Examples |
| :--- | :--- | :--- | :--- | :--- |
| **`E0`** | **Unassisted** | Every line of code, word of prose, or creative asset was manually authored by the human with zero AI involvement. | Hand-writing an 8086 assembly decompressor instruction-by-instruction and cycle-counting it manually. | Typing an article on a mechanical keyboard, editing video cuts manually, or illustrating artwork entirely by hand. |
| **`E1`** | **Assisted** | The delivered code or creative work is human-authored. AI or machine-learning tools were used only for read-only diagnostics (bug-finding, static review), reference lookups (phrase thesaurus, syntax lookup), non-generative signal cleanup (audio denoising, speech-to-text transcription), or minor inline autocomplete and repetitive boilerplate. | Writing C or assembly code manually, then asking an LLM to inspect the human-written source for off-by-one bugs or boundary errors. | Writing prose entirely by hand while using an LLM as an interactive phrase thesaurus, or using a neural filter to reduce reverb in field audio recordings. |
| **`E2`** | **Collaborative** | Human and AI each produced substantial portions of the delivered work, such as a human writing the core engine or primary prose while AI generated supporting utilities, build scripts, charts/diagrams from human data, or secondary routines. | Hand-coding the core simulation or runtime engine while using an LLM to generate test harnesses, data visualization scripts, or CLI argument parsers. | Authoring the primary text of a technical article while using AI to generate summary charts, graphs, or diagrams from author-supplied source data. |
| **`E3`** | **Directed** | Generative AI wrote the vast majority of the component's code or content, operating strictly as an implementation engine under human direction, detailed multi-paragraph specifications, explicit algorithms, constraints, and human verification/testing. | Providing an LLM with a complete, human-authored algorithm specification, bit-packing format, and constraints so it writes a host compressor utility in a language the author did not wish to spend months learning, followed by rigorous human testing. | Translating a human-authored work into another language using an LLM under strict terminology constraints, followed by human verification and editing. |
| **`E4`** | **Autonomous** | The delivered output was generated end-to-end by AI from minimal prompts with little or no human specification, code review, or manual modification. | Accepting bulk agent-generated application code from a brief prompt without reviewing or verifying the internal logic ("vibe-coding"). | Publishing raw AI-generated articles, images, video, or music directly from a prompt without manual editing. |

---

## 4. The 5×5 AIDE Matrix

Because Ideation (`I`) and Execution (`E`) are orthogonal, AIDE captures 25 distinct human-AI workflows. The table below illustrates key archetypes across the matrix:

| Ideation \ Execution | `E0` (Unassisted) | `E1` (Assisted) | `E2` (Collaborative) | `E3` (Directed) | `E4` (Autonomous) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`I0` (Unassisted)** | **`I0 / E0`**<br>100% Human Mind & Craft. Zero AI used anywhere. | **`I0 / E1`**<br>Pure human concept & code; AI used only for bug-checking or cleanup. | **`I0 / E2`**<br>Pure human design & core code; AI wrote helper scripts or charts. | **`I0 / E3`**<br>Pure human algorithm & spec; AI acted as a compiler to write target code. | **`I0 / E4`**<br>Human concept handed off to AI with no code review. |
| **`I1` (Assisted)** | **`I1 / E0`**<br>Human-designed (with AI background research); 100% hand-crafted execution. | **`I1 / E1`**<br>Human-designed & human-written; AI used for research, linting, or thesaurus. | **`I1 / E2`**<br>Human-designed; shared execution across core (human) and tooling (AI). | **`I1 / E3`**<br>Human-designed algorithm with minor AI tweaks; AI implemented code from strict human spec. | **`I1 / E4`**<br>Human-designed concept generated by AI without verification. |
| **`I2` (Collaborative)** | **`I2 / E0`**<br>Co-brainstormed design; 100% hand-crafted by human. | **`I2 / E1`**<br>Co-brainstormed design; human-written with AI diagnostics. | **`I2 / E2`**<br>True 50/50 human-AI partnership in both design and build. | **`I2 / E3`**<br>Co-brainstormed design implemented primarily by AI under human testing. | **`I2 / E4`**<br>Co-brainstormed design generated autonomously by AI. |
| **`I3` (Directed)** | **`I3 / E0`**<br>AI-proposed design curated by human, then 100% hand-crafted by human. | **`I3 / E1`**<br>AI-proposed design; human-written execution with minor AI assist. | **`I3 / E2`**<br>AI-proposed design; shared human-AI implementation. | **`I3 / E3`**<br>AI-proposed design and AI-written code, curated and tested by human. | **`I3 / E4`**<br>AI-proposed design and unreviewed AI execution. |
| **`I4` (Autonomous)** | **`I4 / E0`**<br>AI-invented concept executed manually by a human. | **`I4 / E1`**<br>AI-invented concept executed by human with minor AI assist. | **`I4 / E2`**<br>AI-invented concept with hybrid implementation. | **`I4 / E3`**<br>AI-invented concept implemented by AI with human testing. | **`I4 / E4`**<br>100% Unsupervised AI ("Vibe-Coded" / Raw Synthetic Output). |

---

## 5. Disclosure Format & Syntax

AIDE supports a **two-tier disclosure format** so hybrid projects (such as a software package combining hand-crafted assembly routines with AI-implemented host utilities) can represent both the whole project and its individual components accurately.

### 5.1 Tier 1: Compact Shorthand Notation
- **Single-Score Format (Uniform Projects):**
  `AIDE: I1 / E0` (or `AIDE: I1-E0` in URL-safe badge strings)
- **Expanded Text Format:**
  `AIDE Rating: Ideation 1 (Assisted) | Execution 0 (Unassisted)`
- **Range Format (Hybrid / Multi-Component Projects):**
  When a project contains distinct components with different levels of AI involvement, express the score as a range from the lowest to the highest component rating:
  `AIDE: I1 / E0–3` (or `AIDE: Ideation 1 | Execution 0–3`)

### 5.2 Tier 2: Component-Level Breakdown
Whenever a range is used (or whenever an author wishes to highlight specific craftsmanship within a release), follow the project-level score with a brief component table or bullet list:

```markdown
**AI Disclosure ([AIDE v1.0](https://example.org/aide)): `I1 / E0–3`**
- **Algorithms & Architecture (`I1` — Assisted Ideation):** Original human concepts and designs; AI was used only for background domain research and minor edge-case refinements.
- **Runtime Decompressors (`E0` — Unassisted Execution):** 100% hand-crafted 8086 assembly language written by the author.
- **Host Compressor Utilities (`E3` — Directed Execution):** Implemented by AI from detailed, multi-paragraph human specifications and verified by the author.
```

### 5.3 Per-File Source Code Header Tags
To prevent individual hand-crafted source files from being misattributed to AI (or vice versa) when inspected in isolation, authors may place an `AIDE-Usage` line tag at the top of source files alongside standard `SPDX-License-Identifier` headers:

**Assembly (`.asm`, `.inc`, `.s`):**
```nasm
; SPDX-License-Identifier: MIT
; AIDE-Usage: I1/E0 (Ideation: Assisted | Execution: Unassisted — 100% Hand-Crafted Assembly)
```

**C / C++ / Rust / Go / JavaScript / C#:**
```c
// SPDX-License-Identifier: MIT
// AIDE-Usage: I1/E3 (Ideation: Assisted | Execution: Directed — AI-Implemented from Human Spec)
```

**Python / Shell / YAML / Makefile:**
```python
# SPDX-License-Identifier: MIT
# AIDE-Usage: I1/E3 (Ideation: Assisted | Execution: Directed — AI-Implemented from Human Spec)
```

---

## 6. Licensing & Governance

To protect the integrity of the rating definitions while ensuring zero-friction adoption for developers and creators, AIDE uses a split-license model:

1. **Canonical Specification (`CC BY-ND 4.0`):**
   This specification document and the formal definitions of `I0`–`I4` and `E0`–`E4` are licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/). Anyone may copy, redistribute, and cite this specification in any medium or format provided appropriate credit is given, a link to the specification is provided, and the level definitions are not altered under the **AIDE** name.
2. **Templates, Badges & Source Header Tags (`CC0 1.0 Public Domain`):**
   All AIDE `README` disclosure snippets, `AIDE-Usage` source code header comments, and SVG badges are dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). Authors may copy, modify, and embed them into any commercial, hobby, or open-source project without restriction or attribution requirements.
