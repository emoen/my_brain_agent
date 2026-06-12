# my_brain_agent

An LLM-powered personal knowledge base agent, inspired by Andrej Karpathy's approach to using LLMs for building and maintaining structured knowledge.

## Inspiration

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">LLM Knowledge Bases<br><br>Something I&#39;m finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images).</p>&mdash; Andrej Karpathy (@karpathy) <a href="https://x.com/karpathy/status/2039805659525644595">April 2, 2026</a></blockquote>

**TLDR from the thread:** Raw data from sources is collected, then compiled by an LLM into a `.md` wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually — it's the domain of the LLM.

---

## What This Repo Does

This project implements that pattern:

1. **Ingest** — PDFs and papers go into `raw/` directories
2. **Compile** — LLM agents (via GitHub Models API / Hugging Face) process them into structured markdown wiki articles
3. **View** — The generated wiki is browsable in Obsidian (or on GitHub)
4. **Enhance** — Tools for building theorem graphs, fixing formatting, and cross-linking content

## Project Structure

```
my_brain_agent/
├── functional_analysis/        ← Knowledge base: Functional Analysis (GTM 208)
│   ├── raw/                    ← Source PDFs
│   ├── wiki/                   ← LLM-generated markdown articles
│   │   ├── chapters/           ← Per-chapter deep summaries
│   │   └── graphs/             ← Theorem dependency graphs (.dot, .mmd, .png)
│   ├── ingest_chapters.py      ← PDF → chapter-level wiki articles
│   ├── ingest_knowledge_base.py← PDF → full-book wiki summary
│   ├── build_theorem_graph.py  ← Generate theorem dependency graphs
│   └── fix_math_delimiters.py  ← Post-process LaTeX formatting
├── test_knowledge_base/        ← Additional knowledge base articles
├── sync_papers.py              ← Sync & summarize new papers from raw/
├── do_sync.py                  ← Paper sync via Hugging Face Inference
├── copilot_agent_test.py       ← GitHub Models API testing
├── load_env.sh                 ← Load environment variables
├── requirements.txt            ← Python dependencies
└── .env.example                ← Template for required secrets
```

## Setup

```bash
# Create virtual environment
python3 -m venv my_brain
source my_brain/bin/activate
pip install -r requirements.txt

# Configure secrets (copy and fill in your tokens)
cp .env.example .env
# Edit .env with your HF_TOKEN and GITHUB_TOKEN

# Load environment variables
source load_env.sh
```

## Required Tokens

| Variable | Source |
|----------|--------|
| `HF_TOKEN` | [Hugging Face Settings → Tokens](https://huggingface.co/settings/tokens) |
| `GITHUB_TOKEN` | [GitHub → Developer Settings → Fine-grained PAT](https://github.com/settings/tokens) (needs `models:read` scope) |

## Usage

```bash
source load_env.sh

# Ingest a PDF book into chapter-level wiki articles
cd functional_analysis
python ingest_chapters.py

# Build theorem dependency graph
python build_theorem_graph.py

# Sync and summarize new papers
cd ..
python sync_papers.py
```

## License

Personal project — not yet licensed for redistribution.
