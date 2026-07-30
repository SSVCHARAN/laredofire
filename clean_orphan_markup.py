#!/usr/bin/env python3
import glob, re

html_files = glob.glob("/home/ssvcharan/Antigravity/LaredoFire/*.html")

for filepath in html_files:
    with open(filepath) as f:
        content = f.read()

    # Find strictly the valid mobile drawer
    clean_drawer = '''    <!-- Mobile Navigation Drawer -->
    <div class="mobile-drawer" id="mobileDrawer">
        <div class="mobile-drawer-header">
            <div class="brand-text">
                <span class="brand-name">LAREDO FIREFIGHTERS</span>
                <span class="brand-sub">RETIREMENT SYSTEM</span>
            </div>
            <button class="mobile-close" id="mobileClose">&times;</button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="index.html" class="mobile-nav-link">Home</a></li>
            <li><a href="plan-document.html" class="mobile-nav-link">Plan Document</a></li>
            <li><a href="documents.html" class="mobile-nav-link">Public Records & Audits</a></li>
            <li><a href="trustees.html" class="mobile-nav-link">Trustees & Staff</a></li>
            <li><a href="mission.html" class="mobile-nav-link">Mission Statement</a></li>
            <li><a href="contact.html" class="mobile-nav-link">Contact Us</a></li>
            <li><a href="login.html" class="mobile-nav-link">PensionEZ Portal Login</a></li>
        </ul>
    </div>'''

    # Remove all drawer variations / duplicate fragments
    content = re.sub(r'<button class="mobile-close".*?</ul>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Mobile Navigation Drawer -->.*?(?=<section|<main)', '', content, flags=re.DOTALL)

    # Re-insert clean single drawer right after </header>
    if "</header>" in content and "login.html" not in filepath:
        content = content.replace("</header>", "</header>\n" + clean_drawer)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"Cleaned orphan markup from {filepath}")

print("Cleaned up all duplicate orphan HTML markup across all pages!")
