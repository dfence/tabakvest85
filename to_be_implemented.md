# To Be Implemented — Tabakvest 85
## Complete Implementation Roadmap for Proposals 1, 4 & 5

> **Status:** All items documented, awaiting implementation instructions.
> **Scope:** Only proposals 1 (minimalist), 4 (boutique), 5 (cinematic).
> **Note:** No changes have been made yet. User will specify priority and execution order.

---

## SECTION A: SEO & METADATA (High Priority)

### A1. Fix `lang` Attribute ✅ QUICK WIN
**Current Issue:** `index.html` in all proposals has `lang="en"` instead of `lang="nl"`.

**Implementation:**
- Change `<html lang="en">` → `<html lang="nl">` in:
  - `proposal_1_minimalist/index.html`
  - `proposal_4_boutique/index.html`
  - `proposal_5_cinematic/index.html`
  - `proposal_1_minimalist/rooms.html`, `room-1.html` through `room-9.html`, `locatie.html`
  - `proposal_4_boutique/rooms.html`, `room-1.html` through `room-9.html`, `locatie.html`
  - `proposal_5_cinematic/rooms.html`, `room-1.html` through `room-9.html`, `locatie.html`

**Impact:** Helps screen readers and Google understand language. Takes ~5 min.

---

### A2. Add Keyword-Friendly `<title>` Tags
**Current Issue:** Generic titles like "Tabakvest 85" or "Onze Kamers — Tabakvest 85".

**Recommended Titles (all proposals, same content):**
- **Homepage (`index.html`):** `"Studentenkamers Antwerpen centrum | Tabakvest 85 – Moderne kamers met eigen badkamer"`
- **Kamers page (`rooms.html`):** `"9 Studentenkamers in Antwerpen | Tabakvest 85 – Eigen badkamer & Gigabit Internet + WiFi"`
- **Room detail pages (`room-1.html` through `room-9.html`):**
  - Kamer 1: `"Kamer 1 – 22m² (+ 11m² hoogslaper) | Studentenkamer Antwerpen | €536/maand"`
  - Kamer 2: `"Kamer 2 – 24m² (+ 8m² hoogslaper) met terrasje | Studentenkamer | €612/maand"`
  - Kamer 3: `"Kamer 3 – 20m² (+ 12m² duplex) | Tussenverdieping | Studentenkamer | €592/maand"`
  - _(Continue pattern for rooms 4–9)_
- **Locatie page (`locatie.html`):** `"Locatie Tabakvest 85 | Hartje Antwerpen – Hogescholen, Meir, Leopoldplaats"`

**Files to update:** All 6 HTML files × 3 proposals = 18 files total (but 6 unique titles per proposal type).

**Impact:** Major SEO boost; improves CTR in search results. 30 min.

---

### A3. Add Unique Meta Descriptions
**Current Issue:** No `<meta name="description">` tags on any page.

**Recommended Descriptions (all proposals, same content):**

| Page | Description |
|------|-------------|
| **Homepage** | "Moderne, chique studentenkamers in Antwerpen met eigen badkamer, gigabit internet en Vlaams kwaliteitslabel. Huur vanaf €536/maand. Beschikbaar 15/09." |
| **Kamers** | "Bekijk onze 9 studentenkamers in hartje Antwerpen. Alle kamers hebben badkamer, verwarming en internet inbegrepen. Filter op beschikbaarheid." |
| **Kamer 1** | "Kamer 1: 22 m² (+ 11 m² hoogslaper) gelijkvloers voorzijde. Eigen badkamer, groot raam. Huur €536/maand incl. kosten." |
| **Kamer 2** | "Kamer 2: 24 m² (+ 8 m² hoogslaper) gelijkvloers met privé-terrasje. Dubbel raam, badkamer. Huur €612/maand incl. kosten." |
| **Kamer 3** | "Kamer 3: 20 m² duplex (+ 12 m² tussenverdieping). Rustig achteraan. Eigen badkamer. Huur €592/maand incl. kosten." |
| **Kamer 4** | "Kamer 4: 16 m² (+ 8 m² hoogslaper) 1e verdieping. Moderne inrichting, afgesloten badkamer. Huur €535/maand incl. kosten." |
| **Kamer 5** | "Kamer 5: 22 m² (+ 8 m² loft) voorkant met 3 grote ramen. Licht, ruim, geschikt voor 2. Huur €612/maand incl. kosten." |
| **Kamer 6** | "Kamer 6: 28 m² (+ 8 m² loft) 2e verdieping. Ruim, aparte tv-hoek. Voor 2 personen. Huur €630/maand incl. kosten." |
| **Kamer 7** | "Kamer 7: 22 m² (+ 8 m² loft) 2e verdieping voorkant. 3 grote ramen, veel licht. Voor 2. Huur €606/maand incl. kosten." |
| **Kamer 8** | "Kamer 8: 18 m² (+ 8 m² duplex) 3e verdieping. Rustig achteraan, Velux ramen. Huur €580/maand incl. kosten." |
| **Kamer 9** | "Kamer 9: 22 m² (+ 10 m² duplex) voorkant 3e verdieping. Licht, 4 Velux ramen. Voor 2. Huur €632/maand incl. kosten." |
| **Locatie** | "Tabakvest 85 ligt in hartje Antwerpen dicht bij Leopoldplaats, Oudevaartplaats, hogescholen en winkelzone Meir. Prima bereikbaar met OV." |

