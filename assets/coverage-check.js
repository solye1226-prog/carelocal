const coverageCheck = document.querySelector("[data-coverage-check]");

if (coverageCheck) {
  const result = coverageCheck.querySelector("[data-coverage-result]");
  const items = Array.from(coverageCheck.querySelectorAll("[data-coverage-item]"));

  function updateCoverageResult() {
    const checkedCount = items.filter((item) => item.checked).length;
    result.textContent = `확인이 필요한 항목 ${checkedCount}개`;
  }

  items.forEach((item) => item.addEventListener("change", updateCoverageResult));
  updateCoverageResult();
}
