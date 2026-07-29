"""
Post-process ppt-master-demo.pptx to add real PowerPoint animations:
- Slide transitions (Fade between all slides)
- Shape entrance animations (Fade In with staggered delays)
- Click-triggered and auto-advance animations

Note: python-pptx has no high-level animation API, so we manipulate
OpenXML directly via lxml to insert p:timing elements.
"""
import copy
from lxml import etree
from pptx import Presentation
from pptx.oxml.ns import qn, nsmap
import os

PPTX_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ppt-master-demo.pptx")
OUT_PATH  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ppt-master-demo-animated.pptx")

# ── XML namespaces used in animations ─────────────────────────
NSMAP_ANIM = {
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}

def qn_p(tag):
    return '{%s}%s' % (NSMAP_ANIM['p'], tag)
def qn_a(tag):
    return '{%s}%s' % (NSMAP_ANIM['a'], tag)

ANIM_NEXT_ID = [100]  # mutable counter for unique animation IDs

def next_id():
    ANIM_NEXT_ID[0] += 1
    return ANIM_NEXT_ID[0]

# ═══════════════════════════════════════════════════════════════
# SLIDE TRANSITIONS
# ═══════════════════════════════════════════════════════════════

def add_slide_transition(slide, trans_type="fade", duration=500):
    """
    Add a slide transition effect to a slide.
    trans_type: 'fade', 'push', 'wipe', 'cover', 'uncover', 'zoom', etc.
    """
    # Remove existing transition if any
    existing = slide.element.find(qn_p('transition'))
    if existing is not None:
        slide.element.remove(existing)

    transition = etree.SubElement(slide.element, qn_p('transition'))
    transition.set('durm', str(duration))  # duration in ms

    # Transition type element
    trans_elem = etree.SubElement(transition, qn_p(trans_type))
    if trans_type == 'fade':
        trans_elem.set('thruBlk', '0')
    elif trans_type in ('push', 'wipe', 'cover', 'uncover'):
        trans_elem.set('dir', 'ld')  # left-to-right by default

    return transition


# ═══════════════════════════════════════════════════════════════
# SHAPE ANIMATIONS
# ═══════════════════════════════════════════════════════════════

def build_timing_root():
    """Build the root p:timing tree skeleton."""
    timing = etree.Element(qn_p('timing'))

    # tnLst → par → cTn (root) → childTnLst → seq → cTn (mainSeq)
    tnLst = etree.SubElement(timing, qn_p('tnLst'))
    par_root = etree.SubElement(tnLst, qn_p('par'))

    root_id = next_id()
    cTn_root = etree.SubElement(par_root, qn_p('cTn'))
    cTn_root.set('id', str(root_id))
    cTn_root.set('dur', 'indefinite')
    cTn_root.set('restart', 'never')
    cTn_root.set('nodeType', 'tmRoot')

    childLst = etree.SubElement(cTn_root, qn_p('childTnLst'))
    seq = etree.SubElement(childLst, qn_p('seq'))
    seq.set('concurrent', '1')
    seq.set('nextAc', 'seek')

    seq_id = next_id()
    cTn_seq = etree.SubElement(seq, qn_p('cTn'))
    cTn_seq.set('id', str(seq_id))
    cTn_seq.set('dur', 'indefinite')
    cTn_seq.set('nodeType', 'mainSeq')

    return timing, cTn_seq


