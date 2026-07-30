#!/usr/bin/env python3
"""
Build the verified allDocuments JS array from scraped JSON data.
Only includes documents that actually exist on www.laredofire.com.
Skips nav-level links (Plan Document, Pre-Retirement Seminar that appear on every page).
"""
import json, re, urllib.parse

BASE = "https://www.laredofire.com/"

def full_url(u):
    u = u.strip()
    if u.startswith("http"):
        return u
    return BASE + u

def url_encode(u):
    """Encode spaces in URL for safe embedding in JS strings."""
    return u.replace(" ", "%20").replace("(", "%28").replace(")", "%29")

# Skip these nav-level links that appear on every page
SKIP_TITLES = {"Plan Document", "PRE-RETIREMENT SEMINAR-PROGRAM 2025"}

docs = []
doc_id = 1

# ==============================
# 1. PRB Requirements (9 items) - from HTML analysis of pub_PRBRequirements.aspx
# Grid positions mapped from the HTML source code analysis done earlier
# ==============================
prb = [
    # Grid pos 1 (PRBLogo1): Actuarial Audit Report - href="#" (no PDF uploaded)
    {"title": "Actuarial Audit Report", "sub": "PRB Filing (No PDF uploaded)", "url": "#", "tag": "PRB"},
    # Grid pos 2 (PRBLogo2): Actuarial Valuation Report
    {"title": "Actuarial Valuation Report", "sub": "PRB Filing", "url": full_url("LOFULF/LOFPRBR/PRBR6302023270.pdf"), "tag": "PRB"},
    # Grid pos 3 (PRBLogo3): Annual Returns - href="#" (no PDF uploaded)
    {"title": "Annual Returns", "sub": "PRB Filing (No PDF uploaded)", "url": "#", "tag": "PRB"},
    # Grid pos 4 (PRBLogo4): Comprehensive Annual Financial Report
    {"title": "Comprehensive Annual Financial Report", "sub": "PRB Filing", "url": full_url("LOFULF/LOFPRBR/PRBR63020232519.pdf"), "tag": "PRB"},
    # Grid pos 5 (PRBLogo5): Investment Policy
    {"title": "Investment Policy", "sub": "PRB Filing", "url": full_url("LOFULF/LOFPRBR/PRBR12420242636.pdf"), "tag": "PRB"},
    # Grid pos 6 (PRBLogo6): Investment Returns & Assumptions Report
    {"title": "Investment Returns and Assumptions Report", "sub": "PRB Filing", "url": full_url("LOFULF/LOFPRBR/PRBR63020231851.pdf"), "tag": "PRB"},
    # Grid pos 7 (PRBLogo7): Registration Information - href="#" (no PDF uploaded)
    {"title": "Registration Information", "sub": "PRB Filing (No PDF uploaded)", "url": "#", "tag": "PRB"},
    # Grid pos 8 (PRBLogo8): Report of Members & Retirees - href="#" (no PDF uploaded)
    {"title": "Report of Members and Retirees (Key Numbers)", "sub": "PRB Filing (No PDF uploaded)", "url": "#", "tag": "PRB"},
    # Grid pos 9 (PRBLogo9): Summary Plan Description
    {"title": "Summary Plan Description", "sub": "PRB Filing", "url": full_url("LOFULF/LOFPRBR/PRBR63020235311.pdf"), "tag": "PRB"},
]
for p in prb:
    docs.append({"id": doc_id, "category": "prb", "year": "2025", "title": p["title"], "sub": p["sub"], "url": url_encode(p["url"]), "tag": p["tag"]})
    doc_id += 1

# ==============================
# 2. Investment History (from scraped_investments.json)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_investments.json") as f:
    inv_raw = json.load(f)

for item in inv_raw:
    if item["title"] in SKIP_TITLES:
        continue
    title = item["title"]
    # Extract FY year from title
    fy_match = re.search(r"FY\s*(\d{4})", title)
    year = fy_match.group(1) if fy_match else "2024"
    docs.append({
        "id": doc_id, "category": "investments", "year": year,
        "title": title, "sub": "Quarterly Performance Report",
        "url": url_encode(full_url(item["url"])), "tag": "PDF"
    })
    doc_id += 1

# ==============================
# 3. Financial Audits (from scraped_financials.json)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_financials.json") as f:
    fin_raw = json.load(f)

for item in fin_raw:
    if item["title"] in SKIP_TITLES:
        continue
    title = item["title"]
    period = item.get("period", "")
    year_match = re.search(r"(\d{4})", period or title)
    year = year_match.group(1) if year_match else "2025"
    docs.append({
        "id": doc_id, "category": "financials", "year": year,
        "title": title, "sub": f"Period Ending {period}" if period else "Financial Audit",
        "url": url_encode(full_url(item["url"])), "tag": "Audit"
    })
    doc_id += 1

# ==============================
# 4. Policies (from scraped_policies.json)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_policies.json") as f:
    pol_raw = json.load(f)

for item in pol_raw:
    if item["title"] in SKIP_TITLES:
        continue
    docs.append({
        "id": doc_id, "category": "policies", "year": "2020",
        "title": item["title"], "sub": "System Governance Policy",
        "url": url_encode(full_url(item["url"])), "tag": "Policy"
    })
    doc_id += 1

# ==============================
# 5. Legal (from scraped_legal.json)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_legal.json") as f:
    leg_raw = json.load(f)

