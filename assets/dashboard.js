(() => {
  const STORAGE_KEY = "carelocal-search-console-dashboard-v1";
  const state = { queries: [], pages: [], dates: [] };
  const fileInput = document.querySelector("[data-search-console-file]");
  const status = document.querySelector("[data-dashboard-status]");
  const importHelp = document.querySelector("[data-import-help]");
  const helpButton = document.querySelector("[data-toggle-import-help]");
  const clearButton = document.querySelector("[data-clear-dashboard]");

  const number = new Intl.NumberFormat("ko-KR");
  const decimal = new Intl.NumberFormat("ko-KR", { maximumFractionDigits: 1 });

  const aliases = {
    clicks: ["clicks", "click", "클릭수", "클릭"],
    impressions: ["impressions", "impression", "노출수", "노출"],
    ctr: ["ctr", "클릭률"],
    position: ["position", "average position", "평균 게재순위", "평균 순위"],
    query: ["query", "queries", "검색어"],
    page: ["page", "pages", "페이지"],
    date: ["date", "dates", "날짜"]
  };

  function normalize(value) {
    return String(value || "").replace(/^\ufeff/, "").trim().toLowerCase();
  }

  function detectDelimiter(text) {
    const firstLine = text.split(/\r?\n/, 1)[0] || "";
    return (firstLine.match(/;/g) || []).length > (firstLine.match(/,/g) || []).length ? ";" : ",";
  }

  function parseCsv(text) {
    const delimiter = detectDelimiter(text);
    const rows = [];
    let row = [];
    let value = "";
    let quoted = false;

    for (let index = 0; index < text.length; index += 1) {
      const char = text[index];
      const next = text[index + 1];
      if (char === '"' && quoted && next === '"') {
        value += '"';
        index += 1;
      } else if (char === '"') {
        quoted = !quoted;
      } else if (char === delimiter && !quoted) {
        row.push(value.trim());
        value = "";
      } else if ((char === "\n" || char === "\r") && !quoted) {
        if (char === "\r" && next === "\n") index += 1;
        row.push(value.trim());
        if (row.some((cell) => cell)) rows.push(row);
        row = [];
        value = "";
      } else {
        value += char;
      }
    }
    row.push(value.trim());
    if (row.some((cell) => cell)) rows.push(row);
    return rows;
  }

  function columnIndex(headers, type) {
    return headers.findIndex((header) => aliases[type].includes(normalize(header)));
  }

  function asNumber(value) {
    const cleaned = String(value || "").replace(/[%,\s]/g, "").replace(/,/g, "");
    return Number.parseFloat(cleaned) || 0;
  }

  function asPercent(value, clicks, impressions) {
    if (String(value || "").includes("%")) return asNumber(value) / 100;
    const parsed = asNumber(value);
    return parsed ? (parsed > 1 ? parsed / 100 : parsed) : (impressions ? clicks / impressions : 0);
  }

  function extractRows(text) {
    const rows = parseCsv(text);
    if (rows.length < 2) throw new Error("행이 부족합니다.");
    const headers = rows.shift();
    const indexes = Object.fromEntries(Object.keys(aliases).map((type) => [type, columnIndex(headers, type)]));
    const dimension = indexes.query > -1 ? "queries" : indexes.page > -1 ? "pages" : indexes.date > -1 ? "dates" : null;
    if (!dimension || indexes.clicks === -1 || indexes.impressions === -1) {
      throw new Error("Search Console에서 내보낸 검색어, 페이지 또는 날짜 CSV인지 확인해 주세요.");
    }

    const keyIndex = indexes[dimension === "queries" ? "query" : dimension === "pages" ? "page" : "date"];
    return {
      dimension,
      rows: rows.map((cells) => {
        const clicks = asNumber(cells[indexes.clicks]);
        const impressions = asNumber(cells[indexes.impressions]);
        return {
          key: cells[keyIndex] || "-",
          clicks,
          impressions,
          ctr: asPercent(cells[indexes.ctr], clicks, impressions),
          position: indexes.position > -1 ? asNumber(cells[indexes.position]) : 0
        };
      }).filter((row) => row.key !== "-")
    };
  }

  function sortByClicks(rows) {
    return [...rows].sort((a, b) => b.clicks - a.clicks || b.impressions - a.impressions);
  }

  function metricSource() {
    return state.dates.length ? state.dates : state.queries.length ? state.queries : state.pages;
  }

  function getMetrics() {
    const rows = metricSource();
    const clicks = rows.reduce((sum, row) => sum + row.clicks, 0);
    const impressions = rows.reduce((sum, row) => sum + row.impressions, 0);
    const weightedPosition = rows.reduce((sum, row) => sum + (row.position * row.impressions), 0);
    return {
      clicks,
      impressions,
      ctr: impressions ? clicks / impressions : 0,
      position: impressions ? weightedPosition / impressions : 0
    };
  }

  function formatPage(value) {
    try {
      const url = new URL(value);
      return `${url.pathname}${url.search}` || "/";
    } catch {
      return value;
    }
  }

  function setText(selector, text) {
    const element = document.querySelector(selector);
    if (element) element.textContent = text;
  }

  function populateTable(selector, rows, type) {
    const body = document.querySelector(selector);
    if (!body) return;
    const values = sortByClicks(rows).slice(0, 10);
    if (!values.length) {
      body.innerHTML = `<tr class="analytics-empty-row"><td colspan="5">${type === "query" ? "검색어" : "페이지"} CSV를 불러오면 이곳에 표시됩니다.</td></tr>`;
      return;
    }
    body.innerHTML = values.map((row) => `
      <tr>
        <th scope="row" title="${escapeHtml(row.key)}">${escapeHtml(type === "page" ? formatPage(row.key) : row.key)}</th>
        <td>${number.format(row.clicks)}</td>
        <td>${number.format(row.impressions)}</td>
        <td>${(row.ctr * 100).toFixed(1)}%</td>
        <td>${row.position ? decimal.format(row.position) : "-"}</td>
      </tr>
    `).join("");
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
  }

  function renderChart() {
    const container = document.querySelector("[data-click-chart]");
    const range = document.querySelector("[data-chart-range]");
    if (!container) return;
    const rows = [...state.dates].sort((a, b) => a.key.localeCompare(b.key));
    if (!rows.length) {
      container.innerHTML = '<div class="analytics-chart-empty">날짜별 CSV를 불러오면 클릭 추이가 표시됩니다.</div>';
      if (range) range.textContent = "날짜 데이터 필요";
      return;
    }
    const max = Math.max(...rows.map((row) => row.clicks), 1);
    const width = 760;
    const height = 240;
    const padding = { top: 18, right: 18, bottom: 34, left: 36 };
    const plotWidth = width - padding.left - padding.right;
    const plotHeight = height - padding.top - padding.bottom;
    const step = rows.length > 1 ? plotWidth / (rows.length - 1) : 0;
    const points = rows.map((row, index) => {
      const x = padding.left + (step * index);
      const y = padding.top + plotHeight - ((row.clicks / max) * plotHeight);
      return { x, y, row };
    });
    const line = points.map((point) => `${point.x.toFixed(1)},${point.y.toFixed(1)}`).join(" ");
    const area = `${padding.left},${padding.top + plotHeight} ${line} ${padding.left + plotWidth},${padding.top + plotHeight}`;
    const labels = [rows[0], rows[Math.floor((rows.length - 1) / 2)], rows[rows.length - 1]].map((row, index) => {
      const x = [padding.left, padding.left + (plotWidth / 2), padding.left + plotWidth][index];
      return `<text x="${x}" y="${height - 10}" text-anchor="${index === 0 ? "start" : index === 2 ? "end" : "middle"}">${escapeHtml(row.key.slice(5))}</text>`;
    }).join("");
    container.innerHTML = `
      <svg viewBox="0 0 ${width} ${height}" role="img" aria-label="날짜별 검색 클릭 추이">
        <line x1="${padding.left}" y1="${padding.top + plotHeight}" x2="${width - padding.right}" y2="${padding.top + plotHeight}" class="analytics-chart-axis" />
        <text x="4" y="${padding.top + 7}" class="analytics-chart-count">${number.format(max)}</text>
        <polygon points="${area}" class="analytics-chart-area" />
        <polyline points="${line}" class="analytics-chart-line" />
        ${points.map((point) => `<circle cx="${point.x}" cy="${point.y}" r="4" class="analytics-chart-point"><title>${escapeHtml(point.row.key)}: ${number.format(point.row.clicks)} 클릭</title></circle>`).join("")}
        ${labels}
      </svg>`;
    if (range) range.textContent = `${rows[0].key} ~ ${rows[rows.length - 1].key}`;
  }

  function persist() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  function render() {
    const metrics = getMetrics();
    setText('[data-metric="clicks"]', metrics.clicks ? number.format(metrics.clicks) : "-");
    setText('[data-metric="impressions"]', metrics.impressions ? number.format(metrics.impressions) : "-");
    setText('[data-metric="ctr"]', metrics.impressions ? `${(metrics.ctr * 100).toFixed(1)}%` : "-");
    setText('[data-metric="position"]', metrics.position ? decimal.format(metrics.position) : "-");
    setText("[data-query-count]", `${number.format(state.queries.length)}개`);
    setText("[data-page-count]", `${number.format(state.pages.length)}개`);
    populateTable("[data-query-table]", state.queries, "query");
    populateTable("[data-page-table]", state.pages, "page");
    renderChart();
  }

  function loadSavedData() {
    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
      if (!saved) return;
      ["queries", "pages", "dates"].forEach((type) => {
        if (Array.isArray(saved[type])) state[type] = saved[type];
      });
      const loaded = [state.queries.length && "검색어", state.pages.length && "페이지", state.dates.length && "날짜"].filter(Boolean).join(" · ");
      if (loaded) status.textContent = `${loaded} 데이터가 이 브라우저에 저장되어 있습니다. 새 파일을 불러오면 해당 항목만 갱신됩니다.`;
    } catch {
      localStorage.removeItem(STORAGE_KEY);
    }
  }

  fileInput?.addEventListener("change", async (event) => {
    const [file] = event.target.files;
    if (!file) return;
    try {
      const parsed = extractRows(await file.text());
      state[parsed.dimension] = parsed.rows;
      persist();
      render();
      const names = { queries: "검색어", pages: "페이지", dates: "날짜" };
      status.textContent = `${names[parsed.dimension]} ${number.format(parsed.rows.length)}개를 불러왔습니다. 다른 탭의 CSV도 이어서 추가할 수 있습니다.`;
    } catch (error) {
      status.textContent = error.message || "CSV를 읽지 못했습니다. 파일 형식을 다시 확인해 주세요.";
    } finally {
      event.target.value = "";
    }
  });

  helpButton?.addEventListener("click", () => {
    const expanded = helpButton.getAttribute("aria-expanded") === "true";
    helpButton.setAttribute("aria-expanded", String(!expanded));
    importHelp.hidden = expanded;
  });

  clearButton?.addEventListener("click", () => {
    if (!window.confirm("이 브라우저에 저장된 통계 데이터를 모두 초기화할까요?")) return;
    state.queries = [];
    state.pages = [];
    state.dates = [];
    localStorage.removeItem(STORAGE_KEY);
    status.textContent = "저장된 통계 데이터를 초기화했습니다.";
    render();
  });

  loadSavedData();
  render();
})();
