from typing import List
from researchx.core.models import ResearchTopic, RawEvidence

class SearchAgent:
    """
    SearchAgent: Gathers multi-source raw evidence from SEC 10-Ks, earnings calls,
    and analyst industry databases.
    """
    def __init__(self):
        self.name = "SearchAgent"
        self.version = "1.0.0"

    def discover_sources(self, topic: ResearchTopic) -> List[RawEvidence]:
        # Simulated multi-source evidence extraction
        return [
            RawEvidence(
                source_id="SEC_10K_AWS",
                publisher="SEC Edgar Database",
                source_type="SEC_FILING",
                url="https://sec.gov/edgar/data/amzn/10k_2025.pdf",
                publication_date="2026-02-14",
                headline="Amazon Q4 10-K: Generative AI & Agentic Compute Expansion",
                content_snippet="AWS enterprise agent compute revenue grew 45.1% YoY with over 40,000 corporate deployments.",
                numerical_metrics={"cagr_growth_pct": 45.1, "market_val_2030_billions": 145.0},
                credibility_weight=0.99
            ),
            RawEvidence(
                source_id="GARTNER_2026_LEADER",
                publisher="Gartner Research",
                source_type="INDUSTRY_BENCHMARK",
                url="https://gartner.com/reports/2026-magic-quadrant-agentic-ai",
                publication_date="2026-01-20",
                headline="Magic Quadrant for Autonomous Agent Platforms",
                content_snippet="Global enterprise adoption of multi-agent architectures projected at 43.8% CAGR through 2030.",
                numerical_metrics={"cagr_growth_pct": 43.8, "market_val_2030_billions": 140.0},
                credibility_weight=0.95
            ),
            RawEvidence(
                source_id="BLOOMBERG_INTELLIGENCE",
                publisher="Bloomberg Intelligence",
                source_type="NEWS_FEED",
                url="https://bloomberg.com/intelligence/ai-agent-market-2030",
                publication_date="2026-03-01",
                headline="Enterprise AI Agent Economy Projected at $142.5B by 2030",
                content_snippet="Consensus equity valuation points to $142.5B TAM by 2030, led by workflow automation and agent-as-a-worker models.",
                numerical_metrics={"cagr_growth_pct": 44.2, "market_val_2030_billions": 142.5},
                credibility_weight=0.92
            )
        ]
