#!/usr/bin/env python3

# 1. Update style.css
with open("/home/ssvcharan/Antigravity/LaredoFire/style.css") as f:
    css = f.read()

# Replace .page-header background
css = css.replace(
    "url('https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1600&q=80')",
    "url('images/hero1.jpg')"
)

with open("/home/ssvcharan/Antigravity/LaredoFire/style.css", "w") as f:
    f.write(css)

print("Updated style.css to point to local generated firefighter images!")

# 2. Update mission.html
with open("/home/ssvcharan/Antigravity/LaredoFire/mission.html") as f:
    m_html = f.read()

m_html = m_html.replace(
    "url('https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?auto=format&fit=crop&w=1600&q=80')",
    "url('images/mission_gear.jpg')"
)

with open("/home/ssvcharan/Antigravity/LaredoFire/mission.html", "w") as f:
    f.write(m_html)

print("Updated mission.html to point to local generated mission gear image!")
