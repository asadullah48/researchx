from typing import List
from researchx.core.models import ResearchTopic, RawEvidence, CrossReferenceCheck, AnalystReport
from researchx.core.synthesis_engine import SynthesisEngine

class ReportAgent:
    """
    ReportAgent: Compiles triangulated findings into institutional market intelligence reports
    with SWOT analyses and complete citation indices.
    """
    def __init__(self):
        self.name = "ReportAgent"
        self.version = "1.0.0"

    def generate_analyst_report(
        self, topic: ResearchTopic, evidence: List[RawEvidence], triangulations: List[CrossReferenceCheck]
    ) -> AnalystReport:
        return SynthesisEngine.compile_report(topic, evidence, triangulations)