**Implementation:**
- Add to `<head>` section of each HTML file:
  ```html
  <meta name="description" content="[text from table above]">
  ```

**Impact:** Critical for search snippets and SEO. 1 hour.

---

### A4. Add Open Graph (OG) + Twitter Meta Tags
**Current Issue:** No social share tags → links look generic on WhatsApp, Facebook, Instagram.

**Implementation:**
Add to `<head>` of each HTML file:

```html
<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="[same as <title>]">
<meta property="og:description" content="[same as meta description]">
<meta property="og:image" content="https://tabakvest85.be/og-image-[page-type].jpg">
<meta property="og:url" content="https://tabakvest85.be/proposal_[X]/[page].html">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[same as <title>]">
<meta name="twitter:description" content="[same as meta description]">
<meta name="twitter:image" content="https://tabakvest85.be/og-image-[page-type].jpg">
```

**OG Image Assets Needed:**
- `og-image-home.jpg` (1200×630px) — hero image or facade photo
- `og-image-rooms.jpg` (1200×630px) — grid of rooms or featured room
- `og-image-room.jpg` (1200×630px) — individual room carousel cover
- `og-image-locatie.jpg` (1200×630px) — location/street photo

**Note:** These images do NOT exist yet; they need to be created or selected from room photos.

**Impact:** Massive for social sharing. 2–3 hours (including image creation).

---

### A5. Add JSON-LD Structured Data
**Current Issue:** Google doesn't know what type of business/property this is.

**Implementation:**

#### A5a. Homepage JSON-LD (LodgingBusiness)
Add to `<head>` of `index.html`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LodgingBusiness",
  "name": "Tabakvest 85",
  "url": "https://tabakvest85.be/proposal_1_minimalist/index.html",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Tabakvest 85",
    "addressLocality": "Antwerpen",
    "postalCode": "2000",
    "addressCountry": "BE"
  },
  "telephone": "+32 3 ...", // ADD ACTUAL PHONE
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 51.2194,
    "longitude": 4.4025
  },
  "priceRange": "€536–€632",
  "image": ["https://tabakvest85.be/pictures/facade.jpg"],
  "description": "Moderne studentenkamers in Antwerpen met eigen badkamer, gigabit internet en Vlaams kwaliteitslabel."
}
</script>
```

#### A5b. Rooms Page JSON-LD (ItemList of Properties)
Add to `<head>` of `rooms.html`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {
      "@type": "Residence",
      "name": "Kamer 1",
      "description": "22 m² gelijkvloers voorzijde...",
      "image": "https://tabakvest85.be/proposal_1_minimalist/pictures/kamer 1/1.jpg",
      "priceRange": "€536/maand"
    },
    // ... repeat for rooms 2–9
  ]
}
</script>
```

