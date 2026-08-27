from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
import time

class ConsensusStatus(str, Enum):
    UNANIMOUS_CONSENSUS = "UNANIMOUS_CONSENSUS"
    WEIGHTED_MAJORITY = "WEIGHTED_MAJORITY"
    CONFLICTING_DIVERGENCE = "CONFLICTING_DIVERGENCE"

class ResearchDepth(str, Enum):
    RAPID_BRIEF = "RAPID_BRIEF"
    INSTITUTIONAL_DEEP_DIVE = "INSTITUTIONAL_DEEP_DIVE"
    COMPREHENSIVE_VALUATION = "COMPREHENSIVE_VALUATION"

class RawEvidence(BaseModel):
    source_id: str
    publisher: str
    source_type: str # SEC_FILING | EARNINGS_CALL | INDUSTRY_BENCHMARK | NEWS_FEED
    url: str
    publication_date: str
    headline: str
    content_snippet: str
    numerical_metrics: Dict[str, float] = Field(default_factory=dict)
    credibility_weight: float = 0.95 # 0.0 to 1.0

class CrossReferenceCheck(BaseModel):
    metric_name: str
    claim_summary: str
    source_ids: List[str]
    extracted_values: Dict[str, float]
    consensus_status: ConsensusStatus
    divergence_delta_pct: float
    triangulated_value: float
    confidence_score: float

class CitationItem(BaseModel):
    citation_id: str
    source_title: str
    publisher: str
    url: str
    accessed_at: str

class AnalystReport(BaseModel):
    report_id: str
    topic: str
    sector: str
    executive_summary: str
    key_findings: List[str]
    metrics_matrix: Dict[str, Any]
    swot_analysis: Dict[str, List[str]] # strengths, weaknesses, opportunities, threats
    investment_thesis: str
    verifiable_citations: List[CitationItem]
    overall_confidence_score: float
    triangulation_checks: List[CrossReferenceCheck]
    generated_at: float = Field(default_factory=time.time)

class ResearchTopic(BaseModel):
    topic_id: str = "RES-9901"
    query: str = "Enterprise Autonomous Multi-Agent AI Market Growth & Cloud Hyperscaler Positioning"
    sector: str = "TECHNOLOGY" # TECHNOLOGY | HEALTHCARE | ENERGY | FINANCIALS
    depth: ResearchDepth = ResearchDepth.INSTITUTIONAL_DEEP_DIVE
    time_horizon: str = "2026 - 2030"
