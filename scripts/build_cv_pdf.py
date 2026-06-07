#!/usr/bin/env python3
"""
Generate a clean, public-safe CV PDF for Justin Simpson.

Source: his CV (CV.docx). Deliberately OMITTED for a public web download:
  - his personal cell phone number
  - the entire "References" section (referees' personal phone/emails)
Everything else is reproduced faithfully.

Output: public/cv.pdf
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether,
)

MOSS = colors.HexColor("#466b54")
INK = colors.HexColor("#232a22")
MUTED = colors.HexColor("#5c5a4c")

styles = getSampleStyleSheet()

name_style = ParagraphStyle("Name", parent=styles["Title"], fontName="Times-Bold",
                            fontSize=22, leading=24, textColor=INK, spaceAfter=2,
                            alignment=0)
sub_style = ParagraphStyle("Sub", fontName="Times-Roman", fontSize=11, leading=14,
                           textColor=MUTED, spaceAfter=1)
contact_style = ParagraphStyle("Contact", fontName="Times-Roman", fontSize=10,
                               leading=13, textColor=MOSS, spaceAfter=10)
section_style = ParagraphStyle("Section", fontName="Times-Bold", fontSize=12.5,
                               leading=15, textColor=MOSS, spaceBefore=12,
                               spaceAfter=2, tracking=1)
inst_style = ParagraphStyle("Inst", fontName="Times-Bold", fontSize=10.5, leading=13,
                            textColor=INK, spaceBefore=5, spaceAfter=1)
entry_style = ParagraphStyle("Entry", fontName="Times-Roman", fontSize=10, leading=13,
                             textColor=INK, spaceAfter=4, alignment=TA_JUSTIFY)
sub_entry = ParagraphStyle("SubEntry", parent=entry_style, fontSize=9.3, leading=12,
                           textColor=MUTED, leftIndent=14, spaceAfter=3, alignment=0)


def section(title):
    return [
        Paragraph(title.upper(), section_style),
        HRFlowable(width="100%", thickness=0.6, color=MOSS, spaceBefore=1, spaceAfter=5),
    ]


def e(text):
    return Paragraph(text, entry_style)


def s(text):
    return Paragraph(text, sub_entry)


def inst(text):
    return Paragraph(text, inst_style)


story = []

# ---- Header ----
story.append(Paragraph("Justin Simpson", name_style))
story.append(Paragraph("Lecturer II &middot; Department of Philosophy, "
                       "University of Texas Rio Grande Valley", sub_style))
story.append(Paragraph('<a href="mailto:justin.simpson@utrgv.edu">'
                       "justin.simpson@utrgv.edu</a>", contact_style))

# ---- Areas ----
story += section("Areas of Specialization")
story.append(e("Environmental Ethics, Social Epistemology, Material Feminisms / "
               "New Materialisms, Science and Technology Studies"))
story += section("Areas of Competence")
story.append(e("Ethics of Technology, Bioethics, Indigenous Philosophies, Ethics, "
               "Food Ethics, and Logic"))

# ---- Appointments ----
story += section("Academic Appointments")
story.append(e("University of Texas Rio Grande Valley (UTRGV), Lecturer, "
               "August 2022&ndash;present"))

# ---- Education ----
story += section("Education")
story.append(e("<b>Ph.D. Philosophy</b>, University of Georgia (UGA), May 2022"))
story.append(s("Dissertation: <i>Posthuman Performances in Environmental Ethics and "
               "Social Epistemology</i>. Committee: Chris Cuomo (chair), Piers Stephens, "
               "Sarah Wright, Ronald Bogue"))
story.append(e("<b>M.A. Philosophy</b>, University of North Florida (UNF), 2015"))
story.append(s("Thesis: <i>Quasi-Subjectivity and Ethics in Non-Modernity</i>. "
               "Committee: Erinn Gilson (chair), Bryan Bannon, Hans-Herbert Koegler"))
story.append(e("<b>B.S. Philosophy</b>, Magna Cum Laude, University of North Florida, 2012"))
story.append(e("<b>B.S. Physics and Mathematics</b>, Magna Cum Laude, "
               "University of North Florida, 2011"))

# ---- Publications ----
story += section("Book")
story.append(e("<i>Toward an Environmental Ethic of Surprise: Adventures in Attention</i>, "
               "December 2025"))

story += section("Chapters in Edited Collections")
story.append(e('&ldquo;A Tale of Two Rices: An Ethical Comparison of Golden Rice and '
               'Carolina Gold Rice Through a Performative New Materialist&rsquo;s Lens,&rdquo; '
               'in <i>Embodying Biodiversity: Sensory Conservation as Refuge and '
               'Sovereignty</i>, The University of Arizona Press, Spring 2024. '
               "ISBN: 9780816553983"))

story += section("Articles")
story.append(e('&ldquo;Moving Forward by Going Back: An Environmental Ethic of Flower and '
               'Song in Aztec Philosophy,&rdquo; <i>Public Philosophy Journal</i> 7(1). '
               '<a href="https://doi.org/10.59522/JVRR4931">doi.org/10.59522/JVRR4931</a>'))
story.append(e('&ldquo;A Posthumanist Social Epistemology: On the Possibility of Nonhuman '
               'Epistemic Injustice,&rdquo; <i>Anthropos: Journal of Psychology &amp; '
               'Philosophy</i> 55(2), Fall 2023, special issue &ldquo;Animals (Dis)Entangled '
               'or towards &lsquo;A New Form of Civilization.&rsquo;&rdquo; '
               '<a href="https://doi.org/10.26493/2630-4082.55.195-213">'
               'doi.org/10.26493/2630-4082.55.195-213</a>'))
story.append(e('&ldquo;Towards a Joyful Environmental Ethic: Open-ended Curiosity as an '
               'Environmental Virtue,&rdquo; <i>Journal of Ethnobiology</i> 43(3), Fall 2023. '
               '<a href="https://doi.org/10.1177/02780771231194777">'
               'doi.org/10.1177/02780771231194777</a>'))
story.append(e('&ldquo;Eventful Conversations and the Positive Virtues of a Listener&rdquo; '
               '(co-authored with Josu&eacute; Pi&ntilde;eiro), <i>Acta Analytica</i>, 2020, 35. '
               '<a href="https://doi.org/10.1007/s12136-020-00429-x">'
               'doi.org/10.1007/s12136-020-00429-x</a>'))
story.append(e('&ldquo;The Significance of Contingency and Detour in Hans Blumenberg&rsquo;s '
               'Philosophical Anthropology,&rdquo; <i>Metaphilosophy</i>, 2020, 50(1), 111&ndash;127. '
               '<a href="https://doi.org/10.1111/meta.12399">doi.org/10.1111/meta.12399</a>'))

story += section("Conference Proceedings")
story.append(e('&ldquo;The Potential and Limitations of Aristotelian Final Causes in the '
               'Life Sciences,&rdquo; a commentary on Lane DesAutels&rsquo; &ldquo;Vindicating '
               'Metaethical Naturalism: A Case for Final Causes in the Life Sciences,&rdquo; '
               '<i>Southwest Philosophy Review: The Journal of the Southwestern Philosophical '
               'Society</i>, 39(2), July 2023. '
               '<a href="https://doi.org/10.5840/swphilreview202339245">'
               'doi.org/10.5840/swphilreview202339245</a>'))

story += section("Pending / Forthcoming")
story.append(e('&ldquo;A Weird and Eerie Analysis of Electrical Cords and Wires,&rdquo; '
               'accepted to the edited collection <i>Finding Our Place In the Digital World</i>, '
               "under contract with Springer"))

story += section("Book Reviews")
story.append(e('<i>The Abyss Stares Back: Encounters with Deep-Sea Life</i> by Stacy Alaimo, '
               'forthcoming in <i>Environmental Values</i>'))
story.append(e('<i>How to Inhabit the Earth: Interviews with Nicolas Truong</i> (with Bruno '
               'Latour), <i>Environmental Values</i>, 34(1), 109&ndash;111, 2024. '
               '<a href="https://doi.org/10.1177/09632719241273551">'
               'doi.org/10.1177/09632719241273551</a>'))
story.append(e('<i>On the Emergence of an Ecological Class: A Memo</i> by Bruno Latour and '
               'Nikolaj Schultz, <i>Environmental Values</i>, 33(5), 571&ndash;573, 2023. '
               '<a href="https://doi.org/10.1177/09632719231196541">'
               'doi.org/10.1177/09632719231196541</a>'))

# ---- Conference Presentations ----
story += section("Conference Presentations")
presentations = [
    "&ldquo;One Person&rsquo;s Trash is Another&rsquo;s Treasure: An Aesthetic Environmental "
    "Ethic of Wasting Fully,&rdquo; International Association of Environmental Philosophy, May 2026",
    "&ldquo;The Death of Logos and Thumos in the Digital Worlds of Social Media and Generative "
    "AI&rdquo; (co-authored with Amin Amouhadi), Digital Worlds Workshop, April 2026",
    "&ldquo;From Confederate monuments to digital worlds: on the epistemic vices and virtues of "
    "material-discursive atmospheres,&rdquo; Bled Philosophical Conference, June 2025",
    "&ldquo;An Environmental Ethic of Love: On Human-Plant Liberations,&rdquo; 29th annual "
    "meeting of the International Association for Environmental Philosophy (IAEP), May 2025",
    "&ldquo;An Aztec Analysis of Plato&rsquo;s Symposium,&rdquo; panel on &ldquo;Encounters with "
    "Nature in Ancient Philosophy,&rdquo; CAMWS conference, March 2025",
    "&ldquo;A Weird and Eerie Analysis of Electrical Cords and Wires,&rdquo; Finding Our Place "
    "in the Digital World Workshop, February&ndash;March 2025",
    "&ldquo;Moving Forward by Going Back: A Diffractive Analysis of Song and Flower in Aztec "
    "Philosophy,&rdquo; Philosophy in the Wild conference, July 2024",
    "&ldquo;Academic Trauma and Healing,&rdquo; East-West Philosopher&rsquo;s Conference "
    "(Hawaii), May 2024",
    "&ldquo;Moving Forward by Going Back: An Environmental, Diffractive Analysis of Song and "
    "Flower in Aztec Philosophy,&rdquo; 28th annual meeting of the IAEP, May 2024",
    "&ldquo;Environmental Philosophy and the Ethics of Attention,&rdquo; webinar hosted by the "
    "ISEE and IAEP, April 2024",
    "&ldquo;Moving Forward by Returning to the Aztec Philosophy of Song and Flower,&rdquo; "
    "New Mexico and Texas Philosophical Society, April 2024",
    "&ldquo;Light in the Dark: On Why and How I teach Gloria Anzald&uacute;a in an Ethics, "
    "Technology, and Society Course,&rdquo; North American Association for Philosophy and "
    "Education Conference, October 2023",
    "&ldquo;Towards a more-than-human social epistemology: on the possibility of nonhuman "
    "epistemic injustice,&rdquo; Bled Philosophical Conference, June 2023",
    "&ldquo;Bio-temporal-diversity and becoming-through-death,&rdquo; Colby Summer Institute in "
    "Environmental Humanities, August 2022",
    "&ldquo;Bio-temporal-diversity and becoming-through-death,&rdquo; IAEP Spring Online "
    "Workshop, June 2022",
    "&ldquo;Reclaiming Our Future: Becoming-Through-Death and Gift Giving,&rdquo; Southeastern "
    "Association for the Continental Tradition, April 2022",
    "&ldquo;On the Breakdown and Restoration of Trust between Science and the Public,&rdquo; "
    "Roles of Governments and Societal Actors in Mitigating Climate Change Webinar (Illinois "
    "Institute of Technology), April 2022",
    "&ldquo;Towards a Positive, Joyful Environmental Ethic: Gratitude, Gift Giving, and "
    "Nonhuman Epistemic Justice,&rdquo; IAEP 25th Annual Meeting, October 2021",
    "&ldquo;Episodic Memory, Material Culture, and Retrospective Epistemic Violence,&rdquo; "
    "Eastern Division Meeting of the American Philosophical Association (APA), January 2021",
    "&ldquo;Episodic Memory, Material Culture, and Retrospective Epistemic Violence,&rdquo; "
    "Georgia Philosophical Society Online Workshop, October 2020",
    "&ldquo;Against Anthropocentric Epistemologies and the Possibility of Nonhuman Testimonial "
    "Injustice,&rdquo; IAEP 24th Annual Meeting, October 2020",
    "&ldquo;Personal Identity, Memory, and Material Culture,&rdquo; 44th Annual Mid-South "
    "Philosophy Conference, March 2020 (cancelled, COVID-19)",
    "&ldquo;Engineering Consent with Ag-Gag Laws&mdash;Oh, the Humanity!&rdquo; Association for "
    "Practical and Professional Ethics, Atlanta, February 2020",
    "&ldquo;Eventful Conversations and the Positive Virtues of a Good Listener,&rdquo; Bled "
    "Philosophical Conference, Slovenia, June 2019",
    "&ldquo;From Farm to Table: A Tale of Two Rice and the ANTs in the Food,&rdquo; Agriculture, "
    "Food, and Human Values Society, Madison, June 2018",
]
for p in presentations:
    story.append(e(p))

# ---- Reviews / commentaries ----
story += section("Journal Article Reviews")
story.append(e("<i>Acta Analytica</i> (Spring 2026); <i>Environmental Values</i> "
               "(Spring 2025; Spring 2026)"))

story += section("Conference Paper Commentaries")
story.append(e('&ldquo;New Ways to be Unheard,&rdquo; Digital Worlds Conference, April 2025'))
story.append(e('&ldquo;The Will to Submit: Surveillance Technologies and Their Impact on '
               'Academia,&rdquo; Digital Worlds Workshop, April 2023'))
story.append(e('&ldquo;Vindicating Metaethical Naturalism: A Case for Final Causes in the Life '
               'Sciences,&rdquo; Southwestern Philosophical Society, November 2022'))

# ---- Awards ----
story += section("Awards")
for a in [
    "Outstanding Commitment to Building Community Award, UGA Graduate School, Spring 2022",
    "Dissertation Completion Award, UGA Franklin College of Arts and Sciences, Spring 2021 ($21,840)",
    "Joseph Bertram Gittler Fellowship, UGA Philosophy Department, 2021 ($3,000)",
    "Outstanding Teaching Assistant, UGA Center for Teaching and Learning, 2020&ndash;2021",
    "IAEP Conference Best Graduate Student Paper Award, October 2020 ($250)",
]:
    story.append(e(a))

# ---- Teaching ----
story += section("Teaching Experience")
story.append(inst("University of Texas Rio Grande Valley"))
for t in [
    "PHIL 4325: Philosophy of Capitalism and Economics, Spring 2026",
    "PHIL 3301: Ancient Philosophy, Spring 2026",
    "PHIL 4328: Environmental Philosophy, Fall 2025",
    "PHIL 4310: Epistemology, Fall 2025",
    "BIET 6316: Environmental Philosophy (online), Spring 2025",
    "PHIL 2322: Ethics, Health, and Culture, Spring 2024 &ndash; Spring 2025",
    "PHIL 4318: Philosophy of Food, Fall 2023",
    "PHIL 3307: Indigenous Philosophy and Religion, Fall 2023",
    "PHIL 2326: Ethics, Technology, and Society, Fall 2022 &ndash; Spring 2026 (incl. online)",
]:
    story.append(s(t))
story.append(inst("University of Georgia (Instructor of Record)"))
for t in [
    "PHIL 2030: Introduction to Ethics, 2018&ndash;2021 (incl. online)",
    "PHIL 2010: Introduction to Philosophy, 2019&ndash;2021 (incl. online)",
    "PHIL 2500: Symbolic Logic, Fall 2019, Spring 2020 (98 students; supervised a graduate TA)",
    "PHIL 2020: Logic and Critical Thinking, Fall 2020 (84 students; supervised a graduate TA)",
]:
    story.append(s(t))
story.append(s("Teaching Assistant: PHIL 2010 (2016, A. Samaras); PHIL 2030 (2017, P. Stephens)"))
story.append(inst("University of North Florida"))
story.append(s("Instructor of Record: Introduction to Philosophy, Fall 2015"))
story.append(s("Grading TA: Business Ethics, 2012&ndash;2013"))
story.append(s("Courses prepared to teach: Philosophy of Science; Modern Philosophy; "
               "20th-Century Continental Philosophy; Feminist Philosophy; Ancient Philosophy"))

# ---- Service ----
story += section("Professional &amp; Departmental Service")
story.append(inst("UTRGV"))
for x in [
    "Chair of the Philosophy Pedagogy Group, Spring 2025&ndash;Spring 2026",
    "Organizer, Philosophy for the People Symposium, Spring 2026",
    "Organizer of Philosophy Film Nights, Fall 2025&ndash;Spring 2026",
    "Search Committee for a three-year lecturer in Bioethics, Spring 2025",
    "Outreach Committee (Fall 2022&ndash;present); Policy Committee (Fall 2022&ndash;present)",
    "Co-organized the &ldquo;Environmental Philosophy and the Ethics of Attention&rdquo; ISEE/IAEP "
    "webinar, April 2024; participated in planning the 2022 Eco Rio conference",
]:
    story.append(s(x))
story.append(inst("UGA"))
for x in [
    "Chair, Racial Justice Committee, United Campus Workers of Georgia, Fall 2021 "
    "(co-led a living-wage campaign; co-authored op-eds and a resolution)",
    "Chair / Co-chair, UGA chapter and Graduate Committee, United Campus Workers of Georgia, "
    "2018&ndash;2021 (led a three-year campaign to eliminate the $450 Special Institutional Fee)",
    "Philosophy Graduate Representative, Graduate Student Association, Fall 2019&ndash;Spring 2021",
    "Assistant Organizer, &ldquo;Nature, Technology, and AI&rdquo; workshop at UGA, Fall 2021",
    "Vice President, Philosophy Graduate Student Association, Fall 2017&ndash;Fall 2019 "
    "(initiated the department&rsquo;s first online courses)",
]:
    story.append(s(x))

# ---- Professional development / misc ----
story += section("Professional Development")
story.append(e("UTRGV B3 Spanish Immersion Program: Beginning Spanish I &amp; II, "
               "Intermediate Spanish II (2022&ndash;2024)"))
story.append(e("Summer Institute in Environmental Humanities, Colby College (Amrith, Chen, "
               "DeLoughrey, Yusoff), 2022; UGA Certificate in Diversity and Inclusion "
               "training, 2021&ndash;2022"))

story += section("Professional Memberships")
story.append(e("American Philosophical Association (APA); International Association for "
               "Environmental Philosophy (IAEP); Association for Practical and Professional "
               "Ethics (APPE)"))

story += section("Languages")
story.append(e("English (native); Spanish (learning, via UTRGV courses)"))

# ---- Dissertation summary ----
story += section("Dissertation Summary")
story.append(e(
    "Existential crises such as climate change and the sixth mass extinction are not merely "
    "technical problems; they require rethinking humanity and our relation to the natural "
    "environment. Drawing on the material feminisms of Karen Barad, Donna Haraway, and Rosi "
    "Braidotti, the dissertation argues that nonhumans&mdash;from clay to COVID-19, amoebas to "
    "supercolliders&mdash;are active participants in the world&rsquo;s becoming, co-constituting "
    "human bodies, experience, identity, and agency."))
story.append(e(
    "It stages three encounters between posthumanisms, environmental ethics, and social "
    "epistemology. First, it develops an environmental ethic for multispecies flourishing "
    "grounded in biocultural diversity, applied to two rices heralded as the future of food: "
    "the landrace Carolina Gold and the genetically modified Golden Rice. Second, it expands "
    "social epistemology to nonhuman animals, arguing that they can suffer testimonial "
    "injustice and epistemic smothering (after Fricker and Dotson), so that species extinction "
    "is the loss of entire worlds and ways of knowing."))
story.append(e(
    "Finally, drawing on Robin Wall Kimmerer&rsquo;s account of gratitude, gift giving, and "
    "reciprocity&mdash;and on Vinciane Despret&rsquo;s ethology&mdash;it presents an affirmative, "
    "joyful environmental ethic centered on the onto-epistemic virtue of openness: a way of "
    "doing good for the environment that can also feel good, and so be sustained."))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Italic", 8)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(letter[0] / 2.0, 0.5 * inch,
                             "Justin Simpson · Curriculum Vitae")
    canvas.drawRightString(letter[0] - 0.85 * inch, 0.5 * inch, "%d" % doc.page)
    canvas.restoreState()


doc = SimpleDocTemplate(
    "public/cv.pdf", pagesize=letter,
    leftMargin=0.85 * inch, rightMargin=0.85 * inch,
    topMargin=0.8 * inch, bottomMargin=0.8 * inch,
    title="Justin Simpson — Curriculum Vitae", author="Justin Simpson",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("Wrote public/cv.pdf")
