from lib import *
from data import ARTICLES

FLAME = MARK.replace('var(--accent)', '#F1DDD4').replace('var(--bg)', '#3A2420')

def home():
    badge = ('<div class="badge" aria-hidden="true"><svg class="ring" viewBox="0 0 150 150"><defs><path id="bp" d="M75,75 m-57,0 a57,57 0 1,1 114,0 a57,57 0 1,1 -114,0"/></defs>'
             '<text font-size="10.5" letter-spacing="3.4" fill="currentColor" style="font-family:var(--sans);text-transform:uppercase"><textPath href="#bp">Burns · Scars · Skin · Hair · Weight ·</textPath></text></svg>'
             f'<span class="core">{FLAME}</span></div>')
    hero = f'''<section class="hero"><div class="container hero-grid"><div>
<span class="eyebrow reveal">Plastic &amp; reconstructive surgeon · Upper Hill, Nairobi</span>
<h1 class="reveal d1">Healing skin. Restoring hair. <em>Rebuilding confidence.</em></h1>
<p class="lead reveal d2">Dr. Wanjiru MD treats burns, scars, skin, hair and weight with one conviction: Black and melanin-rich skin deserves care designed for it, not borrowed from textbooks that forgot it.</p>
<div class="btn-row reveal d3"><a class="btn btn--solid" href="contact.html">Book a consultation</a><a class="btn" href="burns.html">Explore burn care</a></div>
<div class="trust reveal d3"><span>Burn &amp; scar specialist</span><span>Skin of colour focus</span><span>One-to-one care</span></div></div>
<div class="collage reveal d2">{img("hero-1", "Dr. Wanjiru, plastic and reconstructive surgeon, in her clinic in Upper Hill, Nairobi", "r34", "c1 float", True)}
{img("hero-2", "Burn scar treatment: healing after a burn injury", "r11", "c2 float d", True)}{img("hero-3", "Glowing, even-toned Black skin after treatment", "r45", "c3 float e", True)}{badge}</div></div></section>
<div class="marquee" aria-hidden="true"><div class="marquee-track">{"".join(f"<span>{x}</span>" for x in ["Burn scar revision","Keloid care","Traction alopecia","Hair transplant","Hyperpigmentation","Acne scarring","Botox &amp; fillers","GLP-1 weight care","Skin tightening","Contracture release"]*2)}</div></div>'''

    why = f'''<section class="section"><div class="container split">
<div class="reveal"><span class="eyebrow">Why “the Burn Doctor”</span><h2>Burns are the work that taught her everything else.</h2>
<p class="lead">A burn is never only a surface problem. It changes how skin heals, how a joint moves, how a person walks into a room.</p>
<p>Burn and reconstructive surgery is the quiet specialty almost nobody markets, and the hardest school in plastic surgery. Every aesthetic treatment here inherits its discipline: gentle hands, honest timelines, and a deep respect for skin that scars, pigments and heals differently.</p>
<p>That is why a patient who comes for hair, a keloid or a glow-up gets the same careful planning as a patient rebuilding after a burn.</p>
<a class="link-arrow" href="burns.html">Read the burn story</a></div>
<div class="reveal d1">{img("burns-hero", "Healing after a burn: scar care for Black skin in Nairobi", "r45", "arch")}</div></div></section>'''

    pillars = f'''<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">What we treat</span><h2>Six specialities. One standard.</h2>
<p class="lead">Each begins with a diagnosis, never a package.</p></div>
<div class="grid g3 mt2">{tile("burns.html","01","Burns &amp; recovery","First aid, scar prevention, contracture release, and the long road after the wound closes.","tile-burns")}
{tile("scars.html","02","Scars &amp; keloids","Raised, tight, dark or pitted: combination care for the scars others are afraid to touch.","tile-scars")}
{tile("hair.html","03","Hair loss &amp; restoration","Traction alopecia, CCCA, thinning, and transplants planned for tight coils.","tile-hair")}
{tile("skin.html","04","Skin of colour","Pigmentation, melasma, acne and razor bumps, treated without risking rebound darkening.","tile-skin")}
{tile("aesthetics.html","05","Non-surgical aesthetics","Botox, fillers, peels, microneedling and tightening: subtle, safe, tailored.","tile-aesthetics")}
{tile("weight-loss.html","06","Weight loss &amp; GLP-1","Medically supervised, muscle-protecting, skin-aware weight care.","tile-weight")}</div></div></section>'''

    didyou = f'''<section class="section section--dark"><div class="container"><div class="center reveal"><span class="eyebrow">Did you know</span><h2>Four things almost nobody tells you.</h2></div>
<div class="mt2">{facts([("20 min","of cool running water is the single best first-aid step for any burn. Not ice. Not butter."),("12–24","months for a scar to fully mature. What you do in that window shapes the result."),("1st","sign of traction alopecia is often tenderness or small bumps, long before the thinning shows."),("3–6","months after rapid weight loss is when hair shedding peaks. It usually recovers, and can often be reduced.")])}</div></div></section>'''

    proof = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Results</span><h2>Real change, honestly shown.</h2>
