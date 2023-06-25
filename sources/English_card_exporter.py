#! /usr/bin/python

import xml.etree.ElementTree as et

# Namespaces on root
nss = {
    'dc': 'http://purl.org/dc/elements/1.1/',
    'cc': 'http://creativecommons.org/ns#',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'svg': 'http://www.w3.org/2000/svg',
    'sodipodi': 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd',
    'inkscape': 'http://www.inkscape.org/namespaces/inkscape',
    '': 'http://www.w3.org/2000/svg',  # Is this needed?
}
for key, url in nss.items():
    et.register_namespace(key , url)

# Useless attributes from inkscape
evil = [
    et.QName('http://www.inkscape.org/namespaces/inkscape', 'connector-curvature'),
    et.QName('http://www.inkscape.org/namespaces/inkscape', 'path-effect'),
    et.QName('http://www.inkscape.org/namespaces/inkscape', 'transform-center-y'),
    et.QName('http://www.inkscape.org/namespaces/inkscape', 'transform-center-x'),
    et.QName('http://www.inkscape.org/namespaces/inkscape', 'original-d'),
    et.QName('http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd', 'nodetypes'),
    et.QName('http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd', 'type'),
    et.QName('http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd', 'cx'),
    et.QName('http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd', 'cy'),
    et.QName('http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd', 'rx'),
    et.QName('http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd', 'ry'),
]
def strip_attrib(el):
    for evil_attrib in evil:
        if evil_attrib in el.attrib:
            del el.attrib[evil_attrib]
def walk(root, process):
    process(root)
    for el in root:
        walk(el, process)

tree = et.parse('English_pattern_playing_cards_deck-2.svg')
root = tree.getroot()

# Remove first four tags which were inkscape kruft etc
del root[0:3]

# Remove useless attributes
walk(root, strip_attrib)

new_root = et.Element('svg')
new_root.attrib.update({
    # 'xmlns': 'http://www.w3.org/2000/svg',
    'version': '1.1',
    'height': '2310',
    'width': '5100',
})

for el in root:
    new_root.append(el)

new_tree = et.ElementTree(new_root)
new_tree.write('new_cards.svg')