for item in leg_raw:
    if item["title"] in SKIP_TITLES:
        continue
    docs.append({
        "id": doc_id, "category": "legal", "year": "2018",
        "title": item["title"], "sub": "QDRO Legal Template",
        "url": url_encode(full_url(item["url"])), "tag": "Legal"
    })
    doc_id += 1

# ==============================
# 6. Forms (from scraped_forms.json)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_forms.json") as f:
    frm_raw = json.load(f)

for item in frm_raw:
    if item["title"] in SKIP_TITLES:
        continue
    docs.append({
        "id": doc_id, "category": "forms", "year": "2025",
        "title": item["title"], "sub": "Member Form",
        "url": url_encode(full_url(item["url"])), "tag": "Form"
    })
    doc_id += 1

# ==============================
# 7. Agendas (from scraped_agendas.json + we know years 2022-2026 exist)
# The scraper only got 2026 (default). For other years, we link to the
# Agendas archive page directly so users can select year.
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_agendas.json") as f:
    ag_raw = json.load(f)

for item in ag_raw:
    yr = item.get("year", "2026")
    tp = item.get("type", "agenda")
    docs.append({
        "id": doc_id, "category": "agendas", "year": yr,
        "title": item["title"], "sub": f"Board {tp.capitalize()} {yr}",
        "url": url_encode(full_url(item["url"])), "tag": tp.capitalize()
    })
    doc_id += 1

# Add archive links for other years
for yr in ["2025", "2024", "2023", "2022"]:
    docs.append({
        "id": doc_id, "category": "agendas", "year": yr,
        "title": f"{yr} Agendas & Minutes Archive",
        "sub": f"Full year board agendas and session minutes",
        "url": f"https://www.laredofire.com/Pub_Agendas.aspx?Type=1",
        "tag": "Archive"
    })
    doc_id += 1

# ==============================
# 8. Documents (Type=1) - we'll add known docs if scraped_documents.json exists
# ==============================
import os
doc_path = "/home/ssvcharan/Antigravity/LaredoFire/scraped_documents.json"
if os.path.exists(doc_path):
    with open(doc_path) as f:
        doc_raw = json.load(f)
    for item in doc_raw:
        if item["title"] in SKIP_TITLES:
            continue
        docs.append({
            "id": doc_id, "category": "documents", "year": "2023",
            "title": item["title"], "sub": "System Document",
            "url": url_encode(full_url(item["url"])), "tag": "PDF"
        })
        doc_id += 1
else:
    # Add the known documents from Type=1/Type=3 manually
    known_docs = [
        {"title": "LFRS Plan Document", "url": "https://www.laredofire.com/LOFULF/LOFDCS/LaredoJan12023-clean-01222026.pdf", "year": "2023", "sub": "Clean Copy Jan 1, 2023", "tag": "Plan"},
        {"title": "Actuarial Valuation 2024", "url": "https://www.laredofire.com/LOFULF/LOFDCS/2025.07.11_2024_Actuarial_Valuation-Laredo_Fire-corrected.pdf", "year": "2024", "sub": "Actuarial Valuation", "tag": "Valuation"},
        {"title": "Actuarial Valuation 2022", "url": "https://www.laredofire.com/LOFULF/LOFDCS/laredo-09-30-2022.pdf", "year": "2022", "sub": "Actuarial Valuation", "tag": "Valuation"},
        {"title": "Actuarial Valuation 2020", "url": "https://www.laredofire.com/LOFULF/LOFDCS/laredo-09-30-2020.pdf", "year": "2020", "sub": "Actuarial Valuation", "tag": "Valuation"},
        {"title": "Actuarial Valuation 2018", "url": "https://www.laredofire.com/LOFULF/LOFDCS/laredo-09-30-2018.pdf", "year": "2018", "sub": "Actuarial Valuation", "tag": "Valuation"},
        {"title": "Actuarial Valuation 2014", "url": "https://www.laredofire.com/LOFULF/LOFDCS/laredo-09-30-2014.pdf", "year": "2014", "sub": "Actuarial Valuation", "tag": "Valuation"},
        {"title": "Actuarial Valuation 2012", "url": "https://www.laredofire.com/LOFULF/LOFDCS/val-9-30-2012.pdf", "year": "2012", "sub": "Actuarial Valuation", "tag": "Valuation"},
    ]
    for kd in known_docs:
        docs.append({"id": doc_id, "category": "documents", "year": kd["year"], "title": kd["title"], "sub": kd["sub"], "url": url_encode(kd["url"]), "tag": kd["tag"]})
        doc_id += 1

# Summary
cats = {}
for d in docs:
    cats[d["category"]] = cats.get(d["category"], 0) + 1

print("=== VERIFIED DOCUMENT COUNT ===")
for cat, count in sorted(cats.items()):
    print(f"  {cat}: {count}")
print(f"  TOTAL: {len(docs)}")

# Write JS array
js_lines = ["const allDocuments = ["]
for d in docs:
    # Escape single quotes in titles
    t = d["title"].replace("'", "\\'").replace("&", "&amp;")
    s = d["sub"].replace("'", "\\'").replace("&", "&amp;")
    js_lines.append(f"    {{ id: {d['id']}, category: '{d['category']}', year: '{d['year']}', title: '{t}', sub: '{s}', url: '{d['url']}', tag: '{d['tag']}' }},")
js_lines.append("];")

js_output = "\n".join(js_lines)
with open("/home/ssvcharan/Antigravity/LaredoFire/verified_docs_array.js", "w") as f:
    f.write(js_output)

print("\nWrote verified_docs_array.js successfully!")
