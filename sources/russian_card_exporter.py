#! /usr/bin/python

import xml.etree.ElementTree as et
orig_tree = et.parse('Russian_playing_cards_deck.svg')
orig_root = orig_tree.getroot()

for card in orig_root:
    card_root = et.Element('svg')
    card_root.attrib.update({
        'xmlns': 'http://www.w3.org/2000/svg',
        'version': '1.1',
        # 'height': '539',
        # 'width': '359',
        'height': '2310',
        'width': '5100',
    })
    card_root.append(card)
    card_tree = et.ElementTree(card_root)
    card_tree.write(card.attrib['id'] + '.svg')
    # card_tree.write(card.attrib['id'] + '.svg', xml_declaration=True)
