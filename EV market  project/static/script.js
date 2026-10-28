/**
 * Electric Vehicle Market Performance & Insights
 * Minimal Client-Side Interactivity Script
 */

// Function to switch between main sections (Overview, Dashboard, Story, About)
function navigateTo(sectionId, event) {
  if (event) {
    event.preventDefault();
  }

  const validSections = ['overview', 'dashboard', 'story', 'about'];
  if (!validSections.includes(sectionId)) {
    sectionId = 'overview';
  }

  // Hide all sections and remove active class
  const sections = document.querySelectorAll('.project-section');
  sections.forEach((sec) => {
    sec.classList.remove('active-view');
  });

  // Show target section
  const targetSection = document.getElementById(sectionId);
  if (targetSection) {
    targetSection.classList.add('active-view');
  }

  // Update navigation items
  const navItems = document.querySelectorAll('.nav-item');
  navItems.forEach((item) => {
    if (item.getAttribute('data-target') === sectionId) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });

  // Update URL hash without causing a page jump
  if (history.pushState) {
    history.pushState(null, null, '#' + sectionId);
  } else {
    location.hash = '#' + sectionId;
  }

  // Close mobile navigation menu if open
  const navLinks = document.getElementById('navLinks');
  if (navLinks && navLinks.classList.contains('open')) {
    navLinks.classList.remove('open');
  }

  // Smooth scroll to top of section or main content
  if (sectionId === 'overview') {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else if (targetSection) {
    const navbarHeight = 75;
    const elementPosition = targetSection.getBoundingClientRect().top;
    const offsetPosition = elementPosition + window.pageYOffset - navbarHeight;
    window.scrollTo({
      top: offsetPosition,
      behavior: 'smooth'
    });
  }
}

// Toggle mobile navigation menu
function toggleMobileMenu() {
  const navLinks = document.getElementById('navLinks');
  if (navLinks) {
    navLinks.classList.toggle('open');
  }
}

// Fullscreen toggle for Tableau visual container
function toggleFullscreen(wrapperId) {
  const wrapper = document.getElementById(wrapperId);
  if (!wrapper) return;

  if (!document.fullscreenElement) {
    if (wrapper.requestFullscreen) {
      wrapper.requestFullscreen();
    } else if (wrapper.webkitRequestFullscreen) {
      wrapper.webkitRequestFullscreen();
    } else if (wrapper.msRequestFullscreen) {
      wrapper.msRequestFullscreen();
    }
    wrapper.classList.add('is-fullscreen');
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    }
    wrapper.classList.remove('is-fullscreen');
  }
}

// Reload iframe content
function reloadFrame(iframeId) {
  const iframe = document.getElementById(iframeId);
  if (iframe) {
    const currentSrc = iframe.src;
    iframe.src = '';
    setTimeout(() => {
      iframe.src = currentSrc;
      showToast('Refreshing Tableau visualization...');
    }, 150);
  }
}

// Copy configuration snippet to clipboard
function copySnippet(snippetId) {
  const codeElement = document.getElementById(snippetId);
  if (!codeElement) return;

  const textToCopy = codeElement.innerText;
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(textToCopy).then(() => {
      showToast('Copied to clipboard!');
    }).catch(() => {
      fallbackCopyText(textToCopy);
    });
  } else {
    fallbackCopyText(textToCopy);
  }
}

function fallbackCopyText(text) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.style.position = 'fixed';
  textArea.style.left = '-999999px';
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();
  try {
    document.execCommand('copy');
    showToast('Copied to clipboard!');
  } catch (err) {
    showToast('Failed to copy. Please select and copy manually.');
  }
  document.body.removeChild(textArea);
}

// Show a temporary toast message
function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;

  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3000);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  // Check URL hash first (e.g. #dashboard or #story)
  const hash = window.location.hash.replace('#', '').toLowerCase();
  const validSections = ['overview', 'dashboard', 'story', 'about'];

  // Check body data attribute passed from Flask backend
  const initialSection = document.body.getAttribute('data-active-section') || 'overview';

  if (hash && validSections.includes(hash)) {
    navigateTo(hash);
  } else if (initialSection && validSections.includes(initialSection)) {
    navigateTo(initialSection);
  }

  // Handle browser forward/back buttons
  window.addEventListener('popstate', () => {
    const popHash = window.location.hash.replace('#', '').toLowerCase();
    if (popHash && validSections.includes(popHash)) {
      navigateTo(popHash);
    } else {
      navigateTo('overview');
    }
  });

  // Listen for fullscreen change events to ensure class is cleared
  document.addEventListener('fullscreenchange', () => {
    if (!document.fullscreenElement) {
      document.querySelectorAll('.iframe-container').forEach(el => {
        el.classList.remove('is-fullscreen');
      });
    }
  });
});

