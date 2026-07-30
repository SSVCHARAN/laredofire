#!/usr/bin/env python3
import json, re

with open("/home/ssvcharan/Antigravity/LaredoFire/verified_documents.json") as f:
    docs = json.load(f)

js_docs = json.dumps(docs, indent=4)

with open("/home/ssvcharan/Antigravity/LaredoFire/documents.html") as f:
    html = f.read()

# Update Title / Header
html = re.sub(
    r'Public Records Repository \(.*?\)',
    f'Public Records Repository ({len(docs)} Official Documents)',
    html
)
html = re.sub(
    r'<h1>Public Records Repository.*?</h1>',
    f'<h1>Public Records Repository ({len(docs)} Official Documents)</h1>',
    html
)

# Initial HTML placeholder for yearFilterBar
year_filter_html = '''<div class="year-filter-bar" id="yearFilterBar">
                    <span class="year-filter-label">Filter by Year:</span>
                    <button class="btn-year active" onclick="selectYear('all', this)">All Years</button>
                </div>'''

html = re.sub(
    r'<div class="year-filter-bar".*?</div>',
    year_filter_html,
    html,
    flags=re.DOTALL
)

# Replace script block using string splitting
idx = html.find("const allDocuments =")
if idx != -1:
    start_idx = html.rfind("<script>", 0, idx)
else:
    script_marker = "<!-- Complete 271-Document Database Script -->"
    start_idx = html.find(script_marker)

end_idx = html.find("</body>")

new_script = f'''    <script>
        const allDocuments = {js_docs};

        let currentCategory = 'agendas';
        let currentYear = 'all';

        const categoryTitles = {{
            'agendas': 'AGENDAS AND MINUTES',
            'financials': 'FINANCIAL AUDITS',
            'documents': 'SYSTEM DOCUMENTS',
            'policies': 'SYSTEM POLICIES',
            'investments': 'INVESTMENT HISTORY',
            'prb': 'PRB REQUIREMENTS',
            'legal': 'LEGAL NOTICES & QDROS',
            'forms': 'MEMBER FORMS'
        }};

        function updateYearFilterBar() {{
            const bar = document.getElementById("yearFilterBar");
            if (!bar) return;

            const categoryDocs = allDocuments.filter(doc => doc.category === currentCategory);
            const availableYears = Array.from(new Set(
                categoryDocs.map(d => d.year).filter(y => y && /^\\d{{4}}$/.test(y))
            )).sort((a, b) => b - a);

            if (availableYears.length === 0) {{
                bar.style.display = 'none';
                return;
            }}
            bar.style.display = 'flex';

            let html = '<span class="year-filter-label">Filter by Year:</span>';
            html += `<button class="btn-year ${{currentYear === 'all' ? 'active' : ''}}" onclick="selectYear('all', this)">All Years (${{categoryDocs.length}})</button>`;
            
            availableYears.forEach(y => {{
                const count = categoryDocs.filter(d => d.year === y).length;
                const isActive = currentYear === y ? 'active' : '';
                html += `<button class="btn-year ${{isActive}}" onclick="selectYear('${{y}}', this)">${{y}} (${{count}})</button>`;
            }});

            bar.innerHTML = html;
        }}

        function selectCategory(cat, btn) {{
            currentCategory = cat;
            currentYear = 'all';

            document.querySelectorAll('.sidebar-btn').forEach(b => b.classList.remove('active'));
            if (!btn) {{
                btn = document.querySelector(`.sidebar-btn[data-cat="${{cat}}"]`);
            }}
            if (btn) btn.classList.add('active');

            const header = document.getElementById('categoryHeader');
            if (header && categoryTitles[cat]) {{
                header.textContent = categoryTitles[cat];
            }}

            updateYearFilterBar();
            renderGrid();
        }}

        function selectYear(yr, btn) {{
            currentYear = yr;
            updateYearFilterBar();
            renderGrid();
        }}

        function renderGrid() {{
            const grid = document.getElementById("docGrid");
            const searchInput = document.getElementById("docSearch");
            const query = searchInput ? searchInput.value.toLowerCase().trim() : "";

            if (!grid) return;

            const categoryDocs = allDocuments.filter(doc => doc.category === currentCategory);
            const filtered = categoryDocs.filter(doc => {{
                const matchesYear = (currentYear === "all" || doc.year === currentYear);
                const matchesQuery = (!query || doc.title.toLowerCase().includes(query) || doc.sub.toLowerCase().includes(query) || doc.year.includes(query));
                return matchesYear && matchesQuery;
            }});

            if (filtered.length === 0) {{
                grid.innerHTML = '<div style="grid-column: 1 / -1; padding: 40px; text-align: center; color: var(--text-muted); font-size: 0.95rem;">No documents found for this category and year filter.</div>';
                return;
            }}

            grid.innerHTML = filtered.map(doc => {{
                const isPending = doc.url === "#";
                const actionText = isPending ? "Pending Upload" : "Download PDF &rarr;";
                const actionClass = isPending ? "doc-action-tag pending" : "doc-action-tag";

                return `<a href="${{doc.url}}" ${{isPending ? '' : 'target="_blank" rel="noopener noreferrer"'}} class="doc-icon-card ${{isPending ? 'disabled' : ''}}">
                    <div class="pdf-icon-shape">${{doc.tag}}</div>
                    <div class="doc-icon-title">${{doc.title}}</div>
                    <div class="doc-icon-sub">${{doc.sub}} &bull; ${{doc.year}}</div>
                    <div class="${{actionClass}}">${{actionText}}</div>
                </a>`;
            }}).join("");
        }}

        document.addEventListener('DOMContentLoaded', function() {{
            const urlParams = new URLSearchParams(window.location.search);
            const catParam = urlParams.get('category');
            if (catParam && categoryTitles[catParam]) {{
                selectCategory(catParam, null);
            }} else {{
                selectCategory('agendas', null);
            }}

            document.getElementById('mobileToggle')?.addEventListener('click', function() {{
                document.getElementById('mobileDrawer')?.classList.add('open');
            }});
            document.getElementById('mobileClose')?.addEventListener('click', function() {{
                document.getElementById('mobileDrawer')?.classList.remove('open');
            }});
        }});
    </script>
'''

updated_html = html[:start_idx] + new_script + html[end_idx:]

with open("/home/ssvcharan/Antigravity/LaredoFire/documents.html", "w") as f:
    f.write(updated_html)

print("Successfully updated documents.html with dynamic year filter bar!")
