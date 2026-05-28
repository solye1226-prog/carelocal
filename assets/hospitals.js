const panel = document.querySelector("[data-hospital-data-panel]");
const list = document.querySelector("[data-hospital-data-list]");
const count = document.querySelector("[data-hospital-data-count]");
const search = document.querySelector("[data-hospital-data-search]");
const region = document.querySelector("[data-hospital-data-region]");
const type = document.querySelector("[data-hospital-data-type]");

let hospitals = [];

function normalize(value) {
  return String(value || "").toLowerCase().trim();
}

function formatCount(value) {
  return new Intl.NumberFormat("ko-KR").format(value);
}

function hospitalMatches(hospital) {
  const query = normalize(search?.value);
  const regionValue = region?.value || "";
  const typeValue = type?.value || "";
  const haystack = normalize([
    hospital.name,
    hospital.type,
    hospital.sido,
    hospital.district,
    hospital.address,
    hospital.phone,
  ].join(" "));

  return (
    (!query || haystack.includes(query)) &&
    (!regionValue || hospital.sido === regionValue) &&
    (!typeValue || hospital.typeCode === typeValue)
  );
}

function renderOptions() {
  const regions = Array.from(new Set(hospitals.map((hospital) => hospital.sido).filter(Boolean))).sort((a, b) => a.localeCompare(b, "ko"));
  region.innerHTML = '<option value="">전체 지역</option>';
  regions.forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    region.append(option);
  });
}

function renderHospitals() {
  const filtered = hospitals.filter(hospitalMatches);
  count.textContent = `${formatCount(filtered.length)}개 병원`;
  list.innerHTML = "";

  filtered.slice(0, 80).forEach((hospital) => {
    const card = document.createElement("article");
    card.className = "hospital-card";
    const website = hospital.website ? `<a class="text-link" href="${hospital.website}" target="_blank" rel="noopener">공식 홈페이지</a>` : "";
    card.innerHTML = `
      <div>
        <h3>${hospital.name}</h3>
        <p>${hospital.address || "주소 정보 확인 필요"}</p>
        <div class="hospital-meta">
          <span>${hospital.sido || "지역 미상"} ${hospital.district || ""}</span>
          <span>${hospital.phone || "전화 확인 필요"}</span>
          ${hospital.doctorCount ? `<span>의사 ${formatCount(hospital.doctorCount)}명</span>` : ""}
          ${website}
        </div>
      </div>
      <span class="status">${hospital.type || "의료기관"}</span>
    `;
    list.append(card);
  });

  if (filtered.length > 80) {
    const note = document.createElement("p");
    note.className = "muted";
    note.textContent = `검색 속도를 위해 상위 80개만 표시합니다. 검색어를 입력하면 결과를 더 좁힐 수 있습니다.`;
    list.append(note);
  }
}

async function loadHospitals() {
  if (!panel || !list || !count || !search || !region || !type) return;

  try {
    const response = await fetch("/data/hospitals.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    hospitals = Array.isArray(data.hospitals) ? data.hospitals : [];
    panel.hidden = false;
    renderOptions();
    renderHospitals();
  } catch (error) {
    panel.hidden = false;
    list.innerHTML = `<div class="notice">병원 데이터 파일을 불러오지 못했습니다. 잠시 후 다시 확인해 주세요.</div>`;
    count.textContent = "데이터 확인 필요";
  }
}

[search, region, type].forEach((control) => {
  control?.addEventListener("input", renderHospitals);
});

loadHospitals();
