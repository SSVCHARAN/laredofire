/**
 * Laredo Firefighters Retirement System - Mobile Navigation Drawer Handler
 * Ensures 100% reliable opening/closing on mobile touch and desktop click.
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

    function toggleMenu(show) {
        if (!mobileDrawer) return;
        const isOpen = show !== undefined ? show : !mobileDrawer.classList.contains('open');
        
        if (isOpen) {
            mobileDrawer.classList.add('open');
            mobileBackdrop.classList.add('open');
            document.body.style.overflow = 'hidden';
        } else {
            mobileDrawer.classList.remove('open');
            mobileBackdrop.classList.remove('open');
            document.body.style.overflow = '';
        }
    }

    // Ensure menu starts completely closed
    toggleMenu(false);

    if (mobileToggle) {
        mobileToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            toggleMenu(true);
        });
    }

    if (mobileClose) {
        mobileClose.addEventListener('click', function(e) {
            e.stopPropagation();
            toggleMenu(false);
        });
    }

    if (mobileBackdrop) {
        mobileBackdrop.addEventListener('click', function() {
            toggleMenu(false);
        });
    }

    // Close menu when clicking any link in mobile drawer
    document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.addEventListener('click', function() {
            toggleMenu(false);
        });
    });

    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') toggleMenu(false);
    });
});
