.. _Configs:

Examples of reconfigure.configs
*******************************

Parsers (:class:`reconfigure.configs`) is a base class that will process string
content.  Parsers have several subclasses available:

* Ajenti (:class:`reconfigure.configs.AjentiConfig`)
* BIND9 (:class:`reconfigure.configs.BIND9Config`)
* csf (:class:`reconfigure.configs.CSFConfig`)
* ctdb (:class:`reconfigure.configs.CTDBConfig`)
* crontab (:class:`reconfigure.configs.CrontabConfig`)
* dhcpd (:class:`reconfigure.configs.DHCPDConfig`)
* exports (:class:`reconfigure.configs.ExportsConfig`)
* fstab (:class:`reconfigure.configs.FSTaBConfig`)
* group (:class:`reconfigure.configs.GroupConfig`)
* hosts (:class:`reconfigure.configs.HostsConfig`)
* iptables (:class:`reconfigure.configs.IPTablesConfig`)
* Net Apple talk (:class:`reconfigure.configs.NetatalkConfig`)
* NSD DNS server (:class:`reconfigure.configs.NSDConfig`)
* UNIX Password (:class:`reconfigure.configs.PasswdConfig`)
* UNIX resolv.conf (:class:`reconfigure.configs.ResolvConfig`)
* Samba (:class:`reconfigure.configs.SambaConfig`)
* Squid (:class:`reconfigure.configs.SquidConfig`)
* Supervisor (:class:`reconfigure.configs.SupervisorConfig`)


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
