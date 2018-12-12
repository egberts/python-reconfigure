.. _Includers:

Examples of reconfigure.includers
*********************************

Parsers (:class:`reconfigure.includers`) is a base class that will process string content.  Parsers have several subclasses available:

* auto includer (:class:`reconfigure.includers.AutoIncluder`)
* BIND9 (:class:`reconfigure.includers.BIND9Includer`)
* NGINX web server (:class:`reconfigure.includers.NginxIncluder`)
* Supervisor (:class:`reconfigure.includers.SupervisorIncluder`)


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
