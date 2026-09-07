# 📈 ResearchX: Autonomous Analyst Agent for Market & Equity Intelligence

> **An autonomous multi-agent framework that independently discovers, verifies, and cross-references industry data across primary sources to produce institutional-grade intelligence reports.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![Tests Passing](https://img.shields.io/badge/Tests-170%2B%20Passing-brightgreen.svg)]()
[![FastAPI](https://img.shields.io/badge/API-FastAPI%20%3A8011-teal.svg)](http://127.0.0.1:8011/docs)
[![Author](https://img.shields.io/badge/Author-Asadullah%20Shafique-purple.svg)](https://asadullahshafique-devunity.vercel.app)

---

## 🚀 Key Value Propositions

1. **Multi-Source Evidence Triangulation**: Cross-references claims across SEC filings, analyst benchmarks, and financial feeds to eliminate hallucinations.
2. **Autonomous Multi-Agent Collaboration**:
   - **`SearchAgent`**: Ingests primary SEC 10-K documents, earnings transcripts, and market data.
   - **`VerifyAgent`**: Calculates divergence deltas and computes credibility-weighted consensus metrics.
   - **`ReportAgent`**: Compiles institutional dossiers with SWOT analyses, investment theses, and verifiable citations.
3. **Plan-Act-Verify Reliability Loops**: Guarantees report veracity through automated cross-referencing and verification assertions.
4. **Institutional Dossier Outputs**: Produces executive briefings, key findings, comparative metric tables, and complete citation indexes.
5. **Interactive Analyst Studio**: Glassmorphic bilingual (English/Arabic RTL) dashboard with live topic runners, triangulation matrix visualizers, and interactive citation inspectors.

---

## 🏛️ ResearchX Architecture

```
                    ┌─────────────────────────┐
                    │     Research Inquiry    │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │    ResearchX Engine     │
                    └────────────┬────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│   SearchAgent    │   │   VerifyAgent    │   │   ReportAgent    │
│ • SEC Filings    │   │ • Triangulation  │   │ • Dossier Layout │
│ • Earnings Data  │   │ • Divergence %   │   │ • SWOT Matrix    │
│ • Real-Time News │   │ • Consensus Stat │   │ • Citation Index │
└──────────────────┘   └──────────────────┘   └──────────────────┘
```

---

## 🛠️ Quick Start

```powershell
# 1. Clone repository
git clone https://github.com/asadullah48/researchx.git
cd researchx

# 2. Install dependencies
pip install -e .

# 3. Run automated test suite
python -m pytest tests -v

# 4. Start local gateway & frontend analyst studio
uvicorn researchx.server:app --host 127.0.0.1 --port 8011 --reload
```

- **Interactive Analyst Studio**: [http://127.0.0.1:8011/](http://127.0.0.1:8011/)
- **Swagger OpenAPI Docs**: [http://127.0.0.1:8011/docs](http://127.0.0.1:8011/docs)

---

## 🤖 Agentic AI Alignment

- **Autonomy** — SearchAgent → VerifyAgent → ReportAgent independently
  discover, cross-verify, and compile institutional dossiers with no
  analyst curating the source list by hand.
- **Resilience** — VerifyAgent's divergence-delta and credibility-weighted
  consensus scoring exist specifically to catch a claim that only one
  source supports, so the pipeline self-checks rather than trusting the
  first source found.
- **Adaptivity** — the Plan-Act-Verify loop retries/re-triangulates when
  evidence is thin, adapting its own confidence rather than always
  reporting the same fixed certainty.

### Roadmap

- Expose SearchAgent/VerifyAgent as MCP tools so other financial-research
  agent systems can reuse the triangulation step directly.
- Extend source coverage beyond SEC filings/earnings calls/market data to
  additional primary-source categories, using the same Plan-Act-Verify
  shape.

## 🤖 Author

Built by **Asadullah Shafique**.

🔗 Explore my portfolio showcasing Agentic AI projects and real-world applications: [asadullahshafique-devunity.vercel.app](https://asadullahshafique-devunity.vercel.app)

## 🌐 Connected Ecosystem & Portfolio

- **DevUnity Portfolio**: [https://asadullahshafique-devunity.vercel.app](https://asadullahshafique-devunity.vercel.app)
- **GraphAI**: [https://github.com/asadullah48/graphai](https://github.com/asadullah48/graphai)
- **LoopAI**: [https://github.com/asadullah48/loopai](https://github.com/asadullah48/loopai)
- **HarnessAI**: [https://github.com/asadullah48/harnessai](https://github.com/asadullah48/harnessai)
- **SecureBridge**: [https://github.com/asadullah48/securebridge](https://github.com/asadullah48/securebridge)
- **WorkforceAI Academy**: [https://github.com/asadullah48/workforceai-academy](https://github.com/asadullah48/workforceai-academy)
- **ConciergeAgent**: [https://github.com/asadullah48/conciergeagent](https://github.com/asadullah48/conciergeagent)
- **ContextX**: [https://github.com/asadullah48/contextx](https://github.com/asadullah48/contextx)
- **GuardrailAI**: [https://github.com/asadullah48/guardrailai](https://github.com/asadullah48/guardrailai)
- **MarketAgentHub**: [https://github.com/asadullah48/marketagenthub](https://github.com/asadullah48/marketagenthub)
- **WorkforceAI**: [https://github.com/asadullah48/workforceai](https://github.com/asadullah48/workforceai)
- **DomainX**: [https://github.com/asadullah48/domainx](https://github.com/asadullah48/domainx)
