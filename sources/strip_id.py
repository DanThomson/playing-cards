#! /usr/bin/python

# Strip out the ids from an svg/xml file. This was used while cleaning up the source.
# Edit line 8, to change the file on which this acts.
# Edit line 28 to change the output file.
import xml.etree.ElementTree as et

filename = 'hearts/all.svg'

# Namespaces
nss = {
    '': 'http://www.w3.org/2000/svg',  # Is this needed?
}
for key, url in nss.items():
    et.register_namespace(key , url)

def strip_attrib(el):
    if 'id' in el.attrib:
        del el.attrib['id']

def walk(root, process):
    process(root)
    for el in root:
        walk(el, process)

tree = et.parse(filename)
walk(tree.getroot(), strip_attrib)
tree.write(filename)
