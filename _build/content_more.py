from lib import *

def _faqsec(items, cat, title, alt=True):
    f = faq(items, cat)
    return f'<section class="section{" section--alt" if alt else ""}"><div class="container narrow"><div class="center reveal"><span class="eyebrow">Questions</span><h2>{title}</h2></div><div class="mt2">{f}</div></div></section>'

# ============================================================== HAIR
def hair():
    h = hero_inner([('Services', 'services.html'), ('Hair loss', None)], 'Hair loss clinic', 'Your hair has a <em>story</em>. So does your hairline.',
                   'Most hair advice is written for straight hair. Tight coils grow differently, break differently and scar differently. A good plan begins with the right diagnosis.',
                   'hair-hero', 'Hair loss treatment for Black and Afro-textured hair in Nairobi')
    pat = [('traction', 'Traction alopecia', dl([('Where', 'Hairline, temples and edges'), ('Cause', 'Sustained pulling from tight braids, weaves, extensions, wigs, ponytails and buns'), ('Early signs', 'Tenderness, small bumps, headaches, broken edges, a thin “fringe” of hairs left at the very front'), ('Reversible?', 'Yes when caught early. Permanent once follicles scar after years of tension'), ('Treatment', 'Remove the tension, calm inflammation, minoxidil, PRP; transplant if scarred')])),
           ('ccca', 'CCCA', dl([('Name', 'Central centrifugal cicatricial alopecia'), ('Where', 'Crown, spreading outward'), ('Cause', 'Not fully understood: genetics and inflammation both appear to play a role, alongside hair-care factors'), ('Signs', 'Itch, tenderness or burning; smooth, shiny scalp where follicle openings are lost'), ('Reversible?', 'Scarred follicles do not return, so early diagnosis matters most'), ('Treatment', 'Anti-inflammatories (topical, injected, oral), minoxidil, PRP. Transplant only after long-term quiet disease')])),
           ('te', 'Telogen effluvium', dl([('Where', 'All over, with a general thinning'), ('Cause', 'A trigger 2 to 3 months earlier: illness, surgery, childbirth, crash dieting or rapid weight loss, low iron, thyroid disease, stress, new medicines'), ('Signs', 'Heavy shedding in the comb, shower or pillow'), ('Reversible?', 'Usually, within about 6 months once the trigger is removed'), ('Treatment', 'Find and treat the trigger, correct nutrients, patience; minoxidil sometimes')])),
           ('aga', 'Androgenetic alopecia', dl([('Where', 'Men: receding hairline and crown. Women: widening part and thinner crown'), ('Cause', 'Inherited sensitivity of follicles to hormones'), ('Course', 'Gradual and progressive without treatment'), ('Treatment', 'Minoxidil, anti-androgen medicines where suitable, PRP, and transplant for stable loss')])),
           ('areata', 'Alopecia areata', dl([('Where', 'Round, smooth patches anywhere on the scalp, beard or eyebrows'), ('Cause', 'Autoimmune: the body attacks follicles that are otherwise intact'), ('Reversible?', 'Often regrows, may recur'), ('Treatment', 'Steroid injections, topical treatments, and specialist options for extensive disease')]))]
    sel = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Interactive</span><h2>Where is your hair loss starting?</h2>
<p class="lead">Different causes start in different places. Select a pattern to see where it usually begins.</p></div>
<div class="mt2 split top reveal" data-tabs><div>{scalp_diagram()}</div><div>{tabs(pat, "Hair loss pattern")}</div></div></div></section>'''

    warn = f'''<section class="section section--alt"><div class="container split top"><div class="reveal"><span class="eyebrow">Do not wait</span><h2>Signs that need <em>early</em> attention.</h2>
