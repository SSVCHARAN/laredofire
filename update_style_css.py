#!/usr/bin/env python3

css_addition = '''

/* --------------------------------------------------------------------------
   ANNOUNCEMENTS & BOARD DISCLOSURES DASHBOARD
   -------------------------------------------------------------------------- */
.dashboard-header-clean {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 24px;
}

.live-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #F1F5F9;
  border: 1px solid var(--border);
  color: var(--dark);
  font-family: var(--font-heading);
  font-size: 0.8rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 20px;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4);
  animation: pulseGreen 2s infinite;
}

@keyframes pulseGreen {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.announcement-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.announcement-card {
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.02);
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}

.announcement-card:hover {
  transform: translateY(-2px);
  border-color: var(--primary);
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
}

.announcement-card.featured-gold {
  border-left: 4px solid var(--accent);
  background: linear-gradient(135deg, #FFFFFF 0%, #FFFDF5 100%);
}

.card-badge-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.badge-tag {
  font-family: var(--font-heading);
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  padding: 3px 8px;
  border-radius: 4px;
  text-transform: uppercase;
}

.badge-tag.gold { background: rgba(245, 158, 11, 0.12); color: #B45309; }
.badge-tag.crimson { background: rgba(158, 27, 27, 0.1); color: var(--primary); }
.badge-tag.navy { background: rgba(15, 23, 42, 0.08); color: var(--dark); }
.badge-tag.slate { background: rgba(100, 116, 139, 0.12); color: #475569; }

.badge-date {
  font-family: var(--font-heading);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text-muted);
}

.announcement-card h3 {
  font-family: var(--font-heading);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--dark);
  margin-bottom: 8px;
  line-height: 1.3;
}

.announcement-card p {
  font-size: 0.88rem;
  color: var(--text-muted);
  line-height: 1.55;
  margin-bottom: 20px;
}

.card-footer-action {
  margin-top: auto;
}

.btn-card-action {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-heading);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--primary);
  text-decoration: none;
  transition: gap 0.2s;
}

.btn-card-action:hover {
  gap: 10px;
  color: var(--primary-dark);
}

/* System Status Bar */
.system-status-bar {
  background: var(--dark);
  color: #FFFFFF;
  border-radius: 12px;
  padding: 24px 32px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  align-items: center;
  border-top: 3px solid var(--accent);
}

.status-col {
  display: flex;
  flex-direction: column;
}

.status-num {
  font-family: var(--font-heading);
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
  margin-bottom: 4px;
}

.status-lbl {
  font-size: 0.8rem;
  color: #94A3B8;
  font-weight: 500;
}

.status-col.contact-quick {
  border-left: 1px solid rgba(255, 255, 255, 0.12);
  padding-left: 20px;
}

.contact-lbl {
  font-family: var(--font-heading);
  font-size: 0.68rem;
  font-weight: 800;
  color: var(--accent);
  letter-spacing: 0.06em;
}

.contact-name {
  font-family: var(--font-heading);
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFFFFF;
  margin: 2px 0;
}

.contact-phone {
  color: #CBD5E1;
  font-size: 0.85rem;
  text-decoration: none;
  font-weight: 600;
}

.contact-phone:hover {
  color: var(--accent);
}

@media (max-width: 900px) {
  .announcement-grid { grid-template-columns: 1fr; }
  .system-status-bar { grid-template-columns: repeat(2, 1fr); }
  .status-col.contact-quick { border-left: none; padding-left: 0; border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: 16px; }
}

@media (max-width: 600px) {
  .system-status-bar { grid-template-columns: 1fr; }
}
'''

with open("/home/ssvcharan/Antigravity/LaredoFire/style.css", "a") as f:
    f.write(css_addition)

print("Appended dashboard CSS rules to style.css!")
