// ResearchX Interactive Controller & Bilingual Localization

let currentLang = 'en';

const TRANSLATIONS = {
  en: {
    badgeTitle: "Autonomous Market Analyst",
    statusLive: "Analyst Active (:8011)",
    heroTitle: "Autonomous Market & Equity Intelligence with Multi-Source Triangulation",
    heroSubtitle: "Generate institutional research dossiers by automatically discovering SEC filings, cross-checking statistical claims, calculating divergence, and compiling verified SWOT reports.",
    metric1Label: "Triangulation Consensus",
    metric1Sub: "Cross-Publisher Validation",
    metric2Label: "Primary Sources Ingested",
    metric2Sub: "SEC 10-K & Benchmarks",
    metric3Label: "Hallucination Rejection",
    metric3Sub: "Explicit Inline Citations",
    metric4Label: "Synthesis Latency",
    metric4Sub: "Instantaneous Dossier Build",
    studioTitle: "Autonomous Analyst Research Studio",
    studioDesc: "Submit market inquiry topics, inspect multi-source cross-reference checks, review SWOT matrices, and explore verified citations in real time.",
    lblPresets: "Select Research Topic:",
    lblQuery: "Research Inquiry Query",
    lblSector: "Industry Sector",
    lblDepth: "Research Depth",
    btnExecuteResearch: "⚡ Ingest Sources & Generate Report",
    titleDossier: "Executive Market Intelligence Dossier",
    lblExecutiveSummary: "Executive Summary & Thesis:",
    lblCitations: "Verifiable Citation Index:"
  },
  ar: {
    badgeTitle: "محلل السوق المستقل",
    statusLive: "المحلل الذكي نشط (:8011)",
    heroTitle: "معلومات السوق والأسهم المستقلة عبر تثليث البيانات متعددة المصادر",
    heroSubtitle: "توليد ملفات بحثية مؤسسية من خلال الاستخراج التلقائي لإفصاحات SEC، وتدقيق التباين الإحصائي، وتوليد تقارير SWOT الموثقة.",
    metric1Label: "التوافق الإحصائي المرجح",
    metric1Sub: "مطابقة متعددة المصادر",
    metric2Label: "المصادر الأولية المستخرجة",
    metric2Sub: "إفصاحات 10-K وبيانات السوق",
    metric3Label: "استبعاد الهلوسة",
    metric3Sub: "توثيق صريح للمراجع",
    metric4Label: "سرعة توليد التقرير",
    metric4Sub: "بناء فوري لملف التحليل",
    studioTitle: "استوديو أبحاث المحلل المستقل",
    studioDesc: "أرسل موضوع البحث، وراقب مطابقة البيانات وتثليثها، واطلع على مصفوفة SWOT والمراجع التوثيقية المعتمدة.",
    lblPresets: "اختر موضوع البحث:",
    lblQuery: "استعلام وموضوع البحث",
    lblSector: "القطاع المؤسسي",
    lblDepth: "عمق البحث",
    btnExecuteResearch: "⚡ استخراج المصادر وتوليد التقرير",
    titleDossier: "ملف التحليل الاستراتيجي ومعلومات السوق",
    lblExecutiveSummary: "الملخص التنفيذي وفرضية الاستثمار:",
    lblCitations: "فهرس المصادر والمراجع المعتمدة:"
  }
};

const SCENARIOS = [
  {
    name: "🤖 Enterprise Multi-Agent AI Market & Hyperscaler TAM",
    query: "Enterprise Autonomous Multi-Agent AI Market Growth & Cloud Hyperscaler Positioning",
    sector: "TECHNOLOGY",
    depth: "INSTITUTIONAL_DEEP_DIVE"
  },
  {
    name: "🧬 GLP-1 Metabolic Drug Market Expansion & Biosimilar Competition",
    query: "Global GLP-1 Receptor Agonists Market Expansion & Patent Expiry Biosimilar Dynamics",
    sector: "HEALTHCARE",
    depth: "INSTITUTIONAL_DEEP_DIVE"
  },
  {
    name: "⚡ Clean Energy Grid-Scale Battery Energy Storage (BESS)",
    query: "Grid-Scale Battery Energy Storage Systems (BESS) Capacity Buildout & LCOE Trajectory",
    sector: "ENERGY",
    depth: "COMPREHENSIVE_VALUATION"
  },
  {
    name: "💳 Real-Time Payments & Cross-Border B2B Settlement Rails",
    query: "ISO 20022 Cross-Border B2B Real-Time Settlement Market Growth & Treasury Optimization",
    sector: "FINANCIALS",
    depth: "INSTITUTIONAL_DEEP_DIVE"
  }
];

function init() {
  renderPresets();
  loadScenario(0);
}

function toggleLanguage() {
  currentLang = currentLang === 'en' ? 'ar' : 'en';
  document.documentElement.lang = currentLang;
  document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
  document.getElementById('langLabel').innerText = currentLang === 'en' ? 'العربية' : 'English';

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (TRANSLATIONS[currentLang][key]) {
      el.innerText = TRANSLATIONS[currentLang][key];
    }
  });
}

function renderPresets() {
  const container = document.getElementById('scenarioButtons');
  container.innerHTML = '';
  SCENARIOS.forEach((sc, idx) => {
    const btn = document.createElement('button');
    btn.className = 'preset-btn';
    btn.innerText = sc.name;
    btn.onclick = () => loadScenario(idx);
    container.appendChild(btn);
  });
}

function loadScenario(idx) {
  const sc = SCENARIOS[idx];
  document.getElementById('queryInput').value = sc.query;
  document.getElementById('sectorSelect').value = sc.sector;
  document.getElementById('depthSelect').value = sc.depth;
}

async function runResearchTask() {
  const btn = document.getElementById('researchBtn');
  const query = document.getElementById('queryInput').value.trim();
  const sector = document.getElementById('sectorSelect').value;
  const depth = document.getElementById('depthSelect').value;

  btn.disabled = true;
  btn.innerText = "Ingesting Primary Sources & Triangulating...";

  try {
    const res = await fetch('/api/v1/research/generate-report', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        topic_id: `RES-${Date.now()}`,
        query: query,
        sector: sector,
        depth: depth,
        time_horizon: "2026 - 2030"
      })
    });

    const report = await res.json();
    renderReport(report);

  } catch (err) {
    document.getElementById('summaryStream').innerText = `Error: ${err.message}`;
  } finally {
    btn.disabled = false;
    btn.innerText = TRANSLATIONS[currentLang].btnExecuteResearch;
  }
}

function renderReport(report) {
  const badge = document.getElementById('confidenceBadge');
  badge.className = 'badge badge-success';
  badge.innerText = `CONFIDENCE: ${intScore(report.overall_confidence_score)}%`;

  // Summary Stream
  document.getElementById('summaryStream').innerText = `${report.executive_summary}

**Investment Thesis:** ${report.investment_thesis}`;

  // Triangulation Tags
  const bar = document.getElementById('triangulationBar');
  bar.innerHTML = '';
  for (const [k, v] of Object.entries(report.metrics_matrix)) {
    const tag = document.createElement('span');
    tag.className = 'tri-tag';
    tag.innerText = `${k}: ${v}`;
    bar.appendChild(tag);
  }

  // Citations
  const list = document.getElementById('citationList');
  list.innerHTML = '';
  report.verifiable_citations.forEach(c => {
    const li = document.createElement('li');
    li.innerText = `${c.citation_id} ${c.source_title} (${c.publisher})`;
    list.appendChild(li);
  });
}

function intScore(score) {
  return Math.round(score * 100);
}

window.addEventListener('DOMContentLoaded', init);
