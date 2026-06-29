# Website Audit & Improvement Ideas — Tabakvest 85

**Date:** June 29, 2026  
**Scope:** Audit of 3 design proposals (proposal_1_minimalist, proposal_4_boutique, proposal_5_cinematic)  
**Status:** Analysis only — No implementation yet

---

## SECTION 1: STRUCTURAL & TECHNICAL ISSUES

### 1.1 File Independence Problem 🚨 CRITICAL
**Issue:** Each proposal CANNOT run independently from the root folder.

**Root Cause:**
- `lightbox.js` is located in the **root folder** only
- All proposal pages reference: `<script src="../lightbox.js"></script>`
- If you host just `proposal_1_minimalist/` on a separate server, the lightbox breaks
- Same applies to any future root-level shared files

**Recommendation:**
- **Copy `lightbox.js` to each proposal's `js/` folder**
  - Change `<script src="../lightbox.js"></script>` → `<script src="js/lightbox.js"></script>`
  - Each proposal becomes fully independent
  - Easier to distribute individual proposals to clients

**Similar Issues:**
- `robots.txt` and `sitemap.xml` in root → Should be duplicated in each proposal
- Root `index.html` redirects to proposal_1 (presumably) → Consider making it a landing page or removing it
- Root `rooms.json` → Confirm if it's used or if each proposal has its own

---

### 1.2 Code Duplication Across Proposals

**Current State:**

| File Type | Status | Implication |
|-----------|--------|-------------|
| **HTML files** (index.html, rooms.html, room-1.html, etc.) | Identical except proposal-specific paths | Content updates require 3 edits |
| **style.css** | **Identical** across all 3 proposals (20,935 bytes) | Could be shared/linked from root |
| **home.css** | Different (different color schemes) | Correct — proposal-specific theming ✓ |
| **pages.css** | Slightly different (7198 → 7416 → 12084 bytes) | Varies; should check if differences are intentional |
| **script.js** | Mostly identical (2251 bytes, except proposal_5 at 2642 bytes) | Proposal_5 has extra lightbox initialization |
| **rooms.js** | Likely identical | Should verify |
| **rooms.json** | Duplicated in all 3 proposals | Updates require 3 edits; consider centralizing |

**Recommendation:**
- **Consider a "shared assets" approach:**
  1. Keep `style.css` in root and reference it from all proposals
  2. Keep `rooms.json` in root and load it via relative path `../../rooms.json`
  3. Document this architecture clearly in `README.md`
- **Or, if keeping everything independent is priority:** 
  1. Copy `lightbox.js` to each proposal
  2. Accept duplication of `style.css` and `rooms.json`
  3. Document that each proposal folder is self-contained

---

### 1.3 HTML Structure Inconsistencies

**Finding:** All proposals share identical HTML structure, but CSS applies different visual styling.

**Implication:** 
- Good for maintainability (same DOM = easier CSS tweaking)
- Bad for scaling (3 copies of every HTML page must be updated manually)

**Recommendation:**
- **Long-term:** Consider a templating approach (e.g., Handlebars, EJS, or static site generator) to generate proposal-specific HTML from shared templates
- **Short-term:** Document the relationship clearly so future updates are synchronized

---

## SECTION 2: MODERN DESIGN & UX IMPROVEMENTS

### 2.1 Layout & Composition

**Current State:**
- Hero section with image & text (side-by-side on desktop)
- About section with text
- Showcase section with 3 featured room images
- Contact section with links
- Footer (minimal)

**Modern Design Recommendations:**

#### 2.1a Featured Rooms Grid (Instead of 3-image showcase)
**Idea:** Replace the current 3-image showcase with an interactive grid of featured rooms.

```
Current:
- Static image gallery showing 1 featured room's photos

Proposed:
- Grid of 3-4 highlighted rooms (Kamer 1, Kamer 5, Kamer 9, etc.)
- Each card shows: room photo, size, price, "View Details" button
- On hover: subtle shadow lift, overlay with key features
- Mobile: single column, touch-friendly cards

Impact:** More engaging, drives conversion to rooms page, better visual variety
```

**Modern Approach:**
- Use CSS Grid with `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))`
- Add subtle hover transitions (scale 1.02, shadow change)
- Include micro-interaction: image parallax or tilt effect on hover

