#!/usr/bin/env python3
import glob, re

# 1. Remove .top-bar from all HTML files
html_files = glob.glob("/home/ssvcharan/Antigravity/LaredoFire/*.html")

for filepath in html_files:
    with open(filepath) as f:
        content = f.read()
    
    # Remove <div class="top-bar">...</div>
    new_content = re.sub(r'\s*<!-- Top Announcement Bar -->\s*<div class="top-bar">.*?</div>\s*', '\n\n', content, flags=re.DOTALL)
    new_content = re.sub(r'<div class="top-bar">.*?</div>\s*', '', new_content, flags=re.DOTALL)
    
    with open(filepath, "w") as f:
        f.write(new_content)

print("Successfully removed top announcement bar from all HTML files!")

# 2. Update index.html with the redesigned, perfectly aligned Office & Contact Banner
with open("/home/ssvcharan/Antigravity/LaredoFire/index.html") as f:
    idx_content = f.read()

new_office_banner = '''            <!-- Redesigned Office & Support Banner -->
            <div class="office-contact-banner mt-5">
                <div class="office-card-item">
                    <div class="office-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                    </div>
                    <div class="office-details">
                        <span class="office-tag">SYSTEM OFFICE</span>
                        <p class="office-text">5219 Tesoro Plaza Dr.<br>Laredo, TX 78041</p>
                    </div>
                </div>

                <div class="office-card-item">
                    <div class="office-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                    </div>
                    <div class="office-details">
                        <span class="office-tag">OFFICE HOURS</span>
                        <p class="office-text">Mon &ndash; Fri: 8:00 AM &ndash; 5:00 PM<br><span class="text-muted-sm">Regular Business Hours</span></p>
                    </div>
                </div>

                <div class="office-card-item">
                    <div class="office-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                    </div>
                    <div class="office-details">
                        <span class="office-tag">TELEPHONE</span>
                        <p class="office-text"><a href="tel:956-717-8018" class="link-dark">956-717-8018</a><br><span class="text-muted-sm">Direct Line</span></p>
                    </div>
                </div>

                <div class="office-card-item">
                    <div class="office-icon">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                    </div>
                    <div class="office-details">
                        <span class="office-tag">PENSION ADMINISTRATOR</span>
                        <p class="office-text">Jaime Jasso<br><a href="mailto:JAIME.JASSO@LAREDOFIRE.COM" class="link-primary-sm">JAIME.JASSO@LAREDOFIRE.COM</a></p>
                    </div>
                </div>
            </div>'''

idx_content = re.sub(r'<div class="office-info-card">.*?</div>', new_office_banner, idx_content, flags=re.DOTALL)

with open("/home/ssvcharan/Antigravity/LaredoFire/index.html", "w") as f:
    f.write(idx_content)

print("Updated index.html with redesigned office contact banner!")
