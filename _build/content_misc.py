from lib import *
from data import ARTICLES

def article(slug, sections, rel):
    t, d, mins = next((a[1], a[2], a[3]) for a in ARTICLES if a[0] == slug)
    toc = '<nav class="toc" aria-label="In this article"><b>In this article</b>' + ''.join(f'<a href="#{i}">{h}</a>' for i, h, _ in sections) + '</nav>'
    body = ''.join(f'<h2 id="{i}">{h}</h2>{b}' for i, h, b in sections)
    hero = (f'<section class="page-hero"><div class="container narrow" style="margin:0 auto"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span><a href="journal.html">Journal</a></span><span aria-current="page">Article</span></nav>'
            f'<span class="eyebrow">Journal · {mins} min read</span><h1 style="font-size:clamp(2.4rem,5vw,4.2rem);max-width:20ch">{t}</h1><p class="lead">{d}</p></div></section>')
    main = (f'<section class="section"><div class="container article-grid">{toc}<article class="prose">{img("article-"+slug, t, "r169", "reveal")}'
            f'<div class="byline"><span class="av">W</span><span><b>Dr. Wanjiru MD</b><br>Plastic &amp; reconstructive surgeon, Upper Hill, Nairobi · Updated 6 Nov 2026</span></div>{body}'
            f'{callout("A note", "This article is for general education and is not a substitute for medical advice. See a doctor about your own situation.")}</article></div></section>')
    return page(f'{slug}.html', f'{t} | Dr. Wanjiru MD'[:70], d, hero + main + related(rel) + cta('Questions about your own case?', 'A consultation turns general advice into a plan for you.'),
                [('Journal', 'journal.html'), (t, None)], article=True, priority='0.6')

