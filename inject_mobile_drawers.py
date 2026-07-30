#!/usr/bin/env python3
import glob, re

drawer_html = '''
    <!-- Mobile Navigation Drawer -->
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
    </div>
'''

html_files = glob.glob("/home/ssvcharan/Antigravity/LaredoFire/*.html")

for filepath in html_files:
    if "login.html" in filepath:
        continue

    with open(filepath) as f:
        content = f.read()

    # If mobileDrawer is already present, remove it first to normalize
    content = re.sub(r'\s*<!-- Mobile Navigation Drawer -->\s*<div class="mobile-drawer" id="mobileDrawer">.*?</div>\s*', '\n', content, flags=re.DOTALL)
    content = re.sub(r'<div class="mobile-drawer" id="mobileDrawer">.*?</div>\s*', '', content, flags=re.DOTALL)

    # Insert mobileDrawer right after </header>
    if "</header>" in content:
        new_content = content.replace("</header>", "</header>\n" + drawer_html)
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Successfully injected mobileDrawer into {filepath}")

print("Mobile drawer injection complete for all pages!")
