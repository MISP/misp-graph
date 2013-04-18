misp-graph
==========

misp-graph is a tool to analyze a MISP XML export and generate graphs from
the events and its attributes. The export format currently supported are dot files (Graphviz)
and gexf file Graph Exchange XML Format. Graph files can then be used with Gephi or another
tools supporting these file formats.

Requirements
------------

 # Python > 2.6
 # networkx

Usage
-----

        Usage: ./bin/misp-graph.py

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


License
-------

This software is licensed under GNU Affero General Public License version 3.

Copyright (c) 2012, 2013 Alexandre Dulaunoy (a AT foo be)

