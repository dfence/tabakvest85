# Ideas & Content Suggestions — Tabakvest 85

> These are **suggestions only**. Nothing here has been applied to the live copy or the
> proposals — the proposal homepages use the exact text that is already on the website.
> Use this as a checklist when you decide to evolve the content.

---

## 0. About the 5 proposals

Each proposal is a full, working copy of the site in its own folder. **Only the homepage
(`index.html`) has been redesigned** — the other pages (Kamers, Kamer-detail, Locatie) are
intact and still navigable in the current style, so you can click around and judge each look
in context. Once you pick a winner, the same design language gets rolled out to every page.

| Folder | Direction | Mood | Best for |
|--------|-----------|------|----------|
| `proposal_1_minimalist` | Minimalist Luxury | Calm, refined, lots of air | Timeless, understated premium |
| `proposal_2_editorial` | Editorial / Magazine | Bold serif, asymmetric | Design-led, characterful |
| `proposal_3_dark` | Dark & Dramatic | Charcoal + gold, moody | High-end, exclusive feel |
| `proposal_4_boutique` | Warm Boutique | Earthy, organic, cozy | Friendly-premium, welcoming |
| `proposal_5_cinematic` | Cinematic Visual | Full-screen imagery | Photography-driven, immersive |

To preview: open each folder's `index.html` in a browser.

---

## 1. Copy / wording improvements

- **Hero subline** is functional but could add a benefit hook. Optional alternative
  (still truthful): *"Unieke studentenkamers in hartje Antwerpen — met eigen badkamer,
  snel internet en het Vlaams kwaliteitslabel."*
- **Consistent terminology:** the site mixes "kamers" and "koten". Pick one as the primary
  term (keep the other for warmth) so messaging feels deliberate.
- **Microcopy on buttons:** "Bekijk onze kamers" is good; consider a softer secondary CTA
  like *"Plan een bezichtiging"* once visits are possible.
- **Avoid English placeholder** still present on the Kamers page (`"[Coming soon - Add
  photos...]"` and one English "Coming Soon" button) — these read as unfinished. The
  proposals hide bracketed notes, but the underlying Kamers page should be cleaned too.

## 2. Trust & conversion (high impact for a premium audience)

- **Reviews / testimonials:** 2–3 short quotes from current or past tenants (first name +
  study programme). Nothing builds trust faster for housing.
- **"Waarom Tabakvest 85" strip:** 3–4 icon points (Eigen badkamer · Gigabit WiFi · Vlaams
  kwaliteitslabel · Op wandelafstand van hogescholen). You already have the facts on the
  room page — surfacing them on the home page is persuasive.
- **Availability badge:** a clear "Beschikbaar vanaf 15/09" or "Volzet — wachtlijst" status
  so prospects instantly know where they stand.
- **Pricing transparency:** even an "vanaf € 536 / maand incl. richtprijs kosten" line sets
  expectations and filters serious leads.

## 3. Structure / new sections worth adding

- **FAQ section** (huurperiode, waarborg, kosten, inschrijving, bezoek). Reduces email
  back-and-forth and is great for SEO.
- **"Zo werkt het" steps:** Contacteer → Bezichtig → Reserveer → Welkom. A simple 4-step
  timeline reassures first-time renters (and their parents).
- **Neighbourhood highlights on the home page:** a teaser of the Locatie page (Leopoldplaats,
  Meir, hogescholen, station) with one strong photo and a "Ontdek de buurt" link.
- **Parents-focused note:** parents often co-decide. One reassuring line about safety,
  quality label and quiet street speaks to them directly.

## 4. Imagery

- **Photography is everything** for the cinematic/visual directions. Recommend a short
  professional shoot: facade at golden hour, each room, the shared kitchen, the woonerf
  street, and one "lifestyle" shot. Bright, consistent white-balance.
- Provide **landscape (16:9) and portrait (3:4)** crops so any layout can use them well.
- Replace gradient/emoji placeholders for rooms 2–9 with real photos as they become
  available; until then a neutral "Binnenkort beschikbaar" cover image looks more premium
  than the colourful gradients.
- Add an **OpenGraph/social share image** (`og:image`) so links look good when shared on
  WhatsApp/Facebook/Instagram.

## 5. SEO & metadata

- Add unique `<meta name="description">` per page (currently missing).
- Add **Open Graph + Twitter** tags (title, description, image) for rich link previews.
- Add **JSON-LD structured data**: `LodgingBusiness` / `Residence` with address, phone,
  geo, priceRange — helps Google show rich results and a map card.
- Set `lang="nl"` consistently (the current `index.html` uses `lang="en"`).
- Add a `sitemap.xml` and `robots.txt`.
- Localised, keyword-friendly titles, e.g. *"Studentenkamers Antwerpen centrum — Tabakvest
  85"*.

## 6. Functionality enhancements

- **Contact form** (name, email, message, preferred move-in date) in addition to the mailto
  link — many users won't open a mail client. Can stay static with a service like Formspree
  or Netlify Forms (no backend needed).
- **WhatsApp click-to-chat** button — very common and expected for student rentals in BE.
- **Embedded Google Map** on the Locatie page (you already link out; an inline map increases
  engagement).
- **Per-room availability filter** on the Kamers page (Beschikbaar / Verhuurd) once more
  rooms have data.
- **Image lightbox/gallery** on room detail pages for full-size photos.
- **Cookie/consent note** if you add analytics or the Google Map embed (GDPR).

## 7. Accessibility & quality

- Ensure every image has a meaningful `alt` (most do — keep it up for new photos).
- Maintain colour-contrast on the dark/cinematic options (kept AA-compliant in the
  proposals; re-check if you tweak colours).
- Add visible keyboard focus states for links/buttons.
- Respect `prefers-reduced-motion` — disable the scroll/parallax animations for users who
  ask for less motion (easy to add to the reveal script).

## 8. Performance

- **Compress & resize photos** (the room photos look like full-resolution camera files).
  Aim for ~150–300 KB each, served at display size.
- Convert large JPEGs to **WebP/AVIF** with JPEG fallback.
- Add `loading="lazy"` to below-the-fold images.
- Self-host the two web fonts (or keep `display=swap`, already set) to avoid layout shift.

## 9. Quick wins (do these first)

1. Fix `lang="en"` → `lang="nl"` on the home page.
2. Remove the leftover English placeholders on the Kamers page.
3. Add meta descriptions + an OG image.
4. Compress the room photos.
5. Add a 3-point "Waarom Tabakvest 85" strip and one testimonial.

---

*Prepared as part of the redesign proposals. Happy to implement any of the above on the
proposal you choose.*
