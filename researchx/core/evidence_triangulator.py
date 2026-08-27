import math
from typing import List, Dict, Tuple
from researchx.core.models import RawEvidence, CrossReferenceCheck, ConsensusStatus

class EvidenceTriangulator:
    """
    EvidenceTriangulator: Cross-references data points across multiple independent sources,
    calculates percentage divergence deltas, and computes weighted consensus metrics.
    Formula: D_delta = |V1 - V2| / V_avg
    """
    @staticmethod
    def triangulate_metric(metric_name: str, claim: str, evidence_list: List[RawEvidence]) -> CrossReferenceCheck:
        values: Dict[str, float] = {}
        weights: Dict[str, float] = {}

        for ev in evidence_list:
            if metric_name in ev.numerical_metrics:
                values[ev.source_id] = ev.numerical_metrics[metric_name]
                weights[ev.source_id] = ev.credibility_weight

        if not values:
            return CrossReferenceCheck(
                metric_name=metric_name,
                claim_summary=claim,
                source_ids=[],
                extracted_values={},
                consensus_status=ConsensusStatus.CONFLICTING_DIVERGENCE,
                divergence_delta_pct=100.0,
                triangulated_value=0.0,
                confidence_score=0.0
            )

        val_list = list(values.values())
        min_v, max_v = min(val_list), max(val_list)
        avg_v = sum(val_list) / len(val_list)

        delta = 0.0 if avg_v == 0 else round(((max_v - min_v) / avg_v) * 100.0, 2)

        # Weighted average
        tot_weight = sum(weights.values())
        triangulated = round(sum(values[sid] * (weights[sid] / tot_weight) for sid in values), 2)

        if delta <= 5.0:
            status = ConsensusStatus.UNANIMOUS_CONSENSUS
            conf = 0.98
        elif delta <= 15.0:
            status = ConsensusStatus.WEIGHTED_MAJORITY
            conf = 0.91
        else:
            status = ConsensusStatus.CONFLICTING_DIVERGENCE
            conf = 0.65

        return CrossReferenceCheck(
            metric_name=metric_name,
            claim_summary=claim,
            source_ids=list(values.keys()),
            extracted_values=values,
            consensus_status=status,
            divergence_delta_pct=delta,
            triangulated_value=triangulated,
            confidence_score=conf
        )
