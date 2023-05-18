Through following steps we can run the attack:

1. run "sudo p4run" command to check the original topology.
2. through "links" command we can see the links in the topology
3. run "sudo python a.py" for the attack in another tab.
4. run "sudo p4run" command to run the p4. and by again "links" command we can see the fake links added to the topology.
5. now in other tab run "sudo python routing-controller.py" command to run the controller.
6. now in the previous tab set up xterm nodes through "xterm h2 h3" command.
7. in xterm nodes run "sudo python recieve.py" in h2 node and "sudo python send_mod.py 10.0.2.2" command in h3 node.
8. we can trace the packets through "sudo wireshark" command in another tab. 
9. for mitigation of this attack we can run "sudo routing-controller_mitigation.py" command where it brings back to the original topology and again re run "sudo p4run" command. 