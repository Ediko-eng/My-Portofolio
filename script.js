(function () {
  'use strict';

  /* ---------- Loader ---------- */
  var loader = document.getElementById('loader');
  var fill = document.getElementById('loaderFill');
  var pct = document.getElementById('loaderPct');

  var progress = 0;
  var timer = setInterval(function () {
    progress += 3 + Math.random() * 9;
    if (progress >= 100) {
      progress = 100;
      clearInterval(timer);
      setTimeout(function () {
        loader.classList.add('done');
        loader.setAttribute('aria-hidden', 'true');
      }, 350);
    }
    fill.style.width = progress.toFixed(0) + '%';
    pct.textContent = Math.round(progress) + '%';
  }, 90);

  /* ---------- Day / night mode ---------- */
  var MODE_KEY = 'room-mode';
  var stored = null;
  try { stored = localStorage.getItem(MODE_KEY); } catch (e) {}
  if (stored === 'day') document.body.classList.add('day');

  var modeBtn = document.getElementById('modeToggle');
  modeBtn.addEventListener('click', function () {
    var isDay = document.body.classList.toggle('day');
    modeBtn.setAttribute('aria-label', isDay ? 'Switch to night mode' : 'Switch to day mode');
    try { localStorage.setItem(MODE_KEY, isDay ? 'day' : 'night'); } catch (e) {}
  });

  /* ---------- Panels ---------- */
  var backdrop = document.getElementById('panelBackdrop');
  var openPanel = null;
  var lastFocus = null;

  function show(name) {
    var panel = document.getElementById('panel-' + name);
    if (!panel) return;
    if (openPanel) hide();
    lastFocus = document.activeElement;
    openPanel = panel;
    panel.hidden = false;
    backdrop.classList.add('open');
    var closeBtn = panel.querySelector('.panel-close');
    if (closeBtn) closeBtn.focus();
    hint && hint.classList.add('gone');
  }

  function hide() {
    if (!openPanel) return;
    openPanel.hidden = true;
    openPanel = null;
    backdrop.classList.remove('open');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  document.querySelectorAll('.hotspot[data-panel]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      show(btn.getAttribute('data-panel'));
    });
  });

  document.querySelectorAll('.mobile-nav button[data-panel]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      show(btn.getAttribute('data-panel'));
    });
  });

  document.querySelectorAll('.panel-close').forEach(function (btn) {
    btn.addEventListener('click', hide);
  });

  backdrop.addEventListener('click', hide);

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') hide();
  });

  /* ---------- Hint ---------- */
  var hint = document.getElementById('hint');
  if (hint) {
    setTimeout(function () { hint.classList.add('gone'); }, 14000);
  }

  /* ---------- Typewriter on the monitor ---------- */
  var codeEl = document.getElementById('typedCode');
  if (codeEl) {
    var lines = [
      { html: '<span class="k">def</span> <span class="s">build_future</span>()' },
      { html: '    stack = [<span class="s">"Python"</span>, <span class="s">"Django"</span>]' },
      { html: '    home  = <span class="s">"Timor-Leste"</span>' },
      { html: '    <span class="k">return</span> ship(stack, home)' },
      { html: '' },
      { html: '<span class="v"># &gt;&gt; portfolio loading...</span>' }
    ];
    var full = lines.map(function (l) { return l.html; }).join('\n');
    var plain = full.replace(/<[^>]+>/g, '');
    var i = 0;

    function type() {
      i++;
      // reveal by plain length but keep html: simple approach — slice html on tag boundaries
      var shown = 0;
      var out = '';
      var pos = 0;
      while (shown < i && pos < full.length) {
        if (full[pos] === '<') {
          var end = full.indexOf('>', pos);
          out += full.slice(pos, end + 1);
          pos = end + 1;
        } else {
          out += full[pos];
          pos++;
          shown++;
        }
      }
      codeEl.innerHTML = out;
      if (i < plain.length) {
        setTimeout(type, plain[i] === '\n' ? 240 : 28 + Math.random() * 35);
      } else {
        setTimeout(function () {
          codeEl.innerHTML = full;
        }, 200);
      }
    }
    setTimeout(type, 1200);
  }

  /* ---------- Year ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- E.D.D.I, the room AI ---------- */
  var aiLine = document.getElementById('aiLine');
  var aiBtn = document.getElementById('aiAudio');
  var aiVoiceOn = false;
  var canSpeak = 'speechSynthesis' in window;

  if (aiBtn && !canSpeak) {
    aiBtn.hidden = true;
  }

  var aiLines = [
    'Good evening. All systems online.',
    "Welcome to Edmilson's lab, sir.",
    'Eight projects loaded. Deep learning module ready.',
    'Shall I open the portfolio for you?',
    'Arc reactor at 98 percent. Coffee levels: low.',
    'Timor-Leste uplink stable. Ready when you are.',
    'Remember, sir: progress, not perfection.',
    'Small steps from Dili can still reach the world.'
  ];

  var aiIndex = 0;

  function speak(text) {
    if (!aiVoiceOn || !canSpeak) return;
    var u = new SpeechSynthesisUtterance(text);
    u.rate = 1.02;
    u.pitch = 0.85;
    u.volume = 0.9;
    var voice = window.speechSynthesis.getVoices().filter(function (v) {
      return /en-(GB|US)/i.test(v.lang);
    })[0];
    if (voice) u.voice = voice;
    window.speechSynthesis.speak(u);
  }

  function typeAiLine() {
    var text = aiLines[aiIndex % aiLines.length];
    aiIndex++;
    var i = 0;
    speak(text);
    var timer = setInterval(function () {
      i++;
      aiLine.textContent = text.slice(0, i);
      if (i >= text.length) {
        clearInterval(timer);
        setTimeout(function () {
          aiLine.textContent = '';
          setTimeout(typeAiLine, 900);
        }, 3200);
      }
    }, 32);
  }

  if (aiLine) {
    setTimeout(typeAiLine, 2600);
  }

  if (aiBtn) {
    aiBtn.addEventListener('click', function () {
      aiVoiceOn = !aiVoiceOn;
      aiBtn.setAttribute('aria-pressed', String(aiVoiceOn));
      aiBtn.textContent = aiVoiceOn ? 'AUDIO ON' : 'AUDIO OFF';
      if (!aiVoiceOn && canSpeak) window.speechSynthesis.cancel();
      if (aiVoiceOn) speak(aiLines[(aiIndex - 1 + aiLines.length) % aiLines.length]);
    });
  }

  /* ---------- Motivational quotes ---------- */
  var quotes = [
    'Build things that outlive the doubt.',
    'Every line of code is a brick in the future.',
    'Dream big, start small, ship today.',
    'Discipline beats motivation when motivation sleeps.',
    'Small steps from Dili can reach the world.',
    'Learn like the island never stops growing.',
    'The best time to build is now.',
    "You don't have to be great to start, but you have to start to be great."
  ];

  var loaderQuote = document.getElementById('loaderQuote');
  if (loaderQuote) {
    loaderQuote.textContent = quotes[Math.floor(Math.random() * quotes.length)];
  }

  var quoteEl = document.getElementById('quote');
  if (quoteEl) {
    var qi = 0;
    function showQuote(text) {
      quoteEl.classList.remove('show');
      setTimeout(function () {
        quoteEl.textContent = text;
        quoteEl.classList.add('show');
      }, 600);
    }
    showQuote(quotes[0]);
    qi = 1;
    setInterval(function () {
      showQuote(quotes[qi % quotes.length]);
      qi++;
    }, 8000);
  }
})();