def articles():
    out = []
    out.append(article('burn-first-aid', [
        ('why', 'Why the first 20 minutes matter', '<p>How a burn is treated in the first minutes affects how deep it becomes, how much it hurts, and how it scars. Cooling stops the heat from continuing to damage deeper layers of skin.</p>'),
        ('steps', 'What to do, step by step', '<ol><li><b>Stop the burning.</b> Remove the person from the source. Put out flames by stop, drop and roll, or smother with a thick blanket. Switch off electricity before you touch someone.</li><li><b>Cool the burn</b> under cool running water for 20 minutes. It still helps up to about three hours after the injury. Do not use ice or iced water.</li><li><b>Remove</b> rings, watches and tight clothing near the burn before it swells. Leave anything that is stuck to the skin.</li><li><b>Cover</b> loosely with clean cling film (laid, not wrapped tightly) or a clean non-fluffy cloth.</li><li><b>Keep warm.</b> Burns can cause rapid heat loss, especially in children.</li><li><b>Get help</b> using the guide below.</li></ol>'),
        ('avoid', 'What not to do', '<p>Do not apply butter, cooking oil, toothpaste, ash, raw egg, herbal pastes or ice. They trap heat, increase the risk of infection, and make it harder for doctors to see the burn. Do not burst blisters.</p>'),
        ('when', 'When to go to hospital', '<ul><li>Burn larger than the person’s palm, or any burn in a baby or young child</li><li>Burns on the face, hands, feet, genitals or over a joint</li><li>White, brown, leathery or widely blistered skin</li><li>Electrical and chemical burns, or burns from fires in enclosed spaces</li><li>Burns that go all the way around a limb, finger or toe</li><li>Burns in older adults or people with diabetes or low immunity</li></ul>'),
        ('special', 'Special situations', '<h3>Chemical burns</h3><p>Brush off dry powder first, then flush with large amounts of running water for at least 20 minutes and remove contaminated clothing. This applies to caustic soda, acids, hair relaxers and some skin-lightening products.</p><h3>Cooking oil and hot liquids</h3><p>Remove soaked clothing quickly (cut it away if needed), then cool as above. Never use water on an oil fire; smother it.</p><h3>Electrical burns</h3><p>Even a small mark can hide deep injury. Always go to hospital.</p>'),
        ('after', 'After the first aid', '<p>Once the wound closes, scar prevention begins: sun protection, silicone, massage and, if needed, pressure garments. Early review by a burn or plastic surgeon makes a real difference to the final result.</p><p><a href="burns.html">Read the full burn care guide</a> or <a href="contact.html">book a scar consultation</a>.</p>')],
        [('burns.html', 'Burn care', 'Depth, treatment and recovery.'), ('scars.html', 'Scars &amp; keloids', 'What happens after healing.'), ('journal.html', 'More articles', 'The full journal.')]))
    out.append(article('traction-alopecia', [
        ('what', 'What is traction alopecia?', '<p>Traction alopecia is hair loss caused by long-term pulling on the hair roots. It is common along the hairline and temples in people who wear tight braids, weaves, extensions, wigs, ponytails or buns, and it is one of the most preventable causes of hair loss.</p>'),
        ('signs', 'Early warning signs', '<ul><li>Tenderness, soreness or headaches after styling</li><li>Small bumps or pimples along the hairline</li><li>Broken, thin hair at the edges</li><li>A thin line of hairs left along the very front of the hairline</li><li>A hairline that has slowly moved back</li></ul>'),
        ('why', 'Why does it happen?', '<p>Constant tension inflames and weakens the follicle. At first the damage is reversible. If tension continues for years, follicles can scar and stop producing hair for good.</p>'),
        ('prevent', 'How to protect your hairline', '<ul><li>If it hurts, take it down. Pain means too tight</li><li>Ask for lighter, smaller extension weights and looser installs</li><li>Keep installs to about 6 to 8 weeks, and give your scalp breaks</li><li>Avoid glue on the hairline and tight edges</li><li>Vary parting and ponytail positions</li><li>Moisturise and gently clean your scalp</li></ul>'),
        ('treat', 'Can hair grow back?', '<p>If caught early and the tension stops, often yes, over several months. Treatment may include calming inflammation, minoxidil and PRP. When follicles are scarred, a carefully planned transplant can restore the hairline.</p><p>Not sure whether it is traction alopecia or something else such as CCCA? The treatments differ, so a scalp examination is worth it. <a href="hair.html">Visit the hair loss clinic page</a>.</p>')],
        [('hair.html', 'Hair loss clinic', 'Find your pattern.'), ('hair-restoration.html', 'Hair restoration', 'When regrowth is not possible.'), ('glp1-hair-skin.html', 'Weight loss and hair', 'Another cause of shedding.')]))
    out.append(article('glp1-hair-skin', [
        ('what', 'What GLP-1 medicines do', '<p>Medicines such as semaglutide and tirzepatide reduce appetite and affect blood-sugar signalling, helping many people lose significant weight when combined with nutrition and movement. They are prescription medicines and need a medical assessment first.</p>'),
        ('hair', 'Why hair can shed', '<p>Rapid weight loss, like any physical stress, can push more hairs into the resting phase. Shedding appears about two to four months later and is called telogen effluvium. It is usually temporary, and low iron, protein or other nutrients can make it worse.</p><ul><li>Eat enough protein and a variety of foods</li><li>Ask about checking iron, vitamin D, B12 and thyroid</li><li>Aim for a steady, not extreme, pace</li></ul>'),
        ('muscle', 'Protecting muscle', '<p>A meaningful share of weight lost can be lean mass, including muscle. Strength training two to three times a week and adequate protein help protect muscle and metabolism. Your doctor will set targets for you.</p>'),
        ('skin', 'Skin and face changes', '<p>Faster loss means less time for skin to adapt, and the face can look more hollow. Hydration, a steady pace and sun protection help. Later, tightening or conservative volume restoration can be considered.</p>'),
        ('safe', 'Staying safe', '<ul><li>Use only prescribed, properly sourced medicine. Falsified pens have been reported</li><li>Report severe or persistent abdominal pain, vomiting or dehydration</li><li>Do not use if pregnant or planning pregnancy</li><li>Plan for maintenance. Many people regain weight after stopping without a plan</li></ul>'),
        ('next', 'Next step', '<p>A consultation covers whether a GLP-1 is suitable, the right pace, and how to protect hair, muscle and skin. <a href="weight-loss.html">See the weight loss programme</a>.</p>')],
        [('weight-loss.html', 'Weight loss', 'The supervised programme.'), ('hair.html', 'Hair loss clinic', 'Shedding and thinning.'), ('skin.html', 'Skin of colour', 'Skin changes after weight loss.')]))
    out.append(article('sunscreen-black-skin', [
        ('myth', 'The myth', '<p>“Black skin does not burn, so it does not need sunscreen” is one of the most repeated skincare myths. Melanin does protect, but only partially: it provides roughly the equivalent of an SPF of 13, and it does not prevent pigmentation, melasma or skin cancer.</p>'),
        ('why', 'Why it matters for dark skin', '<ul><li>Sun worsens dark marks, so acne and razor-bump marks last longer</li><li>It triggers and worsens melasma</li><li>Healed burns and scars are especially sensitive and can darken</li><li>Skin cancers, though less common, are often found later in people with darker skin</li></ul>'),
        ('choose', 'How to choose one', '<ul><li>Broad-spectrum SPF 30 or higher</li><li>Look for “no white cast”, or a lightly tinted formula. Iron oxides also help against visible light and melasma</li><li>Choose a texture you will actually use: gel, fluid or lotion</li><li>Apply a generous amount to face and neck, and reapply every two hours in strong sun</li></ul>'),
        ('hacks', 'What to skip', '<p>Do not rely on foundation with SPF alone, and do not use lemon, baking soda or toothpaste to “lighten” marks. They irritate skin and often make marks darker.</p>'),
        ('next', 'Next step', '<p>If you have stubborn marks, melasma or scars, a consultation can build a full plan. <a href="skin.html">Read about skin of colour care</a>.</p>')],
        [('skin.html', 'Skin of colour', 'Pigmentation and acne.'), ('scars.html', 'Scars &amp; keloids', 'Protecting scars from sun.'), ('aesthetics.html', 'Aesthetics', 'Peels and microneedling.')]))
    out.append(article('keloids-explained', [
        ('what', 'What is a keloid?', '<p>A keloid is a scar that keeps growing beyond the edges of the original wound. It is raised, firm and rubbery, and may be itchy or tender. It is benign, but can be distressing.</p>'),
        ('vs', 'Keloid or hypertrophic scar?', '<p>A hypertrophic scar is also raised, but stays within the wound and often settles over a year or two. A keloid spreads beyond the original wound and rarely settles on its own. The difference changes the treatment.</p>'),
        ('who', 'Who is at risk?', '<p>Keloids are more common in people of African, Asian and Hispanic descent, often run in families, and favour the earlobes, chest, shoulders and jawline. Ear piercings, acne, surgery and minor skin injuries can trigger them.</p>'),
        ('fail', 'Why cutting alone often fails', '<p>Surgery is a new injury. In keloid-prone skin it can trigger an even larger scar, so removal without a plan has a high rate of recurrence. Better results come from combination treatment: injections, silicone, pressure and, where appropriate, carefully timed surgery with adjuvant therapy.</p>'),
        ('prevent', 'Prevention', '<ul><li>Tell clinicians, piercers and tattoo artists that you are keloid-prone</li><li>Treat acne early, especially on the chest and back</li><li>Use silicone and sun protection on any new scar</li><li>Seek early treatment if a scar starts to thicken</li></ul>'),
        ('next', 'Next step', '<p>Learn more on the <a href="scars.html">scars and keloids page</a>, or <a href="contact.html">book a scar consultation</a>.</p>')],
        [('scars.html', 'Scars &amp; keloids', 'The full toolkit.'), ('burns.html', 'Burn care', 'Burn scars and contractures.'), ('skin.html', 'Skin of colour', 'Acne and pigmentation.')]))
    return out

