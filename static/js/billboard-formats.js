/**
 * billboard-formats.js — переключение табов по Figma 140-6071
 */
(function () {
  const section = document.querySelector('[data-billboard-formats]');
  if (!section) return;

  const tabs = section.querySelectorAll('[data-billboard-tab]');
  const panels = section.querySelectorAll('[data-billboard-panel]');

  function activateTab(index) {
    tabs.forEach(function (tab, i) {
      tab.classList.toggle('is-active', i === index);
      tab.setAttribute('aria-selected', i === index ? 'true' : 'false');
    });
    panels.forEach(function (panel, i) {
      panel.classList.toggle('is-visible', i === index);
      panel.hidden = i !== index;
    });
  }

  tabs.forEach(function (tab, index) {
    tab.addEventListener('click', function () {
      activateTab(index);
    });
  });

  activateTab(2);
})();
