/**
 * Laredo Firefighters Retirement System (LFRS)
 * Main JavaScript File: Navigation, Global Shortcuts, and Pension Calculator
 */

document.addEventListener('DOMContentLoaded', function () {
    // =========================================================================
    // 1. MOBILE NAVIGATION DRAWER & ACCESSIBILITY HANDLER
    // =========================================================================
    const mobileToggle = document.getElementById('mobileToggle');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const mobileClose = document.getElementById('mobileClose');
    let previouslyFocusedElement = null;

    let mobileBackdrop = document.getElementById('mobileBackdrop');
    if (!mobileBackdrop) {
        mobileBackdrop = document.createElement('div');
        mobileBackdrop.id = 'mobileBackdrop';
        mobileBackdrop.className = 'mobile-backdrop';
        mobileBackdrop.setAttribute('role', 'presentation');
        document.body.appendChild(mobileBackdrop);
    }

    if (mobileDrawer) {
        mobileDrawer.setAttribute('role', 'dialog');
        mobileDrawer.setAttribute('aria-modal', 'true');
        if (!mobileDrawer.hasAttribute('aria-label')) {
            mobileDrawer.setAttribute('aria-label', 'Mobile Navigation Menu');
        }
    }
    if (mobileClose && !mobileClose.hasAttribute('aria-label')) {
        mobileClose.setAttribute('aria-label', 'Close Navigation Menu');
    }

    function getFocusableElements(container) {
        if (!container) return [];
        return Array.from(container.querySelectorAll(
            'a[href], button:not([disabled]), input:not([disabled]), textarea:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])'
        )).filter(el => el.offsetWidth > 0 || el.offsetHeight > 0 || el === mobileClose);
    }

    function handleFocusTrap(e) {
        if (e.key !== 'Tab' || !mobileDrawer || !mobileDrawer.classList.contains('open')) return;

        const focusables = getFocusableElements(mobileDrawer);
        if (focusables.length === 0) return;

        const firstEl = focusables[0];
        const lastEl = focusables[focusables.length - 1];

        if (e.shiftKey) {
            if (document.activeElement === firstEl || !mobileDrawer.contains(document.activeElement)) {
                e.preventDefault();
                lastEl.focus();
            }
        } else {
            if (document.activeElement === lastEl || !mobileDrawer.contains(document.activeElement)) {
                e.preventDefault();
                firstEl.focus();
            }
        }
    }

    function toggleMenu(show) {
        if (!mobileDrawer) return;
        const isOpen = show !== undefined ? show : !mobileDrawer.classList.contains('open');

        if (isOpen) {
            previouslyFocusedElement = document.activeElement;
            mobileDrawer.classList.add('open');
            if (mobileBackdrop) mobileBackdrop.classList.add('open');
            document.body.style.overflow = 'hidden';

            const focusables = getFocusableElements(mobileDrawer);
            if (mobileClose) {
                mobileClose.focus();
            } else if (focusables.length > 0) {
                focusables[0].focus();
            }

            document.addEventListener('keydown', handleFocusTrap);
        } else {
            mobileDrawer.classList.remove('open');
            if (mobileBackdrop) mobileBackdrop.classList.remove('open');
            document.body.style.overflow = '';

            document.removeEventListener('keydown', handleFocusTrap);

            if (previouslyFocusedElement && typeof previouslyFocusedElement.focus === 'function') {
                previouslyFocusedElement.focus();
            }
        }
    }

    toggleMenu(false);

    if (mobileToggle) {
        mobileToggle.addEventListener('click', function (e) {
            e.stopPropagation();
            toggleMenu(true);
        });
    }

    if (mobileClose) {
        mobileClose.addEventListener('click', function (e) {
            e.stopPropagation();
            toggleMenu(false);
        });
    }

    if (mobileBackdrop) {
        mobileBackdrop.addEventListener('click', function () {
            toggleMenu(false);
        });
    }

    document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.addEventListener('click', function () {
            toggleMenu(false);
        });
    });

    // =========================================================================
    // 2. GLOBAL KEYBOARD SHORTCUTS
    // - '/' or 'Ctrl+K' / 'Cmd+K': Focus search bar immediately
    // - 'Esc': Close open drawers, modals, and unfocus inputs
    // =========================================================================
    function focusSearchBar() {
        const searchInput = document.getElementById('docSearch') ||
                            document.querySelector('input[data-search-input]') ||
                            document.querySelector('.search-box-clean input') ||
                            document.querySelector('input[type="search"]') ||
                            document.querySelector('input[placeholder*="Search"]');
        
        if (searchInput) {
            searchInput.focus();
            if (searchInput.value) {
                searchInput.select();
            }
            return true;
        } else {
            // Navigate to public records document search if on another page
            if (!window.location.pathname.includes('documents.html')) {
                window.location.href = 'documents.html?focus=search';
                return true;
            }
        }
        return false;
    }

    // Auto-focus search input if redirected via keyboard shortcut query param
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('focus') === 'search') {
        setTimeout(focusSearchBar, 100);
    }

    document.addEventListener('keydown', function (e) {
        const isEditable = e.target.matches('input, textarea, select, [contenteditable="true"]');

        // Esc Key: Close mobile drawers, modals, popovers
        if (e.key === 'Escape') {
            if (mobileDrawer && mobileDrawer.classList.contains('open')) {
                toggleMenu(false);
            }
            const openModals = document.querySelectorAll('.modal.open, .modal.active, [role="dialog"].open');
            openModals.forEach(m => m.classList.remove('open', 'active'));

            if (isEditable) {
                e.target.blur();
            }
            return;
        }

        // '/' or 'Ctrl+K' / 'Cmd+K': Focus Search Bar
        const isKCombination = (e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K');
        const isForwardSlash = e.key === '/' && !isEditable;

        if (isKCombination || isForwardSlash) {
            e.preventDefault();
            focusSearchBar();
        }
    });

    // Instant document search listener if docSearch input exists
    const docSearchInput = document.getElementById('docSearch');
    if (docSearchInput) {
        docSearchInput.addEventListener('input', function () {
            if (typeof renderGrid === 'function') {
                renderGrid();
            }
        });
    }

    // =========================================================================
    // 3. INTERACTIVE PENSION BENEFIT CALCULATOR LOGIC (TLFFRA RULES)
    // =========================================================================
    function initPensionCalculators() {
        const calcContainers = document.querySelectorAll('[data-pension-calculator]');
        if (!calcContainers || calcContainers.length === 0) return;

        calcContainers.forEach(container => {
            const yearsSlider = container.querySelector('#calcYearsService, #loginCalcYearsService, .js-calc-slider[min="10"]');
            const yearsNum = container.querySelector('#calcYearsServiceNum, #loginCalcYearsServiceNum, .js-calc-num[min="10"]');
            
            const salarySlider = container.querySelector('#calcSalary, #loginCalcSalary, .js-calc-slider[min="4000"]');
            const salaryNum = container.querySelector('#calcSalaryNum, #loginCalcSalaryNum, .js-calc-num[min="4000"]');
            
            const ageSlider = container.querySelector('#calcAge, #loginCalcAge, .js-calc-slider[min="50"]');
            const ageNum = container.querySelector('#calcAgeNum, #loginCalcAgeNum, .js-calc-num[min="50"]');

            function update() {
                let years = parseInt(yearsSlider ? yearsSlider.value : 20, 10);
                let salary = parseFloat(salarySlider ? salarySlider.value : 6500);
                let age = parseInt(ageSlider ? ageSlider.value : 55, 10);

                // Clamp inputs within bounds
                years = Math.max(10, Math.min(35, isNaN(years) ? 20 : years));
                salary = Math.max(4000, Math.min(12000, isNaN(salary) ? 6500 : salary));
                age = Math.max(50, Math.min(65, isNaN(age) ? 55 : age));

                // TLFFRA Pension Multiplier Math: 2.5% per year, max 75.0% (reached at 30 years)
                const rawMultiplier = years * 2.5;
                const cappedMultiplier = Math.min(rawMultiplier, 75.0);
                const monthlyAnnuity = salary * (cappedMultiplier / 100);
                const annualAnnuity = monthlyAnnuity * 12;

                // Multiplier Progress Bar relative to 75% cap
                const barWidthPercent = Math.min(100, (cappedMultiplier / 75.0) * 100);

                // Update text displays
                const yearsDisplay = container.querySelector('.js-years-display');
                if (yearsDisplay) yearsDisplay.textContent = years;

                const salaryDisplay = container.querySelector('.js-salary-display');
                if (salaryDisplay) salaryDisplay.textContent = '$' + salary.toLocaleString('en-US');

                const ageDisplay = container.querySelector('.js-age-display');
                if (ageDisplay) ageDisplay.textContent = age;

                const monthlyDisplay = container.querySelector('.js-monthly-display');
                if (monthlyDisplay) monthlyDisplay.textContent = '$' + monthlyAnnuity.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

                const annualDisplay = container.querySelector('.js-annual-display');
                if (annualDisplay) annualDisplay.textContent = '$' + annualAnnuity.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' estimated annual benefit';

                const multiplierDisplay = container.querySelector('.js-multiplier-display');
                if (multiplierDisplay) multiplierDisplay.textContent = cappedMultiplier.toFixed(1) + '%';

                const multiplierBar = container.querySelector('.js-multiplier-bar');
                if (multiplierBar) multiplierBar.style.width = barWidthPercent.toFixed(2) + '%';

                const capNote = container.querySelector('.js-cap-note');
                if (capNote) {
                    if (years >= 30) {
                        capNote.textContent = 'Maximum 75.0% cap reached at 30 years of credited service.';
                    } else {
                        capNote.textContent = '2.5% per year of service \u2022 Max 75.0% cap reached at 30 years';
                    }
                }

                const formulaEq = container.querySelector('.js-formula-equation');
                if (formulaEq) {
                    formulaEq.innerHTML = '$' + salary.toLocaleString('en-US') + ' (FAS) &times; ' + cappedMultiplier.toFixed(1) + '% (2.5% &times; ' + years + ' yrs) = <strong>$' + monthlyAnnuity.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' / month</strong>';
                }

                // Dynamic Eligibility Status Logic
                const statusBadge = container.querySelector('.js-status-badge');
                const statusMessage = container.querySelector('.js-status-message');
                const statusBanner = container.querySelector('.js-status-banner');

                if (statusBadge && statusMessage && statusBanner) {
                    statusBanner.className = 'eligibility-status-banner js-status-banner';

                    if (years >= 20 && age >= 50) {
                        statusBadge.textContent = 'NORMAL RETIREMENT ELIGIBLE';
                        statusBadge.className = 'status-badge status-normal js-status-badge';
                        statusBanner.classList.add('status-normal');
                        statusMessage.textContent = 'You meet both service (' + years + ' yrs \u2265 20) and age (' + age + ' \u2265 50) requirements for immediate Normal Retirement pension annuity under TLFFRA.';
                    } else if (years >= 20 && age < 50) {
                        statusBadge.textContent = 'EARLY RETIREMENT / DEFERRED';
                        statusBadge.className = 'status-badge status-early js-status-badge';
                        statusBanner.classList.add('status-early');
                        statusMessage.textContent = 'You meet the 20-year service milestone (' + years + ' yrs)! Full annuity commences at age 50 (in ' + (50 - age) + ' yrs), or you may elect early deferred benefit options.';
                    } else if (years >= 10) {
                        statusBadge.textContent = '100% VESTED DEFERRED ANNUITY';
                        statusBadge.className = 'status-badge status-vested js-status-badge';
                        statusBanner.classList.add('status-vested');
                        statusMessage.textContent = 'You are 100% vested in accrued pension benefits (' + years + ' yrs \u2265 10). Deferred monthly annuity will be payable upon reaching age 50.';
                    } else {
                        statusBadge.textContent = 'VESTING IN PROGRESS';
                        statusBadge.className = 'status-badge status-unvested js-status-badge';
                        statusBanner.classList.add('status-unvested');
                        statusMessage.textContent = 'Currently ' + years + ' years of credited service. 10 years of service required for 100% vested pension rights under TLFFRA.';
                    }
                }
            }

            // Sync Sliders & Number Inputs
            function bindPair(slider, num) {
                if (!slider || !num) return;
                slider.addEventListener('input', function () {
                    num.value = slider.value;
                    update();
                });
                num.addEventListener('input', function () {
                    slider.value = num.value;
                    update();
                });
                num.addEventListener('change', function () {
                    let val = parseFloat(num.value);
                    const min = parseFloat(num.min);
                    const max = parseFloat(num.max);
                    if (isNaN(val)) val = min;
                    if (val < min) val = min;
                    if (val > max) val = max;
                    num.value = val;
                    slider.value = val;
                    update();
                });
            }

            bindPair(yearsSlider, yearsNum);
            bindPair(salarySlider, salaryNum);
            bindPair(ageSlider, ageNum);

            // Stepper buttons handler
            container.querySelectorAll('.js-stepper').forEach(btn => {
                btn.addEventListener('click', function () {
                    const targetId = btn.getAttribute('data-target');
                    const delta = parseInt(btn.getAttribute('data-delta'), 10);
                    const targetInput = container.querySelector('#' + targetId) || container.querySelector('input.js-calc-slider');
                    const targetNum = container.querySelector('#' + targetId + 'Num') || container.querySelector('input.js-calc-num');

                    if (targetInput && !isNaN(delta)) {
                        let currentVal = parseFloat(targetInput.value);
                        let newVal = currentVal + delta;
                        const min = parseFloat(targetInput.min);
                        const max = parseFloat(targetInput.max);
                        if (newVal < min) newVal = min;
                        if (newVal > max) newVal = max;

                        targetInput.value = newVal;
                        if (targetNum) targetNum.value = newVal;
                        update();
                    }
                });
            });

            // Preset scenarios handler
            container.querySelectorAll('.calc-preset-btn').forEach(presetBtn => {
                presetBtn.addEventListener('click', function () {
                    const presetYears = presetBtn.getAttribute('data-years');
                    const presetSalary = presetBtn.getAttribute('data-salary');
                    const presetAge = presetBtn.getAttribute('data-age');

                    if (yearsSlider) yearsSlider.value = presetYears;
                    if (yearsNum) yearsNum.value = presetYears;

                    if (salarySlider) salarySlider.value = presetSalary;
                    if (salaryNum) salaryNum.value = presetSalary;

                    if (ageSlider) ageSlider.value = presetAge;
                    if (ageNum) ageNum.value = presetAge;

                    container.querySelectorAll('.calc-preset-btn').forEach(b => b.classList.remove('active'));
                    presetBtn.classList.add('active');

                    update();
                });
            });

            // Initial calculation run
            update();
        });
    }

    initPensionCalculators();
});