def journal():
    cards = ''.join(post_card(s, t, d, m, i) for i, (s, t, d, m) in enumerate(ARTICLES))
    body = (f'<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-current="page">Journal</span></nav>'
            f'<span class="eyebrow reveal">Journal</span><h1 class="reveal d1">Straight talk, in <em>plain language.</em></h1><p class="lead reveal d2">Clear, evidence-based guides on burns, scars, hair, skin and weight, written for Black and melanin-rich skin.</p></div></section>'
            f'<section class="section"><div class="container"><div class="grid g3">{cards}</div></div></section>')
    return page('journal.html', 'Journal: Burns, Hair, Skin & Weight Guides | Dr. Wanjiru MD', 'Plain-language guides on burn first aid, traction alopecia, keloids, sunscreen for Black skin and GLP-1 weight loss, from a Nairobi plastic surgeon.',
                body + cta('Have a question we have not answered?', 'Ask at your consultation, and it may become the next article.'), [('Journal', None)], 'CollectionPage', '0.8')

def faq_page():
    sets = [
        ('burns', 'Burns', [('What should I do first for a burn?', 'Cool it under running water for 20 minutes, remove rings and tight clothing, cover loosely with clean cling film or a clean cloth, and get medical help if it is large, deep, on the face, hands, feet, genitals or joints, or caused by chemicals or electricity.'),
                            ('Can burn scars be improved years later?', 'Yes. Old burn scars can often be softened, released and re-contoured. Timing affects the approach, not whether help is possible.'),
                            ('Will I need skin grafts?', 'Deep partial-thickness and full-thickness burns often do. Superficial burns heal without them.')]),
        ('scars', 'Scars', [('What is the difference between a keloid and a hypertrophic scar?', 'Hypertrophic scars stay within the wound and often settle over time. Keloids grow beyond the wound and rarely settle without treatment.'),
                            ('Is keloid treatment guaranteed?', 'No treatment can guarantee permanent flattening, but combination plans reduce recurrence and improve comfort and appearance.')]),
        ('hair', 'Hair', [('Can traction alopecia be reversed?', 'Early, often yes. Once follicles are scarred, regrowth is not possible and restoration may be considered.'),
                          ('Is a hair transplant suitable for Afro-textured hair?', 'Yes, with specialised technique and planning for curved follicles and scar risk.')]),
        ('skin', 'Skin', [('Do I need sunscreen with dark skin?', 'Yes. It prevents dark marks from worsening, helps melasma and protects scars.'),
                          ('Are chemical peels safe on dark skin?', 'Superficial peels with proper skin preparation and conservative strength can be safe. Strong peels carry a higher risk of dark or pale marks.')]),
        ('aesthetics', 'Aesthetics', [('How long do Botox and fillers last?', 'Botulinum toxin usually lasts about three to four months. Fillers last from several months to over a year, depending on product and area.'),
                                      ('Is there downtime?', 'Usually minimal. Fillers can cause swelling or bruising for a few days.')]),
        ('weight', 'Weight loss', [('Who can take GLP-1 medicines?', 'Adults who meet medical criteria after assessment. They are prescription-only, and some conditions rule them out.'),
                                   ('Will I lose muscle or hair?', 'Some muscle is usually lost with weight loss, and hair shedding can occur. Protein, strength training and nutrient checks reduce both.')]),
        ('clinic', 'The clinic', [('Where is the clinic?', 'Upper Hill, Nairobi. See the contact page for the building, floor and directions.'),
                                  ('Do I need a referral?', 'No referral is needed to book a consultation.'),
                                  ('How much does treatment cost?', 'Costs depend on the plan. You receive a clear written quote after your consultation.')])]
    chips = '<button class="chip" data-cat="all" aria-pressed="true">All</button>' + ''.join(f'<button class="chip" data-cat="{c}" aria-pressed="false">{l}</button>' for c, l, _ in sets)
    blocks = ''.join(faq(items, c) for c, _, items in sets).replace('</div><div class="faq reveal">', '')
    body = (f'<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-current="page">FAQ</span></nav><span class="eyebrow reveal">FAQ</span>'
            f'<h1 class="reveal d1">Your questions, <em>answered.</em></h1><p class="lead reveal d2">Search or filter by topic. Anything we have missed, ask at your consultation.</p></div></section>'
            f'<section class="section"><div class="container narrow"><input id="faq-search" class="faq-search" type="search" placeholder="Search questions" aria-label="Search questions"><div class="chips">{chips}</div>{blocks}</div></section>')
    return page('faq.html', 'FAQ: Burns, Scars, Hair, Skin & Weight Loss | Dr. Wanjiru MD', 'Answers on burn first aid, keloids, traction alopecia, hair transplants, sunscreen, Botox, fillers and GLP-1 weight loss, from a Nairobi plastic surgeon.',
                body + cta('Still have a question?', '', 'Contact the clinic'), [('FAQ', None)], 'WebPage', '0.7')

