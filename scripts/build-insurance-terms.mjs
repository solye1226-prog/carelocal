import { mkdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { articles } from './insurance-terms-data.mjs';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const origin = 'https://hospital.hbuby.com';
const escape = value => String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const link = ([label, href]) => `<a href="${escape(href)}"${href.startsWith('https:') ? ' target="_blank" rel="noopener"' : ''}>${escape(label)}</a>`;
const pathOf = a => `/${a.section}/${a.slug}`;
const imagePath = (a, type) => `/assets/images/terms-${a.slug}-${type}.webp`;
const category = a => a.section === 'silbi' ? '실비보험' : '약관·기준';
const header = `<header class="site-header"><nav class="nav" aria-label="주요 메뉴"><a class="brand" href="/"><span class="brand-mark">CL</span><span><strong>케어로컬</strong><small>보험 정보 자료실</small></span></a><div class="nav-links"><a href="/claims/">보험금 청구</a><a href="/silbi/">실비보험</a><a href="/diagnosis-benefit/">진단비</a><a href="/surgery-benefit/">수술비</a><a href="/standards/">약관·기준</a></div></nav></header>`;
const cta = `<div class="insurance-company-cta"><a href="/insurance-companies/">보험사별 공식 홈페이지 확인하기</a></div><section class="kakao-inquiry-cta" aria-labelledby="contact-title"><p class="cta-label">문의 안내 <span>보험</span></p><h2 id="contact-title">가입한 보험의 보장이 궁금하신가요?</h2><p>가입한 보험의 보장 내용이나 콘텐츠와 관련해 궁금한 점이 있다면 카카오톡으로 문의해 주세요. 주민등록번호·진단서·영수증 등 민감한 개인정보가 포함된 자료는 전송하지 않는 것을 권장합니다.</p><a class="kakao-button" href="https://open.kakao.com/o/sVyT7uph" target="_blank" rel="noopener">카카오톡으로 문의하기</a></section>`;
const head = (title, description, path, extra = '') => `<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${escape(title)}</title><meta name="description" content="${escape(description)}"><link rel="canonical" href="${origin}${path}"><link rel="stylesheet" href="/assets/site.css?v=20260922-terms-v2"><link rel="stylesheet" href="/assets/insurance-terms.css?v=20260922-1">${extra}<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2258793659580551" crossorigin="anonymous"></script></head><body>${header}`;
const figure = (a, type, alt) => `<figure class="guide-image-panel"><img src="${imagePath(a, type)}" width="1672" height="941" loading="${type === 'thumb' ? 'eager' : 'lazy'}" decoding="async" alt="${escape(alt)}"></figure>`;

if (articles.length !== 17 || articles.some((a, i) => a.order !== i + 4)) throw new Error('Expected series order 4 through 20');
if (!process.argv.includes('--allow-missing-images')) {
  for (const a of articles) for (const type of ['thumb', 'body1', 'body2']) {
    if (!existsSync(join(root, imagePath(a, type)))) throw new Error(`Missing image: ${a.slug} ${type}`);
  }
}

for (const a of articles) {
  const schema = {
    '@context': 'https://schema.org', '@type': 'Article', headline: a.title,
    description: a.description, mainEntityOfPage: origin + pathOf(a),
    image: ['thumb', 'body1', 'body2'].map(type => origin + imagePath(a, type)),
    author: { '@type': 'Organization', name: '케어로컬', url: origin + '/' },
    publisher: { '@type': 'Organization', name: '케어로컬' }, inLanguage: 'ko-KR'
  };
  const table = `<table><caption>${escape(a.tableTitle)}</caption><thead><tr><th scope="col">구분</th><th scope="col">뜻과 기준</th><th scope="col">확인할 점</th></tr></thead><tbody>${a.rows.map(row => `<tr>${row.map((cell, i) => `<td data-label="${['구분', '뜻과 기준', '확인할 점'][i]}">${escape(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
  const sections = a.sections.map(([title, ...paragraphs], index) => `<section aria-labelledby="section-${index + 1}"><h2 id="section-${index + 1}">${escape(title)}</h2>${paragraphs.map(p => `<p>${escape(p)}</p>`).join('\n')}${index === 0 ? figure(a, 'body1', a.scenes[0]) : index === 2 ? figure(a, 'body2', a.scenes[1]) : ''}</section>`).join('\n');
  const extras = `<meta property="og:type" content="article"><meta property="og:locale" content="ko_KR"><meta property="og:title" content="${escape(a.title)}"><meta property="og:description" content="${escape(a.description)}"><meta property="og:url" content="${origin}${pathOf(a)}"><meta property="og:image" content="${origin}${imagePath(a, 'thumb')}"><script type="application/ld+json">${JSON.stringify(schema).replaceAll('<', '\\u003c')}</script>`;
  const html = `${head(a.title, a.description, pathOf(a), extras)}
<main class="section article-body insurance-series-article terms-article"><div class="breadcrumb"><a href="/">홈</a> / <a href="/${a.section}/">${category(a)}</a> / ${escape(a.keyword)}</div><p class="eyebrow">보험 용어</p><h1>${escape(a.title)}</h1><p class="lead">${escape(a.lead)}</p><p class="article-byline">작성: 케어로컬</p>
${figure(a, 'thumb', a.cover.replace('\n', ', ') + ' 카드뉴스')}
<nav class="terms-toc" aria-label="본문 목차"><strong>이 글의 내용</strong><ol>${a.sections.map(([title], i) => `<li><a href="#section-${i + 1}">${escape(title)}</a></li>`).join('')}</ol></nav>
${table}
${sections}
<h2>내 계약에서 확인할 순서</h2><ol>${a.checks.map(c => `<li>${escape(c)}</li>`).join('')}</ol>
<h2>자주 묻는 질문</h2><div class="faq">${a.faqs.map(([q, answer]) => `<details><summary>${escape(q)}</summary><p>${escape(answer)}</p></details>`).join('')}</div>
<h2>함께 보면 좋은 글</h2><ul class="terms-related">${a.related.map(item => `<li>${link(item)}</li>`).join('')}</ul>
<h2>공식 확인처</h2><ul class="terms-sources">${a.sources.map(item => `<li>${link(item)}</li>`).join('')}</ul>
<div class="notice">본 콘텐츠는 일반적인 보험 정보 제공을 목적으로 작성되었습니다. 보험금 지급 여부는 가입 상품, 약관, 가입 시기와 심사 기준에 따라 달라질 수 있습니다. 정확한 보장 여부는 개별 계약과 약관 확인이 필요합니다. 가상 예시와 개별 상품의 설명은 모든 계약에 공통으로 적용되는 지급 기준이 아닙니다.</div>
${cta}</main></body></html>\n`;
  writeFileSync(join(root, a.section, `${a.slug}.html`), html, 'utf8');
  console.log(`${a.order}. ${pathOf(a)} (${a.sections.flat().join('').length} section characters)`);
}

const firstArticle = { section: 'standards', slug: 'actual-vs-fixed-benefit', title: '실손보상과 정액보상 차이, 실비보험·진단비는 어떻게 다를까?', description: '실제 의료비를 기준으로 하는 보상과 약정한 금액을 확인하는 보상의 차이를 비교합니다.', thumbnail: '/assets/images/actual-vs-fixed-benefit-thumb.png' };
const standardArticles = [firstArticle, ...articles.filter(a => a.section === 'standards')];
const card = a => `<article class="article-card has-thumb"><a class="post-card" href="${pathOf(a)}"><figure class="post-thumb"><img src="${a.thumbnail || imagePath(a, 'thumb')}" width="1672" height="941" loading="lazy" decoding="async" alt="${escape(a.cover?.replace('\n', ', ') || a.title)}"></figure><div class="post-card-body"><p class="meta">보험 용어</p><h2>${escape(a.title)}</h2><p>${escape(a.description)}</p></div></a></article>`;
const pagePath = page => page === 1 ? '/standards/' : `/standards/page/${page}/`;
const pages = Math.ceil(standardArticles.length / 9);
for (let page = 1; page <= pages; page++) {
  const title = page === 1 ? '보험 용어와 약관·기준' : `보험 용어와 약관·기준 ${page}페이지`;
  const description = '보험가액, 고지의무, 주계약·특약, 갱신, 자동차보험 담보 등 헷갈리는 보험 용어를 사례와 비교표로 확인하세요.';
  const items = standardArticles.slice((page - 1) * 9, page * 9);
  const pagination = `<nav class="pagination" aria-label="글 목록 페이지">${Array.from({ length: pages }, (_, i) => i + 1).map(i => i === page ? `<span aria-current="page">${i}</span>` : `<a href="${pagePath(i)}" aria-label="${i}페이지">${i}</a>`).join('')}</nav>`;
  const rel = (page > 1 ? `<link rel="prev" href="${origin}${pagePath(page - 1)}">` : '') + (page < pages ? `<link rel="next" href="${origin}${pagePath(page + 1)}">` : '');
  const extraGuides = page === 1 ? `<h2>함께 확인할 기준</h2><ul class="terms-related"><li><a href="/underwriting/">유병자보험 고지 기준</a></li><li><a href="/underwriting/simplified-health-insurance-cancer-brain.html">간편심사보험 치료비</a></li><li><a href="/surgery-benefit/surgery-classification">수술분류표</a></li><li><a href="/diagnosis-benefit/">진단코드와 진단비</a></li><li><a href="/silbi/covered-vs-noncovered-medical-costs">급여와 비급여 차이</a></li><li><a href="/silbi/deductible-vs-copayment">자기부담금과 공제금액</a></li></ul>` : '';
  const html = `${head(title + ' | 케어로컬', description, pagePath(page), rel)}<main class="section article-body terms-index"><div class="breadcrumb"><a href="/">홈</a> / <a href="/standards/">약관·기준</a>${page > 1 ? ` / ${page}페이지` : ''}</div><h1>${title}</h1><p class="lead">보험증권과 약관에서 만나는 용어의 뜻, 서로 다른 보상 기준과 확인 방법을 살펴보세요.</p><div class="article-feed">${items.map(card).join('\n')}</div>${pagination}${extraGuides}</main></body></html>\n`;
  const folder = join(root, pagePath(page));
  mkdirSync(folder, { recursive: true });
  writeFileSync(join(folder, 'index.html'), html, 'utf8');
}

// Only the marked block is generated; existing category content stays untouched.
const silbiFile = join(root, 'silbi', 'index.html');
let silbiHtml = readFileSync(silbiFile, 'utf8');
const start = '<!-- insurance-terms:start -->';
const end = '<!-- insurance-terms:end -->';
const block = `${start}\n<h2>실비보험 비용 용어</h2><ul class="terms-related">${articles.filter(a => a.section === 'silbi').map(a => `<li>${link([a.title, pathOf(a)])}</li>`).join('')}</ul>\n${end}`;
if (silbiHtml.includes(start)) silbiHtml = silbiHtml.slice(0, silbiHtml.indexOf(start)) + block + silbiHtml.slice(silbiHtml.indexOf(end) + end.length);
else silbiHtml = silbiHtml.replace('      <h2>실비보험 주요 글</h2>', block + '\n      <h2>실비보험 주요 글</h2>');
writeFileSync(silbiFile, silbiHtml, 'utf8');

const manifest = articles.map(a => ({ order: a.order, title: a.title, keyword: a.keyword, path: pathOf(a), sources: a.sources, images: ['thumb', 'body1', 'body2'].map(type => imagePath(a, type)) }));
writeFileSync(join(root, 'docs', 'insurance-terms-manifest.json'), JSON.stringify(manifest, null, 2) + '\n', 'utf8');
