(() => {
  const $ = (id) => document.getElementById(id);
  const format = new Intl.NumberFormat('ko-KR');
  const state = { password: '', busy: false, catalog: [], overall: null, detail: null, selected: null, page: 1, controller: null };
  const pathKey = (path) => path.replace(/\.html$/, '').replace(/\/$/, '') || '/';
  const text = (tag, value) => { const node = document.createElement(tag); node.textContent = value; return node; };

  function renderChart(data) {
    const svgNode = (tag, attrs) => {
      const node = document.createElementNS('http://www.w3.org/2000/svg', tag);
      for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
      return node;
    };
    const metrics = [['views', '#5278ed', $('show-views').checked], ['visits', '#14756b', $('show-visits').checked]].filter((item) => item[2]);
    const width = Math.max(320, $('chart').clientWidth);
    const height = 280, left = 40, right = width - 18, top = 20, bottom = 242;
    const max = Math.ceil(Math.max(1, ...data.daily.flatMap((day) => metrics.map(([key]) => day[key]))) / 4) * 4;
    const x = (index) => data.daily.length === 1 ? (left + right) / 2 : left + index * (right - left) / (data.daily.length - 1);
    const y = (value) => bottom - value / max * (bottom - top);
    const svg = svgNode('svg', { viewBox: `0 0 ${width} ${height}`, role: 'img', 'aria-label': '선택 기간의 날짜별 조회수와 방문 횟수. 아래 날짜별 수치에서도 확인할 수 있습니다.' });
    for (let i = 0; i <= 4; i++) {
      const value = max * i / 4;
      svg.append(svgNode('line', { x1: left, x2: right, y1: y(value), y2: y(value), stroke: '#e2e6ec' }));
      const label = svgNode('text', { x: left - 8, y: y(value) + 4, 'text-anchor': 'end', fill: '#677184', 'font-size': 11 });
      label.textContent = Number.isInteger(value) ? value : value.toFixed(1);
      svg.append(label);
    }
    const stride = Math.max(1, Math.ceil(data.daily.length / (width < 500 ? 4 : 8)));
    for (const [index, day] of data.daily.entries()) {
      if (index % stride === 0 || index === data.daily.length - 1 && data.daily.length % stride > 1) {
        const label = svgNode('text', { x: x(index), y: 269, 'text-anchor': 'middle', fill: '#677184', 'font-size': 11 });
        label.textContent = day.date.slice(5).replace('-', '/'); svg.append(label);
      }
    }
    for (const [seriesIndex, [key, color]] of metrics.entries()) {
      if ($('chart-mode').value === 'line') {
        const points = data.daily.map((day, index) => `${x(index)},${y(day[key])}`).join(' ');
        svg.append(svgNode('polygon', { points: `${x(0)},${bottom} ${points} ${x(data.daily.length - 1)},${bottom}`, fill: color, opacity: '.09' }));
        svg.append(svgNode('polyline', { points, fill: 'none', stroke: color, 'stroke-width': 2.5, 'stroke-linejoin': 'round' }));
      }
      data.daily.forEach((day, index) => {
        const barWidth = Math.max(2, Math.min(18, (right - left) / data.daily.length / 3));
        const mark = $('chart-mode').value === 'bar'
          ? svgNode('rect', { x: x(index) + (seriesIndex - .5) * barWidth - barWidth / 2, y: y(day[key]), width: barWidth, height: bottom - y(day[key]), fill: color })
          : svgNode('circle', { cx: x(index), cy: y(day[key]), r: 3, fill: color });
        const title = svgNode('title', {}); title.textContent = `${day.date} ${key === 'views' ? '조회수' : '방문 횟수'} ${format.format(day[key])}`;
        mark.append(title); svg.append(mark);
      });
    }
    $('chart').replaceChildren(svg);
    $('daily-data').replaceChildren(...data.daily.map((day) => text('p', `${day.date} · 조회수 ${format.format(day.views)} · 방문 횟수 ${format.format(day.visits)}`)));
    $('date-range').textContent = `${data.daily[0]?.date || ''} ~ ${data.daily.at(-1)?.date || ''}`;
  }

  function renderTopPosts() {
    if (!state.overall) return;
    const counts = new Map();
    for (const row of state.overall.pages) counts.set(pathKey(row.path), (counts.get(pathKey(row.path)) || 0) + row.views);
    const articles = state.catalog.map((article) => ({ ...article, views: counts.get(article.path) || 0 })).filter((article) => article.views > 0).sort((a, b) => b.views - a.views).slice(0, 10);
    $('top-posts').replaceChildren();
    for (const article of articles) {
      const button = text('button', article.title);
      button.className = 'rank-row';
      button.style.setProperty('--bar', `${article.views / articles[0].views * 100}%`);
      button.append(text('strong', format.format(article.views)));
      button.addEventListener('click', () => { if (!state.busy) { state.selected = article; refresh(); } });
      $('top-posts').append(button);
    }
    if (!articles.length) $('top-posts').textContent = '선택 기간에 수집된 게시글 조회가 없습니다.';
  }

  function renderList() {
    const counts = new Map();
    for (const row of state.overall?.pages || []) counts.set(pathKey(row.path), (counts.get(pathKey(row.path)) || 0) + row.views);
    const query = $('search').value.trim().toLocaleLowerCase('ko-KR');
    const articles = state.catalog.filter((article) => `${article.title} ${article.category}`.toLocaleLowerCase('ko-KR').includes(query));
    articles.sort((a, b) => ($('sort').value === 'views' ? (counts.get(b.path) || 0) - (counts.get(a.path) || 0) : 0) || a.title.localeCompare(b.title, 'ko'));
    const totalPages = Math.max(1, Math.ceil(articles.length / 15));
    state.page = Math.min(state.page, totalPages);
    $('article-count').textContent = `${articles.length}개`;
    $('page-number').textContent = `${state.page} / ${totalPages}`;
    $('previous').disabled = state.page === 1;
    $('next').disabled = state.page === totalPages;
    $('pages').replaceChildren();
    for (const article of articles.slice((state.page - 1) * 15, state.page * 15)) {
      const row = document.createElement('tr');
      const label = document.createElement('td');
      const link = text('a', article.title);
      link.href = article.path;
      label.append(text('small', article.category), link);
      const count = counts.get(article.path);
      const value = !state.overall ? '—' : count === undefined && !state.overall.pagesComplete ? '미집계' : format.format(count || 0);
      const detail = document.createElement('td');
      const button = text('button', '통계');
      button.type = 'button';
      button.setAttribute('aria-label', `${article.title} 통계 보기`);
      button.disabled = !state.overall || state.busy;
      button.addEventListener('click', () => { state.selected = article; refresh(); $('overview').scrollIntoView({ behavior: 'smooth' }); });
      detail.append(button);
      row.append(label, text('td', value), detail);
      $('pages').append(row);
    }
    if (!articles.length) {
      const row = document.createElement('tr');
      const cell = text('td', '검색 결과가 없습니다.');
      cell.colSpan = 3;
      row.append(cell);
      $('pages').append(row);
    }
  }

  function renderDetails(data) {
    $('detail-heading').textContent = state.selected ? state.selected.title : '사이트 전체';
    $('all-pages').hidden = !state.selected;
    $('visits').textContent = format.format(data.visits);
    $('views').textContent = format.format(data.views);
    renderChart(data);
    renderTopPosts();
    $('referrers').replaceChildren();
    for (const referrer of data.referrers) {
      const row = document.createElement('tr');
      const host = referrer.host === 'hospital.hbuby.com' ? `${referrer.host} (내부 이동)` : referrer.host || '직접 방문·출처 미확인';
      row.append(text('td', host), text('td', format.format(referrer.views)));
      row.firstChild.style.background = `linear-gradient(to right, #e8ecff ${referrer.views / Math.max(1, data.referrers[0].views) * 100}%, transparent 0)`;
      $('referrers').append(row);
    }
    if (!data.referrers.length) {
      const row = document.createElement('tr');
      const cell = text('td', '선택 기간에 수집된 유입 기록이 없습니다.');
      cell.colSpan = 2;
      row.append(cell);
      $('referrers').append(row);
    }
    $('devices').replaceChildren();
    const names = { desktop: 'PC', mobile: '모바일', tablet: '태블릿' };
    for (const device of data.devices) $('devices').append(text('p', `${names[device.device.toLowerCase()] || device.device} · ${format.format(device.views)}회`));
    if (!data.devices.length) $('devices').textContent = '선택 기간에 수집된 기기 기록이 없습니다.';
  }

  function clearData() {
    state.overall = null;
    state.detail = null;
    $('visits').textContent = $('views').textContent = '—';
    $('chart').textContent = $('devices').textContent = '통계 연결 후 표시됩니다.';
    $('daily-data').replaceChildren();
    $('top-posts').textContent = '통계 연결 후 표시됩니다.';
    $('date-range').textContent = '';
    $('referrers').replaceChildren();
    $('updated').textContent = '자동 갱신 대기';
    $('list-note').textContent = '조회수는 통계 연결 후 표시됩니다.';
    renderList();
  }

  async function load(path, signal) {
    const params = new URLSearchParams({ days: $('period').value });
    if (path) params.set('path', path);
    const response = await fetch(`/api/analytics?${params}`, {
      cache: 'no-store', signal,
      headers: state.password ? { Authorization: `Bearer ${state.password}` } : {},
    });
    if (response.status === 401) {
      const tried = Boolean(state.password);
      state.password = '';
      $('login').hidden = false;
      $('logout').hidden = true;
      clearData();
      throw new Error(tried ? '비밀번호를 다시 확인해 주세요.' : '운영자 인증 후 통계를 확인할 수 있습니다.');
    }
    if (!response.headers.get('Content-Type')?.includes('application/json')) throw new Error('통계 서버 연결을 확인해 주세요.');
    const data = await response.json();
    if (!response.ok) throw new Error(data.message || '통계를 불러오지 못했습니다.');
    return data;
  }

  async function refresh() {
    if (state.busy) return;
    state.busy = true;
    state.controller = new AbortController();
    const timer = setTimeout(() => state.controller?.abort(), 45000);
    $('refresh').disabled = $('period').disabled = true;
    $('all-pages').disabled = true;
    renderList();
    try {
      const overall = await load(null, state.controller.signal);
      const detail = state.selected ? await load(state.selected.path, state.controller.signal) : overall;
      state.overall = overall;
      state.detail = detail;
      $('login').hidden = true;
      $('logout').hidden = false;
      renderDetails(detail);
      $('updated').textContent = `마지막 갱신 ${new Date(overall.generatedAt).toLocaleString('ko-KR')}`;
      $('list-note').textContent = `${$('period').selectedOptions[0].textContent} · ${overall.pagesComplete ? '0은 선택 기간에 수집된 조회 기록이 없다는 의미입니다.' : '조회 가능한 목록 한도에 도달했습니다. 누락된 글은 미집계로 표시합니다.'}`;
      $('status').textContent = '게시글 조회수와 유입 경로가 연결되었습니다.';
    } catch (error) {
      $('status').textContent = `${error.name === 'AbortError' ? '통계 조회 시간이 초과되었습니다.' : error.message}${state.overall ? ' 현재 화면은 마지막으로 불러온 통계입니다.' : ''}`;
    } finally {
      clearTimeout(timer);
      state.busy = false;
      $('refresh').disabled = $('period').disabled = false;
      $('all-pages').disabled = false;
      renderList();
    }
  }

  $('login').addEventListener('submit', (event) => {
    event.preventDefault();
    if (state.busy) return;
    state.password = $('password').value;
    $('password').value = '';
    refresh();
  });
  $('logout').addEventListener('click', () => {
    state.controller?.abort();
    state.password = '';
    state.selected = null;
    clearData();
    $('login').hidden = false;
    $('logout').hidden = true;
    $('status').textContent = '통계 화면이 잠겼습니다.';
    $('detail-heading').textContent = '사이트 전체';
    $('all-pages').hidden = true;
  });
  $('refresh').addEventListener('click', refresh);
  $('period').addEventListener('change', () => { clearData(); refresh(); });
  $('all-pages').addEventListener('click', () => { state.selected = null; refresh(); });
  $('search').addEventListener('input', () => { state.page = 1; renderList(); });
  $('sort').addEventListener('change', () => { state.page = 1; renderList(); });
  $('previous').addEventListener('click', () => { state.page--; renderList(); });
  $('next').addEventListener('click', () => { state.page++; renderList(); });
  for (const id of ['show-views', 'show-visits', 'chart-mode']) $(id).addEventListener('change', () => { if (state.detail) renderChart(state.detail); });
  new ResizeObserver(() => { if (state.detail) renderChart(state.detail); }).observe($('chart'));
  setInterval(() => { if (!document.hidden && state.password) refresh(); }, 300000);
  fetch('/assets/article-catalog.json', { cache: 'no-cache' }).then((response) => {
    if (!response.ok) throw new Error();
    return response.json();
  }).then((catalog) => { state.catalog = catalog; renderList(); renderTopPosts(); }).catch(() => { $('list-note').textContent = '게시글 목록을 불러오지 못했습니다. 새로고침해 주세요.'; });
  refresh();
})();