def about():
    body = (f'''<section class="page-hero"><div class="container page-hero-grid"><div><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-current="page">About</span></nav><span class="eyebrow reveal">About</span>
<h1 class="reveal d1">Meet Dr. <em>Wanjiru.</em></h1><p class="lead reveal d2">Plastic and reconstructive surgeon. Burn care champion. Believer that skin, hair and confidence are medical matters worth taking seriously.</p></div>{img("about-portrait", "Portrait of Dr. Wanjiru MD, plastic and reconstructive surgeon in Nairobi", "r34", "arch reveal d2", True)}</div></section>
<section class="section"><div class="container split"><div class="reveal">{img("clinic-4", "Dr. Wanjiru's clinic in Upper Hill, Nairobi", "r169")}</div><div class="reveal d1"><span class="eyebrow">Her story</span><h2>[Why she chose burns]</h2>
<p>[Placeholder: Dr. Wanjiru to supply two or three paragraphs in her own words: why she chose plastic surgery, what moved her toward burn care, and what she wants every patient to feel when they leave the clinic.]</p>
<p>Her practice rests on three promises: honest timelines, gentle hands, and care designed for Black skin and hair.</p><div class="btn-row"><a class="btn btn--solid" href="contact.html">Book a consultation</a></div></div></div></section>
<section class="section section--alt"><div class="container"><div class="center reveal"><span class="eyebrow">Principles</span><h2>How she practises.</h2></div><div class="grid g3 mt2">
<div class="card reveal"><span class="num">I</span><h3>Diagnosis before treatment</h3><p>Every plan starts with understanding exactly what is going on.</p></div><div class="card reveal d1"><span class="num">II</span><h3>Skin of colour first</h3><p>Techniques chosen for melanin-rich skin and its healing patterns.</p></div><div class="card reveal d2"><span class="num">III</span><h3>Honest timelines</h3><p>You know what to expect, when, and what can go wrong.</p></div>
<div class="card reveal"><span class="num">IV</span><h3>Natural results</h3><p>Subtle changes that keep you looking like you.</p></div><div class="card reveal d1"><span class="num">V</span><h3>Whole-person care</h3><p>Healing includes comfort, confidence and mental wellbeing.</p></div><div class="card reveal d2"><span class="num">VI</span><h3>Aftercare that lasts</h3><p>Reviews and support long after the procedure.</p></div></div></div></section>
<section class="section"><div class="container"><div class="center reveal"><span class="eyebrow">Credentials</span><h2>Training &amp; membership.</h2></div><div class="grid g3 mt2"><div class="card reveal"><h3>Medical degree</h3><p>[University · Year]</p></div><div class="card reveal d1"><h3>Plastic &amp; reconstructive surgery</h3><p>[Training programme · Year]</p></div><div class="card reveal d2"><h3>Registration &amp; societies</h3><p>[KMPDC registration · memberships]</p></div></div><p class="small center mt">Placeholders. Publish verified credentials only.</p></div></section>
<section class="section section--dark"><div class="container"><p class="quote reveal">Healing is not only what happens to the skin. It is what happens to the person in it.<cite>Dr. Wanjiru</cite></p></div></section>''')
    return page('about.html', 'About Dr. Wanjiru MD | Plastic & Reconstructive Surgeon Nairobi', 'Meet Dr. Wanjiru MD, a plastic and reconstructive surgeon in Upper Hill, Nairobi, specialising in burn recovery, scars, hair, skin and weight care.',
                body, [('About', None)], 'AboutPage', '0.7')

