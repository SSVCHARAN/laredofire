/**
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
