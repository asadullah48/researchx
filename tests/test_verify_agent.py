import pytest
from researchx.agents.verify_agent import VerifyAgent
from researchx.agents.search_agent import SearchAgent
from researchx.core.models import ResearchTopic

def test_verify_agent_cross_check():
    search = SearchAgent()
    verify = VerifyAgent()
    topic = ResearchTopic(query="Enterprise AI Growth")
    sources = search.discover_sources(topic)
    checks = verify.cross_check_evidence(sources)
    assert len(checks) >= 2
    for c in checks:
        assert c.confidence_score >= 0.85
        assert len(c.source_ids) >= 2
