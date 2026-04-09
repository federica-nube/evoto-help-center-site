const BASE_PATH = document.documentElement.dataset.basePath || "";
const SEARCH_INDEX_URL = `${BASE_PATH}/search-index.json`;

const state = {
  indexPromise: null,
};

function getSearchIndex() {
  if (!state.indexPromise) {
    state.indexPromise = fetch(SEARCH_INDEX_URL).then((response) => response.json());
  }
  return state.indexPromise;
}

function normalizeQuery(value) {
  return (value || "").trim().toLowerCase();
}

function scoreResult(result, query) {
  const title = result.title.toLowerCase();
  const excerpt = (result.excerpt || "").toLowerCase();
  const section = (result.section || "").toLowerCase();
  let score = 0;
  if (title.includes(query)) score += 6;
  if (title.startsWith(query)) score += 4;
  if (section.includes(query)) score += 3;
  if (excerpt.includes(query)) score += 2;
  return score;
}

async function search(query) {
  const normalized = normalizeQuery(query);
  if (!normalized) return [];
  const index = await getSearchIndex();
  return index
    .map((entry) => ({ ...entry, score: scoreResult(entry, normalized) }))
    .filter((entry) => entry.score > 0)
    .sort((a, b) => b.score - a.score || a.title.localeCompare(b.title))
    .slice(0, 8);
}

function attachSearchSuggestions() {
  const forms = document.querySelectorAll(".search-form");
  forms.forEach((form) => {
    const input = form.querySelector("[data-search-input]");
    const results = form.querySelector("[data-search-results]");
    if (!input || !results) return;

    input.addEventListener("input", async () => {
      const query = input.value.trim();
      if (query.length < 2) {
        results.classList.remove("is-visible");
        results.innerHTML = "";
        return;
      }

      const matches = await search(query);
      if (!matches.length) {
        results.classList.remove("is-visible");
        results.innerHTML = "";
        return;
      }

      results.innerHTML = matches
        .map(
          (match) => `
            <a class="search-result-item" href="${match.url}">
              <strong>${match.title}</strong>
              <span>${match.langLabel}${match.section ? " · " + match.section : ""}</span>
            </a>
          `
        )
        .join("");
      results.classList.add("is-visible");
    });

    document.addEventListener("click", (event) => {
      if (!form.contains(event.target)) {
        results.classList.remove("is-visible");
      }
    });
  });
}

function attachSearchPageResults() {
  const container = document.querySelector("[data-search-page-results]");
  if (!container) return;
  const params = new URLSearchParams(window.location.search);
  const initialQuery = params.get("q") || "";
  const input = document.querySelector("[data-search-input]");
  if (input) input.value = initialQuery;

  const render = async (query) => {
    const normalized = normalizeQuery(query);
    if (!normalized) {
      container.innerHTML = '<p class="toc-empty">Enter a few keywords to search the Evoto help center.</p>';
      return;
    }

    const matches = await search(normalized);
    if (!matches.length) {
      container.innerHTML = '<p class="toc-empty">No results matched this query. Try broader product or feature keywords.</p>';
      return;
    }

    container.innerHTML = matches
      .map(
        (match) => `
          <a class="search-page-result" href="${match.url}">
            <small>${match.langLabel}${match.section ? " · " + match.section : ""}</small>
            <strong>${match.title}</strong>
            <p>${match.excerpt || "Open this article."}</p>
          </a>
        `
      )
      .join("");
  };

  render(initialQuery);
}

function attachLanguageSwitcher() {
  document.querySelectorAll("[data-language-switch]").forEach((select) => {
    select.addEventListener("change", () => {
      if (select.value) {
        window.location.href = select.value;
      }
    });
  });
}

function attachSidebarToggle() {
  document.querySelectorAll("[data-sidebar-open]").forEach((button) => {
    button.addEventListener("click", () => document.body.classList.add("nav-open"));
  });
  document.querySelectorAll("[data-sidebar-close]").forEach((button) => {
    button.addEventListener("click", () => document.body.classList.remove("nav-open"));
  });
}

function attachPrimaryNavDropdownExclusive() {
  const nav = document.querySelector(".hero-primary-nav");
  if (!nav) return;
  const dropdowns = nav.querySelectorAll("details.primary-nav-dropdown");
  dropdowns.forEach((details) => {
    details.addEventListener("toggle", () => {
      if (!details.open) return;
      dropdowns.forEach((other) => {
        if (other !== details) other.open = false;
      });
    });
  });
  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target)) {
      dropdowns.forEach((d) => {
        d.open = false;
      });
      return;
    }
    if (!event.target.closest("details.primary-nav-dropdown")) {
      dropdowns.forEach((d) => {
        d.open = false;
      });
    }
  });
}

function normalizePathname(pathname) {
  let p = pathname.replace(/\/index\.html?$/i, "");
  p = p.replace(/\/+$/, "");
  return p || "/";
}

function learningCenterHrefMatchesCurrentPage(href) {
  if (!href) return false;
  const resolved = new URL(href, window.location.href);
  return normalizePathname(resolved.pathname) === normalizePathname(window.location.pathname);
}

function attachLearningCenterHomeNavGuard() {
  document.querySelectorAll("a.primary-nav-dropdown__item--current").forEach((anchor) => {
    anchor.addEventListener("click", (event) => {
      const href = anchor.getAttribute("href");
      if (learningCenterHrefMatchesCurrentPage(href)) {
        event.preventDefault();
      }
    });
  });
}

function init() {
  attachSearchSuggestions();
  attachSearchPageResults();
  attachLanguageSwitcher();
  attachSidebarToggle();
  attachPrimaryNavDropdownExclusive();
  attachLearningCenterHomeNavGuard();
}

document.addEventListener("DOMContentLoaded", init);
