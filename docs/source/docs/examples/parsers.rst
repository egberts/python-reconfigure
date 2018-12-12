.. _Parsers:

Examples of reconfigure.parsers
*******************************

Parsers (:class:`reconfigure.parsers`) is a base class that will process string
content.  Parsers have several subclasses available:

* BIND9 (:class:`reconfigure.parsers.BIND9Parser`)
* crontab (:class:`reconfigure.parsers.CrontabParser`)
* exports (:class:`reconfigure.parsers.ExportsParser`)
* iptables (:class:`reconfigure.parsers.IPtablesParser`)
* JSON (:class:`reconfigure.parsers.JsonParser`)
* NGINX web server (:class:`reconfigure.parsers.NginxParser`)
* NSD DNS server (:class:`reconfigure.parsers.NSDParser`)
* Shell (:class:`reconfigure.parsers.ShellParser`)
* Space-separated value (SSV) (:class:`reconfigure.parsers.SSVParser`)


Space-Separated Value (SSV) Parser
==================================

::: code-block python
    import reconfigure

    parser = reconfigure.SSVParser()
    node_tree = parser.parse("""col1 col2 col3
    John Doe 123-333-1234
    Mia Hamm 321-321-1234
    Jill Greene 333-333-3333"""
    print(node_tree)

Variable `node_tree` is defined as ``Nodes`` with children nodes.
