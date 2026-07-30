#!/usr/bin/env python3

with open("/home/ssvcharan/Antigravity/LaredoFire/style.css") as f:
    css = f.read()

idx = css.find("Clean Office Info Card")
if idx != -1:
    comment_start = css.rfind("/*", 0, idx)
    css_base = css[:comment_start]
else:
    css_base = css

new_css = '''/* Redesigned Office Contact Banner */
.office-contact-banner {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px 28px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.02);
}

.office-card-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
}

.office-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: #F1F5F9;
  color: var(--primary);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border: 1px solid #E2E8F0;
}

.office-details {
  display: flex;
  flex-direction: column;
}

.office-tag {
  font-family: var(--font-heading);
  font-size: 0.68rem;
  font-weight: 800;
  color: var(--text-muted);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.office-text {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--dark);
  line-height: 1.45;
}

.text-muted-sm {
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--text-muted);
}

.link-dark {
  color: var(--dark);
  text-decoration: none;
}

.link-dark:hover {
  color: var(--primary);
}

.link-primary-sm {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--primary);
  text-decoration: none;
  word-break: break-all;
}

.link-primary-sm:hover {
  text-decoration: underline;
}

@media (max-width: 1024px) {
  .office-contact-banner { grid-template-columns: repeat(2, 1fr); gap: 20px; }
}

@media (max-width: 600px) {
  .news-cards-grid { grid-template-columns: 1fr; }
  .office-contact-banner { grid-template-columns: 1fr; gap: 20px; }
}
'''

with open("/home/ssvcharan/Antigravity/LaredoFire/style.css", "w") as f:
    f.write(css_base + new_css)

print("Updated style.css with redesigned office contact banner styles!")
