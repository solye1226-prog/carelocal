const homeHospitalMap = document.querySelector("[data-home-hospital-map]");
const homeHospitalMapDetail = document.querySelector("[data-home-hospital-map-detail]");
const homeHospitalMapCount = document.querySelector("[data-home-hospital-map-count]");

const homeRegionMapPositions = {
  서울: { x: 42, y: 28 },
  경기: { x: 34, y: 35 },
  인천: { x: 25, y: 33 },
  강원: { x: 60, y: 24 },
  충북: { x: 47, y: 46 },
  충남: { x: 32, y: 52 },
  대전: { x: 42, y: 56 },
  세종시: { x: 39, y: 50 },
  전북: { x: 36, y: 65 },
  전남: { x: 32, y: 79 },
  광주: { x: 27, y: 74 },
  경북: { x: 62, y: 55 },
  대구: { x: 60, y: 66 },
  경남: { x: 56, y: 77 },
  울산: { x: 72, y: 72 },
  부산: { x: 67, y: 83 },
  제주: { x: 30, y: 94 },
};

function homeFormatCount(value) {
  return new Intl.NumberFormat("ko-KR").format(value);
}

function renderHomeMapDetail(regionName, regionHospitals) {
  if (!homeHospitalMapDetail) return;

  const advancedCount = regionHospitals.filter((hospital) => hospital.typeCode === "01").length;
  const samples = regionHospitals
    .slice(0, 4)
    .map((hospital) => `<li>${hospital.name}<small>${hospital.type || "의료기관"}</small></li>`)
    .join("");
  const regionUrl = `/hospitals/?region=${encodeURIComponent(regionName)}`;

  homeHospitalMapDetail.innerHTML = `
    <span class="card-label">Region Map</span>
    <h3>${regionName} 병원 ${homeFormatCount(regionHospitals.length)}곳</h3>
    <p>상급종합병원 ${homeFormatCount(advancedCount)}곳, 종합병원 ${homeFormatCount(regionHospitals.length - advancedCount)}곳을 현재 데이터에서 확인할 수 있습니다.</p>
    <ul class="map-sample-list">${samples}</ul>
    <a class="map-filter-button" href="${regionUrl}">${regionName} 병원 목록 보기</a>
  `;
}

function renderHomeHospitalMap(hospitals) {
  if (!homeHospitalMap || !homeHospitalMapDetail || !homeHospitalMapCount) return;

  const byRegion = new Map();
  hospitals.forEach((hospital) => {
    if (!hospital.sido || !homeRegionMapPositions[hospital.sido]) return;
    if (!byRegion.has(hospital.sido)) byRegion.set(hospital.sido, []);
    byRegion.get(hospital.sido).push(hospital);
  });

  homeHospitalMap.innerHTML = "";
  homeHospitalMapCount.textContent = `${homeFormatCount(hospitals.length)}개 병원`;

  const entries = Array.from(byRegion.entries()).sort((a, b) => b[1].length - a[1].length);
  entries.forEach(([regionName, regionHospitals], index) => {
    const position = homeRegionMapPositions[regionName];
    const marker = document.createElement("button");
    marker.type = "button";
    marker.className = "hospital-map-region";
    marker.style.left = `${position.x}%`;
    marker.style.top = `${position.y}%`;
    marker.setAttribute("aria-label", `${regionName} 병원 ${regionHospitals.length}곳 보기`);
    marker.innerHTML = `<strong>${regionName}</strong><span>${homeFormatCount(regionHospitals.length)}</span>`;
    marker.addEventListener("click", () => {
      homeHospitalMap.querySelectorAll(".hospital-map-region").forEach((node) => node.classList.remove("is-active"));
      marker.classList.add("is-active");
      renderHomeMapDetail(regionName, regionHospitals);
    });
    homeHospitalMap.append(marker);

    if (index === 0) {
      marker.classList.add("is-active");
      renderHomeMapDetail(regionName, regionHospitals);
    }
  });
}

async function loadHomeHospitalMap() {
  if (!homeHospitalMap) return;

  try {
    const response = await fetch("/data/hospitals.json", { cache: "no-store" });
    if (!response.ok) throw new Error("병원 데이터를 불러오지 못했습니다.");
    const data = await response.json();
    const hospitals = Array.isArray(data.hospitals) ? data.hospitals : [];
    renderHomeHospitalMap(hospitals);
  } catch (error) {
    if (homeHospitalMapCount) homeHospitalMapCount.textContent = "지도 오류";
    if (homeHospitalMapDetail) {
      homeHospitalMapDetail.innerHTML = `
        <span class="card-label">Map Guide</span>
        <h3>지도를 불러오지 못했습니다</h3>
        <p>잠시 후 다시 시도하거나 전체 병원 찾기 페이지에서 지역을 선택해 주세요.</p>
      `;
    }
  }
}

loadHomeHospitalMap();