<ul class="checks"><li>Pain, burning, itching or tenderness on the scalp</li><li>Small bumps or pimples around the hairline or crown</li><li>A smooth, shiny patch where hair used to grow</li><li>Hair that breaks off at the edges after styling</li><li>Sudden round bald patches</li><li>Shedding that lasts more than three months</li></ul>
{callout("Why early matters", "In scarring forms of hair loss such as CCCA and advanced traction alopecia, follicles that are lost are lost for good. Treating while the inflammation is active protects the hair you still have.")}</div>
<div class="reveal d1"><h3>What happens at your first hair visit</h3><ol class="steps"><li><h3>History</h3><p>Styles, products, heat, family history, diet, periods, pregnancies, illnesses and medicines.</p></li>
<li><h3>Scalp examination</h3><p>Under magnification (trichoscopy), pull test, and photographs to track progress.</p></li>
<li><h3>Tests where needed</h3><p>Iron studies, thyroid, vitamin D, hormones; a small scalp biopsy if scarring is suspected.</p></li>
<li><h3>A staged plan</h3><p>Protect what you have, regrow what can regrow, restore what cannot, in that order.</p></li></ol></div></div></section>'''

    styles = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Style safety</span><h2>Protective styles, protected properly.</h2>
<p class="lead">You do not have to give up the styles you love. You do have to respect tension.</p></div><div class="mt2">{table(["Style","Main risk","Safer way"],[
("Braids &amp; twists","Tension at the hairline, especially when long, heavy or tight","Ask for looser, smaller-weight installs; start the braid with your own hair, not extensions, at the edges; remove within 6 to 8 weeks"),
("Weaves &amp; sew-ins","Tight cornrow base, glue, heavy hair","Avoid glue on the scalp; keep the base loose; leave out the edges; rest the scalp between installs"),
("Wigs &amp; lace fronts","Adhesives and tight bands on the hairline","Use breathable caps, non-adhesive grips, and take them off at night"),
("Ponytails &amp; buns","Constant pull in the same direction","Vary the position, use soft ties, avoid very high or tight pulls"),
("Locs","Weight and tension at the root, over-twisting","Gentle maintenance; avoid tight retwists and heavy additions"),
("Relaxers &amp; hot combs","Scalp burns and breakage if overused","Space out treatments, avoid scalp contact, and never relax a sore or burnt scalp")])}</div>
{callout("The 3-second rule", "If a style hurts, causes headaches, raises bumps, or you cannot comfortably frown or blink, it is too tight. Take it down. Tension damage is cumulative and silent.")}</div></section>'''

    ladder = f'''<section class="section section--dark"><div class="container"><div class="center reveal"><span class="eyebrow">Treatment ladder</span><h2>From protection to restoration.</h2></div>
<div class="grid g4 mt2">{"".join(f'<div class="card reveal d{i%4}"><span class="num">{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Protect &amp; calm","Styling changes, scalp care, treating inflammation and underlying causes such as low iron or thyroid disease."),("Medical therapy","Minoxidil, anti-androgens or anti-inflammatory medicines as appropriate. Slow, steady, and monitored."),("In-clinic treatments","PRP, steroid injections for active patches, and microneedling to support follicles."),("Restoration","Hair transplantation for stable, permanent loss, planned for coils and for scar risk.")]))}</div>
<p class="center mt2 reveal"><a class="btn" href="hair-restoration.html">Hair restoration, in depth</a></p></div></section>'''

    myth = f'''<section class="section"><div class="container"><span class="eyebrow reveal">Hair myths</span><h2 class="reveal" style="max-width:18ch">What the salon forgot to mention.</h2><div class="mt">{myths([
("“Protective styles always protect.”","Not if they pull. A style is protective only if it is low tension, clean and removed on time."),
("“Hair loss is just genetics, nothing can be done.”","Some is, much is not. Traction, inflammation, nutrition and hormones are all treatable, and even inherited loss responds to treatment."),
("“Oils and growth serums regrow hair.”","Oils help moisture and breakage. They do not treat scarring or hormonal loss, and heavy products can aggravate scalp inflammation."),
("“Shedding after weight loss means it is permanent.”","Telogen effluvium after rapid weight loss is usually temporary. Nutrient support and pacing reduce it."),
("“A transplant fixes everything.”","Only stable loss with a healthy donor area is suitable, and it does not stop ongoing loss in untreated areas.")])}</div></div></section>'''
    faqs = _faqsec([
        ('Can hair loss from braids or weaves grow back?', 'If caught early, often yes. Once follicles scar, regrowth is not possible and a transplant may be the option, once the scalp is stable.'),
        ('Can I keep wearing protective styles?', 'Usually, with adjustments: lower tension, shorter wear time, no glue on the scalp, and breaks between installs.'),
        ('When will I see results?', 'Hair grows slowly. Medical therapies take about 3 to 6 months to show; transplanted hair takes around 9 to 12 months to mature.'),
        ('Is minoxidil safe for dark skin and scalp?', 'Yes, it is widely used. A prescriber will choose topical or oral forms and monitor for side effects. Not suitable for everyone, including in pregnancy.'),
        ('Why is my hair thinning at the crown?', 'Common causes include CCCA, androgenetic alopecia and traction. A scalp examination is the only way to tell them apart, and the treatments differ.'),
        ('Does stress cause hair loss?', 'Severe or prolonged stress can trigger telogen effluvium, which causes shedding two to three months later and usually recovers.')], 'hair', 'Hair loss FAQ')
    rel = related([('hair-restoration.html', 'Hair restoration', 'Transplants and regrowth plans.'), ('traction-alopecia.html', 'Traction alopecia guide', 'The full article.'), ('glp1-hair-skin.html', 'Weight loss and hair', 'Shedding after rapid weight loss.')])
    return page('hair.html', 'Hair Loss Treatment in Nairobi for Black Hair | Dr. Wanjiru MD',
                'Traction alopecia, CCCA, thinning and shedding diagnosed properly and treated for Afro-textured hair. Hair loss clinic in Upper Hill, Nairobi.',
                h + sel + warn + styles + ladder + myth + faqs + rel + cta('Find out what is really happening to your hair.', 'A scalp examination is the first step.', 'Book a hair consultation'),
                [('Services', 'services.html'), ('Hair loss', None)], 'MedicalWebPage', '0.9')