---

#### 2.1b Above-the-Fold CTA Optimization
**Current:** Hero section has two CTAs ("Bekijk onze kamers" and "Neem contact op")

**Improvement:**
- Make the primary CTA more prominent (different color, larger, stronger visual weight)
- Consider adding a tertiary option: "Take Virtual Tour" (if available later)
- Ensure contrast is WCAG AA at minimum (verify on proposal_5 dark theme)

---

#### 2.1c Content Hierarchy & Spacing
**Current:** Generous whitespace (good), but could benefit from:

**Recommendations:**
- **Increase visual rhythm:** Add more varied section background colors (subtle alternating backgrounds)
  - E.g., light beige / white / light beige / white pattern
- **Section margins:** Increase spacing between major sections (current: looks around 4rem–6rem, increase to 6rem–8rem)
- **Typography scale:** Add more variety
  - Consider: h1 > 3.2rem | h2 > 2rem | h3 > 1.4rem (currently more uniform)
- **Add decorative elements:**
  - Subtle dividers or icons between sections (e.g., Vlaams logo centered with margin space)
  - Background patterns or gradients (very subtle, 2-5% opacity)

---

### 2.2 Typography & Visual Identity

**Current State:**
- Proposal 1: Cormorant Garamond (serif) + Jost (sans)
- Proposal 4: DM Serif Display + Mulish (modern pairing)
- Proposal 5: Sora (clean modern sans-serif)

**Modern Improvements:**

#### 2.2a Font Loading & Performance
**Check:**
- Currently using `display=swap` on Google Fonts (good ✓)
- Verify font weights are minimal (e.g., 400, 500, 600, 700 only—not loading 300-900 range)

**Recommendation:**
- Use `font-display: swap` explicitly (prevents FOIT)
- Preload: `<link rel="preload" as="font" href="..." crossorigin>`
- Consider using **variable fonts** for modern approach (reduces HTTP requests)

---

#### 2.2b Typographic Contrast
**Idea:** Add more visual contrast between headings and body text.

**Current:** 
- Body: 17px, 1.8 line-height
- Headings: styled with serif, but sizes are moderate

**Improvement:**
- Use **ALL CAPS + letter-spacing** for `.eyebrow` (already done ✓)
- Increase heading line-height to 1.1–1.2 (tighter, more modern)
- Add text-decoration or underline effects on hover for headings
- Consider a "subtitle" style with slightly larger, lighter weight

---

### 2.3 Color & Contrast

**Current State:**
- Proposal 1: Gold/brown + cream (warm, elegant)
- Proposal 4: Terra/olive + cream (earthy, boutique)
- Proposal 5: Dark navy + white (cinematic, high-contrast)

