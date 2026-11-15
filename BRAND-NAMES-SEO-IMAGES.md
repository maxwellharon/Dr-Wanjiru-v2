# LOGO NOTES (read first)
- Built from the logo she approved: terracotta arch, crossed "W", spaced serif name, hairline rule, two-line tagline.
- The approved artwork reads "DR. WANJIRU M". These files read "DR. WANJIRU MD". To change it, edit `NAME` at the top of `_build/logos.py` and run `python3 _build/build.py`.
- Palette: terracotta #9F5C53, blush #F1DDD4, title rose #9C625A, cocoa #4F3B32, deep terracotta #7E4540, cream #FBF3EE, rose gold #D9A596, night #2B1D19.
- Logo SVGs use a close-match serif and sans because Cormorant Garamond and Jost were not installed here. The website itself uses the real Cormorant Garamond and Jost. For exact brand files, retype the text in Canva/Figma with those fonts.

# Dr. Wanjiru MD · Brand names, SEO notes, image prompts

## 1. Brand names (beyond "The Burn Doctor")
Top picks are used in the logos. Availability (domain, Instagram, KEBS/BRS trademark) is NOT checked: search each before committing.

| # | Name | Meaning / feel | Why it works |
|---|---|---|---|
| 1 | **Afterglow** (by Dr. Wanjiru) | The glow after the fire | Links burn recovery to skin radiance. Soft, aesthetic, memorable. LOGO 3 |
| 2 | **Upya** | Swahili: newness, renewal | Rooted in Kenya, short, covers scars + skin + hair. LOGO 4 |
| 3 | **Ngozi** | Swahili: skin (also an Igbo name meaning blessing) | Proud, local, clear. Easy to say. LOGO 5 |
| 4 | **Nuru** | Swahili: light, radiance | Premium and warm. Works for aesthetics-led positioning |
| 5 | **Second Skin Studio** | New skin after injury | Speaks to burns and skin together, English-friendly |
| 6 | **Gold Seam** | Scars as gold repair (kintsugi idea) | Reframes scars as beautiful. Strong story for burn survivors |
| 7 | **Ash & Aura** | Fire and glow | Poetic, ties burns to aesthetics |
| 8 | **Beyond the Burn** | Life after the injury | Very clear for burn patients; weaker for aesthetics |
| 9 | **Ember Rose** | Warmth and softness | Feminine, elegant, flame reference |
| 10 | **Cheche Skin & Hair** | Swahili: spark | Light, friendly, energetic |
| 11 | **The Skin Atelier** | Craft and precision | Luxury positioning |
| 12 | **Wanjiru MD** | Her own name | Safest long-term: stays valid if services change |

**My recommendation:** Keep **Wanjiru MD** as the legal/professional name and website domain (best for trust and SEO), and use **Afterglow** or **Upya** as the aesthetic programme brand. Use "The Burn Doctor" as the social-media handle and burn-care signature line. Always keep "Dr. Wanjiru" in page titles so search engines connect the brand to her.

## 2. Logos
`logos/` holds the approved logo system: primary, stacked, wordmark, service taglines, mark, avatar, app icon, favicon and one-colour versions, as SVG (text outlined) with PNGs in `logos/png/`, and `LOGO-BOARD.png` for presenting.

| Brand | Colourways |
|---|---|
| Wanjiru MD | ivory-beige (your white + beige), cocoa-champagne, sage-linen |
| The Burn Doctor | ember-on-beige, midnight-flame, terracotta |
| Afterglow | blush-plum, plum-night, peach-cocoa |
| Upya | emerald-cream, forest-night, sage-clay |
| Ngozi | spectrum-cream, espresso-gold, terracotta-sand |

## 3. SEO done in the site
- Unique title (<=60 chars) and meta description on every page; one H1 per page; clean heading hierarchy
- Canonical, hreflang (en-KE), robots, Open Graph and Twitter cards, share image `images/og-default.png`
- JSON-LD: Physician (PlasticSurgery, Nairobi), WebSite, BreadcrumbList, MedicalWebPage, Article, FAQPage (only real on-page FAQs)
- `sitemap.xml`, `robots.txt`, favicon set, web manifest, 404 page
- Navigation and nav/footer in static HTML (crawlable), descriptive internal links, breadcrumbs, related-content blocks
- Local SEO copy: "Upper Hill, Nairobi" across headings and body; long-tail topics (keloid, traction alopecia, Afro-textured hair transplant, GLP-1)
- Content hub: 5 journal articles, an FAQ page, and 6 deep service pages
- Performance: lazy images with width/height, no JS dependencies, reduced-motion support, mobile-first layout

