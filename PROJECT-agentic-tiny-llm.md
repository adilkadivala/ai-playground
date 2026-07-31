# Project: StudyForge — Tiny LLM + Agentic Assistant

**Student project** for learning: agents, agentic loops, and a small language model path.  
**Repo folder:** `ai-playground/studyforge/` (to create when we start coding)

---

## What you’re building (one sentence)

A **local study agent** that can answer questions about *your* notes/PDFs, use **tools** (search files, calculator, write notes), and run a **multi-step agent loop** — powered first by a **small/local LLM**, with an optional **tiny from-scratch** language model experiment later.

---

## Why this project

| Learning goal | How the project teaches it |
|---------------|----------------------------|
| Tiny / small LLM | Call a small local model (Ollama) + later a toy next-token model |
| Agent | Plan → tool call → observe → answer |
| Agentic | Multi-step tasks, memory, retries |
| Your roadmap | Replaces “abstract PDF only” with a portfolio piece |

---

## Product features (MVP → v2 → stretch)

### MVP (ship in ~2 weeks of part-time work)
1. **Chat CLI** — you type a question, get an answer  
2. **Tool: `search_notes`** — search `notes/` and return snippets  
3. **Tool: `calculator`** — safe math for homework-style questions  
4. **Agent loop** — model may request a tool, you execute it, feed result back (max N steps)  
5. **Logs** — print each step (thought / tool / result) so you *see* agentic behavior  

### v1.5 (after RAG phase)
6. **RAG over your PDFs** — chunk + embed + retrieve, then answer with sources  
7. **Citations** — “from notes/day-03…”  

### v2 (after agents PDFs)
8. **Multi-tool routing** — search + write_note + list_files  
9. **Simple memory** — last K turns in context  
10. **FastAPI** — HTTP API around the same agent  

### Stretch (optional, advanced)
11. **Tiny LLM from scratch** — character-level or tiny transformer trained on a small text file (links to deep-learning book projects)  
12. **Two-agent crew** — Researcher agent + Writer agent  

---

## Architecture (simple)

```text
You (CLI)
   │
   ▼
┌─────────────────┐
│  Agent loop     │  plan → act → observe → (repeat) → final answer
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐  ┌──────────────┐
│ Tools │  │ Small LLM    │  Ollama (e.g. tinyllama / phi / qwen-small)
└───────┘  └──────────────┘
 search_notes
 calculator
 write_note (later)
```

**Later optional path:**
```text
ToyTinyLLM (your trained mini model) ── can replace or sit next to Ollama for demos
```

---

## Tech stack (keeps it learnable)

| Piece | Choice | Why |
|-------|--------|-----|
| Language | Python 3.11+ | Matches your course |
| LLM (practical) | **Ollama** + small model | Real agent without GPU farm |
| Agent loop | **Your own 50–100 lines** first | No black-box framework at start |
| Later frameworks | LangGraph / simple custom | After you understand the loop |
| Vectors (RAG) | ChromaDB | Simple, local |
| API (later) | FastAPI | Matches your FastAPI PDF |
| From-scratch toy LM | NumPy / tiny PyTorch | After more DL chapters |

**Avoid at MVP:** full AutoGen/CrewAI stacks (add after your loop works).

---

## Folder layout (target)

```text
ai-playground/studyforge/
  README.md
  requirements.txt
  .env.example
  app/
    main.py           # CLI entry
    agent.py          # agent loop
    llm.py            # talk to Ollama (or toy model)
    tools/
      search_notes.py
      calculator.py
      write_note.py
    prompts.py
  data/               # optional sample docs
  scripts/
    train_tiny_lm.py  # stretch: toy next-token model
  tests/
    test_calculator.py
    test_agent_loop.py
```

---

## Build phases (aligned with your speedup roadmap)

| Phase | When (speedup) | Deliverable |
|------:|----------------|-------------|
| **P0** | This week | Scaffold repo + calculator tool + fake agent (no LLM) that runs tools by keyword |
| **P1** | Week 1–2 | Ollama wired + real tool-calling loop (JSON tool requests) |
| **P2** | With RAG weeks | Notes/PDF retrieval tool + citations |
| **P3** | With FastAPI | `POST /chat` API |
| **P4** | Stretch | Tiny from-scratch LM demo (generate a few characters/words) |
| **P5** | Portfolio | README + demo GIF/script + architecture diagram |

---

## “Tiny LLM” — two tracks (both valuable)

### Track A — Small *local* LLM (do this first)
- Install Ollama, pull e.g. `tinyllama` or `phi3:mini` / `qwen2.5:0.5b`
- Your agent calls it via HTTP API  
- **You learn agents**, not GPU training  

### Track B — Tiny *from-scratch* LM (do this later)
- Train a mini next-token model on a small text (e.g. your notes export, or a nursery rhyme corpus)
- Show: train loss down (like your `tiny_train_loop.py` but for text)
- Generate a short sample  
- **You learn** what an LLM *is* under the hood  

**Portfolio story:**  
“I built an agentic study assistant on a small local model, and also trained a toy LM from scratch to understand next-token prediction.”

---

## Definition of done (MVP)

- [ ] `python -m app.main` opens a chat loop  
- [ ] Agent can use **calculator** and **search_notes**  
- [ ] Terminal shows step log: `THOUGHT / TOOL / RESULT / ANSWER`  
- [ ] At least 3 demo prompts documented in README  
- [ ] Works offline except optional model download once  

---

## Example demo prompts (MVP)

1. `What is 17 * 24?` → should call calculator  
2. `What did I learn about ReLU?` → should search notes  
3. `Search my notes for backprop, then explain in 2 sentences` → multi-step agentic  

---

## Risk control (so you don’t stall)

| Risk | Mitigation |
|------|------------|
| Framework rabbit hole | Own loop first; frameworks later |
| GPU / training too hard | Ollama first; from-scratch is stretch |
| Scope creep | MVP tools = 2 only |
| Math overwhelm | No need for full GPT math for Track A |

---

## Next class action

When you say **“start StudyForge”** we will:
1. Create `studyforge/` scaffold  
2. Implement calculator + keyword agent (no LLM yet)  
3. Then wire Ollama  

Your call on model preference when we start:
- smallest/fastest: `tinyllama`  
- smarter small: `phi3:mini` or `qwen2.5:0.5b` (if machine allows)