def build_fade_anim(target_shape_id, delay_ms=0, duration_ms=500, trigger="onClick"):
    """
    Build one par animation node for a Fade In effect.
    trigger: 'onClick' or 'afterPrevious'
    Returns (par_elem, next_cond_delay_or_none)
    """
    par = etree.Element(qn_p('par'))

    node_id = next_id()
    cTn = etree.SubElement(par, qn_p('cTn'))
    cTn.set('id', str(node_id))
    cTn.set('dur', str(duration_ms))  # autoRev not needed here
    cTn.set('fill', 'hold')

    # Start condition
    stCondLst = etree.SubElement(cTn, qn_p('stCondLst'))
    cond = etree.SubElement(stCondLst, qn_p('cond'))
    cond.set('delay', str(delay_ms))

    # Child timeline
    childLst = etree.SubElement(cTn, qn_p('childTnLst'))

    # Inner par
    inner_par = etree.SubElement(childLst, qn_p('par'))
    inner_id = next_id()
    inner_cTn = etree.SubElement(inner_par, qn_p('cTn'))
    inner_cTn.set('id', str(inner_id))
    inner_cTn.set('fill', 'hold')

    inner_stCond = etree.SubElement(inner_cTn, qn_p('stCondLst'))
    inner_cond = etree.SubElement(inner_stCond, qn_p('cond'))
    inner_cond.set('delay', '0')

    # Animation effect: Fade In
    inner_childLst = etree.SubElement(inner_cTn, qn_p('childTnLst'))
    anim_effect = etree.SubElement(inner_childLst, qn_p('animEffect'))
    anim_effect.set('transition', 'in')
    anim_effect.set('filter', 'fade')

    # Behavior
    cBhvr = etree.SubElement(anim_effect, qn_p('cBhvr'))
    bhvr_id = next_id()
    bhvr_cTn = etree.SubElement(cBhvr, qn_p('cTn'))
    bhvr_cTn.set('id', str(bhvr_id))
    bhvr_cTn.set('dur', str(duration_ms))
    bhvr_cTn.set('fill', 'hold')

    # Target element
    tgtEl = etree.SubElement(cBhvr, qn_p('tgtEl'))
    spTgt = etree.SubElement(tgtEl, qn_p('spTgt'))
    spTgt.set('spid', str(target_shape_id))

    # Attribute name list
    attrNameLst = etree.SubElement(cBhvr, qn_p('attrNameLst'))
    attrName = etree.SubElement(attrNameLst, qn_p('attrName'))
    attrName.text = 'style.opacity'

    return par


def build_flyin_anim(target_shape_id, delay_ms=0, duration_ms=500, direction="fromBottom"):
    """
    Build one par animation node for a Fly In effect.
    direction: 'fromBottom', 'fromTop', 'fromLeft', 'fromRight'
    """
    par = etree.Element(qn_p('par'))

    node_id = next_id()
    cTn = etree.SubElement(par, qn_p('cTn'))
    cTn.set('id', str(node_id))
    cTn.set('dur', str(duration_ms))
    cTn.set('fill', 'hold')

    stCondLst = etree.SubElement(cTn, qn_p('stCondLst'))
    cond = etree.SubElement(stCondLst, qn_p('cond'))
    cond.set('delay', str(delay_ms))

    childLst = etree.SubElement(cTn, qn_p('childTnLst'))

    inner_par = etree.SubElement(childLst, qn_p('par'))
    inner_id = next_id()
    inner_cTn = etree.SubElement(inner_par, qn_p('cTn'))
    inner_cTn.set('id', str(inner_id))
    inner_cTn.set('fill', 'hold')

    inner_stCond = etree.SubElement(inner_cTn, qn_p('stCondLst'))
    inner_cond = etree.SubElement(inner_stCond, qn_p('cond'))
    inner_cond.set('delay', '0')

    inner_childLst = etree.SubElement(inner_cTn, qn_p('childTnLst'))
    anim_effect = etree.SubElement(inner_childLst, qn_p('animEffect'))
    anim_effect.set('transition', 'in')
    anim_effect.set('filter', 'fly')
    anim_effect.set('dir', direction)

    cBhvr = etree.SubElement(anim_effect, qn_p('cBhvr'))
    bhvr_id = next_id()
    bhvr_cTn = etree.SubElement(cBhvr, qn_p('cTn'))
    bhvr_cTn.set('id', str(bhvr_id))
    bhvr_cTn.set('dur', str(duration_ms))
    bhvr_cTn.set('fill', 'hold')

    tgtEl = etree.SubElement(cBhvr, qn_p('tgtEl'))
    spTgt = etree.SubElement(tgtEl, qn_p('spTgt'))
    spTgt.set('spid', str(target_shape_id))

    attrNameLst = etree.SubElement(cBhvr, qn_p('attrNameLst'))
    attrName = etree.SubElement(attrNameLst, qn_p('attrName'))
    attrName.text = 'style.visibility'

    return par


