#!/usr/bin/env python3

index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laredo Firefighters Retirement System | Home</title>
    <meta name="description" content="Official website of the Laredo Firefighters Retirement System. Provides pension benefit administration, financial stewardship, public disclosures, and member resources.">
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

    <!-- Announcements & Board Disclosures Section -->
    <main class="home-section">
        <div class="container">
            <div class="dashboard-header-clean">
                <div>
                    <h2 class="section-title-clean">Announcements & Board Disclosures</h2>
                    <p class="section-desc-clean">Official board notices, member program announcements, and system compliance updates.</p>
                </div>
                <div class="live-status-pill">
                    <span class="pulse-dot"></span> System Operational & PRB Compliant
                </div>
            </div>

            <!-- Announcements Grid -->
            <div class="announcement-grid">
                
                <!-- Announcement 1: Pre-Retirement Seminar -->
                <div class="announcement-card featured-gold">
                    <div class="card-badge-row">
                        <span class="badge-tag gold">MEMBER PROGRAM</span>
                        <span class="badge-date">2025 EDITION</span>
                    </div>
                    <h3>Pre-Retirement Seminar Program 2025</h3>
                    <p>Comprehensive retirement preparation guide covering benefit options, PLOP elections, survivor annuities, and healthcare transition for Laredo firefighters.</p>
                    <div class="card-footer-action">
                        <a href="https://www.laredofire.com/LOFULF/LOFDCS/LAREDOFIREFIGHTERSPRERETIREMENTSEMINARPROGRAM2025.pdf" target="_blank" rel="noopener noreferrer" class="btn-card-action">Download Program PDF &rarr;</a>
                    </div>
                </div>

                <!-- Announcement 2: Latest Board Meeting Notices -->
                <div class="announcement-card">
                    <div class="card-badge-row">
                        <span class="badge-tag crimson">BOARD GOVERNANCE</span>
                        <span class="badge-date">2026 RECORDS</span>
                    </div>
                    <h3>Board Meeting Agendas & Session Minutes</h3>
                    <p>Access official published notices, meeting agendas, and approved session minutes for all 2026 board meetings (June 30, June 24, May 28, etc.).</p>
                    <div class="card-footer-action">
                        <a href="documents.html?category=agendas" class="btn-card-action">View All 124 Agendas & Minutes &rarr;</a>
                    </div>
                </div>

                <!-- Announcement 3: State PRB Compliance -->
                <div class="announcement-card">
                    <div class="card-badge-row">
                        <span class="badge-tag navy">STATE DISCLOSURES</span>
                        <span class="badge-date">PRB COMPLIANT</span>
                    </div>
                    <h3>Annual Actuarial & Financial Disclosures</h3>
                    <p>Full disclosures filed with the Texas Pension Review Board (PRB), including CAFR reports, actuarial valuations, and investment return assumptions.</p>
                    <div class="card-footer-action">
                        <a href="documents.html?category=prb" class="btn-card-action">View PRB Filings & Reports &rarr;</a>
                    </div>
                </div>

                <!-- Announcement 4: PensionEZ Portal -->
                <div class="announcement-card">
                    <div class="card-badge-row">
                        <span class="badge-tag slate">ONLINE PORTAL</span>
                        <span class="badge-date">MEMBER ACCESS</span>
                    </div>
                    <h3>PensionEZ Benefit Portal Registration</h3>
                    <p>Secure online portal for active members and retirees to review benefit statement history, track service credit years, and update profile preferences.</p>
                    <div class="card-footer-action">
                        <a href="login.html" class="btn-card-action">Access PensionEZ Portal &rarr;</a>
                    </div>
                </div>

            </div>

            <!-- System Metrics & Support Bar -->
            <div class="system-status-bar mt-5">
                <div class="status-col">
                    <span class="status-num">124</span>
                    <span class="status-lbl">Board Agendas & Minutes</span>
                </div>
                <div class="status-col">
                    <span class="status-num">100%</span>
                    <span class="status-lbl">PRB Reporting Compliance</span>
                </div>
                <div class="status-col">
                    <span class="status-num">FY2025</span>
                    <span class="status-lbl">Financial Audit Complete</span>
                </div>
                <div class="status-col contact-quick">
                    <span class="contact-lbl">PENSION ADMINISTRATOR</span>
                    <span class="contact-name">Jaime Jasso</span>
                    <a href="tel:956-717-8018" class="contact-phone">📞 956-717-8018</a>
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

print("Updated index.html with Announcements & Board Disclosures Dashboard!")
