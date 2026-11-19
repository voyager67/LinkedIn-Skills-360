(() => {
  "use strict";
  const $ = (selector, root = document) => root.querySelector(selector);
  const create = (tag, className, text) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined) element.textContent = text;
    return element;
  };
  const fetchJson = async (url) => {
    const response = await fetch(url, { headers: { Accept: "application/json" } });
    if (!response.ok) throw new Error("Catalogue request failed: " + response.status);
    return response.json();
  };
  const externalLink = (url, label) => {
    const link = create("a", "", label);
    link.href = url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    return link;
  };

  const menuButton = $(".menu-toggle");
  const nav = $("#primary-nav");
  if (menuButton && nav) {
    menuButton.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      menuButton.setAttribute("aria-expanded", String(open));
      menuButton.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
    });
    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) {
        nav.classList.remove("is-open");
        menuButton.setAttribute("aria-expanded", "false");
        menuButton.setAttribute("aria-label", "Open navigation");
      }
    });
  }

  const skillRoot = $("[data-skill-catalog]");
  if (skillRoot) {
    const search = $("#skill-search");
    const category = $("#skill-category");
    const clear = $("#clear-filters");
    const resultCount = $("#skill-results");
    const grid = $("#skill-results-grid");
    const loadMore = $("#skill-load-more");
    const pageSize = 30;
    let filteredSkills = [];
    let displayedCount = 0;

    const render = (total) => {
      grid.replaceChildren();
      const visible = filteredSkills.slice(0, displayedCount);
      if (!visible.length) {
        grid.append(create("div", "empty-state", "No matching skills. Try another term or clear the filters."));
      } else {
        const fragment = document.createDocumentFragment();
        visible.forEach((item) => {
          const card = create("article", "skill-card");
          const top = create("div", "skill-card-top");
          top.append(create("span", "skill-category", item.category || "General"));
          top.append(create("span", "skill-agent", item.agent || "Specialist workflow"));
          const title = create("h3", "", item.title || item.slug);
          const description = create("p", "", item.description || "A focused professional workflow.");
          const link = externalLink(item.github, "Read SKILL.md ↗");
          card.append(top, title, description, link);
          fragment.append(card);
        });
        grid.append(fragment);
      }
      resultCount.textContent = "Showing " + visible.length + " of " + filteredSkills.length + " matching skills · " + total + " total";
      loadMore.hidden = displayedCount >= filteredSkills.length;
    };

    fetchJson(skillRoot.dataset.catalogUrl)
      .then((skills) => {
        const categories = Array.from(new Set(skills.map((item) => item.category).filter(Boolean))).sort();
        categories.forEach((value) => {
          const option = create("option", "", value);
          option.value = value;
          category.append(option);
        });

        const params = new URLSearchParams(window.location.search);
        search.value = params.get("q") || "";

        const filter = () => {
          const query = search.value.trim().toLocaleLowerCase();
          const selectedCategory = category.value;
          filteredSkills = skills.filter((item) => {
            const matchesCategory = selectedCategory === "all" || item.category === selectedCategory;
            const haystack = [item.title, item.slug, item.description, item.agent, item.category].join(" ").toLocaleLowerCase();
            return matchesCategory && (!query || haystack.includes(query));
          });
          displayedCount = Math.min(pageSize, filteredSkills.length);
          render(skills.length);
        };

        search.addEventListener("input", filter);
        category.addEventListener("change", filter);
        clear.addEventListener("click", () => {
          search.value = "";
          category.value = "all";
          window.history.replaceState({}, "", window.location.pathname);
          filter();
          search.focus();
        });
        loadMore.addEventListener("click", () => {
          displayedCount = Math.min(displayedCount + pageSize, filteredSkills.length);
          render(skills.length);
        });
        filter();
      })
      .catch((error) => {
        console.error(error);
        grid.replaceChildren(create("div", "empty-state", "The catalogue could not be loaded. Use the Markdown index in the repository instead."));
        resultCount.textContent = "Catalogue unavailable";
      });
  }

  const agentRoot = $("[data-agent-catalog]");
  if (agentRoot) {
    const search = $("#agent-search");
    const resultCount = $("#agent-results");
    const grid = $("#agent-results-grid");
    fetchJson(agentRoot.dataset.catalogUrl)
      .then((agents) => {
        const render = () => {
          const query = search.value.trim().toLocaleLowerCase();
          const results = agents.filter((agent) =>
            [agent.title, agent.slug, agent.description].join(" ").toLocaleLowerCase().includes(query)
          );
          grid.replaceChildren();
          if (!results.length) {
            grid.append(create("div", "empty-state", "No agent roles match that search."));
          } else {
            const fragment = document.createDocumentFragment();
            results.forEach((agent, index) => {
              const card = create("article", "agent-card");
              const top = create("div", "agent-card-top");
              top.append(create("span", "", "SPECIALIST / " + String(index + 1).padStart(2, "0")));
              top.append(create("span", "agent-card-mark", agent.slug === "orchestrator" ? "◎" : "↗"));
              const title = create("h3", "", agent.title);
              const description = create("p", "", agent.description);
              const link = externalLink(agent.github, "Open agent prompt ↗");
              card.append(top, title, description, link);
              fragment.append(card);
            });
            grid.append(fragment);
          }
          resultCount.textContent = results.length + " of " + agents.length + " agent roles";
        };
        search.addEventListener("input", render);
        render();
      })
      .catch((error) => {
        console.error(error);
        grid.replaceChildren(create("div", "empty-state", "The agent directory could not be loaded. Browse the agent source files in GitHub."));
        resultCount.textContent = "Agent directory unavailable";
      });
  }

  document.addEventListener("keydown", (event) => {
    if (event.key !== "/" || event.ctrlKey || event.metaKey || event.altKey) return;
    const target = event.target;
    if (target && /INPUT|TEXTAREA|SELECT/.test(target.tagName)) return;
    const search = $("#skill-search") || $("#agent-search");
    if (search) {
      event.preventDefault();
      search.focus();
    }
  });
})();