# ============================================================== HAIR RESTORATION
def restoration():
    h = hero_inner([('Services', 'services.html'), ('Hair restoration', None)], 'Hair restoration', 'A hairline that <em>looks like you</em>.',
                   'Hair transplantation for Black and Afro-textured hair demands a different technique, a different design and a different level of care for scarring.',
                   'hair-restoration-hero', 'Hair transplant planning for Afro-textured hair in Nairobi')
    cand = f'''<section class="section"><div class="container split top"><div class="reveal"><span class="eyebrow">Are you a candidate?</span><h2>Restoration works best when the <em>why</em> is clear.</h2>
<p class="lead">A transplant moves healthy follicles to where they are needed. It does not cure the cause of loss, so diagnosis comes first.</p></div>
<div class="grid g2 reveal d1"><div class="card"><h3>Often a good fit</h3><ul class="checks"><li>Stable loss for 6 to 12 months or more</li><li>Healthy, dense donor area</li><li>Inflammation controlled and diagnosis confirmed</li><li>Realistic expectations about density</li><li>Scars or burns on the scalp, brow or beard that are fully matured</li></ul></div>
<div class="card"><h3>Needs treatment first</h3><ul class="checks no"><li>Active scarring alopecia (CCCA)</li><li>Ongoing traction with no change in styling</li><li>Untreated thyroid, iron or hormonal causes</li><li>Very limited donor hair</li><li>Poorly controlled keloid tendency at the donor area</li></ul></div></div></div></section>'''

    diff = f'''<section class="section section--alt"><div class="container split"><div class="reveal">{img("clinic-3", "Hair transplant planning for tightly curled hair", "r45", "arch")}</div>
<div class="reveal d1"><span class="eyebrow">What is different</span><h2>Why coils change <em>everything.</em></h2>
<ul class="checks"><li><b>Curved follicles.</b> Tightly curled hair grows in a curve under the skin, so grafts are easier to damage. Extraction needs specialised punch sizing and technique.</li><li><b>Scar risk.</b> Skin that forms keloids needs careful choice of method and donor area, and often a smaller, scatter-free pattern.</li><li><b>Curl is an advantage.</b> Coiled hair gives more visual coverage per graft, so natural density can be achieved with thoughtful placement.</li><li><b>Hairline design.</b> A natural hairline for a Black face is not the template used for straight hair. Shape, height, temple points and softness are designed around you.</li><li><b>Healing and styling.</b> Plans account for protective styles, edges, and the weeks when tension must be avoided.</li></ul></div></div></section>'''

    opts = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Compare options</span><h2>The restoration toolkit.</h2></div><div class="mt2">{table(["Option","Best for","How it works","What to know"],[
("Medical therapy","Early thinning, androgenetic loss","Daily or oral medicines that slow loss and thicken hair","Needs months and ongoing use; foundation for any plan"),
("PRP","Early thinning, supporting weak follicles","Platelet-rich plasma from your blood, injected into the scalp","A course of sessions; adjunct, not a cure"),
("FUE transplant","Stable loss; most coiled-hair patients","Individual follicular units are extracted and implanted","Skill-dependent in coiled hair; leaves tiny dot scars; can be done with a short shave"),
("FUT (strip)","Larger sessions in selected patients","A strip of donor scalp is removed and dissected into grafts","A linear scar; usually avoided if keloid-prone"),
("Scar &amp; brow/beard restoration","Burn, surgical or traumatic scars; sparse brows or beards","Grafts placed into matured scar tissue or facial areas","Scar tissue has weaker blood supply, so results vary and sessions may be staged")])}</div></div></section>'''

    tl = f'''<section class="section section--dark"><div class="container"><div class="center reveal"><span class="eyebrow">The journey</span><h2>What to expect, month by month.</h2></div>{timeline([
("Day 0","Procedure","Local anaesthetic; extraction and placement over one day, sometimes two. Most people go home the same day."),
("Day 1–10","Scabs and swelling","Tiny scabs form and fall in about a week or two. Keep the head elevated when sleeping, avoid pressure and tension."),
("Week 2–8","Shedding","Transplanted hairs shed. This “shock loss” is normal and temporary."),
("Month 3–5","New growth","Fine hairs begin to appear. Patience matters."),
("Month 6–9","Thickening","Noticeable density; hairline softens."),
("Month 12–18","Final result","Hair matures and thickens. Styling returns to normal under guidance.")])}</div></section>'''

    ask = f'''<section class="section"><div class="container split top"><div class="reveal"><span class="eyebrow">Trust checklist</span><h2>Questions to ask <em>any</em> hair transplant clinic.</h2>
