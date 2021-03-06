##############################################################################
# MIT License
#
# Copyright (c) 2020 William Gaylord
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
import urllib.request




#Regex for the OSLR webpage to grab all nodes and links between them.
IpRegex = re.compile("""(\d+\.\d+\.\d+\.\d+)""")

#Regex for the Mesh Status webpage to grab ip and netmask data.
IpNodeRegex = re.compile("""<tr><th align=right><nobr>LAN address<\/nobr><\/th><td>(\d+\.\d+\.\d+\.\d+) <small>\/ (\d+)<\/small><br>""")


html = urllib.request.urlopen("http://localnode:2006")
html = html.read().decode("utf8")
html = html.split("Topology")[1]
html = html.split("HNA")[0]
raw_data = IpRegex.findall(html)
node_ips = list(set(raw_data))

print("Node Ip,      Node LAN Address, Netmask")



for x in node_ips:
    html = urllib.request.urlopen("http://"+x+":8080/cgi-bin/status")
    raw_data = IpNodeRegex.findall(html.read().decode("utf8"))
    print(x,raw_data)