<p class="lead">Drag to compare. Every case comes with its timeline, because healing is never overnight.</p></div>
<div class="grid g3 mt2">{ba("burn-scar-1","Forearm burn scar","Silicone, injections and laser · 9 months")}{ba("hair-ba-1","Hairline restoration","Traction alopecia · 10 months")}{ba("skin-ba-1","Hyperpigmentation","Medical-grade plan · 12 weeks")}</div>
<div class="mt">{DISCLAIMER}</div></div></section>'''

    process = f'''<section class="section section--alt"><div class="container split top"><div class="reveal"><span class="eyebrow">Your first visit</span><h2>Unhurried. Thorough. <em>Honest.</em></h2>
<p class="lead">No pressure packages, no template plans. You leave with a diagnosis, a roadmap and a realistic timeline.</p>
{img("clinic-1", "Calm consultation room at Dr. Wanjiru's clinic, Upper Hill, Nairobi", "r169", "mt")}</div>
<ol class="steps reveal d1"><li><h3>We listen</h3><p>Your history, your goals, what you have tried and what worried you about it.</p></li>
<li><h3>We examine</h3><p>Skin, scalp or scar assessed under magnification, with baseline photographs.</p></li>
<li><h3>We plan</h3><p>Options ranked from gentlest to most definitive, with timelines, costs and risks in writing.</p></li>
<li><h3>We begin, and we follow up</h3><p>Treatment in stages, with review points so nothing is repeated without a reason.</p></li></ol></div></section>'''

    menu = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Non-surgical menu</span><h2>Subtle by design.</h2></div>
<div class="grid g4 mt2">{"".join(f'<div class="card reveal d{i%4}"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Botulinum toxin","Softens lines, slims the jaw, lifts the brow. Natural movement kept."),("Dermal fillers","Restores volume and contour, with precise placement and safety first."),("Peels &amp; resurfacing","Gentle, melanin-aware peels for tone, texture and clarity."),("Microneedling &amp; PRP","Collagen stimulation for scars, texture, and hair support."),("Skin tightening","Radiofrequency and ultrasound options for early laxity."),("Laser (selected)","Only wavelengths proven safe for deeper skin tones."),("Hair therapies","PRP and medical therapy for thinning and shedding."),("Scar treatments","Injections, needling, laser and release for every scar type.")]))}</div>
<div class="center mt2 reveal"><a class="btn" href="aesthetics.html">See the full menu</a></div></div></section>'''

    journal = f'''<section class="section section--alt"><div class="container"><div class="reveal" style="display:flex;justify-content:space-between;align-items:end;gap:2rem;flex-wrap:wrap"><div><span class="eyebrow">Journal</span><h2 style="margin:0">Straight talk, in plain language.</h2></div><a class="link-arrow" href="journal.html">All articles</a></div>
<div class="grid g3 mt2">{"".join(post_card(s,t,d,m,i) for i,(s,t,d,m) in enumerate(ARTICLES[:3]))}</div></div></section>'''

    faqs = faq([
        ('Who is Dr. Wanjiru?', 'Dr. Wanjiru MD is a plastic and reconstructive surgeon based in Upper Hill, Nairobi, with a special interest in burn recovery and in aesthetic care for Black and melanin-rich skin, hair and body.'),
        ('Do you only treat burns?', 'No. Burn and scar care is the foundation of the practice, but Dr. Wanjiru also treats hair loss, skin concerns, non-surgical aesthetics and medical weight loss, using the same careful, skin-of-colour-first approach.'),
        ('Is it safe to have lasers, peels or microneedling on dark skin?', 'It can be, with the right device, conservative settings, test patches and an experienced practitioner. The wrong approach can cause lasting dark or pale marks, so the plan is always tailored to your skin.'),
        ('Do I need a consultation first?', 'Yes. Every plan starts with a consultation so we can diagnose properly, discuss risks and give you a written roadmap before anything is done.'),
        ('Where is the clinic?', 'In Upper Hill, Nairobi. Exact building, floor and access details are on the contact page.')])
    faqsec = f'<section class="section"><div class="container narrow"><div class="center reveal"><span class="eyebrow">Common questions</span><h2>Before you book.</h2></div><div class="mt2">{faqs}</div><p class="center mt"><a class="link-arrow" href="faq.html">More questions</a></p></div></section>'
    body = hero + why + pillars + didyou + proof + process + menu + journal + faqsec + cta('One honest conversation about your skin, your hair, your body.', 'Consultations are one-to-one, unhurried, and end with a written plan.', 'Book a consultation', 'contact.html', ('Explore services', 'services.html'))
    return page('index.html', 'Dr. Wanjiru MD | Burn Scar, Skin & Hair Surgeon in Nairobi',
                'Plastic & reconstructive surgeon in Upper Hill, Nairobi. Burn scar revision, keloids, hair restoration, skin of colour care and GLP-1 weight loss.', body, [], 'WebPage', '1.0')