<p class="lead">Hair restoration is surgery. Use this list, here or anywhere else.</p></div>
<ul class="checks reveal d1"><li>Who personally performs the extraction and the placement?</li><li>How many Afro-textured hair patients have you treated, and can I see unretouched results on skin like mine?</li><li>How will you protect my donor area for the future?</li><li>What is my keloid and scarring risk, and what will you do about it?</li><li>What is the graft count, and what exactly is included in the written quote?</li><li>What happens if growth is poor?</li><li>Who do I call if something goes wrong at 2 a.m.?</li><li>Am I being rushed, or sold a “package”?</li></ul></div></section>'''

    proof = f'''<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">Results</span><h2>Density that looks like you.</h2></div><div class="grid g2 mt2" style="max-width:900px;margin-inline:auto">{ba("hair-ba-1","Hairline restoration","Traction alopecia · 10 months")}{ba("hair-ba-2","Crown density","Thinning crown · 8 months")}</div><div class="mt">{DISCLAIMER}</div></div></section>'''

    faqs = _faqsec([
        ('How many grafts will I need?', 'It depends on the area, your donor density and the density you want. You will get a written graft estimate after assessment, never a number from a photo.'),
        ('Is a hair transplant permanent?', 'Transplanted follicles are taken from areas resistant to loss, so they usually last. Untreated native hair around them can still thin, which is why a long-term plan matters.'),
        ('Will it scar?', 'FUE leaves tiny dot scars that are usually hard to see; FUT leaves a linear scar. For keloid-prone skin, technique and donor choice are planned with extra care.'),
        ('When can I braid or wear weaves again?', 'Not for several weeks, and never tight on the recipient area. Your surgeon will give a timeline and advise safe installs.'),
        ('How much does it cost?', 'Pricing depends on the number of grafts and the complexity. You will receive a clear written quote after assessment.'),
        ('Can women have transplants?', 'Yes, if the cause is stable and suitable. Many women with traction alopecia or hairline loss are good candidates once the cause is controlled.')], 'restoration', 'Hair restoration FAQ', False)
    rel = related([('hair.html', 'Hair loss clinic', 'Diagnosis and non-surgical plans.'), ('scars.html', 'Scars &amp; keloids', 'Scar care that supports restoration.'), ('traction-alopecia.html', 'Traction alopecia', 'Read the full guide.')])
    return page('hair-restoration.html', 'Hair Transplant Nairobi for Afro-Textured Hair | Dr. Wanjiru',
                'Hair transplant and restoration planned for Black and coiled hair, scar-aware and honest about results. Upper Hill, Nairobi.',
                h + cand + diff + opts + tl + ask + proof + faqs + rel + cta('Plan your restoration, properly.', 'Bring your questions. We will bring the diagnosis.', 'Book a restoration consultation'),
                [('Services', 'services.html'), ('Hair restoration', None)], 'MedicalWebPage', '0.9')

