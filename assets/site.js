const hospitalCards = Array.from(document.querySelectorAll("[data-hospital-card]"));
const searchInput = document.querySelector("[data-search]");
const districtSelect = document.querySelector("[data-district]");
const departmentSelect = document.querySelector("[data-department]");

function normalize(value) {
  return String(value || "").toLowerCase().trim();
}

function filterHospitals() {
  const query = normalize(searchInput?.value);
  const district = normalize(districtSelect?.value);
  const department = normalize(departmentSelect?.value);

  hospitalCards.forEach((card) => {
    const text = normalize(card.textContent);
    const cardDistrict = normalize(card.dataset.district);
    const cardDepartment = normalize(card.dataset.department);

    const matchesQuery = !query || text.includes(query);
    const matchesDistrict = !district || cardDistrict === district;
    const matchesDepartment = !department || cardDepartment === department;

    card.hidden = !(matchesQuery && matchesDistrict && matchesDepartment);
  });
}

[searchInput, districtSelect, departmentSelect].forEach((control) => {
  control?.addEventListener("input", filterHospitals);
});
