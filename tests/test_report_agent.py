import pytest
from researchx.agents.report_agent import ReportAgent
from researchx.agents.search_agent import SearchAgent
from researchx.agents.verify_agent import VerifyAgent
from researchx.core.models import ResearchTopic

def test_report_agent_synthesis():
    search = SearchAgent()
    verify = VerifyAgent()
    report_agent = ReportAgent()
    
    topic = ResearchTopic(query="Agentic AI Compute TAM")
    sources = search.discover_sources(topic)
    checks = verify.cross_check_evidence(sources)
    report = report_agent.generate_analyst_report(topic, sources, checks)
    
    assert report.topic == topic.query
    assert len(report.key_findings) >= 3
    assert len(report.verifiable_citations) >= 3
    assert "strengths" in report.swot_analysis
    assert "Executive Intelligence Briefing" in report.executive_summary
