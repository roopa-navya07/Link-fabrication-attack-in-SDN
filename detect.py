import json

topo_file1 = "/home/p4/p4-tools/p4-learning/examples/fabrication/p4app1.json"
with open(topo_file1 , "r") as f:
    original_topo = json.load(f)

topo_file = "/home/p4/p4-tools/p4-learning/examples/fabrication/p4app.json"
with open(topo_file, "r") as f:
    modified_topo = json.load(f)

# Compare the two topologies
if original_topo == modified_topo:
    print("The topology is the same")
else:
    print("The topology is changed")
    # Run the original p4app1.json file
    # You can use the Mininet API to create the network from the topology in p4app1.json
    # and start the switches and hosts