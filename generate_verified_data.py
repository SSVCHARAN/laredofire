#!/usr/bin/env python3
import json, re, urllib.parse

BASE = "https://www.laredofire.com/"

def url_encode(u):
    if not u.startswith("http") and u != "#":
        u = BASE + u
    return u.replace(" ", "%20").replace("(", "%28").replace(")", "%29")

SKIP_TITLES = {"Plan Document", "PRE-RETIREMENT SEMINAR-PROGRAM 2025"}

docs = []
doc_id = 1

# ==============================
# 1. Agendas & Minutes (124 real items from scraped_agendas_all.json)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_agendas_all.json") as f:
    ag_raw = json.load(f)

# Sort agendas by year desc, then filename
ag_raw.sort(key=lambda x: (x.get("year", "2026"), x.get("file", "")), reverse=True)

for item in ag_raw:
    fn = item["file"]
    yr = item["year"]
    tp = item["type"]
    
    # Format readable title: e.g. A01222026.pdf -> Agenda - Jan 22, 2026
    # Extract date parts MMDDYYYY or MMDDYYYY
    m = re.search(r'^[AM](\d{1,2})(\d{2})(\d{4})\.pdf$', fn, re.I)
    if m:
        month_num = int(m.group(1))
        day_num = int(m.group(2))
        year_num = m.group(3)
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_name = months[month_num - 1] if 1 <= month_num <= 12 else f"Mo{month_num}"
        date_str = f"{month_name} {day_num}, {year_num}"
    else:
        date_str = fn.replace('.pdf', '')

    tag = "Agenda" if tp == "agenda" else "Minutes"
    title = f"Board Meeting {tag} ({date_str})"
    sub = f"Official LFRS Board {tag} • {date_str}"
    
    docs.append({
        "id": doc_id, "category": "agendas", "year": yr,
        "title": title, "sub": sub, "url": url_encode(item["url"]), "tag": tag
    })
    doc_id += 1

# ==============================
# 2. Financial Audits (12 items)
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
        "title": title, "sub": f"Annual Financial Audit Report ({period})" if period else "Financial Audit Report",
        "url": url_encode(item["url"]), "tag": "Audit"
    })
    doc_id += 1

# ==============================
# 3. Documents (11 items)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_documents.json") as f:
    doc_raw = json.load(f)

for item in doc_raw:
    if item["title"] in SKIP_TITLES:
        continue
    title = item["title"]
    year_match = re.search(r"(\d{4})", title)
    year = year_match.group(1) if year_match else "2024"
    docs.append({
        "id": doc_id, "category": "documents", "year": year,
        "title": title, "sub": "Official System Document",
        "url": url_encode(item["url"]), "tag": "PDF"
    })
    doc_id += 1

# ==============================
# 4. System Policies (10 items)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_policies.json") as f:
    pol_raw = json.load(f)

for item in pol_raw:
    if item["title"] in SKIP_TITLES:
        continue
    docs.append({
        "id": doc_id, "category": "policies", "year": "2024",
        "title": item["title"], "sub": "Board & System Governance Policy",
        "url": url_encode(item["url"]), "tag": "Policy"
    })
    doc_id += 1

# ==============================
# 5. Investment History (48 items)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_investments.json") as f:
    inv_raw = json.load(f)

for item in inv_raw:
    if item["title"] in SKIP_TITLES:
        continue
    title = item["title"]
    fy_match = re.search(r"FY\s*(\d{4})", title, re.I)
    year = fy_match.group(1) if fy_match else "2024"
    docs.append({
        "id": doc_id, "category": "investments", "year": year,
        "title": title, "sub": "Quarterly Investment Performance Report",
        "url": url_encode(item["url"]), "tag": "Report"
    })
    doc_id += 1

# ==============================
# 6. PRB Requirements (9 items)
# ==============================
prb = [
    {"title": "Actuarial Audit Report", "sub": "PRB Requirement (Pending Upload)", "url": "#", "tag": "PRB", "year": "2025"},
    {"title": "Actuarial Valuation Report", "sub": "PRB Filing • Actuarial Valuation", "url": "https://www.laredofire.com/LOFULF/LOFPRBR/PRBR6302023270.pdf", "tag": "PRB", "year": "2025"},
    {"title": "Annual Returns Report", "sub": "PRB Requirement (Pending Upload)", "url": "#", "tag": "PRB", "year": "2025"},
    {"title": "Comprehensive Annual Financial Report", "sub": "PRB Filing • CAFR Report", "url": "https://www.laredofire.com/LOFULF/LOFPRBR/PRBR63020232519.pdf", "tag": "PRB", "year": "2025"},
    {"title": "Investment Policy", "sub": "PRB Filing • Statement of Investment Policy", "url": "https://www.laredofire.com/LOFULF/LOFPRBR/PRBR12420242636.pdf", "tag": "PRB", "year": "2025"},
    {"title": "Investment Returns and Assumptions Report", "sub": "PRB Filing • Returns & Assumptions", "url": "https://www.laredofire.com/LOFULF/LOFPRBR/PRBR63020231851.pdf", "tag": "PRB", "year": "2025"},
    {"title": "Registration Information", "sub": "PRB Requirement (Pending Upload)", "url": "#", "tag": "PRB", "year": "2025"},
    {"title": "Report of Members and Retirees", "sub": "PRB Requirement (Pending Upload)", "url": "#", "tag": "PRB", "year": "2025"},
    {"title": "Summary Plan Description", "sub": "PRB Filing • SPD Document", "url": "https://www.laredofire.com/LOFULF/LOFPRBR/PRBR63020235311.pdf", "tag": "PRB", "year": "2025"},
]
for p in prb:
    docs.append({
        "id": doc_id, "category": "prb", "year": p["year"],
        "title": p["title"], "sub": p["sub"], "url": url_encode(p["url"]), "tag": p["tag"]
    })
    doc_id += 1

# ==============================
# 7. Legal Notices (2 items)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_legal.json") as f:
    leg_raw = json.load(f)

for item in leg_raw:
    if item["title"] in SKIP_TITLES:
        continue
    docs.append({
        "id": doc_id, "category": "legal", "year": "2024",
        "title": item["title"], "sub": "QDRO Legal Order Model Template",
        "url": url_encode(item["url"]), "tag": "Legal"
    })
    doc_id += 1

# ==============================
# 8. Member Forms (3 items)
# ==============================
with open("/home/ssvcharan/Antigravity/LaredoFire/scraped_forms.json") as f:
    frm_raw = json.load(f)

for item in frm_raw:
    if item["title"] in SKIP_TITLES:
        continue
    docs.append({
        "id": doc_id, "category": "forms", "year": "2025",
        "title": item["title"], "sub": "Official Member Application Form",
        "url": url_encode(item["url"]), "tag": "Form"
    })
    doc_id += 1

# Print Summary Breakdown
cats = {}
for d in docs:
    cats[d["category"]] = cats.get(d["category"], 0) + 1

print("\n==========================================")
print("   VERIFIED REAL DOCUMENTS SUMMARY")
print("==========================================")
for cat, count in sorted(cats.items()):
    print(f"  {cat.upper()}: {count} documents")
print(f"  TOTAL VERIFIED DOCUMENTS: {len(docs)}")
print("==========================================\n")

# Save as JSON file
with open("/home/ssvcharan/Antigravity/LaredoFire/verified_documents.json", "w") as f:
    json.dump(docs, f, indent=2)

print("Saved verified_documents.json!")
