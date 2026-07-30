/**
 * Laredo Firefighters Retirement System - Multi-Page Navigation JavaScript
 */

document.addEventListener('DOMContentLoaded', function () {
    const mobileToggle = document.getElementById('mobileToggle');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const mobileClose = document.getElementById('mobileClose');

    if (mobileToggle && mobileDrawer) {
        mobileToggle.addEventListener('click', function () {
            mobileDrawer.classList.add('open');
        });
    }

    if (mobileClose && mobileDrawer) {
        mobileClose.addEventListener('click', function () {
            mobileDrawer.classList.remove('open');
        });
    }
});
