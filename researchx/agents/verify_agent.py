from typing import List
from researchx.core.models import RawEvidence, CrossReferenceCheck
from researchx.core.evidence_triangulator import EvidenceTriangulator

class VerifyAgent:
    """
    VerifyAgent: Cross-references claims across disparate sources, verifies statistics,
    and calculates multi-source consensus metrics.
    """
    def __init__(self):
        self.name = "VerifyAgent"
        self.version = "1.0.0"

    def cross_check_evidence(self, evidence: List[RawEvidence]) -> List[CrossReferenceCheck]:
        c1 = EvidenceTriangulator.triangulate_metric(
            metric_name="cagr_growth_pct",
            claim="Global multi-agent enterprise CAGR projection through 2030",
            evidence_list=evidence
        )
        c2 = EvidenceTriangulator.triangulate_metric(
            metric_name="market_val_2030_billions",
            claim="Projected Total Addressable Market (TAM) Valuation by 2030",
            evidence_list=evidence
        )
        return [c1, c2]
