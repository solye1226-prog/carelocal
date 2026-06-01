const panel = document.querySelector("[data-hospital-data-panel]");
const list = document.querySelector("[data-hospital-data-list]");
const count = document.querySelector("[data-hospital-data-count]");
const search = document.querySelector("[data-hospital-data-search]");
const region = document.querySelector("[data-hospital-data-region]");
const type = document.querySelector("[data-hospital-data-type]");
const hospitalMap = document.querySelector("[data-hospital-map]");
const hospitalMapDetail = document.querySelector("[data-hospital-map-detail]");
const hospitalMapCount = document.querySelector("[data-hospital-map-count]");

let hospitals = [];

const diagnosisSearches = [
  {
    keys: ["갑상선암", "갑상샘암", "갑상선"],
    label: "갑상선암",
    guide: "/cancers/thyroid-cancer.html",
    check: "갑상선외과, 내분비내과, 이비인후과, 핵의학과, 갑상선센터 운영 여부",
  },
  {
    keys: ["폐암", "폐"],
    label: "폐암",
    guide: "/cancers/lung-cancer.html",
    check: "호흡기내과, 흉부외과, 종양내과, 방사선종양학과 협진 여부",
  },
  {
    keys: ["유방암", "유방"],
    label: "유방암",
    guide: "/cancers/breast-cancer.html",
    check: "유방외과, 종양내과, 방사선종양학과, 유방암센터 운영 여부",
  },
  {
    keys: ["전립선암", "전립선"],
    label: "전립선암",
    guide: "/cancers/prostate-cancer.html",
    check: "비뇨의학과, 방사선종양학과, 로봇수술 또는 입자치료 상담 창구",
  },
  {
    keys: ["대장암", "직장암", "결장암", "대장"],
    label: "대장암",
    guide: "/cancers/colorectal-cancer.html",
    check: "대장항문외과, 종양내과, 방사선종양학과 협진 여부",
  },
  {
    keys: ["위암", "위"],
    label: "위암",
    guide: "/cancers/stomach-cancer.html",
    check: "소화기내과, 위장관외과, 종양내과, 영양 상담 가능 여부",
  },
  {
    keys: ["간암", "간"],
    label: "간암",
    guide: "/cancers/liver-cancer.html",
    check: "간담췌외과, 소화기내과, 영상의학과, 종양내과 다학제 진료",
  },
  {
    keys: ["췌장암", "췌장"],
    label: "췌장암",
    guide: "/cancers/pancreatic-cancer.html",
    check: "간담췌외과, 소화기내과, 종양내과, 담도 배액 시술 가능 여부",
  },
  {
    keys: ["자궁경부암", "자궁경부"],
    label: "자궁경부암",
    guide: "/cancers/cervical-cancer.html",
    check: "부인암센터, 산부인과 종양 진료, 방사선종양학과 연계 여부",
  },
  {
    keys: ["난소암", "난소"],
    label: "난소암",
    guide: "/cancers/ovarian-cancer.html",
    check: "부인암센터, 종양내과, 유전 상담, 재발 관리 창구",
  },
  {
    keys: ["신장암", "신장"],
    label: "신장암",
    guide: "/cancers/kidney-cancer.html",
    check: "비뇨의학과, 종양내과, 부분절제 또는 표적·면역치료 상담 가능 여부",
  },
  {
    keys: ["방광암", "방광"],
    label: "방광암",
    guide: "/cancers/bladder-cancer.html",
    check: "비뇨의학과, 방광내시경, 방광내 주입치료, 요로전환 상담 가능 여부",
  },
];

function normalize(value) {
  return String(value || "").toLowerCase().trim();
}

function formatCount(value) {
  return new Intl.NumberFormat("ko-KR").format(value);
}

function formatDate(value) {
  const text = String(value || "");
  if (!/^\d{8}$/.test(text)) return "";
  return `${text.slice(0, 4)}.${text.slice(4, 6)}.${text.slice(6, 8)} 개설`;
}

function getMapUrl(hospital) {
  if (!hospital.address) return "";
  return `https://map.naver.com/p/search/${encodeURIComponent(hospital.address)}`;
}

