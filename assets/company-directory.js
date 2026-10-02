(() => {
  const search = document.querySelector('.company-search');
  const input = document.getElementById('company-search');
  const status = document.getElementById('company-search-status');
  const empty = document.getElementById('company-search-empty');
  if (!search || !input || !status || !empty) return;

  const normalize = (value) => value.normalize('NFKC').replace(/\s+/g, '').toLocaleLowerCase('ko-KR');
  const groups = ['nonlife', 'life'].map((id) => ({
    title: document.getElementById(`${id}-title`),
    description: document.getElementById(`${id}-description`),
    directory: document.getElementById(`${id}-companies`),
    cards: Array.from(document.querySelectorAll(`#${id}-companies .company-card`)).map((card) => ({
      element: card,
      name: normalize(card.querySelector('h3').textContent),
    })),
  }));

  function filterCompanies() {
    const query = normalize(input.value);
    let total = 0;
    for (const group of groups) {
      let count = 0;
      for (const card of group.cards) {
        const matches = card.name.includes(query);
        card.element.hidden = !matches;
        if (matches) count += 1;
      }
      group.title.hidden = count === 0;
      group.description.hidden = count === 0;
      group.directory.hidden = count === 0;
      total += count;
    }
    empty.hidden = total !== 0;
    status.textContent = query ? `검색 결과 ${total}개 보험사` : `전체 ${total}개 보험사`;
  }

  input.addEventListener('input', filterCompanies);
  input.addEventListener('search', filterCompanies);
  search.hidden = false;
  filterCompanies();
})();