**Audit Findings:**
- ✓ Color palettes are distinct and well-chosen
- ⚠️ Proposal 5 (dark theme): Verify text color contrast meets WCAG AA (4.5:1 for normal text)
  - Light text on dark background: measure white (#fff) on navy (#0a0a0b)
  - Should be sufficient, but test with axe DevTools

**Recommendations:**
- Add a **"tertiary" color** to each palette for interactive states (buttons, links, hover states)
  - Currently using primary colors, but could be more nuanced
  - E.g., Proposal 1: Add a muted gold for secondary interactions
- **Introduce subtle color overlays** on hero images
  - Add a `background: linear-gradient(135deg, rgba(154, 123, 79, 0.15) 0%, rgba(0,0,0,0) 100%)`
  - Creates depth and ensures text legibility

---

### 2.4 Animations & Motion

**Current State:**
- ✓ Scroll-reveal animations (fade-in on scroll)
- ✓ `prefers-reduced-motion` support (CSS media query already added in C3)
- ✓ Hamburger menu toggle

**Modern Improvements:**

#### 2.4a Micro-interactions
**Add subtle animations for:**
- **Button hover states:** 
  - Translate 2px up + shadow depth change
  - Background color transition (200ms, easeOutQuad)
- **Link hover underline:** 
  - Animated underline from left-to-right (300ms)
  - Use `background: linear-gradient()` + `background-position` animation
- **Form focus states:**
  - Input border color change (200ms)
  - Subtle glow on focus (box-shadow)

#### 2.4b Scroll-based Effects
**Recommendations:**
- **Parallax on hero image:** Subtle depth effect (current: might already have this?)
- **Image reveal animations:** Use `clip-path` or `object-fit` for staggered reveals
- **Counter animations:** If stats section is added, count up numbers on scroll

---

### 2.5 Interactive & Engagement Features

**Current State:**
- ❌ No testimonials or reviews
- ❌ No FAQ section
- ❌ No newsletter signup
- ❌ No trust badges (besides Vlaams label)
- ❌ No social proof / student quotes
- ❌ No live chat or chat widget

**Modern Additions (Optional):**

#### 2.5a Testimonials Section
**Idea:** Add a section with 3-4 student quotes/reviews.

```
Example:
"Fijne kamer, heel goed onderhouden. Landlord is erg helpend."
— Stef V., 3rd year Student
```

**Benefits:**
- Builds trust
- Improves SEO (fresh content, structured data)
- Increases time on page

**Implementation:** 
- CSS Grid or Carousel (3 items visible on desktop, 1 on mobile)
- Use `<blockquote>` semantic HTML
- Add star rating (⭐⭐⭐⭐⭐) or similar

---

#### 2.5b FAQ Section
**Questions to address:**
- How do I apply?
- What's included in the rent?
- Is WiFi really gigabit?
- Pet policy?
- Lease duration?
- Deposit amount?

**Modern Approach:**
- Accordion UI (collapsible items)
- Use `<details>` and `<summary>` HTML elements (native, no JS needed)
- Smooth collapse/expand animation with CSS `max-height` or `grid-template-rows`

---

#### 2.5c Call-to-Action Buttons
**Current:** Two buttons on hero (primary + secondary)

**Modern Improvement:**
- Add subtle animation: hover state should feel tactile
- Consider a **third option:** "Request 3D Tour" or "Schedule Viewing"
- Make button text action-oriented: "See Available Rooms" instead of "Bekijk onze kamers"

---

### 2.6 Mobile & Responsive Design

**Current State:**
- Hamburger menu present
- Responsive grid layouts
- Touch-friendly buttons

**Audit & Improvements:**

#### 2.6a Mobile Navigation
**Current:** Hamburger menu is basic

**Modernization:**
- Add animation to hamburger icon (morph effect when opened)
  - X shape when menu is open, hamburger shape when closed
  - Smooth 300ms animation
- Consider: Mobile menu should overlay full-screen with backdrop blur
  - Current state: likely works, but verify no content shift

#### 2.6b Mobile CTA
**Idea:** Add persistent "Contact Now" or "Call" button at bottom of mobile viewport

```
Sticky footer on mobile:
- Full-width button or floating action button (FAB)
- "Call: +32 495 91 65 13" or "WhatsApp Chat"
- Appears after scrolling past hero section
```

**Benefit:** High visibility for contact conversion on mobile (where users primarily browse)

---

### 2.7 Footer Enhancement

**Current State:**
```
© 2024 Tabakvest 85. Alle rechten voorbehouden.
Studentenhuisvesting in Antwerpen
```

**Modern Footer:**

**Expand to include:**
1. **Quick Links Section:**
   - Home, Kamers, Locatie, Contact
   
2. **Company Info:**
   - Address: Tabakvest 85, Antwerpen
   - Email: tabakvest85@gmail.com
   - Phone: +32 495 91 65 13

3. **Social Links:**
   - Facebook, Instagram (if exists), LinkedIn

4. **Legal:**
   - Privacy Policy
   - Terms of Service
   - Cookie Policy (if applicable)

5. **Newsletter Signup:**
   - "Stay updated about new rooms"
   - Email input + Subscribe button

**Layout:** Multi-column grid on desktop, single column on mobile

**Modern Touch:**
- Add subtle background color or pattern to footer
- Use flexbox/grid for alignment
- Top border divider (thin, gold accent color)

---

## SECTION 3: PERFORMANCE & TECHNICAL RECOMMENDATIONS

### 3.1 Image Optimization ✓ Already Done
- ✓ Images resized with proper aspect ratios (vogelmarkt 1400×600, leopold 1000×750)
- ✓ JPEG quality 80% with optimization
- ✓ `loading="lazy"` attribute present (verify on all `<img>` tags)

**Remaining:**
- Consider WebP format with fallback to JPEG (for modern browsers)
  - `<picture>` element with multiple sources
  - Saves 25-30% file size

---

### 3.2 CSS Organization

**Current:**
- `home.css` (base styles, typography, common components)
- `pages.css` (room detail, location page specific styles)
- `style.css` (identical across all proposals—unclear purpose)

**Recommendation:**
- **Clarify `style.css` purpose:**
  - Is it needed, or should it be merged into `home.css`?
  - Document its role in comments
- **Consider SCSS/SASS if scaling:**
  - Variables for colors (currently defined in `:root`)
  - Mixins for responsive breakpoints
  - Nested selectors for clarity
  - But only if budget allows; plain CSS is fine for current size

---

### 3.3 JavaScript Refactoring

**Current Issues:**
1. Proposal_5 has extra JS (2642 bytes vs 2251)
2. `lightbox.js` in root is a dependency issue
3. IntersectionObserver is used (good for performance ✓)

**Recommendations:**
1. **Move `lightbox.js` to each proposal's `js/` folder** (to solve independence issue)
2. **Consolidate `script.js` across proposals:**
   - Extract proposal-specific code to separate files
   - Share common utilities in a shared file
3. **Add error handling:**
   - What if rooms.json fails to load? (currently no visible error state)
   - Add try-catch and user-friendly error message
4. **Add loading states:**
   - Show spinner while room data loads
   - Current: "Kamer laden…" is good, but no visual feedback

---

## SECTION 4: ACCESSIBILITY ENHANCEMENTS

### 4.1 Already Implemented ✓
- ✓ C2: Keyboard focus states
- ✓ C3: `prefers-reduced-motion` CSS media query
- ✓ Semantic HTML (`<nav>`, `<main>`, `<section>`, `<footer>`, `<blockquote>`)
- ✓ Alt text on images (verify all new images have meaningful alt text)

### 4.2 Improvements

#### 4.2a Focus Management
**Add visible focus outline:**
```css
*:focus-visible {
  outline: 2px solid var(--accent-color);
  outline-offset: 2px;
}
```
(Verify this is implemented on all interactive elements)

#### 4.2b Color Contrast (Proposal 5)
**Action:** Use WebAIM Contrast Checker to verify:
- White text on dark navy background: ✓ Should pass (likely 10:1+)
- Muted text color on dark background: ⚠️ Check if 4.5:1

#### 4.2c ARIA Labels
**Add where applicable:**
- `<button>` elements: aria-label (for icon-only buttons)
- `<a href="../lightbox.js"></a>` (probably not needed, but check)
- Mobile menu: `aria-expanded` attribute on hamburger button
- Form inputs: `<label for="">` elements (if contact form added)

#### 4.2d Language Attribute
- ✓ `lang="nl"` is set (already fixed in A1)

---

## SECTION 5: CONTENT & INFORMATION ARCHITECTURE

### 5.1 Navigation Structure

**Current:**
- Home → Kamers → Locatie → Contact (simple 4-item nav)

**Improvements:**
- ✓ Clear hierarchy (good)
- Consider adding breadcrumbs on room detail pages: "Home > Kamers > Kamer 1"
- Consider mega-menu on desktop (if more sections are added)

---

### 5.2 Call-to-Action Consistency

**Current:**
- Hero: "Bekijk onze kamers" + "Neem contact op"
- Showcase: "Ontdek alle kamers"
- Contact section: Email/phone/WhatsApp/Facebook links

**Recommendation:**
- Ensure CTA text is **consistent and action-oriented**
- Use similar language across proposals (current: might vary)
- Add a "Request More Info" CTA button in the locatie page (conversion point)

---

## SECTION 6: SEO & METADATA (From to_be_implemented.md)

### 6.1 Completed ✓
- ✓ lang="nl" on all HTML pages (A1)
- ✓ Meta descriptions added to key pages (A3)
- ✓ Open Graph + Twitter meta tags (A4)

### 6.2 Pending
- A2: Keyword-friendly `<title>` tags (verify all rooms have unique, SEO-optimized titles)
- A5: JSON-LD structured data (verify implemented correctly)
- A6: sitemap.xml + robots.txt (at root level)

**Recommendation:** Ensure sitemap.xml is correct for all 3 proposals (might need separate sitemaps or consolidated)

---

## SECTION 7: MODERN STYLING ENHANCEMENTS

### 7.1 Visual Effects (Non-invasive)

#### Subtle Gradients
Add light gradients to sections:
```css
section {
  background: linear-gradient(135deg, var(--bg) 0%, var(--bg-alt) 100%);
}
```

#### Decorative Elements
- Thin horizontal dividers between sections (CSS border or `<hr>`)
- Colored accents (gold, terra, sand) as left-side borders on pull-quotes
- Rounded corners on image containers (16-24px border-radius)

#### Glassmorphism (Optional, if modern aesthetic desired)
- Apply to CTA buttons or cards
- `backdrop-filter: blur(10px)` + semi-transparent background
- (May need vendor prefixes for browser support)

---

### 7.2 Card & Container Styling

**Current:** Minimal—mostly text on background

**Modern Additions:**
- Add subtle `box-shadow` to room cards: `0 2px 8px rgba(0,0,0,0.08)`
- On hover: increase shadow depth to `0 8px 24px rgba(0,0,0,0.12)`
- Add `border-radius` to image containers (currently might be sharp corners)

---

## SECTION 8: PROPOSAL-SPECIFIC NOTES

### Proposal 1 (Minimalist)
- ✓ Clean, elegant aesthetic
- Consider: Could use slightly more visual hierarchy (more varied spacing)
- Gold accent color is nice—ensure it's used consistently on CTAs

### Proposal 4 (Boutique)
- ✓ Warm, organic feel with terra tones
- Consider: Leverage the warmer palette for backgrounds (sections with light terra/sand tints)
- DM Serif Display + Mulish is a strong pairing

### Proposal 5 (Cinematic)
- ✓ Bold, modern dark theme
- ⚠️ Verify color contrast on muted text (might be below WCAG AA)
- Consider: Add subtle background images or patterns (dark overlays) to hero sections for visual depth

---

## SUMMARY TABLE: Priority Recommendations

| Priority | Category | Issue | Quick Fix? | Impact |
|----------|----------|-------|-----------|--------|
| 🔴 **CRITICAL** | Structure | lightbox.js in root → proposals can't run independently | Copy to each `js/` folder | High |
| 🟠 **HIGH** | Layout | Add featured rooms grid instead of static showcase | New HTML + CSS section | High |
| 🟠 **HIGH** | UX | Mobile sticky CTA (call/chat button) | Button + CSS `position: sticky` | High |
| 🟠 **HIGH** | Footer | Expand footer with links, social, newsletter | Add HTML + styling | Medium |
| 🟡 **MEDIUM** | Content | Add testimonials section | New HTML section + data | Medium |
| 🟡 **MEDIUM** | Content | Add FAQ section with accordion | New HTML + CSS `<details>` | Medium |
| 🟡 **MEDIUM** | Design | Improve mobile navigation (hamburger morph) | CSS + JS animation | Low |
| 🟡 **MEDIUM** | Accessibility | Verify Proposal 5 contrast; add focus outlines | Audit + CSS tweaks | Medium |
| 🟢 **LOW** | Performance | Optimize images to WebP format | Modern format implementation | Low |
| 🟢 **LOW** | Styling | Add subtle gradients + decorative elements | CSS enhancements | Low |
| 🟢 **LOW** | SEO | Verify all structured data is correct | Audit JSON-LD | Low |

---

## NEXT STEPS

1. **Decide on architecture:** Keep proposals independent or share `style.css` + `rooms.json`?
2. **Prioritize improvements:** Focus on critical (lightbox independence) and high-impact items (grid layout, mobile CTA)
3. **Create design system document:** Document color palettes, typography, spacing for consistency
4. **Plan content expansion:** Testimonials, FAQ, newsletter signup (design & copy)
5. **Accessibility audit:** Run axe DevTools on all proposals; prioritize Proposal 5 contrast check

---

**End of Audit Document**