# ============================================================== SKIN
def skin():
    h = hero_inner([('Services', 'services.html'), ('Skin of colour', None)], 'Skin of colour', 'Glow is a <em>medical</em> outcome.',
                   'Melanin-rich skin is powerful and reactive. It rarely forgives guesswork. Every plan here begins with protecting the skin, then improving it.',
                   'skin-hero', 'Skin care for melanin-rich Black skin in Nairobi')
    fitz = ''.join(f'<div class="{c}" style="background:{b}">{r}</div>' for r, b, c in [('I', '#F3D9C4', 'lt'), ('II', '#E3B995', 'lt'), ('III', '#C99068', ''), ('IV', '#A86B45', ''), ('V', '#6F4126', ''), ('VI', '#34190E', '')])
    why = f'''<section class="section"><div class="container split"><div class="reveal"><span class="eyebrow">The rule of melanin</span><h2>Why dark skin needs a <em>different</em> approach.</h2>
<p>Melanocytes in deeper skin tones respond to inflammation, irritation and injury by making more pigment. A peel that is fine on lighter skin can leave dark marks on yours. A harsh laser can cause pale or dark patches. Over-the-counter bleaching creams can cause permanent damage.</p>
<p>So the plan is low and slow: calm the skin, protect it from sun, treat pigment gently, and escalate only when the skin is ready.</p>
<div class="swatches" aria-label="Fitzpatrick skin types I to VI">{fitz}</div><p class="small">Fitzpatrick types describe how skin reacts to sun, not ethnicity. Most Kenyans sit in types IV to VI, where pigment complications are the main risk.</p></div>
<div class="reveal d1">{img("skin-hero", "Even-toned glowing Black skin", "r45", "arch")}</div></div></section>'''

    routines = [
        ('acne', 'Acne-prone', dl([('Morning', 'Gentle cleanser → niacinamide or azelaic acid → oil-free moisturiser → SPF 30+'), ('Evening', 'Gentle cleanser → adapalene (a few nights a week, building up) → moisturiser'), ('Avoid', 'Scrubs, picking, toothpaste, lemon, harsh alcohol toners'), ('See us if', 'Deep cysts, scarring, or no change after 8 to 12 weeks')])),
        ('pigment', 'Dark marks &amp; melasma', dl([('Morning', 'Gentle cleanser → vitamin C or azelaic acid → moisturiser → tinted SPF 30+ with iron oxides'), ('Evening', 'Gentle cleanser → azelaic acid or niacinamide → moisturiser; prescription options at consultation'), ('Avoid', 'Unregulated bleaching creams, DIY lemon or baking soda, sun without protection'), ('See us if', 'Marks are spreading, symmetrical on the cheeks, or not fading after 3 months')])),
        ('dull', 'Dry &amp; dull', dl([('Morning', 'Creamy cleanser → hydrating serum (hyaluronic acid) → moisturiser → SPF 30+'), ('Evening', 'Cleanser → lactic acid or mild exfoliant 1 to 2 nights a week → rich moisturiser'), ('Avoid', 'Very hot water, over-exfoliating, fragranced products on irritated skin'), ('Tip', 'Moisturise on damp skin and seal with an occlusive on dry areas')])),
        ('razor', 'Razor bumps &amp; sensitive', dl([('Shaving', 'Shave with the grain, use a clean single-blade or clippers with a guard, warm water, no stretching the skin'), ('After', 'Calming moisturiser; low-strength salicylic or glycolic acid a few nights a week'), ('Avoid', 'Very close shaves, plucking ingrown hairs deeply, harsh astringents'), ('See us if', 'Persistent bumps or dark marks. Prescription treatment or laser hair reduction can help')]))]
    rt = f'''<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">Interactive</span><h2>Build a starter routine.</h2>
<p class="lead">General guidance for common concerns. Prescription-strength plans are made after examination.</p></div><div class="mt2 reveal" data-tabs>{tabs(routines, "Routine type")}</div></div></section>'''

    cond = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Concerns we treat</span><h2>Common, and commonly mistreated.</h2></div><div class="grid g3 mt2">
{"".join(f'<div class="card reveal d{i%3}"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Hyperpigmentation (PIH)","Dark marks after acne, shaving, eczema or injury. The first goal is to stop the trigger, then fade the mark."),("Melasma","Hormonal, sun-triggered patches that return easily. Managed, not “cured”, with strict sun protection and layered therapy."),("Acne &amp; acne scarring","Control active acne first, then address texture with careful, melanin-aware techniques."),("Razor bumps (PFB)","Curved hairs re-enter the skin and inflame it. Shaving changes, medical therapy, and laser hair reduction."),("Dermatosis papulosa nigra","Small dark benign bumps on the cheeks, common on darker skin, treated gently if desired."),("Bleaching damage","Recovery from steroid, mercury or high-strength hydroquinone harm, with respect and no judgement.")]))}</div></div></section>'''

    ing = f'''<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">Ingredients</span><h2>What helps, and what to watch.</h2></div><div class="mt2">{table(["Ingredient","Helps with","Notes for dark skin"],[
("Sunscreen SPF 30+","All pigment concerns, scars","Daily, reapplied. Choose formulas that blend without a cast; iron-oxide tints also help melasma"),
("Azelaic acid","Acne, dark marks, melasma","Gentle and effective; suitable for long-term use"),
("Niacinamide","Oiliness, tone, barrier","Well tolerated; good starter ingredient"),
("Vitamin C","Glow, mild pigment","Use stable formulas; may sting if skin is irritated"),
("Retinoids (adapalene, tretinoin)","Acne, texture, dark marks","Introduce slowly; irritation itself can cause new dark marks"),
("Hydroquinone","Stubborn pigment","Prescription only, short cycles, supervised. Prolonged high-strength use can cause permanent darkening"),
("Tranexamic acid","Melasma","Topical or oral under medical supervision; oral requires screening"),
("Superficial peels","Acne, texture, tone","Low strength, built up slowly with skin conditioning")])}</div>
{callout("Avoid", "Creams containing mercury or undeclared steroids, “skin lightening” injections, and DIY lemon, baking soda or toothpaste treatments. They can cause lasting damage.", True)}</div></section>'''

    proof = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Results</span><h2>Even tone. Real texture. Still you.</h2></div><div class="grid g2 mt2" style="max-width:900px;margin-inline:auto">{ba("skin-ba-1","Hyperpigmentation","Medical-grade plan · 12 weeks")}{ba("skin-ba-2","Acne scarring","Combination plan · 5 months")}</div><div class="mt">{DISCLAIMER}</div></div></section>'''
    faqs = _faqsec([
        ('Does Black skin need sunscreen?', 'Yes. Melanin gives some protection (roughly an SPF of 13), but not enough to prevent pigmentation, melasma, burns or skin cancer. Daily sunscreen is the most useful product for dark skin.'),
        ('Is it safe to lighten my skin?', 'Evening out dark marks and melasma is safe when done medically. Lightening your natural skin colour is not something we do.'),
        ('Why do my dark marks keep coming back?', 'Usually because the trigger is still active: sun, inflammation, hormones or harsh products. We treat the trigger, not only the mark.'),
        ('Do I need many sessions?', 'Most skin concerns need a series and consistent home care. You will have a clear plan and a review point before anything is repeated.'),
        ('Can lasers be used on dark skin?', 'Some can, with the correct wavelength, conservative energy and a test patch. The device and the operator matter more than the brand.'),
        ('Is it normal for skin to darken after a peel?', 'Mild temporary darkening can occur. That is why dark skin needs low-strength peels, skin preparation and strict sun protection.')], 'skin', 'Skin FAQ')
    rel = related([('sunscreen-black-skin.html', 'Sunscreen guide', 'Why it matters and how to pick.'), ('aesthetics.html', 'Non-surgical aesthetics', 'Peels, microneedling and more.'), ('scars.html', 'Scars &amp; keloids', 'Acne scars and beyond.')])
    return page('skin.html', 'Skin of Colour Clinic Nairobi | Dr. Wanjiru MD',
                'Medical skin care for melanin-rich skin: hyperpigmentation, melasma, acne and acne scars, razor bumps and bleaching damage. Upper Hill, Nairobi.',
                h + why + rt + cond + ing + proof + faqs + rel + cta('A plan built for melanin, not borrowed from a brochure.', '', 'Book a skin consultation'),
                [('Services', 'services.html'), ('Skin of colour', None)], 'MedicalWebPage', '0.9')

# ============================================================== AESTHETICS
def aesthetics():
    h = hero_inner([('Services', 'services.html'), ('Non-surgical aesthetics', None)], 'Non-surgical aesthetics', 'Subtle. Safe. <em>Unmistakably</em> you.',
                   'Botulinum toxin, fillers, peels, microneedling and tightening, planned by a plastic surgeon who understands anatomy, and Black skin.',
                   'aesthetics-hero', 'Non-surgical aesthetic treatments including botulinum toxin and fillers in Nairobi')
    t = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">The menu</span><h2>Treatments at a glance.</h2><p class="lead">Availability of each treatment is confirmed at consultation.</p></div><div class="mt2">{table(["Treatment","Best for","Starts working","Typically lasts","Downtime"],[
("Botulinum toxin","Frown, forehead and crow’s feet lines; jaw slimming; brow shaping","3 to 7 days, peak at ~2 weeks","About 3 to 4 months","None to minimal"),
("Dermal fillers (hyaluronic acid)","Cheeks, chin, jawline, lips, tear troughs","Immediately","6 to 18 months, by area and product","Swelling or bruising for 2 to 5 days"),
("Skin boosters / PRP facial","Hydration, glow, fine lines","2 to 6 weeks","Series, then maintenance","Minimal"),
("Superficial peels","Tone, acne, texture","1 to 2 weeks","Series","Light flaking for 2 to 5 days"),
("Microneedling / RF needling","Scars, texture, early laxity","4 to 6 weeks","Series of 3 to 6","Redness for 1 to 3 days"),
("Laser hair removal (Nd:YAG)","Unwanted hair, razor bumps","Gradual over sessions","Long-term reduction","Minimal"),
("Skin tightening (RF / ultrasound)","Mild laxity of face, neck, body","2 to 3 months","Up to about a year","Minimal")])}</div></div></section>'''

    age = f'''<section class="section section--alt"><div class="container split"><div class="reveal">{img("clinic-2", "Consultation for natural-looking aesthetic treatment in Nairobi", "r169")}</div>
<div class="reveal d1"><span class="eyebrow">Ageing, honestly</span><h2>“Black don’t crack” is half the story.</h2>
<p>Melanin does protect against sun damage, so deep lines often appear later. But dark skin still ages, usually through <b>volume loss</b> in the mid-face, <b>uneven pigment</b>, dullness and loss of firmness.</p>
<p>That changes the plan: less about freezing expression, more about supporting structure, restoring light reflection and keeping tone even, with a lighter hand than the “standard” template.</p></div></div></section>'''

    safe = f'''<section class="section"><div class="container split top"><div class="reveal"><span class="eyebrow">Safety first</span><h2>How to choose an injector.</h2>
<p class="lead">Injectables are medical procedures. These questions protect you wherever you go.</p></div><ul class="checks reveal d1"><li>Is the person a doctor trained in facial anatomy?</li><li>Will you see the sealed product, its brand and batch number?</li><li>Is hyaluronidase (the filler-dissolving antidote) on hand?</li><li>Do they explain risks, including vascular complications, before you decide?</li><li>Is it a sterile clinic, not a home, a party or a pop-up?</li><li>Can they show results on skin tones like yours?</li><li>Are you given time to think, or pushed to decide on the day?</li></ul></div></section>'''
    warn = f'<section class="section" style="padding-top:0"><div class="container narrow">{callout("Call straight away if", "after filler you notice severe or increasing pain, skin turning white, grey or mottled, or changes in vision. These can signal a blood-vessel complication that needs urgent treatment.", True)}</div></section>'

    proof = f'''<section class="section section--dark"><div class="container"><div class="center reveal"><span class="eyebrow">Our approach</span><h2>Natural, never overdone.</h2></div><div class="grid g3 mt2">
<div class="card reveal"><span class="num">I</span><h3>Map before we touch</h3><p>Photographs, anatomy and your goals agreed before a needle comes out.</p></div>
<div class="card reveal d1"><span class="num">II</span><h3>Less, then review</h3><p>Conservative first sessions with a two-week review. You can always add more.</p></div>
<div class="card reveal d2"><span class="num">III</span><h3>Care that continues</h3><p>Aftercare advice, emergency contact and follow-up included.</p></div></div></div></section>'''
    faqs = _faqsec([
        ('Will I look frozen or “done”?', 'Not if the plan is conservative. The goal is to soften what bothers you while keeping natural movement and your own features.'),
        ('Do fillers work on Black faces?', 'Yes. The planning differs: structure, volume and proportion are often more relevant than lines, and technique is adjusted to reduce bruising and pigment risks.'),
        ('How much downtime is there?', 'Most treatments have little. Botulinum toxin needs none; fillers may bring swelling or bruising for a few days; peels may flake for several.'),
        ('Can fillers be dissolved?', 'Hyaluronic acid fillers can be dissolved with hyaluronidase if needed, which is one reason they are widely used.'),
        ('Is it safe to combine treatments?', 'Often yes, and sequencing matters. Your plan will say what to do first and what to leave until the skin is ready.')], 'aesthetics', 'Aesthetics FAQ', False)
    rel = related([('skin.html', 'Skin of colour', 'Pigmentation, acne and glow.'), ('weight-loss.html', 'Weight loss', 'Facial volume and skin after weight loss.'), ('scars.html', 'Scars &amp; keloids', 'Needling and laser for scars.')])
    return page('aesthetics.html', 'Botox, Fillers & Non-Surgical Aesthetics Nairobi | Dr. Wanjiru',
                'Botulinum toxin, dermal fillers, peels, microneedling and skin tightening for Black skin, by a plastic surgeon in Upper Hill, Nairobi.',
                h + t + age + safe + warn + proof + faqs + rel + cta('Natural results start with a conversation.', '', 'Book an aesthetics consultation'),
                [('Services', 'services.html'), ('Non-surgical aesthetics', None)], 'MedicalWebPage', '0.9')

# ============================================================== WEIGHT
def weight():
    h = hero_inner([('Services', 'services.html'), ('Weight loss', None)], 'Medical weight loss &amp; GLP-1', 'Lose the weight. <em>Keep</em> the rest of you.',
                   'GLP-1 medicines can be powerful tools. Used well, they change health. Used carelessly, they can cost muscle, hair and skin quality. This clinic plans for all three.',
                   'weight-hero', 'Medically supervised GLP-1 weight loss in Nairobi')
    what = f'''<section class="section"><div class="container split"><div class="reveal"><span class="eyebrow">What these medicines do</span><h2>A tool, <em>not</em> a shortcut.</h2>
<p>GLP-1 receptor agonists, such as semaglutide and tirzepatide (which also acts on GIP), act on appetite and blood-sugar signalling. Alongside nutrition, movement and follow-up, they can produce significant weight loss. They are prescription medicines that need a medical assessment first.</p>
<p>Doses are started low and increased gradually, often every few weeks, to reduce side effects. Nausea, constipation, diarrhoea and reflux are common early on and are managed with dose pacing and food choices.</p></div>
<div class="grid g2 reveal d1"><div class="card"><h3>May suit</h3><ul class="checks"><li>BMI 30 or above</li><li>BMI 27 or above with a weight-related condition</li><li>Type 2 diabetes, prediabetes, fatty liver, sleep apnoea, PCOS</li><li>Past attempts at lifestyle change that did not hold</li></ul></div>
<div class="card"><h3>Needs review first</h3><ul class="checks no"><li>Pregnancy or planning pregnancy</li><li>History of pancreatitis or gallbladder disease</li><li>Personal or family history of medullary thyroid cancer or MEN2</li><li>Severe digestive disease, or a history of eating disorder</li></ul></div></div></div></section>'''

    cost = f'''<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">The part most clinics skip</span><h2>What fast weight loss does to the rest of you.</h2></div>
<div class="grid g3 mt2"><div class="card reveal"><span class="num">01</span><h3>Muscle</h3><p>A meaningful share of weight lost can be lean mass, including muscle. Protein targets and resistance training protect strength and metabolism.</p></div>
<div class="card reveal d1"><span class="num">02</span><h3>Hair</h3><p>Rapid loss can trigger temporary shedding about 2 to 4 months later. Checking iron, protein and other nutrients early reduces the risk.</p></div>
<div class="card reveal d2"><span class="num">03</span><h3>Skin &amp; face</h3><p>Faces can look hollow and bodies can have loose skin. A steady pace, hydration, and later options such as tightening or contouring are planned from the start.</p></div></div></div></section>'''

    stages = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Your programme</span><h2>Four stages, one doctor.</h2></div>{timeline([
("Stage 1","Assess","History, examination, bloodwork, blood pressure and body composition. A candid conversation about goals, past attempts and food."),
("Stage 2","Start low","Medicine chosen if appropriate, dose increased gradually, with a side-effect plan from day one."),
("Stage 3","Protect","Protein, strength training, hydration, sleep, and regular reviews of hair, skin and mood."),
("Stage 4","Maintain &amp; contour","A plan for staying at goal, and aesthetic options for the body you now have.")])}</div></section>'''

    weeks = f'''<section class="section section--dark"><div class="container split top"><div class="reveal"><span class="eyebrow">Daily habits</span><h2>The four <em>non-negotiables.</em></h2>
<ul class="checks"><li><b>Protein at every meal</b>, at a level your doctor sets for you</li><li><b>Strength training</b> two to three times a week to protect muscle</li><li><b>Fluids and fibre</b> to manage constipation and dehydration</li><li><b>Sleep and stress care</b>, which influence both appetite and hair</li></ul>
<p class="mt">We also monitor weight and waist, blood pressure, glucose, cholesterol, liver and kidney tests, and nutrients such as iron, B12 and vitamin D.</p></div>
<div class="reveal d1">{callout("Beware falsified pens", "Falsified and unregulated GLP-1 products have been reported worldwide and sold online. Only use medicines prescribed and supplied through a licensed pharmacy, with the packaging and batch checked.", True)}
{callout("Stopping", "In clinical trials, many people regain a large share of the weight after stopping, if no maintenance plan is in place. That is why maintenance is planned from the start.")}</div></div></section>'''

    after = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">After weight loss</span><h2>Skin-aware body care.</h2></div><div class="grid g4 mt2">
{"".join(f'<div class="card reveal d{i%4}"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Skin tightening","Non-surgical options for mild to moderate laxity, selected for darker skin tones."),("Facial volume","Conservative restoration where weight loss has changed the face."),("Stretch marks","Needling and other therapies to improve texture and colour."),("Surgical contouring","Considered once weight has been stable for several months, with careful scar planning for keloid-prone skin.")]))}</div></div></section>'''
    proof = f'<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">Results</span><h2>Healthier, and still recognisably you.</h2></div><div class="mt2" style="max-width:420px;margin-inline:auto">{ba("weight-ba-1","Medically supervised weight programme","7 months")}</div><div class="mt">{DISCLAIMER}</div></div></section>'
    faqs = _faqsec([
        ('Will I regain the weight if I stop?', 'Many people do if habits and support do not change. Maintenance, including nutrition, strength training and sometimes ongoing medication, is planned from the start.'),
        ('Is it only for people with obesity?', 'Eligibility depends on BMI, health conditions and medical history, and is a decision made at consultation.'),
        ('Will it make my hair fall out?', 'Temporary shedding can follow rapid weight loss. Nutrient support and a steady pace reduce it, and it usually recovers within months.'),
        ('How fast should I lose weight?', 'A steady pace is safer for muscle, skin and hair. Your doctor will set targets for you rather than chase the fastest possible loss.'),
        ('Can I have a tummy tuck or body lift later?', 'Often yes, once weight has been stable for some months and you are healthy. Planning for scars starts early.')], 'weight', 'Weight care FAQ', False)
    rel = related([('glp1-hair-skin.html', 'GLP-1, hair and skin', 'The full article.'), ('hair.html', 'Hair loss clinic', 'Shedding after weight loss.'), ('aesthetics.html', 'Non-surgical aesthetics', 'Face and skin after weight loss.')])
    return page('weight-loss.html', 'Medical Weight Loss & GLP-1 Nairobi | Dr. Wanjiru MD',
                'Doctor-supervised GLP-1 weight loss that protects muscle, hair and skin, with body contouring planned for the body that follows. Upper Hill, Nairobi.',
                h + what + cost + stages + weeks + after + proof + faqs + rel + cta('Start with a conversation, not a prescription.', '', 'Book a weight consultation'),
                [('Services', 'services.html'), ('Weight loss', None)], 'MedicalWebPage', '0.9')