def services():
    body = f'''<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-current="page">Services</span></nav>
<span class="eyebrow reveal">Services</span><h1 class="reveal d1">Six specialities, <em>one</em> standard of care.</h1>
<p class="lead reveal d2">Choose a path, or start with a consultation and we will map it together.</p></div></section>
<section class="section"><div class="container"><div class="grid g3">{tile("burns.html","01","Burns &amp; recovery","First aid, scar prevention, contracture release and long-term care.","tile-burns")}
{tile("scars.html","02","Scars &amp; keloids","Hypertrophic, keloid, acne and surgical scars.","tile-scars")}{tile("hair.html","03","Hair loss clinic","Traction alopecia, CCCA, thinning, shedding, scalp health.","tile-hair")}
{tile("hair-restoration.html","04","Hair restoration","Transplants and regrowth plans for Afro-textured hair.","tile-hair")}{tile("skin.html","05","Skin of colour","Pigmentation, melasma, acne, razor bumps and glow.","tile-skin")}
{tile("aesthetics.html","06","Non-surgical aesthetics","Botox, fillers, peels, microneedling and tightening.","tile-aesthetics")}</div>
<div class="mt">{tile("weight-loss.html","07","Medical weight loss &amp; GLP-1","Supervised, muscle-protecting, skin-aware.","tile-weight","wide")}</div></div></section>
<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">How we work</span><h2>Five principles behind every plan.</h2></div>
<div class="grid g3 mt2"><div class="card reveal"><span class="num">I</span><h3>Diagnosis first</h3><p>No treatment before we know exactly what we are treating and why.</p></div>
<div class="card reveal d1"><span class="num">II</span><h3>Skin of colour, always</h3><p>Devices, peels and medicines chosen for melanin-rich skin and its healing patterns.</p></div>
<div class="card reveal d2"><span class="num">III</span><h3>Gentlest effective option</h3><p>We climb the treatment ladder only as far as your goals require.</p></div>
<div class="card reveal"><span class="num">IV</span><h3>Honest timelines</h3><p>You will know what to expect, when, and what can go wrong.</p></div>
<div class="card reveal d1"><span class="num">V</span><h3>Aftercare that lasts</h3><p>Reviews, home plans and support that continue after the procedure.</p></div>
<div class="card reveal d2"><span class="num">VI</span><h3>Your decision</h3><p>Information and options, never pressure.</p></div></div></div></section>'''
    return page('services.html', 'Services | Burns, Hair, Skin & Weight Loss | Dr. Wanjiru MD',
                'Burn care, scar and keloid treatment, hair loss and transplants, skin of colour care, non-surgical aesthetics and GLP-1 weight loss in Upper Hill, Nairobi.',
                body + cta('Not sure where to start?', 'Book a consultation and we will map your plan together.'), [('Services', None)], 'CollectionPage', '0.9')

