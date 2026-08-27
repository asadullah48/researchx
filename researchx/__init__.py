"""
ResearchX: Autonomous Analyst Agent Framework for Multi-Source Triangulation & Verified Market Intelligence
"""

__version__ = "1.0.0"

from researchx.agents.search_agent import SearchAgent
from researchx.agents.verify_agent import VerifyAgent
from researchx.agents.report_agent import ReportAgent
from researchx.orchestration.research_engine import ResearchEngine

__all__ = [
    "SearchAgent",
    "VerifyAgent",
    "ReportAgent",
    "ResearchEngine"
]
