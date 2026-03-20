// Copy code blocks
document.querySelectorAll('pre').forEach(pre => {
  const btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.textContent = 'copy';
  pre.style.position = 'relative';
  pre.appendChild(btn);
  btn.addEventListener('click', () => {
    const code = pre.querySelector('code');
    navigator.clipboard.writeText(code ? code.innerText : pre.innerText);
    btn.textContent = 'copied!';
    btn.style.color = 'var(--accent3)';
    setTimeout(() => { btn.textContent = 'copy'; btn.style.color = ''; }, 1500);
  });
});

// Active nav link
const links = document.querySelectorAll('.nav-link');
const current = location.pathname.split('/').pop() || 'index.html';
links.forEach(l => {
  if (l.getAttribute('href') === current) l.classList.add('active');
});

// Search filter (sidebar nav)
const searchInput = document.querySelector('.search-input');
if (searchInput) {
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase();
    document.querySelectorAll('.nav-link').forEach(l => {
      l.style.display = l.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
  });
}