# ============================================================== BURNS
def burns():
    h = hero_inner([('Services', 'services.html'), ('Burns', None)], 'Burn care &amp; recovery', 'The burn <em>nobody</em> talks about.',
                   'Most burns happen at home, to ordinary people, in a second. The injury is quick. The recovery is long, and the second half is almost never explained.',
                   'burns-hero', 'Burn recovery and scar care by a plastic surgeon in Nairobi')
    glance = f'<section class="section" style="padding-bottom:0"><div class="container">{facts([("20 min","cool running water as first aid"),("48–72 h","for a burn to show its true depth"),("12–24 mo","for a burn scar to mature"),("Day 1","is when scar prevention begins")])}</div></section>'

    depth_items = [
        ('d1', 'Superficial', dl([('Layer', 'Epidermis only'), ('Looks like', 'Red, dry, no blisters. Typical of sunburn.'), ('Feels', 'Painful, tender'), ('Heals in', '3 to 7 days'), ('Scar risk', 'Very low; temporary colour change possible'), ('Care', 'Cool, moisturise, protect from sun'), ])),
        ('d2a', 'Superficial partial', dl([('Layer', 'Epidermis and upper dermis'), ('Looks like', 'Blisters, moist, pink or red, blanches when pressed'), ('Feels', 'Very painful, sensitive to air'), ('Heals in', '1 to 3 weeks'), ('Scar risk', 'Low to moderate; pigment change is common on darker skin'), ('Care', 'Dressings, infection watch, sun protection for months')])),
        ('d2b', 'Deep partial', dl([('Layer', 'Deep dermis'), ('Looks like', 'Mottled red and white, drier, may not blanch'), ('Feels', 'Pressure, less sharp pain'), ('Heals in', 'More than 3 weeks if it heals on its own'), ('Scar risk', 'High: thick, raised or tight scars'), ('Care', 'Often surgical: removal of dead tissue and skin grafting')])),
        ('d3', 'Full thickness', dl([('Layer', 'Through the whole dermis, sometimes deeper'), ('Looks like', 'White, brown, charred or leathery'), ('Feels', 'Little or no pain in the centre (nerves destroyed)'), ('Heals in', 'Cannot heal fully without surgery'), ('Scar risk', 'Very high: contractures and functional loss'), ('Care', 'Hospital, surgery, rehabilitation, long-term scar care')]))]
    depth = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Interactive</span><h2>How deep is the burn?</h2>
<p class="lead">Depth, not size alone, decides how a burn heals and whether it will scar. Select a depth to see it in the skin.</p></div>
<div class="mt2 split top reveal" data-tabs><div>{skin_diagram()}</div><div>{tabs(depth_items, "Burn depth")}</div></div>
{callout("Important", "Only a clinician can judge burn depth. Burns often look shallower on day one and deepen over 48 to 72 hours. If in doubt, get it seen.")}</div></section>'''

    firstaid = f'''<section class="section section--alt"><div class="container split top"><div class="reveal"><span class="eyebrow">First aid</span><h2>The first twenty minutes.</h2>
