/* Property Management Web App - Client-side JavaScript */
/* Sprint 2: Editor, auto-save, dirty flag, beforeunload warning */
/* Sprint 3: Dashboard widget toggles, search */
/* Sprint 4: PWA install prompt, service worker registration */

let autoSaveTimer = null;
let isDirty = false;
let originalContent = '';
const AUTO_SAVE_DELAY = 2000;

/* ================================================================
   Editor
   ================================================================ */

function initEditor() {
    const textarea = document.getElementById('editor-textarea');
    if (!textarea) return;

    const saveBtn = document.getElementById('save-btn');
    const cancelBtn = document.getElementById('cancel-btn');
    const autoSaveToggle = document.getElementById('auto-save-toggle');
    const saveStatus = document.getElementById('save-status');
    const filePath = textarea.dataset.filePath;

    originalContent = textarea.value;

    // Track changes
    textarea.addEventListener('input', () => {
        isDirty = textarea.value !== originalContent;
        saveBtn.disabled = !isDirty;

        // Auto-save
        if (autoSaveToggle && autoSaveToggle.checked && isDirty) {
            clearTimeout(autoSaveTimer);
            autoSaveTimer = setTimeout(() => {
                doSave(textarea, filePath, saveStatus, saveBtn);
            }, AUTO_SAVE_DELAY);
        }
    });

    // Manual save
    saveBtn.addEventListener('click', (e) => {
        e.preventDefault();
        clearTimeout(autoSaveTimer);
        doSave(textarea, filePath, saveStatus, saveBtn);
    });

    // Cancel
    cancelBtn.addEventListener('click', (e) => {
        e.preventDefault();
        if (isDirty) {
            if (!confirm('You have unsaved changes. Discard them?')) {
                return;
            }
        }
        isDirty = false; // Allow navigation without beforeunload warning
        window.location.href = '/file/' + filePath;
    });

    // Auto-save toggle change
    if (autoSaveToggle) {
        autoSaveToggle.addEventListener('change', () => {
            if (!autoSaveToggle.checked) {
                clearTimeout(autoSaveTimer);
            }
        });
    }

    // Keyboard shortcut: Ctrl/Cmd+S to save
    textarea.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 's') {
            e.preventDefault();
            if (isDirty) {
                clearTimeout(autoSaveTimer);
                doSave(textarea, filePath, saveStatus, saveBtn);
            }
        }
    });
}

function doSave(textarea, filePath, saveStatus, saveBtn) {
    saveStatus.textContent = 'Saving...';
    saveBtn.disabled = true;

    const formData = new FormData();
    formData.append('content', textarea.value);

    fetch('/api/file/' + filePath, {
        method: 'PUT',
        body: formData,
    })
    .then(r => r.text())
    .then(html => {
        // Insert the toast HTML into save-status area
        saveStatus.innerHTML = html;
        originalContent = textarea.value;
        isDirty = false;
        saveBtn.disabled = true;

        // Also show a positioned toast notification
        const toastContainer = document.getElementById('toast-container');
        if (toastContainer) {
            toastContainer.innerHTML = html;
        }

        // Auto-hide toast after 3 seconds
        setTimeout(() => {
            const toast = document.getElementById('toast');
            if (toast) toast.remove();
            // Clear status text but keep it subtle
            saveStatus.innerHTML = '<span style="color: var(--color-success);">Saved</span>';
            setTimeout(() => {
                if (!isDirty) {
                    saveStatus.textContent = '';
                }
            }, 2000);
        }, 3000);
    })
    .catch(err => {
        saveStatus.innerHTML = '<span class="text-error">Save failed</span>';
        saveBtn.disabled = false;
    });
}

// Warn before leaving page with unsaved changes
window.addEventListener('beforeunload', (e) => {
    if (isDirty) {
        e.preventDefault();
        e.returnValue = '';
    }
});

// Also warn on HTMX navigation (sidebar clicks while editing)
document.addEventListener('htmx:beforeRequest', (e) => {
    if (isDirty && e.detail.target && e.detail.target.id === 'main') {
        if (!confirm('You have unsaved changes. Discard them?')) {
            e.preventDefault();
        } else {
            isDirty = false; // Allow navigation
        }
    }
});

// Re-initialize editor after HTMX swaps (in case editor is loaded via HTMX)
document.addEventListener('htmx:afterSettle', () => {
    initEditor();
    initDashboard();
});

/* ================================================================
   Dashboard Widget Toggles
   ================================================================ */

function initDashboard() {
    const widgets = ['open-tasks', 'recent-files', 'pinned-files', 'property-cards'];
    widgets.forEach(id => {
        const hidden = localStorage.getItem('widget-' + id + '-hidden') === 'true';
        const el = document.getElementById('widget-' + id);
        const btn = document.querySelector('[data-widget="' + id + '"]');
        if (hidden && el) {
            el.style.display = 'none';
            // Remove hx-trigger so hidden widgets don't load
            el.removeAttribute('hx-trigger');
            if (btn) {
                btn.classList.remove('active');
                btn.classList.add('toggle-off');
            }
        } else if (el && btn) {
            btn.classList.add('active');
            btn.classList.remove('toggle-off');
        }
    });
}

function toggleWidget(id) {
    const el = document.getElementById('widget-' + id);
    const btn = document.querySelector('[data-widget="' + id + '"]');
    if (!el) return;

    const isHidden = el.style.display === 'none';
    if (isHidden) {
        el.style.display = '';
        localStorage.setItem('widget-' + id + '-hidden', 'false');
        if (btn) {
            btn.classList.add('active');
            btn.classList.remove('toggle-off');
        }
        // Trigger load if not loaded yet
        if (!el.dataset.loaded) {
            htmx.ajax('GET', '/api/widget/' + id, {target: '#widget-' + id, swap: 'innerHTML'});
            el.dataset.loaded = 'true';
        }
    } else {
        el.style.display = 'none';
        localStorage.setItem('widget-' + id + '-hidden', 'true');
        if (btn) {
            btn.classList.remove('active');
            btn.classList.add('toggle-off');
        }
    }
}

/* ================================================================
   PWA: Service Worker Registration + Install Prompt
   ================================================================ */

let deferredInstallPrompt = null;

function initPWA() {
    // Register service worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js', { scope: '/' })
            .then(reg => console.log('SW registered:', reg.scope))
            .catch(err => console.log('SW registration failed:', err));
    }

    // Listen for install prompt
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredInstallPrompt = e;
        showInstallBanner();
    });

    // Install button handler
    const installBtn = document.getElementById('install-btn');
    if (installBtn) {
        installBtn.addEventListener('click', async () => {
            if (!deferredInstallPrompt) return;
            deferredInstallPrompt.prompt();
            const result = await deferredInstallPrompt.userChoice;
            deferredInstallPrompt = null;
            hideInstallBanner();
        });
    }

    // Dismiss button handler
    const dismissBtn = document.getElementById('install-dismiss');
    if (dismissBtn) {
        dismissBtn.addEventListener('click', () => {
            hideInstallBanner();
            localStorage.setItem('pwa-install-dismissed', 'true');
        });
    }
}

function showInstallBanner() {
    if (localStorage.getItem('pwa-install-dismissed') === 'true') return;
    const banner = document.getElementById('install-banner');
    if (banner) banner.classList.add('visible');
}

function hideInstallBanner() {
    const banner = document.getElementById('install-banner');
    if (banner) banner.classList.remove('visible');
}

/* ================================================================
   Init
   ================================================================ */

document.addEventListener('DOMContentLoaded', () => {
    initEditor();
    initDashboard();
    initPWA();
});
