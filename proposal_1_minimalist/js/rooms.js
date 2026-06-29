/* Tabakvest 85 — reads rooms.json and renders rooms grid + room detail with availability filter. */
const EUR = n => '\u20ac ' + Number(n).toLocaleString('nl-BE');
const statusLabel = s => s === 'vrij' ? 'Vrij' : 'Verhuurd';
let allRooms = [];
let currentFilter = 'all';

async function loadRooms() {
  const res = await fetch('rooms.json');
  return (await res.json());
}

function buildRoomCard(r) {
  const cover = `pictures/kamer ${r.id}/${(r.images && r.images[0]) || '1.jpg'}`;
  const thumbAlt = `${r.name}: ${r.size}m² - ${EUR(r.rent)} per maand`;
  return `<article class="room-card">
    <a href="room-${r.id}.html">
      <div class="thumb"><img src="${cover}" alt="${thumbAlt}" loading="lazy"></div>
      <div class="body">
        <span class="type">${r.type || ''}</span>
        <h3>${r.name}</h3>
        <div class="row">
          <span class="price">${EUR(r.rent)} <small>/ maand</small></span>
          <span class="status ${r.status}">${statusLabel(r.status)}</span>
        </div>
      </div>
    </a>
  </article>`;
}

function filterGrid(filter) {
  currentFilter = filter;
  const filtered = filter === 'all' ? allRooms : allRooms.filter(r => r.status === filter);
  const grid = document.querySelector('.rooms-grid');
  if (!grid) return;
  if (filtered.length === 0) {
    grid.innerHTML = '<p class="loading" style="grid-column: 1/-1; text-align: center;">Geen kamers beschikbaar met deze filter.</p>';
  } else {
    grid.innerHTML = filtered.map(buildRoomCard).join('');
  }
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.filter === filter);
  });
}

function buildDetail(data) {
  const wrap = document.querySelector('.room-detail');
  if (!wrap) return;
  const r = data.rooms.find(x => x.id === window.ROOM_ID);
  if (!r) { wrap.innerHTML = '<p class="loading">Kamer niet gevonden.</p>'; return; }
  const s = data.settings;
  document.title = `${r.name} — Tabakvest 85`;
  const imgs = (r.images && r.images.length ? r.images : ['1.jpg']);
  const roomAlt = `${r.name}: ${r.size}m²${r.loft ? ' + ' + r.loft + 'm² ' : ''}${r.type || ''}`;
  const slides = imgs.map(f => `<img src="pictures/kamer ${r.id}/${f}" alt="${roomAlt}" loading="lazy" data-glightbox="gallery=room${r.id}">`).join('');
  const dots = imgs.map((_, i) => `<button data-i="${i}" class="${i===0?'active':''}" aria-label="Foto ${i+1}"></button>`).join('');
  const highlights = (r.highlights || []).map(h => `<li>${h}</li>`).join('');
  wrap.innerHTML = `
    <div class="page-hero"><div class="container">
      <h1>${r.name}</h1><p>${r.type || ''}</p>
    </div></div>
    <div class="container">
      <div class="detail-meta">
        <div><div class="k">Grootte</div><div class="v">${r.size} m²</div></div>
        <div><div class="k">Huur</div><div class="v">${EUR(r.rent)}</div></div>
        <div><div class="k">Kosten</div><div class="v">${EUR(r.costs)}</div></div>
        <div><div class="k">Status</div><div class="v"><span class="status ${r.status}">${statusLabel(r.status)}</span></div></div>
      </div>
      <div class="carousel"><div class="carousel-track">${slides}</div>
        <button class="carousel-btn prev" aria-label="Vorige"><i class="fas fa-chevron-left"></i></button>
        <button class="carousel-btn next" aria-label="Volgende"><i class="fas fa-chevron-right"></i></button>
        <span class="carousel-count">1 / ${imgs.length}</span>
      </div>
      <div class="carousel-dots">${dots}</div>
      <div class="detail-body">
        <h2>Omschrijving</h2><p>${r.description || ''}</p>
        <h2>Bijzonderheden</h2><ul>${highlights}</ul>
        <h2>Technische fiche</h2>
        <div class="spec-grid">
          <div><span>Oppervlakte</span><span>${r.size} m²</span></div>
          <div><span>Hoogslaper</span><span>${r.loft||'-'} m²</span></div>
          <div><span>Maandelijkse huur</span><span>${EUR(r.rent)}</span></div>
          <div><span>Kosten (${s.costsInclude})</span><span>${EUR(r.costs)}/maand</span></div>
          <div><span>Huurwaarborg</span><span>${s.deposit}</span></div>
          <div><span>Huurperiode</span><span>${s.rentalPeriod}</span></div>
          <div><span>Keuken</span><span>Gemeenschappelijk</span></div>
          <div><span>Internet</span><span>Gigabit WiFi</span></div>
        </div>
        <div class="detail-cta">
          <h2>Interesse in ${r.name}?</h2>
          <a href="index.html#contact" class="btn btn-primary">Neem contact op</a>
          <a href="rooms.html" class="btn btn-secondary">Andere kamers</a>
        </div>
      </div>
    </div>`;
  initCarousel(imgs.length);
}

function initCarousel(count) {
  const track = document.querySelector('.carousel-track');
  if (!track || count < 1) return;
  const dots = [...document.querySelectorAll('.carousel-dots button')];
  const counter = document.querySelector('.carousel-count');
  let i = 0;
  const go = n => { i = (n + count) % count; track.style.transform = `translateX(-${i*100}%)`;
    dots.forEach((d,x) => d.classList.toggle('active', x===i)); if (counter) counter.textContent = `${i+1} / ${count}`; };
  document.querySelector('.carousel-btn.next').onclick = () => go(i+1);
  document.querySelector('.carousel-btn.prev').onclick = () => go(i-1);
  dots.forEach(d => d.onclick = () => go(+d.dataset.i));
  document.addEventListener('keydown', e => { if (e.key==='ArrowRight') go(i+1); if (e.key==='ArrowLeft') go(i-1); });
}

loadRooms().then(data => {
  allRooms = data.rooms;
  const filterBtns = document.querySelectorAll('.filter-btn');
  filterBtns.forEach(btn => btn.addEventListener('click', () => filterGrid(btn.dataset.filter)));
  filterGrid('all');
  buildDetail(data);
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
}).catch(() => { const e = document.querySelector('.loading'); if (e) e.textContent = 'Kon kamergegevens niet laden.'; });
