misp-graph
==========

misp-graph is a tool to analyze a MISP XML export and generate graphs from
the events and its attributes. The export format currently supported are dot files (Graphviz)
and gexf file Graph Exchange XML Format. Graph files can then be used with Gephi or another
tools supporting these file formats. misp-graph can be used directed with the REST API of MISP or using
an XML dump.

![A Sample Graph visualized with Gephi](https://raw.github.com/MISP/misp-graph/master/sample/sample.png)

Requirements
------------

* Python > 2.6
* networkx

Usage
-----

        Usage: misp-graph.py

        Options:
          -h, --help            show this help message and exit
          -d, --debug           debug messages on stderr
          -t RECORDTYPE, --type=RECORDTYPE
                                type of the record (default record is 'domain')
          -f FILENAME, --file=FILENAME
                                filename of the MISP XML file to read (default MISP
                                XML dump is 'malwg.xml')
          -c CENTER, --center=CENTER
                                center node (could be an event id or also a value of a
                                record) into a subgraph. By default, all events and
                                matching attributes are added to the graph.
          -r RADIUS, --radius=RADIUS
                                maximum distance between node
          -o OUTPUTFORMAT, --outputformat=OUTPUTFORMAT
                                format of the graph output dot (graphviz), gexf
                                (default format is dot)
          -n OUTFILENAME, --outfilename=OUTFILENAME
                                output filename (default is out.<format>)
          -u URL, --url=URL     url to access MISP
          -a AUTHKEY, --authkey=AUTHKEY
                                authentication key to access MISP


### Use case(s)

If you have a specific event (e.g. from OSINT or from a vendor providing a large set of IOCs) and you would like to see the direct neighbors to this event sharing
the same attributes. As example, you want to see the shared attributes from event 310 with the other event with a maximum distance of 2 hops:

    misp-graph.py -o dot -c 310 -r 2 -n event310.dot


If you would like to make a quick visualization of your MISP export, there will be a file called out.dot containing the XML in dot format.

    misp-graph -f yourdump.xml

License
-------

This software is licensed under GNU Affero General Public License version 3.

Copyright (c) 2012, 2013 Alexandre Dulaunoy (a AT foo be)

