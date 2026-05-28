import { mkdir, writeFile } from "node:fs/promises";

const HIRA_ENDPOINT = "http://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList";
const OUT_FILE = new URL("../data/hospitals.json", import.meta.url);

const TAGS = [
  "ykiho",
  "yadmNm",
  "addr",
  "telno",
  "hospUrl",
  "clCd",
  "clCdNm",
  "sidoCd",
  "sidoCdNm",
  "sgguCd",
  "sgguCdNm",
  "emdongNm",
  "postNo",
  "estbDd",
  "drTotCnt",
  "XPos",
  "YPos",
];

const TARGETS = [
  { clCd: "01", label: "상급종합병원", numOfRows: 120 },
  { clCd: "11", label: "종합병원", numOfRows: 450 },
];

function xmlDecode(value) {
  return String(value || "")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function tagValue(xml, tag) {
  const match = xml.match(new RegExp(`<${tag}>([\\s\\S]*?)<\\/${tag}>`));
  return match ? xmlDecode(match[1].trim()) : "";
}

function parseItems(xml) {
  const items = [];
  const itemRegex = /<item>([\s\S]*?)<\/item>/g;
  let match;

  while ((match = itemRegex.exec(xml)) !== null) {
    const itemXml = match[1];
    const item = {};
    TAGS.forEach((tag) => {
      item[tag] = tagValue(itemXml, tag);
    });
    items.push({
      id: item.ykiho || `${item.yadmNm}-${item.addr}`,
      name: item.yadmNm,
      type: item.clCdNm,
      typeCode: item.clCd,
      address: item.addr,
      phone: item.telno,
      website: item.hospUrl,
      sido: item.sidoCdNm,
      sidoCode: item.sidoCd,
      district: item.sgguCdNm,
      districtCode: item.sgguCd,
      neighborhood: item.emdongNm,
      postalCode: item.postNo,
      establishedAt: item.estbDd,
      doctorCount: Number(item.drTotCnt) || null,
      longitude: item.XPos ? Number(item.XPos) : null,
      latitude: item.YPos ? Number(item.YPos) : null,
    });
  }

  return {
    resultCode: tagValue(xml, "resultCode"),
    resultMsg: tagValue(xml, "resultMsg"),
    totalCount: Number(tagValue(xml, "totalCount")) || items.length,
    items,
  };
}

async function fetchWithTimeout(url, timeoutMs = 45000) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(url, { signal: controller.signal });
    return await response.text();
  } finally {
    clearTimeout(timeout);
  }
}

async function fetchHospitals(target, serviceKey) {
  const params = new URLSearchParams({
    ServiceKey: serviceKey,
    pageNo: "1",
    numOfRows: String(target.numOfRows),
    clCd: target.clCd,
  });
  const xml = await fetchWithTimeout(`${HIRA_ENDPOINT}?${params.toString()}`);
  const parsed = parseItems(xml);

  if (parsed.resultCode && parsed.resultCode !== "00") {
    throw new Error(`${target.label} fetch failed: ${parsed.resultCode} ${parsed.resultMsg}`);
  }

  return parsed.items;
}

function sortHospitals(a, b) {
  return (
    String(a.sido || "").localeCompare(String(b.sido || ""), "ko") ||
    String(a.district || "").localeCompare(String(b.district || ""), "ko") ||
    String(a.name || "").localeCompare(String(b.name || ""), "ko")
  );
}

async function main() {
  const serviceKey = String(process.env.HIRA_SERVICE_KEY || "").replace(/\s+/g, "");
  if (!serviceKey) {
    throw new Error("HIRA_SERVICE_KEY environment variable is required.");
  }

  const allItems = [];
  for (const target of TARGETS) {
    console.log(`Fetching ${target.label}...`);
    allItems.push(...(await fetchHospitals(target, serviceKey)));
  }

  const deduped = Array.from(new Map(allItems.map((item) => [item.id, item])).values()).sort(sortHospitals);
  const byRegion = deduped.reduce((acc, item) => {
    const key = item.sido || "기타";
    acc[key] = (acc[key] || 0) + 1;
    return acc;
  }, {});

  const payload = {
    source: "건강보험심사평가원_병원정보서비스",
    generatedAt: new Date().toISOString(),
    refreshGuide: "병원 기본정보는 HIRA API로 수동 또는 예약 갱신합니다.",
    scope: ["상급종합병원", "종합병원"],
    count: deduped.length,
    byRegion,
    hospitals: deduped,
  };

  await mkdir(new URL("../data/", import.meta.url), { recursive: true });
  await writeFile(OUT_FILE, `${JSON.stringify(payload, null, 2)}\n`, "utf8");
  console.log(`Wrote ${deduped.length} hospitals to ${OUT_FILE.pathname}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
