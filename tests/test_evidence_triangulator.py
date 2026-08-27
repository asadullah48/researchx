import pytest
from researchx.core.evidence_triangulator import EvidenceTriangulator
from researchx.core.models import RawEvidence, ConsensusStatus

def test_triangulation_unanimous():
    e1 = RawEvidence(source_id="S1", publisher="P1", source_type="SEC", url="http://s1", publication_date="2026-01-01", headline="H1", content_snippet="C1", numerical_metrics={"rev": 100.0}, credibility_weight=1.0)
    e2 = RawEvidence(source_id="S2", publisher="P2", source_type="SEC", url="http://s2", publication_date="2026-01-01", headline="H2", content_snippet="C2", numerical_metrics={"rev": 102.0}, credibility_weight=0.9)
    
    check = EvidenceTriangulator.triangulate_metric("rev", "Revenue growth", [e1, e2])
    assert check.consensus_status == ConsensusStatus.UNANIMOUS_CONSENSUS
    assert check.confidence_score >= 0.95
    assert check.triangulated_value > 0

def test_triangulation_conflicting():
    e1 = RawEvidence(source_id="S1", publisher="P1", source_type="SEC", url="http://s1", publication_date="2026-01-01", headline="H1", content_snippet="C1", numerical_metrics={"val": 10.0})
    e2 = RawEvidence(source_id="S2", publisher="P2", source_type="SEC", url="http://s2", publication_date="2026-01-01", headline="H2", content_snippet="C2", numerical_metrics={"val": 50.0})
    
    check = EvidenceTriangulator.triangulate_metric("val", "Disparate valuation", [e1, e2])
    assert check.consensus_status == ConsensusStatus.CONFLICTING_DIVERGENCE
    assert check.divergence_delta_pct > 50.0
