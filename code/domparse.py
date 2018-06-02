from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
         if node2.nodeType == Node.TEXT_NODE:
             print(node2.data)
