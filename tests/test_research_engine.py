import pytest
from researchx.orchestration.research_engine import ResearchEngine
from researchx.core.models import ResearchTopic

def test_research_engine_end_to_end():
    engine = ResearchEngine()
    topic = ResearchTopic(query="Autonomous Multi-Agent Enterprise TAM 2030")
    report = engine.conduct_research(topic)
    
    assert report.overall_confidence_score >= 0.90
    assert len(report.triangulation_checks) >= 2
    assert len(report.verifiable_citations) == 3
    assert "44.2%" in report.metrics_matrix["Consensus CAGR"]
