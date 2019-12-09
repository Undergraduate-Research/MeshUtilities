##############################################################################
# MIT License
#
# Copyright (c) 2019 William Gaylord
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#################################################################################
import re
import networkx as nx
import matplotlib.pyplot as plt
import urllib.request


G = nx.Graph()

#Regex for the OSLR webpage to grab all nodes and links between them.
IpRegex = """<tr><td><a href="http:\/\/\d+\.\d+\.\d+\.\d+:8080\/">(\d+\.\d+\.\d+\.\d+)<\/a><\/td><td width="30%">\(<a href="http:\/\/\w+-\d:8080\/">(\w+-\d+)<\/a>\)<\/td><td><a href="http:\/\/\d+\.\d+\.\d+\.\d+:8080\/">(\d+\.\d+\.\d+\.\d+)<\/a><\/td><td width="30\%">\(<a href="http:\/\/\w+-\d:8080\/">(\w+-\d+)<\/a>\)<\/td>"""

while True:
    html = urllib.request.urlopen("http://localnode:1978/nodes")
    raw_data = re.findall(IpRegex,html.read().decode("utf8"))
    nodes = set()
    edges = []
    for x in raw_data:
        nodes.add(x[1])
        nodes.add(x[3])
        edges.append((x[1],x[3]))
        
    G.add_nodes_from(list(nodes))
    G.add_edges_from(edges)
    plt.clf()
    nx.draw(G,with_labels=True)
    plt.ion()
    plt.show()
    plt.pause(30)