def contact():
    body = (f'''<section class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-current="page">Contact</span></nav><span class="eyebrow reveal">Contact</span>
<h1 class="reveal d1">Let’s talk about <em>you.</em></h1><p class="lead reveal d2">Tell us what brings you in. The team will reply to confirm your consultation.</p></div></section>
<section class="section"><div class="container split top"><form class="contact reveal" novalidate>
<label>Full name<input type="text" name="name" autocomplete="name" required></label><label>Phone / WhatsApp<input type="tel" name="phone" autocomplete="tel" required></label>
<label>I’m interested in<select name="topic"><option>Burns &amp; scars</option><option>Hair loss &amp; restoration</option><option>Skin of colour</option><option>Non-surgical aesthetics</option><option>Weight loss</option><option>Not sure yet</option></select></label>
<label>Tell us a little<textarea name="msg" rows="5"></textarea></label><button class="btn btn--solid" type="submit">Request a consultation</button><p class="form-note" role="status"></p></form>
<div class="reveal d1"><span class="eyebrow">Visit</span><h3>Upper Hill, Nairobi</h3><p>[Building · Floor · Suite]<br>[Parking and access notes]</p><span class="eyebrow" style="margin-top:1.6rem">Hours</span><p>[Mon–Fri · hours]<br>[Saturday · hours]</p><span class="eyebrow" style="margin-top:1.6rem">Reach us</span><p>[+254 phone / WhatsApp]<br>[email]<br>[Instagram handle]</p>{img("contact-hero", "Dr. Wanjiru's clinic reception, Upper Hill, Nairobi", "r169", "mt")}</div></div></section>''')
    return page('contact.html', 'Book a Consultation | Dr. Wanjiru MD, Upper Hill Nairobi', 'Book a consultation with Dr. Wanjiru MD, plastic and reconstructive surgeon, in Upper Hill, Nairobi.', body, [('Contact', None)], 'ContactPage', '0.8')

def not_found():
    body = '<section class="hero"><div class="container center"><span class="eyebrow">404</span><h1>This page has <em>healed</em> and moved on.</h1><p class="lead">Try the home page or our services.</p><div class="btn-row" style="justify-content:center"><a class="btn btn--solid" href="index.html">Home</a><a class="btn" href="services.html">Services</a></div></div></section>'
    return page('404.html', 'Page not found | Dr. Wanjiru MD', 'Page not found.', body, [], noindex=True)
