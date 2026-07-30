#!/usr/bin/env python3
import glob, re

# 1. Update style.css
with open("/home/ssvcharan/Antigravity/LaredoFire/style.css") as f:
    css = f.read()

# Update .mobile-toggle span
css = css.replace(
    ".mobile-toggle span { display: block; width: 20px; height: 2px; background: #0F172A; border-radius: 2px; }",
    ".mobile-toggle span { display: block; width: 20px; height: 2px; background: #0F172A; border-radius: 2px; pointer-events: none; }"
)

# Replace .mobile-drawer rules with compact right-side drawer & backdrop
old_drawer_css = """.mobile-drawer { position: fixed; inset: 0; z-index: 2000; background: #FFF; padding: 24px; transform: translateX(100%); transition: transform 0.3s; }
.mobile-drawer.open { transform: translateX(0); }"""

new_drawer_css = """/* Mobile Drawer & Backdrop Overlay */
.mobile-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(4px);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
  z-index: 1999;
}
.mobile-backdrop.open {
  opacity: 1;
  visibility: visible;
}
.mobile-drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 320px;
  max-width: 85vw;
  z-index: 2000;
  background: #FFFFFF;
  padding: 24px;
  box-shadow: -8px 0 30px rgba(15, 23, 42, 0.15);
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
}
.mobile-drawer.open {
  transform: translateX(0);
}"""

if old_drawer_css in css:
    css = css.replace(old_drawer_css, new_drawer_css)
else:
    css += "\n" + new_drawer_css

with open("/home/ssvcharan/Antigravity/LaredoFire/style.css", "w") as f:
    f.write(css)

print("Updated style.css with compact right-side drawer & backdrop styles!")

# 2. Update main.js
main_js_content = """/**
 * Laredo Firefighters Retirement System - Mobile Menu & Drawer Script
 */

document.addEventListener('DOMContentLoaded', function () {
    const mobileToggle = document.getElementById('mobileToggle');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const mobileClose = document.getElementById('mobileClose');

    // Create backdrop element dynamically if not present
    let mobileBackdrop = document.getElementById('mobileBackdrop');
    if (!mobileBackdrop) {
        mobileBackdrop = document.createElement('div');
        mobileBackdrop.id = 'mobileBackdrop';
        mobileBackdrop.className = 'mobile-backdrop';
        document.body.appendChild(mobileBackdrop);
    }

    function openMenu(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        if (mobileDrawer) mobileDrawer.classList.add('open');
        if (mobileBackdrop) mobileBackdrop.classList.add('open');
        document.body.style.overflow = 'hidden';
    }

    function closeMenu(e) {
        if (e) {
            e.preventDefault();
            e.stopPropagation();
        }
        if (mobileDrawer) mobileDrawer.classList.remove('open');
        if (mobileBackdrop) mobileBackdrop.classList.remove('open');
        document.body.style.overflow = '';
    }

    if (mobileToggle) {
        mobileToggle.addEventListener('click', openMenu);
        mobileToggle.addEventListener('touchstart', openMenu, { passive: false });
    }

    if (mobileClose) {
        mobileClose.addEventListener('click', closeMenu);
        mobileClose.addEventListener('touchstart', closeMenu, { passive: false });
    }

    if (mobileBackdrop) {
        mobileBackdrop.addEventListener('click', closeMenu);
    }

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeMenu();
    });
});
"""

with open("/home/ssvcharan/Antigravity/LaredoFire/main.js", "w") as f:
    f.write(main_js_content)

print("Updated main.js with robust mobile drawer event handlers!")

# 3. Update all HTML files to include main.js and remove inline toggle duplicates
html_files = glob.glob("/home/ssvcharan/Antigravity/LaredoFire/*.html")

for filepath in html_files:
    with open(filepath) as f:
        html = f.read()

    # Remove inline mobileToggle event listeners if any
    html = re.sub(r"document\.getElementById\(['\"]mobileToggle['\"]\)\?\.\s*addEventListener.*?\n", "", html)
    html = re.sub(r"document\.getElementById\(['\"]mobileClose['\"]\)\?\.\s*addEventListener.*?\n", "", html)

    # Ensure <script src="main.js"></script> is present before </body>
    if 'src="main.js"' not in html:
        html = html.replace('</body>', '    <script src="main.js"></script>\n</body>')

    with open(filepath, "w") as f:
        f.write(html)

print("Added main.js script tag to all HTML files!")
