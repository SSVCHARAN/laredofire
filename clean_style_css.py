#!/usr/bin/env python3

with open("/home/ssvcharan/Antigravity/LaredoFire/style.css") as f:
    css = f.read()

idx = css.find("ANNOUNCEMENTS & BOARD DISCLOSURES DASHBOARD")
if idx != -1:
    comment_start = css.rfind("/*", 0, idx)
    css_clean = css[:comment_start]
else:
    css_clean = css

clean_addition = '''/* --------------------------------------------------------------------------
   SYSTEM ANNOUNCEMENTS & DISCLOSURES
   -------------------------------------------------------------------------- */
.section-header-block {
  margin-bottom: 28px;
}

.news-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.news-card {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  transition: border-color 0.2s, box-shadow 0.2s;
}

.news-card:hover {
  border-color: var(--primary);
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
}

.news-category {
  font-family: var(--font-heading);
  font-size: 0.72rem;
  font-weight: 800;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 8px;
  display: block;
}

.news-card h3 {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--dark);
  margin-bottom: 8px;
  line-height: 1.3;
}

.news-card p {
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.55;
  margin-bottom: 20px;
}

.news-link {
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--primary);
  text-decoration: none;
  margin-top: auto;
}

.news-link:hover {
  text-decoration: underline;
}

/* Clean Office Info Card */
.office-info-card {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 24px;
  margin-top: 32px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  align-items: start;
}

.office-col {
  display: flex;
  flex-direction: column;
}

.office-label {
  font-family: var(--font-heading);
  font-size: 0.68rem;
  font-weight: 800;
  color: var(--text-muted);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.office-val {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--dark);
  line-height: 1.4;
}

.office-val a, .office-email {
  color: var(--primary);
  text-decoration: none;
  font-weight: 600;
}

.office-val a:hover, .office-email:hover {
  text-decoration: underline;
}

@media (max-width: 900px) {
  .news-cards-grid { grid-template-columns: 1fr; }
  .office-info-card { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 550px) {
  .office-info-card { grid-template-columns: 1fr; }
}
'''

with open("/home/ssvcharan/Antigravity/LaredoFire/style.css", "w") as f:
    f.write(css_clean + clean_addition)

print("Replaced style.css rules cleanly with zero AI slop!")