<p class="lead">First aid changes the outcome more than almost any treatment that follows.</p>
<ol class="steps"><li><h3>Stop the burning</h3><p>Remove the person from the source. Put out flames by stop, drop and roll, or smother with a thick blanket. Switch off electricity before touching anyone.</p></li>
<li><h3>Cool for 20 minutes</h3><p>Cool, running tap water, not ice or iced water. Start as soon as possible; it still helps up to about three hours after the injury.</p></li>
<li><h3>Take off rings, watches, tight clothing</h3><p>Before swelling starts. Do not pull off anything stuck to the skin.</p></li>
<li><h3>Cover loosely</h3><p>Clean cling film laid lengthwise, or a clean non-fluffy cloth. Keep the person warm, especially children.</p></li>
<li><h3>Get help</h3><p>Use the list on the right to decide how urgently. Pain relief such as paracetamol is reasonable while you travel.</p></li></ol></div>
<div class="reveal d1">{callout("Never apply", "Butter, cooking oil, toothpaste, ash, raw egg, herbal pastes, or ice. They trap heat, add infection risk, and make the wound harder to assess.", True)}
<h3 class="mt">Go to hospital now if the burn is:</h3><ul class="checks"><li>Larger than the person’s palm (adult) or any size in a young child</li><li>On the face, hands, feet, genitals, or over a joint</li><li>Deep: white, brown, leathery, or blistering widely</li><li>Electrical (even if it looks small), chemical, or from a fire in an enclosed space</li><li>All the way around a limb, finger or toe</li><li>In a baby, a child, an older adult, or someone with diabetes or low immunity</li></ul>
<div class="callout reveal"><b>Chemical burns</b><p>Brush off dry powder first, then flush with large amounts of running water for at least 20 minutes. Remove contaminated clothing. This includes caustic soda, acids, hair relaxers and some skin-lightening products.</p></div></div></div></section>'''

    causes = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Where burns happen</span><h2>Common causes in Kenyan homes.</h2>
<p class="lead">Most serious burns are preventable, and most happen in the kitchen.</p></div><div class="grid g3 mt2">
{"".join(f'<div class="card reveal d{i%3}"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Hot liquids","Tea, uji, porridge, soup and boiling water cause most toddler scalds. A child can be scalded in under a second."),("Paraffin &amp; jiko","Kerosene stoves and lamps, charcoal jikos and gas cooking cause flame and flash burns, especially with loose clothing."),("Cooking oil","Oil burns hotter than boiling water and sticks to the skin. Never use water on an oil fire."),("Electrical","Faulty wiring, illegal connections and water heaters. Internal injury can be much worse than the skin suggests."),("Chemicals","Caustic soda, acids, hair relaxers and unregulated skin-lightening creams cause deep, slowly worsening burns."),("Hot surfaces","Irons, hair straighteners, and motorbike exhaust pipes, a common cause of burns on children’s legs.")]))}</div></div></section>'''

    aftermath = f'''<section class="section section--dark"><div class="container split"><div class="reveal"><span class="eyebrow">After the wound closes</span><h2>The part <em>nobody</em> explains.</h2>
<p class="lead">Closed skin is not finished skin. It is the beginning of scar maturation.</p>
<p>For 12 to 24 months a burn scar is biologically active: it can thicken, tighten, itch, darken or pale. Burned skin has lost its natural defences against sunlight, sweating and stretch. And for many survivors, the hardest part is how it feels to be seen.</p>
<ul class="checks"><li>Protect healed burns from the sun for at least a year</li><li>Moisturise and massage as taught: it softens and desensitises</li><li>Wear pressure garments if prescribed, usually most of the day</li><li>Keep moving: stretching prevents tight scars from limiting joints</li><li>Ask for help with itch, pain, sleep and mood. They are part of healing</li></ul></div>
<div class="reveal d1">{img("burns-detail", "Burn scar maturation and recovery in Black skin", "r169")}<div class="mt">{timeline([("Day 0–3","Stabilise","Cooling, assessment, pain control, tetanus status, and a decision on where to treat."),("Week 1–3","Wound healing","Dressings and infection watch. Deeper burns may need grafting. Movement starts early."),("Month 1–3","Scar shaping begins","Silicone, massage and pressure therapy. The best window to prevent thick scars."),("Month 3–12","Active scar treatment","Injections, laser, needling and release of tight bands, timed to the scar."),("Year 1–2","Refine","Revision, fat grafting and contour work once the scar has settled.")])}</div></div></div></section>'''

    scartypes = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Know your scar</span><h2>Five kinds of scar, five different plans.</h2></div><div class="mt2">
{table(["Type","Looks like","Boundary","Typical course","Approach"],[
("Normal / maturing","Flat or slightly raised, pink to dark","Stays within the wound","Softens and fades over 1–2 years","Silicone, massage, sun protection"),
("Hypertrophic","Raised, red or dark, firm, itchy","Stays within the wound","Often settles over 1–2 years","Silicone, pressure, injections, laser"),
("Keloid","Raised, rubbery, grows beyond the wound","Spreads past the original edges","Rarely settles on its own","Combination therapy; cutting alone often fails"),
("Contracture","Tight, pulls skin, limits movement","Across joints and folds","Tightens as it matures","Therapy, release, grafts or flaps"),
("Atrophic","Sunken or pitted","Within the wound","Stable","Needling, filler, resurfacing")])}</div>
<p class="center mt reveal"><a class="link-arrow" href="scars.html">Scars and keloids in depth</a></p></div></section>'''

    ladder = f'''<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">Treatment ladder</span><h2>From gentle to definitive.</h2>