#### A5c. Individual Room Detail JSON-LD (Residence)
Add to `<head>` of each `room-N.html`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Residence",
  "name": "Kamer [N]",
  "url": "https://tabakvest85.be/proposal_1_minimalist/room-[N].html",
  "address": "Tabakvest 85, 2000 Antwerpen, Belgium",
  "description": "[room description]",
  "image": ["https://tabakvest85.be/proposal_1_minimalist/pictures/kamer [N]/1.jpg", ...],
  "numberOfRooms": 1,
  "floorSize": {
    "@type": "QuantitativeValue",
    "value": [SIZE],
    "unitCode": "MTK"
  },
  "priceCurrency": "EUR",
  "price": "[RENT]/maand"
}
</script>
```

**Impact:** Enables Google House Cards, rich results, and better search understanding. 2 hours.

---

### A6. Create `sitemap.xml` and `robots.txt`
**Current Issue:** Not essential for small sites, but best practice.

**Implementation:**

#### A6a. `sitemap.xml` (create at project root)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Proposal 1 -->
  <url>
    <loc>https://tabakvest85.be/proposal_1_minimalist/index.html</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://tabakvest85.be/proposal_1_minimalist/rooms.html</loc>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://tabakvest85.be/proposal_1_minimalist/room-1.html</loc>
    <priority>0.8</priority>
  </url>
  <!-- ... rooms 2–9 -->
  <url>
    <loc>https://tabakvest85.be/proposal_1_minimalist/locatie.html</loc>
    <priority>0.8</priority>
  </url>
  
  <!-- Proposal 4 (repeat above with proposal_4_boutique) -->
  <!-- Proposal 5 (repeat above with proposal_5_cinematic) -->
</urlset>
```

#### A6b. `robots.txt` (create at project root)
```
User-agent: *
Allow: /
Disallow: /student.jpg

Sitemap: https://tabakvest85.be/sitemap.xml
```

**Impact:** Minor SEO; looks professional. 15 min.

---

## SECTION B: FUNCTIONALITY ENHANCEMENTS (Medium Priority)

### B1. Contact Form
**Current Issue:** Only `mailto:` link; many users won't open email client.

**Recommendation:**
- Use **Formspree** (free, no backend needed) or **Netlify Forms** (if hosted on Netlify)
- Form fields: Name, Email, Message, Preferred move-in date, Phone (optional)
- Add to homepage + rooms page

**Implementation:**
- Create `contact.html` or add form section to `index.html`
- JavaScript to handle submission
- 2–3 hours

---

### B2. WhatsApp Click-to-Chat Button
**Current Issue:** Very common in Belgium for student rentals; missing here.

**Recommendation:**
- Add floating WhatsApp button (bottom-right corner)
- Link: `https://wa.me/32XXX [your phone]?text=Hallo, ik ben geïnteresseerd in Tabakvest 85`
- Add to all pages or at least homepage + rooms

**Implementation:**
- Simple HTML button + inline JavaScript or external library (e.g., `WhatsApp Button`)
- 30 min

---

### B3. Embedded Google Map on Locatie Page
**Current Issue:** Currently only a `<a href>` link to Google Maps; no inline map.

**Recommendation:**
- Embed an `<iframe>` of Google Maps with Tabakvest 85 pinned
- Show nearby landmarks (hogescholen, Meir, station)
- Replace or complement the current text

**Implementation:**
- Get embed code from Google Maps
- Add to `locatie.html`
- Requires GDPR cookie consent (see A-7c below)
- 1 hour

---

### B4. Availability Filter on Kamers Page
**Current Issue:** Currently shows all rooms; could filter by status.

**Recommendation:**
- Add filter buttons: "Alle" | "Beschikbaar" | "Verhuurd"
- Already partially implemented in `rooms.js`; just needs polishing

**Implementation:**
- Check current state of `filterGrid()` function
- Ensure buttons work across all 3 proposals
- 30 min

---

### B5. Image Lightbox/Gallery on Room Detail Pages
**Current Issue:** Carousel is good but no full-screen/lightbox view.

**Recommendation:**
- Add library like **GLightbox** or **Fancybox**
- Click image → opens full-screen gallery with prev/next
- Much better UX for photo-heavy rooms

**Implementation:**
- Add library JS + CSS
- Modify `initCarousel()` to trigger lightbox
- 1 hour

---

## SECTION C: ACCESSIBILITY & QUALITY (Low-Medium Priority)

### C1. Ensure Meaningful `alt` Text on All Images
**Current Issue:** Most images have alt text; need to verify new photos.

**Recommendation:**
- Every image should have descriptive `alt`:
  - Room photos: `"Kamer 2: gelijkvloers achterzijde met terrasje en dubbel raam"`
  - Hero images: `"Tabakvest 85 facade aan Tabakvest in Antwerpen"`
  - Location photos: `"Leopoldplaats in hartje Antwerpen"`

**Implementation:**
- Audit all `<img>` tags in HTML
- Update `alt` attributes
- Add to any new images
- 1 hour

---