### To finish before launch (cannot be known from here)
1. Replace the placeholder domain `https://www.drwanjirumd.com` in `_build/lib.py` (SITE_URL), then run `python3 _build/build.py`
2. Add real phone, street address, hours, Instagram to the footer/contact and into the JSON-LD (telephone, streetAddress, geo, openingHours, sameAs)
3. Create and verify a Google Business Profile (biggest local-search lever) and submit sitemap.xml in Search Console
4. Add real photos (names below). Replace the descriptive `alt` text if the photo differs
5. Add her verified credentials. Do not publish unverified ones
6. Have Dr. Wanjiru review all medical copy. Check KMPDC advertising rules (before/after photos, claims)
7. Brand chosen: Dr. Wanjiru MD (arch logo). The brand switcher has been removed.

## 4. Images
The site shows illustrative art until real photos exist. Put JPGs in `images/` with these names and they appear automatically:
hero-1, hero-2, hero-3, about-portrait, burns-hero, burns-detail, scars-hero, hair-hero, hair-restoration-hero, skin-hero, aesthetics-hero, weight-hero, contact-hero, clinic-1..4, tile-burns/scars/hair/skin/aesthetics/weight, article-<slug>, and pairs `<pair>-before.jpg` / `<pair>-after.jpg` for burn-scar-1, burn-scar-2, keloid-1, hair-ba-1, hair-ba-2, skin-ba-1, skin-ba-2, weight-ba-1.

**Rules:** only real patients with signed written consent, same light/angle/distance, unretouched. AI images must be labelled illustrative and never presented as her results.

**Style suffix for every prompt:** editorial medical-beauty photography, soft natural window light, cream and beige background, accurate melanin-rich skin tones, true skin texture, no retouching or plastic smoothing.

| Slot | Prompt |
|---|---|
| hero-1 / about-portrait | Confident Black woman doctor in her late 30s, white coat over beige silk blouse, calm cream consultation room, soft smile |
| burns-hero | Macro of a healed, softened scar on a dark-skinned forearm, raking light, dignified, no open wounds |
| hair-hero | Black woman, natural 4C coils, healthy hairline, side profile, beige backdrop |
| skin-hero | Close portrait, dark-skinned woman, luminous even tone, minimal makeup |
| weight-hero | Black woman in neutral athletic wear, sunlit minimalist room, strong and healthy |
| clinic-1..4 | Minimal luxury clinic interior, ivory walls, oak shelf, beige armchair, plants, Nairobi light |
| burn-scar-1 | BEFORE: raised dark tight scald scar on a dark forearm. AFTER: same arm, same light, flatter, softer scar |
| hair-ba-1 | BEFORE: traction thinning at both temples. AFTER: same angle, restored natural hairline |
| skin-ba-1 | BEFORE: uneven post-acne dark marks on cheek. AFTER: same cheek, tone more even, pores visible |
| weight-ba-1 | BEFORE/AFTER: same woman, same clothing and pose, visibly slimmer, healthy-looking |

## 5. Image status (15 generated photos placed)
Filled with generated close-ups: hero-2, hero-3, burns-hero, burns-detail, scars-hero, hair-hero, hair-restoration-hero, skin-hero, aesthetics-hero, weight-hero, tile-* (6), article-* (5).
aesthetics-hero currently reuses a close crop of the glowing-skin image; replace with a syringe/treatment close-up when available.
Still showing placeholder art until real photos exist (drop the JPG in `images/` with the same name): hero-1, about-portrait, clinic-1..4, contact-hero, and all before/after pairs (burn-scar-1, keloid-1, hair-ba-1, hair-ba-2, skin-ba-1, skin-ba-2, weight-ba-1). These must be real photos with written patient consent.
