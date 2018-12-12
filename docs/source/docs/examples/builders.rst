.. _Builders:

Examples of reconfigure.builders
********************************

Parsers (:class:`reconfigure.builders`) is a base class that will process string*
content.  Parsers have several subclasses available:

* BIND9 (:class:`reconfigure.builders`)
* crontab (:class:`reconfigure.builders.BoundBuilder`)


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