def add_timing_to_slide(slide, timing_elem):
    """Attach a p:timing tree to a slide."""
    # Remove existing timing if any
    existing = slide.element.find(qn_p('timing'))
    if existing is not None:
        slide.element.remove(existing)
    slide.element.append(timing_elem)


def get_shape_ids(slide):
    """Return list of shape element IDs on the slide (for spTgt)."""
    ids = []
    for i, shape in enumerate(slide.shapes):
        # shape.shape_id is the internal drawing ID
        try:
            sid = shape._element.get('spid') or shape.shape_id
            ids.append((i, sid, shape))
        except:
            pass
    return ids


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

print("Loading presentation...")
prs = Presentation(PPTX_PATH)

total_content_shapes = 0

for slide_idx, slide in enumerate(prs.slides):
    print(f"\n── Slide {slide_idx + 1} ──")

    # 1) Add transition (Fade between slides)
    add_slide_transition(slide, trans_type="fade", duration=400)
    print(f"   ✅ Fade transition added")

    # 2) Add entrance animations for content shapes
    shape_info = get_shape_ids(slide)
    if not shape_info:
        print(f"   ⚠️  No shapes found")
        continue

    # Build timing tree
    timing, main_seq_cTn = build_timing_root()
    main_childLst = main_seq_cTn.find(qn_p('childTnLst'))
    if main_childLst is None:
        main_childLst = etree.SubElement(main_seq_cTn, qn_p('childTnLst'))

    # Animate content shapes (text boxes, rectangles, cards) with staggered fade-in
    delay = 0
    animated_count = 0

    for i, sid, shape in shape_info:
        # Skip background rectangles and tiny shapes
        if hasattr(shape, 'is_placeholder') and shape.is_placeholder:
            continue

        # Get shape position/size to filter small elements
        left = shape.left
        top = shape.top
        width = shape.width
        height = shape.height

        # Animate larger content shapes (cards, text boxes)
        # Skip very small or very large (full-slide background) shapes
        if width < 300000 or height < 10000:  # skip tiny elements
            continue

        # Add fade-in animation
        anim_par = build_fade_anim(sid, delay_ms=delay, duration_ms=350)
        main_childLst.append(anim_par)
        delay += 80  # stagger 80ms between shapes
        animated_count += 1
        total_content_shapes += 1

    # Also add a few Fly-In animations for variety on key slides
    if slide_idx in (0, 2, 6):  # Title, Templates, Comparison slides
        for i, sid, shape in shape_info:
            if i % 4 == 0 and animated_count > 3:  # every 4th shape gets fly-in
                anim_par = build_flyin_anim(sid, delay_ms=delay, duration_ms=400, direction="fromBottom")
                main_childLst.append(anim_par)
                delay += 60
                animated_count += 1

    add_timing_to_slide(slide, timing)
    print(f"   ✅ {animated_count} entrance animations added (staggered fade-in)")

print(f"\n{'='*60}")
print(f"✅ Animations added! Total shapes animated: {total_content_shapes}")
print(f"   - Slide transitions: Fade (all {len(prs.slides)} slides)")
print(f"   - Shape animations: staggered Fade In + selective Fly In")

# Save
prs.save(OUT_PATH)
print(f"\n💾 Saved to: {OUT_PATH}")
print(f"   File size: {os.path.getsize(OUT_PATH) / 1024:.1f} KB")
print(f"\n🎬 Open in PowerPoint and press F5 to see animations in action!")
