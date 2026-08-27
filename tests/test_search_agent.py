import pytest
from researchx.agents.search_agent import SearchAgent
from researchx.core.models import ResearchTopic

def test_search_agent_discovery():
    agent = SearchAgent()
    topic = ResearchTopic(query="Cloud Hyperscaler AI Compute")
    sources = agent.discover_sources(topic)
    assert len(sources) >= 3
    assert any(s.source_type == "SEC_FILING" for s in sources)
    assert any("cagr_growth_pct" in s.numerical_metrics for s in sources)
