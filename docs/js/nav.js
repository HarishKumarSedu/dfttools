// Inject sidebar nav
function renderNav() {
  return `
  <nav class="sidebar">
    <div class="sidebar-logo">
      <div class="logo-mark">DFT<span>tools</span></div>
      <div class="logo-sub">Test Framework Docs</div>
    </div>
    <div class="search-wrap">
      <span class="search-icon">🔍</span>
      <input class="search-input" placeholder="Search docs..." type="search">
    </div>
    <div class="nav-section">
      <div class="nav-section-label">Getting Started</div>
      <a href="index.html" class="nav-link"><span class="icon">🏠</span>Overview</a>
      <a href="installation.html" class="nav-link"><span class="icon">📦</span>Installation</a>
      <a href="quickstart.html" class="nav-link"><span class="icon">⚡</span>Quick Start</a>
      <a href="architecture.html" class="nav-link"><span class="icon">🏗️</span>Architecture</a>
    </div>
    <div class="nav-section">
      <div class="nav-section-label">Core Concepts</div>
      <a href="dftide.html" class="nav-link"><span class="icon">🛠️</span>DFTide IDE</a>
      <a href="global-context.html" class="nav-link"><span class="icon">🌐</span>Global Context</a>
      <a href="callbacks.html" class="nav-link"><span class="icon">🔌</span>Callbacks</a>
      <a href="json-format.html" class="nav-link"><span class="icon">📋</span>JSON Test Format</a>
    </div>
    <div class="nav-section">
      <div class="nav-section-label">API Reference</div>
      <a href="api-force.html" class="nav-link"><span class="icon">⚡</span>Force Instructions</a>
      <a href="api-measure.html" class="nav-link"><span class="icon">📊</span>Measure Instructions</a>
      <a href="api-i2c.html" class="nav-link"><span class="icon">🔗</span>I2C Instructions</a>
      <a href="api-signal.html" class="nav-link"><span class="icon">📡</span>Signal Measurements</a>
      <a href="api-time.html" class="nav-link"><span class="icon">⏱️</span>Time Measurements</a>
      <a href="api-trigger.html" class="nav-link"><span class="icon">🎯</span>Trigger Instructions</a>
      <a href="api-sweep.html" class="nav-link"><span class="icon">📈</span>Force Sweep</a>
    </div>
    <div class="nav-section">
      <div class="nav-section-label">Tutorials</div>
      <a href="tutorial-bandgap.html" class="nav-link"><span class="icon">🔬</span>Bandgap Trimming</a>
      <a href="tutorial-vi-sense.html" class="nav-link"><span class="icon">🧪</span>VI Sense Measurement</a>
      <a href="tutorial-startup.html" class="nav-link"><span class="icon">🚀</span>Startup Procedure</a>
      <a href="tutorial-boost.html" class="nav-link"><span class="icon">📐</span>Boost Converter Test</a>
    </div>
    <div class="nav-section">
      <div class="nav-section-label">Reference</div>
      <a href="examples.html" class="nav-link"><span class="icon">💡</span>Full Examples</a>
      <a href="faq.html" class="nav-link"><span class="icon">❓</span>FAQ</a>
    </div>
  </nav>`;
}

document.body.insertAdjacentHTML('afterbegin', renderNav());
