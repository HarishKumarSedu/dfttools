const NAV = `<nav id="topnav">
  <a href="index.html" class="nav-brand">dft<span>tools</span></a>
  <a href="index.html" class="nav-link">Home</a>
  <a href="getting-started.html" class="nav-link">Setup</a>
  <a href="api-measure.html" class="nav-link">Measure</a>
  <a href="api-force.html" class="nav-link">Force</a>
  <a href="api-i2c.html" class="nav-link">I²C</a>
  <a href="api-trigger.html" class="nav-link">Trigger</a>
  <a href="test-programs.html" class="nav-link">Tests</a>
  <a href="https://github.com/HarishKumarSedu/dfttools" target="_blank" class="nav-github">
    <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
    GitHub
  </a>
</nav>`;

document.addEventListener('DOMContentLoaded', () => {
  document.body.insertAdjacentHTML('afterbegin', NAV);
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(a => { if (a.getAttribute('href') === path) a.classList.add('active'); });
  const obs = new IntersectionObserver(e => e.forEach(x => { if (x.isIntersecting) { x.target.classList.add('in'); obs.unobserve(x.target); } }), { threshold: 0.06 });
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  document.querySelectorAll('pre').forEach(pre => {
    const w = pre.parentElement; w.style.position = 'relative';
    const b = document.createElement('button');
    b.textContent = 'COPY';
    b.style.cssText = 'position:absolute;top:8px;right:8px;padding:3px 9px;background:rgba(245,166,35,.1);border:1px solid rgba(245,166,35,.25);border-radius:2px;color:#6b4510;cursor:pointer;opacity:0;transition:opacity .2s,color .2s;font-size:10px;font-family:"SF Mono","Cascadia Code","Fira Code","Consolas","Courier New",monospace;letter-spacing:.08em';
    w.addEventListener('mouseenter', () => { b.style.opacity='1'; b.style.color='#f5a623'; });
    w.addEventListener('mouseleave', () => { b.style.opacity='0'; b.style.color='#6b4510'; });
    b.onclick = () => { navigator.clipboard.writeText(pre.textContent); b.textContent='COPIED!'; b.style.color='#39ff14'; setTimeout(() => { b.textContent='COPY'; b.style.color='#f5a623'; }, 1600); };
    w.appendChild(b);
  });
});
