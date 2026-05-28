const HIRA_ENDPOINT = "https://apis.data.go.kr/B551182/hospInfoService/getHospBasisList";

const TAGS = [
  "yadmNm",
  "addr",
  "telno",
  "hospUrl",
  "clCd",
  "clCdNm",
  "dgsbjtCd",
  "dgsbjtCdNm",
  "sidoCd",
  "sidoCdNm",
  "sgguCd",
  "sgguCdNm",
  "emdongNm",
  "postNo",
  "XPos",
  "YPos",
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

function parseHospitals(xml) {
  const items = [];
  const itemRegex = /<item>([\s\S]*?)<\/item>/g;
  let match;

  while ((match = itemRegex.exec(xml)) !== null) {
    const itemXml = match[1];
    const item = {};
    TAGS.forEach((tag) => {
      item[tag] = tagValue(itemXml, tag);
    });
    items.push(item);
  }

  return {
    totalCount: Number(tagValue(xml, "totalCount")) || items.length,
    pageNo: Number(tagValue(xml, "pageNo")) || 1,
    numOfRows: Number(tagValue(xml, "numOfRows")) || items.length,
    items,
  };
}

function json(data, init = {}) {
  return new Response(JSON.stringify(data, null, 2), {
    ...init,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=300, s-maxage=86400",
      ...(init.headers || {}),
    },
  });
}

export async function onRequestGet(context) {
  const serviceKey = context.env.HIRA_SERVICE_KEY;

  if (!serviceKey) {
    return json(
      {
        error: "HIRA_SERVICE_KEY is not configured.",
        help: "Cloudflare Pages > Settings > Variables and Secrets에서 HIRA_SERVICE_KEY를 추가하세요.",
      },
      { status: 500 },
    );
  }

  const requestUrl = new URL(context.request.url);
  const incoming = requestUrl.searchParams;
  const params = new URLSearchParams({
    pageNo: incoming.get("pageNo") || "1",
    numOfRows: incoming.get("numOfRows") || "10",
  });

  const allowedParams = [
    "sidoCd",
    "sgguCd",
    "emdongNm",
    "yadmNm",
    "zipCd",
    "clCd",
    "dgsbjtCd",
    "xPos",
    "yPos",
    "radius",
  ];

  allowedParams.forEach((name) => {
    const value = incoming.get(name);
    if (value) params.set(name, value);
  });

  const keyword = incoming.get("q");
  if (keyword && !params.has("yadmNm")) {
    params.set("yadmNm", keyword);
  }

  const encodedKey = serviceKey.includes("%") ? serviceKey : encodeURIComponent(serviceKey);
  const hiraUrl = `${HIRA_ENDPOINT}?ServiceKey=${encodedKey}&${params.toString()}`;
  const hiraResponse = await fetch(hiraUrl, {
    headers: { accept: "application/xml,text/xml,*/*" },
  });
  const xml = await hiraResponse.text();

  if (!hiraResponse.ok) {
    return json(
      {
        error: "HIRA request failed.",
        status: hiraResponse.status,
        body: xml.slice(0, 800),
      },
      { status: 502 },
    );
  }

  return json({
    source: "건강보험심사평가원_병원정보서비스",
    query: Object.fromEntries(params),
    ...parseHospitals(xml),
  });
}