<p class="lead">We climb only as high as your scar and your goals require.</p></div>
<div class="grid g4 mt2">{"".join(f'<div class="card reveal d{i%4}"><span class="num">{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Foundation","Silicone sheets or gel, massage, moisturising, strict sun protection, pressure garments where needed."),("Injections","Steroid injections to flatten thick scars, sometimes with 5-fluorouracil. Botulinum toxin can reduce tension in selected scars."),("Energy &amp; needling","Vascular laser for redness and itch, carefully chosen fractional lasers for texture, and microneedling or radiofrequency needling."),("Surgery","Scar release (Z-plasty), skin grafts, flaps, tissue expansion and fat grafting, timed once the scar has matured.")]))}</div></div></section>'''

    myth = f'''<section class="section"><div class="container"><span class="eyebrow reveal">Seven things people are rarely told</span><h2 class="reveal" style="max-width:20ch">Myths, and what is actually true.</h2><div class="mt">{myths([
("“Once it has closed, it is healed.”","Closed skin is the start of scar maturation, which can take 12 to 24 months. What you do in those months shapes the final result."),
("“Dark skin scars badly, so nothing can be done.”","Melanin-rich skin has a higher tendency to keloid, thick scars and pigment change. That is a reason for earlier, smarter care, not for giving up."),
("“A scar that does not hurt is not a problem.”","A tight scar over a joint can quietly limit movement for years. Contractures often begin painlessly."),
("“Lasers are unsafe on Black skin.”","The wrong device, wrong settings or wrong provider is unsafe. The right wavelength, conservative energy and a test patch can be done safely."),
("“Burn scars are only a physical injury.”","Many survivors carry months of pain, itch, disturbed sleep and anxiety about being seen. Good burn care includes the person, not only the scar."),
("“Surgery is the only real fix.”","Many scars improve with layered non-surgical care: silicone, pressure, injections, lasers and needling, with surgery reserved for what remains."),
("“It is too late.”","Old scars, even childhood ones, can still be softened, released and re-contoured. Timing affects the approach, not whether help is possible.")])}</div></div></section>'''

    prevent = f'''<section class="section section--alt"><div class="container split top"><div class="reveal"><span class="eyebrow">Prevention</span><h2>Make the kitchen safer.</h2>
<ul class="checks"><li>Keep kettles, sufurias and hot drinks away from table edges. Never hold a child while drinking something hot</li><li>Cook on back burners and turn pot handles inward</li><li>Store paraffin in labelled, closed containers away from children and from heat</li><li>Set water heaters to 49°C (120°F) or below; test bath water with your elbow</li><li>Cap unused sockets and replace damaged cables. Never improvise connections</li><li>Store caustic soda, acids and relaxers locked away, in original containers</li><li>Teach children: stop, drop and roll; cool a burn under running water</li></ul></div>
<div class="reveal d1"><h3>Children and burns</h3><p>Children’s skin is thinner, so the same exposure burns deeper. Scalds are the most common cause under five. Because children grow, scars can tighten as they do, which is why they need follow-up well beyond healing.</p><p>Treatment is planned with parents, around school and growth, aiming for the fewest procedures and the most normal childhood possible.</p>
<a class="btn mt" href="burn-first-aid.html">Read: burn first aid guide</a></div></div></section>'''

    faqs = faq([
        ('When should I first see a burn specialist?', 'As early as possible for anything deep, large or on a critical area. For healed burns, ideally within the first few months, while scars are still forming and easiest to shape.'),
        ('Will my burn scar disappear?', 'Scars are never erased, but most can be made flatter, softer, less visible and more comfortable. Your plan will state honestly what is realistic.'),
        ('Are scar treatments safe on dark skin?', 'Yes, when chosen and set carefully. Conservative energy settings, test patches and treatment sequencing protect pigment and reduce the risk of keloid or dark marks.'),
        ('Can children be treated for burn scars?', 'Yes. Care is planned with parents and around growth. Early silicone, massage, sun protection and monitoring prevent many problems.'),
        ('How long does a scar plan take?', 'Often 6 to 18 months, in stages. You will see the full roadmap at your first visit.'),
        ('Do you treat old burn scars from childhood?', 'Yes. Old scars can often be released, softened and re-contoured. Timing affects the approach, not whether help is possible.'),
        ('Should I put honey, oil or toothpaste on a burn?', 'No. Cool the burn under running water for 20 minutes, then cover it loosely with clean cling film or a clean cloth, and get it assessed.'),
        ('Can I get burn care and aesthetic treatment in the same clinic?', 'Yes. The same careful planning applies to both, and many patients combine scar care with skin or hair treatment.')], 'burns')
    f = f'<section class="section"><div class="container narrow"><div class="center reveal"><span class="eyebrow">Questions</span><h2>Burn care FAQ.</h2></div><div class="mt2">{faqs}</div></div></section>'
    rel = related([('scars.html', 'Scars &amp; keloids', 'Every scar type, and the combination plans that work.'), ('hair-restoration.html', 'Hair restoration', 'Including transplants into scarred scalp.'), ('burn-first-aid.html', 'Burn first aid guide', 'The full 20-minute guide to read and share.')])
    return page('burns.html', 'Burn Care & Burn Scar Treatment in Nairobi | Dr. Wanjiru MD',
                'Burn first aid, scar prevention and revision, contracture release and long-term recovery for Black skin. Plastic surgeon in Upper Hill, Nairobi.',
                h + glance + depth + firstaid + causes + aftermath + scartypes + ladder + myth + prevent + f + rel + cta('It is not too late to feel at home in your skin.', 'Old burn or new, there is a plan.', 'Book a scar consultation'),
                [('Services', 'services.html'), ('Burns', None)], 'MedicalWebPage', '1.0')

# ============================================================== SCARS
def scars():
    h = hero_inner([('Services', 'services.html'), ('Scars &amp; keloids', None)], 'Scars &amp; keloids', 'Scars are <em>not</em> a life sentence.',
                   'Raised, tight, dark, pitted or itchy: scars in Black skin behave differently. Treating them well starts with knowing exactly which kind you have.',
                   'scars-hero', 'Scar and keloid treatment for Black skin in Nairobi')
    sel = [('hyper', 'Hypertrophic', dl([('What it is', 'An overgrowth of scar tissue that stays inside the original wound.'), ('Typical triggers', 'Burns, wounds that took long to heal, tension across joints'), ('Course', 'Often improves over 1 to 2 years'), ('Treatment', 'Silicone, pressure, steroid injections, laser, sometimes surgery')])),
           ('keloid', 'Keloid', dl([('What it is', 'A scar that keeps growing beyond the original wound edges.'), ('Typical triggers', 'Ear piercings, acne on the chest and jaw, surgery, minor cuts. Runs in families.'), ('Course', 'Rarely settles on its own; can recur after removal'), ('Treatment', 'Combination therapy. Cutting alone often leads to a bigger scar.')])),
           ('acne', 'Acne scars', dl([('Types', 'Icepick (narrow, deep), boxcar (wide, sharp edges), rolling (wavy)'), ('Also common', 'Dark marks (PIH) that are not true scars and fade with the right care'), ('Treatment', 'Subcision, microneedling, TCA CROSS, fillers, carefully chosen lasers'), ('Key point', 'Treat active acne first, or new scars keep forming')])),
           ('surgical', 'Surgical &amp; C-section', dl([('Goal', 'A thin, flat, well-camouflaged line'), ('Prevention', 'Silicone and sun protection from the moment stitches are out, for 6 to 12 months'), ('If it thickens', 'Steroid injections, laser, revision after maturation'), ('Tip', 'Tell your surgeon in advance that you scar thickly')])),
           ('stretch', 'Stretch marks', dl([('What they are', 'Tears in the deeper skin layer from rapid stretching: pregnancy, growth, weight change'), ('Early (red/purple)', 'Respond best to treatment'), ('Old (pale/silver)', 'Improve in texture with needling and energy devices, rarely vanish'), ('Honesty', 'Improvement, not erasure')]))]
    types = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Interactive</span><h2>What kind of scar is it?</h2></div><div class="mt2 reveal" data-tabs>{tabs(sel, "Scar type")}</div></div></section>'''

    keloid = f'''<section class="section section--dark"><div class="container split"><div class="reveal"><span class="eyebrow">Keloids</span><h2>Why cutting alone <em>often fails.</em></h2>
<p class="lead">A keloid is a healing response that never switches off. Surgery is another injury, and the body can answer it with an even bigger keloid.</p>
<p>Keloids are more common in people of African, Asian and Hispanic descent, often appear after piercings, and tend to run in families. Removing one without a plan to quiet the healing response leads to high recurrence rates.</p>
<ul class="checks"><li>Combination plans: injections, silicone, pressure and, where appropriate, carefully timed surgery</li><li>Adjuvant options in selected cases to lower recurrence</li><li>Honest discussion of recurrence risk before any procedure</li><li>Prevention advice: before piercing, tattooing or elective surgery, tell your clinician you are keloid-prone</li></ul>
<a class="link-arrow" href="keloids-explained.html">Read: keloids explained</a></div>
<div class="reveal d1">{ba("keloid-1","Keloid scar","Combination plan · 8 months")}</div></div></section>'''

    approach = f'''<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Treatments</span><h2>The toolkit.</h2></div><div class="grid g3 mt2">
{"".join(f'<div class="card reveal d{i%3}"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([("Silicone &amp; pressure","The foundation for most raised scars. Cheap, safe and effective when used consistently."),("Steroid injections","Injected into thick scars every 4 to 6 weeks to flatten and soften. Dosing is cautious to avoid thinning or pale marks."),("Microneedling &amp; RF","Remodels texture, with energy delivered below the surface, which suits darker skin."),("Selected lasers","Vascular laser for redness and itch; fractional lasers for texture, with conservative settings and test patches."),("Subcision &amp; fillers","Releases tethered rolling acne scars and lifts depressions."),("Surgical revision","Excision, Z-plasty, grafts or flaps for scars that limit movement or remain disfiguring after maturation.")]))}</div></div></section>'''

    faqs = faq([
        ('Is a keloid cancerous or dangerous?', 'No. Keloids are benign overgrowths of scar tissue. They can be itchy, tender and distressing, and are worth treating properly.'),
        ('Can a keloid be removed permanently?', 'Many keloids can be flattened and kept under control, but recurrence is a real risk. The aim is a long-term plan, not a one-off cut.'),
        ('Can I get my ears pierced if I am keloid-prone?', 'It is a risk. Discuss it first. If you do pierce, choose a clean, experienced piercer, avoid piercing the cartilage, and seek early treatment if a bump forms.'),
        ('How long before scar treatments work?', 'Most plans need a series over several months. Early scars respond faster than old, mature ones.'),
        ('Do dark marks after acne count as scars?', 'Usually not. Post-inflammatory hyperpigmentation is a colour change that fades with sun protection and the right medical care, often over months.')], 'scars')
    f = f'<section class="section section--alt"><div class="container narrow"><div class="center reveal"><span class="eyebrow">Questions</span><h2>Scar FAQ.</h2></div><div class="mt2">{faqs}</div></div></section>'
    rel = related([('burns.html', 'Burn care', 'Scars that start with a burn.'), ('skin.html', 'Skin of colour', 'Pigmentation and acne.'), ('keloids-explained.html', 'Keloids explained', 'The full guide.')])
    return page('scars.html', 'Keloid & Scar Treatment in Nairobi | Dr. Wanjiru MD',
                'Keloid, hypertrophic, acne, surgical and burn scar treatment for Black skin in Upper Hill, Nairobi. Combination plans that lower recurrence.',
                h + types + keloid + approach + f + rel + cta('Tell us about your scar.', 'A short consultation is the fastest way to know what is possible.'),
                [('Services', 'services.html'), ('Scars &amp; keloids', None)], 'MedicalWebPage', '0.9')
