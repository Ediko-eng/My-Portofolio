const root = document.documentElement;
const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');
const themeToggle = document.getElementById('themeToggle');
const themeIcon = themeToggle ? themeToggle.querySelector('i') : null;

const readSavedTheme = () => {
  try {
    return localStorage.getItem('portfolio-theme');
  } catch (error) {
    console.warn('Could not read the saved theme preference.', error);
    return null;
  }
};

const prefersLight = () =>
  window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches;

const applyTheme = (theme) => {
  const selectedTheme = theme === 'light' ? 'light' : 'dark';
  root.setAttribute('data-theme', selectedTheme);
  if (themeIcon) {
    themeIcon.classList.toggle('fa-moon', selectedTheme === 'dark');
    themeIcon.classList.toggle('fa-sun', selectedTheme === 'light');
  }
  if (themeToggle) {
    themeToggle.setAttribute('aria-label', `Switch to ${selectedTheme === 'dark' ? 'light' : 'dark'} mode`);
    themeToggle.setAttribute('aria-pressed', String(selectedTheme === 'light'));
  }
  try {
    localStorage.setItem('portfolio-theme', selectedTheme);
  } catch (error) {
    console.warn('Could not save the theme preference.', error);
  }
};

const currentTheme = readSavedTheme() || root.getAttribute('data-theme') || (prefersLight() ? 'light' : 'dark');
applyTheme(currentTheme);

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const nextTheme = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    applyTheme(nextTheme);
  });
}

if (menuToggle && mobileMenu) {
  menuToggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('show');
  });
}

// Smooth scrolling for all anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
      if (mobileMenu) mobileMenu.classList.remove('show');
    }
  });
});

window.addEventListener('resize', () => {
  if (window.innerWidth > 968 && mobileMenu) {
    mobileMenu.classList.remove('show');
  }
});