function getMapPosition(hospital) {
  const longitude = Number(hospital.longitude);
  const latitude = Number(hospital.latitude);
  if (!Number.isFinite(longitude) || !Number.isFinite(latitude)) return null;

  const bounds = {
    minLng: 124.4,
    maxLng: 131.5,
    minLat: 33,
    maxLat: 39.2,
  };
  const x = ((longitude - bounds.minLng) / (bounds.maxLng - bounds.minLng)) * 100;
  const y = ((bounds.maxLat - latitude) / (bounds.maxLat - bounds.minLat)) * 100;
  return {
    x: Math.min(96, Math.max(4, x)),
    y: Math.min(94, Math.max(5, y)),
  };
}

function renderMapDetail(hospital) {
  if (!hospitalMapDetail) return;

  const mapUrl = getMapUrl(hospital);
  const website = hospital.website ? `<a class="text-link" href="${hospital.website}" target="_blank" rel="noopener">공식 홈페이지</a>` : "";
  const mapLink = mapUrl ? `<a class="text-link" href="${mapUrl}" target="_blank" rel="noopener">네이버 지도</a>` : "";
  hospitalMapDetail.innerHTML = `
    <span class="card-label">${hospital.type || "의료기관"} · ${hospital.sido || "지역 미상"}</span>
    <h3>${hospital.name}</h3>
    <p>${hospital.address || "주소 정보 확인 필요"}</p>
    <div class="hospital-meta">
      <span>${hospital.phone || "전화 확인 필요"}</span>
      ${hospital.district ? `<span>${hospital.district}</span>` : ""}
      ${hospital.doctorCount ? `<span>의사 ${formatCount(hospital.doctorCount)}명</span>` : ""}
      ${website}
      ${mapLink}
    </div>
  `;
}

function renderHospitalMap(filtered) {
  if (!hospitalMap || !hospitalMapDetail || !hospitalMapCount) return;

  const mapHospitals = filtered
    .filter((hospital) => getMapPosition(hospital))
    .sort((a, b) => {
      if (a.typeCode === b.typeCode) return String(a.name).localeCompare(String(b.name), "ko");
      return a.typeCode === "01" ? -1 : 1;
    })
    .slice(0, 120);

  hospitalMap.innerHTML = `
    <span class="map-region-label map-region-seoul">서울·경기</span>
    <span class="map-region-label map-region-gangwon">강원</span>
    <span class="map-region-label map-region-chungcheong">충청</span>
    <span class="map-region-label map-region-yeongnam">영남</span>
    <span class="map-region-label map-region-honam">호남</span>
    <span class="map-region-label map-region-jeju">제주</span>
  `;
  hospitalMapCount.textContent = `${formatCount(mapHospitals.length)}개 위치 표시`;

  mapHospitals.forEach((hospital, index) => {
    const position = getMapPosition(hospital);
    const marker = document.createElement("button");
    marker.type = "button";
    marker.className = `hospital-map-marker${hospital.typeCode === "01" ? " is-advanced" : ""}`;
    marker.style.left = `${position.x}%`;
    marker.style.top = `${position.y}%`;
    marker.title = hospital.name;
    marker.setAttribute("aria-label", `${hospital.name} 위치 보기`);
    marker.addEventListener("click", () => {
      hospitalMap.querySelectorAll(".hospital-map-marker").forEach((node) => node.classList.remove("is-active"));
      marker.classList.add("is-active");
      renderMapDetail(hospital);
    });
    hospitalMap.append(marker);

    if (index === 0) {
      marker.classList.add("is-active");
      renderMapDetail(hospital);
    }
  });

  if (!mapHospitals.length) {
    hospitalMapDetail.innerHTML = `
      <span class="card-label">No Result</span>
      <h3>표시할 위치가 없습니다</h3>
      <p>검색어 또는 지역 필터를 바꿔 다시 확인해 주세요.</p>
    `;
  }
}

function getDiagnosisSearch() {
  const query = normalize(search?.value);
  if (!query) return null;
  return diagnosisSearches.find((item) => item.keys.some((key) => query.includes(normalize(key))));
}

