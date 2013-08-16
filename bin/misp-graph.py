#!/usr/bin/python
#
# This script is used to convert a MISP XML file (first version)
# into dot file or gexf for later processing (with Gephi).
#
# This software is free software released the AGPL.
#
# Copyright (C) 2012-2013 Alexandre Dulaunoy (a@foo.be)


from optparse import OptionParser
import sys
import networkx
import urllib2

usage = "usage: %s" % sys.argv[0]
parser = OptionParser(usage)

# find the right lxml/elementtree library
try:
  from lxml import etree
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
        except ImportError:
          print("Failed to import ElementTree from any known place")

def fetch(url=None, auth=None):
    if url is None or auth is None:
        return False
    req = urllib2.Request(url+"/events/xml/"+auth)
    r = urllib2.urlopen(req)
    v = r.read()
    return v

parser.add_option("-d", "--debug", dest="debug", action="store_true", default=False, help="debug messages on stderr")
parser.add_option("-t", "--type", dest="recordtype", help="type of the record (default record is 'domain')", default="domain")
parser.add_option("-f", "--file", dest="filename", help="filename of the MISP XML file to read (default MISP XML dump is 'malwg.xml')", default="malwg.xml")
parser.add_option("-c", "--center", dest="center", help="center node (could be an event id or also a value of a record) into a subgraph. By default, all events and matching attributes are added to the graph.", default=None)
parser.add_option("-r", "--radius", dest="radius", help="maximum distance between node", default=2)
parser.add_option("-o", "--outputformat", dest="outputformat", help="format of the graph output dot (graphviz), gexf (default format is dot)", default="dot")
parser.add_option("-n", "--outfilename", dest="outfilename", help="output filename (default is out.<format>)", default="out.")
parser.add_option("-u", "--url", dest="url", help="url to access MISP", default=None)
parser.add_option("-a", "--authkey", dest="authkey", help="authentication key to access MISP", default=None)

(options, args) = parser.parse_args()


if options.url is None or options.authkey is None:
    tree = etree.parse(options.filename)
else:
    tree = etree.fromstring(fetch(url=options.url,auth=options.authkey))

g = networkx.Graph()

typematch = False
for element in tree.iter():
   if element.tag == "event_id":
        if options.debug:
            sys.stderr.write(element.text+"node added\n")
        if options.url:
            eid = options.url+"/events/view/"+element.text
        else:
            eid = "Event "+element.text
        g.add_node(eid)
   if element.tag == "type" and element.text == options.recordtype:
        typematch = True
   if typematch and element.tag == "value":
        if options.debug:
            sys.stderr.write(element.text+"edge added to "+ eid+ "\n")
        g.add_edge(eid,element.text)
        typematch = False

if options.center is not None:
    g = networkx.ego_graph(g, options.center, radius=options.radius)

if options.outfilename is not "out.":
    outfilename = options.outfilename
else:
    outfilename = options.outfilename+options.outputformat

if options.outputformat == "dot":
    networkx.write_dot(g, outfilename)
elif options.outputformat == "gexf":
    networkx.write_gexf(g, outfilename)
