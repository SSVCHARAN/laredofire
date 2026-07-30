#!/usr/bin/env python3

index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laredo Firefighters Retirement System | Home</title>
    <meta name="description" content="Official website of the Laredo Firefighters Retirement System. Providing pension benefit administration, financial stewardship, public disclosures, and member resources.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Top Announcement Bar -->
    <div class="top-bar">
        <div class="container top-bar-content">
            <div class="top-bar-left">
                <span class="badge-live">NOTICE</span>
                <span class="top-bar-text">Pre-Retirement Seminar Program 2025 document is available.</span>
                <a href="https://www.laredofire.com/LOFULF/LOFDCS/LAREDOFIREFIGHTERSPRERETIREMENTSEMINARPROGRAM2025.pdf" target="_blank" rel="noopener noreferrer" class="top-bar-link">Download PDF &rarr;</a>
            </div>
            <div class="top-bar-right">
                <a href="tel:956-717-8018" class="contact-pill">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                    956-717-8018
                </a>
                <a href="login.html" class="btn-sm-gold">PensionEZ Portal Login</a>
            </div>
        </div>
    </div>

    <!-- Header Navigation -->
    <header class="site-header">
        <div class="container header-container">
            <a href="index.html" class="brand-logo">
                <div class="logo-badge">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L3 9v11a2 2 0 0 1-2 2h14a2 2 0 0 1-2-2V9l-9-7z"/><path d="M12 7v7"/><path d="M9 11h6"/></svg>
                </div>
                <div class="brand-text">
                    <span class="brand-name">LAREDO FIREFIGHTERS</span>
                    <span class="brand-sub">RETIREMENT SYSTEM</span>
                </div>
            </a>

            <nav class="main-nav">
                <ul class="nav-list">
                    <li><a href="index.html" class="nav-link active">Home</a></li>
                    <li><a href="plan-document.html" class="nav-link">Plan Document</a></li>
                    <li><a href="documents.html" class="nav-link">Public Records</a></li>
                    <li><a href="trustees.html" class="nav-link">Trustees & Staff</a></li>
                    <li><a href="mission.html" class="nav-link">Mission</a></li>
                    <li><a href="contact.html" class="nav-link">Contact Us</a></li>
                </ul>
            </nav>

            <a href="login.html" class="btn-primary">PensionEZ Login</a>

            <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle Menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

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

    <!-- Hero Showcase Section -->
    <section class="hero-simple">
        <div class="container hero-simple-content">
            <span class="hero-simple-tag">PUBLIC PENSION FUND SYSTEM</span>
            <h1>Laredo Firefighters Retirement System</h1>
            <p>Providing pension benefit administration, financial stewardship, and official plan disclosures for Laredo Fire Department personnel and retirees.</p>
            <div class="hero-actions">
                <a href="documents.html" class="btn-hero-primary">Browse Public Records &rarr;</a>
                <a href="plan-document.html" class="btn-hero-secondary">View Plan Document</a>
            </div>
        </div>
    </section>

    <!-- Announcements & Public Disclosures Section -->
    <main class="home-section">
        <div class="container">
            <div class="section-header-block">
                <h2 class="section-title-clean">System Announcements & Disclosures</h2>
                <p class="section-desc-clean">Official board meeting notices, annual financial filings, and member resources for the Laredo Firefighters Retirement System.</p>
            </div>

            <!-- News & Resources Cards -->
            <div class="news-cards-grid">
                
                <div class="news-card">
                    <span class="news-category">Notice</span>
                    <h3>2025 Pre-Retirement Seminar Program</h3>
                    <p>Information guide and presentation schedule for active department members approaching retirement eligibility.</p>
                    <a href="https://www.laredofire.com/LOFULF/LOFDCS/LAREDOFIREFIGHTERSPRERETIREMENTSEMINARPROGRAM2025.pdf" target="_blank" rel="noopener noreferrer" class="news-link">Download Program Guide (PDF) &rarr;</a>
                </div>

                <div class="news-card">
                    <span class="news-category">Board Governance</span>
                    <h3>Board Meeting Agendas & Minutes</h3>
                    <p>Published agendas, official meeting notices, and approved session minutes from Board of Trustees meetings.</p>
                    <a href="documents.html?category=agendas" class="news-link">View Agendas & Minutes &rarr;</a>
                </div>

                <div class="news-card">
                    <span class="news-category">Public Disclosure</span>
                    <h3>Texas Pension Review Board Disclosures</h3>
                    <p>Annual actuarial valuations, financial audit reports, and investment policy statements submitted to the State of Texas.</p>
                    <a href="documents.html?category=prb" class="news-link">View PRB Filings &rarr;</a>
                </div>

                <div class="news-card">
                    <span class="news-category">Member Services</span>
                    <h3>PensionEZ Member Portal Access</h3>
                    <p>Log in to view your pension service credit, request beneficiary updates, or contact system administration.</p>
                    <a href="login.html" class="news-link">Log In to PensionEZ &rarr;</a>
                </div>

            </div>

            <!-- Clean Office & Support Card -->
            <div class="office-info-card">
                <div class="office-col">
                    <span class="office-label">SYSTEM OFFICE LOCATION</span>
                    <p class="office-val">5219 Tesoro Plaza Dr.<br>Laredo, TX 78041</p>
                </div>
                <div class="office-col">
                    <span class="office-label">OFFICE HOURS</span>
                    <p class="office-val">Monday &ndash; Friday<br>8:00 AM &ndash; 5:00 PM</p>
                </div>
                <div class="office-col">
                    <span class="office-label">TELEPHONE</span>
                    <p class="office-val"><a href="tel:956-717-8018">956-717-8018</a></p>
                </div>
                <div class="office-col">
                    <span class="office-label">PENSION ADMINISTRATOR</span>
                    <p class="office-val">Jaime Jasso</p>
                    <a href="mailto:JAIME.JASSO@LAREDOFIRE.COM" class="office-email">JAIME.JASSO@LAREDOFIRE.COM</a>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="site-footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <h4>Laredo Firefighters Retirement System</h4>
                <p>Public retirement system providing benefit administration and financial stewardship for Laredo firefighters.</p>
            </div>
            <div class="footer-col">
                <h5>Navigation</h5>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="plan-document.html">Plan Document</a></li>
                    <li><a href="documents.html">Public Records</a></li>
                    <li><a href="trustees.html">Board of Trustees</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h5>Document Quick Links</h5>
                <ul>
                    <li><a href="documents.html?category=agendas">Agendas & Minutes</a></li>
                    <li><a href="documents.html?category=financials">Financial Audits</a></li>
                    <li><a href="documents.html?category=legal">QDRO Model Orders</a></li>
                    <li><a href="documents.html?category=forms">Beneficiary Forms</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h5>Office Contact</h5>
                <p style="font-size: 0.85rem;">5219 Tesoro Plaza Dr.<br>Laredo, TX 78041<br>Phone: 956-717-8018</p>
            </div>
        </div>
        <div class="footer-bottom-text">
            <p>&copy; 2026 Laredo Firefighters Retirement System. All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        document.getElementById('mobileToggle')?.addEventListener('click', function() {
            document.getElementById('mobileDrawer')?.classList.add('open');
        });
        document.getElementById('mobileClose')?.addEventListener('click', function() {
            document.getElementById('mobileDrawer')?.classList.remove('open');
        });
    </script>
</body>
</html>
'''

with open("/home/ssvcharan/Antigravity/LaredoFire/index.html", "w") as f:
    f.write(index_html)

print("Re-written index.html cleanly without any AI slop status pills!")