function hospitalMatches(hospital) {
  const query = normalize(search?.value);
  const diagnosis = getDiagnosisSearch();
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
    (!query || diagnosis || haystack.includes(query)) &&
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

function applyUrlFilters() {
  const params = new URLSearchParams(window.location.search);
  const queryValue = params.get("q") || params.get("keyword") || "";
  const regionValue = params.get("region") || params.get("sido") || "";
  const typeValue = params.get("type") || params.get("clCd") || "";

  search.value = queryValue;
  if (regionValue) region.value = regionValue;
  if (typeValue) type.value = typeValue;
}

function syncUrlFilters() {
  const params = new URLSearchParams();
  if (search.value.trim()) params.set("q", search.value.trim());
  if (region.value) params.set("region", region.value);
  if (type.value) params.set("type", type.value);

  const nextUrl = params.toString() ? `${window.location.pathname}?${params.toString()}` : window.location.pathname;
  window.history.replaceState({}, "", nextUrl);
}

function renderHospitals() {
  const diagnosis = getDiagnosisSearch();
  const filtered = hospitals.filter(hospitalMatches);
  count.textContent = `${formatCount(filtered.length)}개 병원`;
  list.innerHTML = "";
  renderHospitalMap(filtered);

  if (diagnosis) {
    const note = document.createElement("div");
    note.className = "notice";
    note.innerHTML = `
      <strong>${diagnosis.label} 검색어를 진단명으로 인식했습니다.</strong>
      <p>현재 병원 데이터는 병원명·주소·의료기관 구분 중심이라 특정 암 진료 가능 여부를 바로 판정하지 않습니다. 아래 병원 목록에서 지역을 좁힌 뒤 ${diagnosis.check}를 공식 홈페이지 또는 전화로 확인하세요.</p>
      <a class="text-link" href="${diagnosis.guide}">${diagnosis.label} 치료 흐름 먼저 보기</a>
    `;
    list.append(note);
  }

  filtered.slice(0, 80).forEach((hospital) => {
    const card = document.createElement("article");
    card.className = "hospital-card";
    const website = hospital.website ? `<a class="text-link" href="${hospital.website}" target="_blank" rel="noopener">공식 홈페이지</a>` : "";
    const mapUrl = getMapUrl(hospital);
    const mapLink = mapUrl ? `<a class="text-link" href="${mapUrl}" target="_blank" rel="noopener">지도에서 보기</a>` : "";
    const established = formatDate(hospital.establishedAt);
    card.innerHTML = `
      <div>
        <h3>${hospital.name}</h3>
        <p>${hospital.address || "주소 정보 확인 필요"}</p>
        <div class="hospital-meta">
          <span>${hospital.sido || "지역 미상"} ${hospital.district || ""}</span>
          <span>${hospital.phone || "전화 확인 필요"}</span>
          ${hospital.doctorCount ? `<span>의사 ${formatCount(hospital.doctorCount)}명</span>` : ""}
          ${established ? `<span>${established}</span>` : ""}
          ${hospital.postalCode ? `<span>우편번호 ${hospital.postalCode}</span>` : ""}
          ${website}
          ${mapLink}
        </div>
      </div>
      <span class="status">${hospital.type || "의료기관"}</span>
    `;
    list.append(card);
  });

  if (filtered.length > 80) {
    const note = document.createElement("p");
    note.className = "muted";
    note.textContent = diagnosis
      ? `검색 속도를 위해 상위 80개만 표시합니다. 지역 또는 구분 필터를 선택하면 결과를 더 좁힐 수 있습니다.`
      : `검색 속도를 위해 상위 80개만 표시합니다. 검색어를 입력하면 결과를 더 좁힐 수 있습니다.`;
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
    applyUrlFilters();
    renderHospitals();
  } catch (error) {
    panel.hidden = false;
    list.innerHTML = `<div class="notice">병원 데이터 파일을 불러오지 못했습니다. 잠시 후 다시 확인해 주세요.</div>`;
    count.textContent = "데이터 확인 필요";
  }
}

[search, region, type].forEach((control) => {
  control?.addEventListener("input", () => {
    syncUrlFilters();
    renderHospitals();
  });
});

loadHospitals();
