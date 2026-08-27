import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any

from researchx.core.models import ResearchTopic, AnalystReport, CrossReferenceCheck
from researchx.orchestration.research_engine import ResearchEngine

app = FastAPI(
    title="ResearchX Autonomous Analyst Gateway",
    version="1.0.0",
    description="Autonomous Market & Equity Intelligence Agent Framework with Multi-Source Triangulation"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = ResearchEngine()

# Mount Static UI Files
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def serve_dashboard():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"service": "ResearchX", "status": "active", "docs": "/docs"}

@app.get("/healthz")
def healthz():
    return {"status": "healthy", "service": "ResearchX", "version": "1.0.0"}

@app.get("/readyz")
def readyz():
    return {"status": "ready", "analyst_agents_active": 3}

@app.post("/api/v1/research/generate-report", response_model=AnalystReport)
def generate_report(topic: ResearchTopic):
    return engine.conduct_research(topic)
