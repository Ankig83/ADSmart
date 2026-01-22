/**
 * Minimal vanilla JS helpers:
 * - mobile menu
 * - modal open/close
 * - toasts
 */

function qs(sel, root = document) {
  return root.querySelector(sel);
}

function qsa(sel, root = document) {
  return Array.from(root.querySelectorAll(sel));
}

function toast(text, tone = "info", timeoutMs = 3500) {
  const stack = qs("[data-toast-stack]");
  if (!stack) return;

  const el = document.createElement("div");
  el.className = `c-toast c-toast--${tone}`;
  el.setAttribute("data-toast", "");
  el.innerHTML = `
    <div class="c-toast__body"></div>
    <button class="c-toast__close" type="button" data-toast-close aria-label="Close">×</button>
  `;
  qs(".c-toast__body", el).textContent = text;
  stack.prepend(el);

  const t = window.setTimeout(() => {
    el.remove();
  }, timeoutMs);

  el.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-toast-close]");
    if (!btn) return;
    window.clearTimeout(t);
    el.remove();
  });
}

function initMenu() {
  const toggle = qs("[data-menu-toggle]");
  const menu = qs("[data-menu]");
  if (!toggle || !menu) return;

  toggle.addEventListener("click", () => {
    const isOpen = menu.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });
}

function initFaqAccordion() {
  const root = qs("[data-faq-accordion]");
  if (!root) return;

  const items = qsa("details.demo-faq__item", root);
  if (!items.length) return;

  items.forEach((d) => {
    d.addEventListener("toggle", () => {
      if (!d.open) return;
      items.forEach((other) => {
        if (other !== d) other.open = false;
      });
    });
  });
}

function initDetailsAccordion(rootSelector, itemSelector = "details") {
  qsa(rootSelector).forEach((root) => {
    const items = qsa(itemSelector, root);
    if (!items.length) return;
    items.forEach((d) => {
      d.addEventListener("toggle", () => {
        if (!d.open) return;
        items.forEach((other) => {
          if (other !== d) other.open = false;
        });
      });
    });
  });
}

function initLeadSuccessModal() {
  const params = new URLSearchParams(window.location.search);
  if (params.get("lead_success") !== "1") return;
  openModal("lead-success-modal");

  // remove param to avoid reopening on refresh/back
  params.delete("lead_success");
  const qsStr = params.toString();
  const newUrl = window.location.pathname + (qsStr ? `?${qsStr}` : "") + window.location.hash;
  window.history.replaceState({}, "", newUrl);
}

function getCookie(name) {
  const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const m = document.cookie.match(new RegExp(`(?:^|; )${escaped}=([^;]*)`));
  return m ? decodeURIComponent(m[1]) : null;
}

function setCookie(name, value, maxAgeSeconds) {
  document.cookie = `${encodeURIComponent(name)}=${encodeURIComponent(value)}; Path=/; Max-Age=${maxAgeSeconds}; SameSite=Lax`;
}

function deleteCookie(name) {
  // Try both Max-Age=0 and Expires in the past for maximum compatibility.
  document.cookie = `${encodeURIComponent(name)}=; Path=/; Max-Age=0; SameSite=Lax`;
  document.cookie = `${encodeURIComponent(name)}=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax`;
}

function initCookieConsent() {
  // Debug helper: /home/?cookie_reset=1 to force-show modal again
  // Don't block reading the cookie policy page.
  if (window.location.pathname.startsWith("/cookie-policy")) return;

  const params = new URLSearchParams(window.location.search);
  let forceShow = false;
  if (params.get("cookie_reset") === "1") {
    deleteCookie("cookie_consent");
    forceShow = true;
    params.delete("cookie_reset");
    const qsStr = params.toString();
    const newUrl = window.location.pathname + (qsStr ? `?${qsStr}` : "") + window.location.hash;
    window.history.replaceState({}, "", newUrl);
  }

  if (!forceShow && getCookie("cookie_consent") === "1") return;
  const modalId = "cookie-consent-modal";
  const modal = document.getElementById(modalId);
  if (!modal) return;

  openModal(modalId);

  const btn = modal.querySelector("[data-cookie-accept]");
  if (!btn) return;
  btn.addEventListener("click", () => {
    setCookie("cookie_consent", "1", 60 * 60 * 24 * 365);
    closeModal(modal);
  });
}

function openModal(id) {
  const m = document.getElementById(id);
  if (!m) return;
  m.hidden = false;
  document.documentElement.style.overflow = "hidden";
}

function closeModal(modalEl) {
  if (!modalEl) return;
  modalEl.hidden = true;
  document.documentElement.style.overflow = "";
}

function initModals() {
  qsa("[data-modal-open]").forEach((btn) => {
    btn.addEventListener("click", () => openModal(btn.getAttribute("data-modal-open")));
  });

  qsa("[data-modal]").forEach((modal) => {
    modal.addEventListener("click", (e) => {
      if (e.target.closest("[data-modal-close]")) closeModal(modal);
    });
  });

  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    qsa("[data-modal]").forEach((m) => {
      if (!m.hidden) closeModal(m);
    });
  });
}

function initDemoButtons() {
  qsa(".js-toast-demo").forEach((btn) => {
    btn.addEventListener("click", () => toast("Hello from toast()", "success"));
  });
}

function initTabs() {
  qsa("[data-tabs]").forEach((tabs) => {
    const buttons = qsa("[data-tab]", tabs);
    const root = tabs.closest("section") || document;
    const panels = qsa("[data-panel]", root);
    if (!buttons.length) return;

    function setActive(name) {
      tabs.setAttribute("data-tabs-active", name);
      buttons.forEach((b) => {
        const isActive = b.getAttribute("data-tab") === name;
        b.setAttribute("aria-selected", String(isActive));
      });
      panels.forEach((p) => {
        const isActive = p.getAttribute("data-panel") === name;
        p.hidden = !isActive;
      });
    }

    buttons.forEach((b) => {
      b.addEventListener("click", () => setActive(b.getAttribute("data-tab")));
    });

    // Initial state (from markup attr) fallback to first tab.
    setActive(tabs.getAttribute("data-tabs-active") || buttons[0].getAttribute("data-tab"));
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initMenu();
  initLeadSuccessModal();
  initCookieConsent();
  initFaqAccordion();
  initDetailsAccordion("[data-transport-accordion]", "details.demo-transport-format");
  initModals();
  initDemoButtons();
  initTabs();

  // wire close buttons for server-rendered toasts
  document.body.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-toast-close]");
    if (!btn) return;
    const t = btn.closest("[data-toast]");
    if (t) t.remove();
  });
});

// Expose for debug
window.toast = toast;



