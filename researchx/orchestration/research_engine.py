import time
from typing import List, Dict, Any
from researchx.core.models import ResearchTopic, AnalystReport, CrossReferenceCheck
from researchx.agents.search_agent import SearchAgent
from researchx.agents.verify_agent import VerifyAgent
from researchx.agents.report_agent import ReportAgent

class ResearchEngine:
    """
    ResearchEngine: Unified autonomous research coordinator executing Plan-Act-Verify
    market and equity inquiry cycles.
    """
    def __init__(self):
        self.search_agent = SearchAgent()
        self.verify_agent = VerifyAgent()
        self.report_agent = ReportAgent()

    def conduct_research(self, topic: ResearchTopic) -> AnalystReport:
        # Step 1: SEARCH (Multi-source ingestion)
        evidence = self.search_agent.discover_sources(topic)

        # Step 2: VERIFY (Triangulation & divergence check)
        triangulations = self.verify_agent.cross_check_evidence(evidence)

        # Step 3: REPORT (Institutional synthesis)
        report = self.report_agent.generate_analyst_report(topic, evidence, triangulations)

        return report