### C2. Add Keyboard Focus States
**Current Issue:** Links/buttons may not have visible `:focus` styling.

**Recommendation:**
- Add CSS:
  ```css
  a:focus, button:focus {
    outline: 2px solid var(--accent-color);
    outline-offset: 2px;
  }
  ```
- Ensure focus order is logical (can tab through links in order)

**Implementation:**
- Update `home.css` and `pages.css` in all 3 proposals
- Test with Tab key
- 30 min

---

### C3. Respect `prefers-reduced-motion`
**Current Issue:** Parallax and scroll animations may trigger motion sensitivity.

**Recommendation:**
Add to CSS (all 3 proposals):
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Also update JS to check:
```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReducedMotion) {
  // run parallax/scroll animations
}
```

**Implementation:**
- Add media query to CSS
- Update reveal script in `script.js`
- 45 min

---

### C4. Color Contrast Check
**Current Issue:** Proposal 5 (dark theme) needs verification.

**Recommendation:**
- Test all text/background pairs with WCAG AA standard (4.5:1 for normal text, 3:1 for large text)
- Use tool: WebAIM Contrast Checker or axe DevTools

**Implementation:**
- Run audit on proposal_5_cinematic specifically
- Adjust if needed
- 30 min

---

## SECTION D: PERFORMANCE (Low Priority — Already Done)

### D1. Image Compression ✅ DONE
Already completed: resized all room photos to 1200px max width, quality 85.

### D2. Lazy Loading ✅ DONE
Already present: `loading="lazy"` on carousel images and grid thumbnails.

### D3. Font Display ✅ DONE
Already set: `display=swap` on Google Fonts to prevent layout shift.

---

## SECTION E: CONTENT CLEANUP (Low Priority)

### E1. Remove English Placeholders
**Current Issue:** Kamers page has `"[Coming soon - Add photos...]"` and English "Coming Soon" button.

**Recommendation:**
- Remove or replace with Dutch text
- Affected file: `proposal_1_minimalist/rooms.html` (and others if they exist)

**Implementation:**
- Search for "Coming soon" in all HTML
- Replace or delete
- 15 min

---

## SUMMARY TABLE

| Priority | Category | Item | Effort | Impact |
|----------|----------|------|--------|--------|
| 🔴 **HIGH** | SEO | A1: Fix `lang="nl"` | 5 min | High |
| 🔴 **HIGH** | SEO | A2: Keyword-friendly titles | 30 min | High |
| 🔴 **HIGH** | SEO | A3: Meta descriptions | 1 hour | High |
| 🔴 **HIGH** | SEO | A4: OG + Twitter tags | 2–3 hours | High |
| 🟡 **MEDIUM** | SEO | A5: JSON-LD structured data | 2 hours | High |
| 🟡 **MEDIUM** | SEO | A6: sitemap.xml + robots.txt | 15 min | Low |
| 🟡 **MEDIUM** | Feature | B1: Contact form | 2–3 hours | High |
| 🟡 **MEDIUM** | Feature | B2: WhatsApp button | 30 min | High |
| 🟡 **MEDIUM** | Feature | B3: Embedded Google Map | 1 hour | Medium |
| 🟡 **MEDIUM** | Feature | B4: Availability filter | 30 min | Low |
| 🟡 **MEDIUM** | Feature | B5: Image lightbox | 1 hour | Medium |
| 🟢 **LOW** | A11y | C1: Alt text audit | 1 hour | Medium |
| 🟢 **LOW** | A11y | C2: Keyboard focus | 30 min | Medium |
| 🟢 **LOW** | A11y | C3: Reduced motion | 45 min | Low |
| 🟢 **LOW** | A11y | C4: Color contrast | 30 min | Low |
| 🟢 **LOW** | Content | E1: Remove English placeholders | 15 min | Low |

---

## TOTAL ESTIMATED EFFORT (HIGH PRIORITY ITEMS)
- **SEO Metadata (A1–A5):** ~6.5 hours
- **Functionality (B1–B2):** ~3 hours
- **Accessibility (C1–C3):** ~2.5 hours
- **Total:** ~12 hours

---

## NEXT STEPS
**Awaiting user instructions:**
1. Which section to start with? (Recommend: A1 → A2 → A3 → A4 → B2)
2. Do you have OG images, or should I create them?
3. Do you have a WhatsApp phone number to use?
4. Should I add the Google Map embed, or skip for now?

