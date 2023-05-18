import sys
from mininet.net import Mininet
from p4utils.utils.tcp_utils import *
import time
import json



if __name__ == "__main__":
    topo_file = "/home/p4/p4-tools/p4-learning/examples/1/p4app.json"
    with open(topo_file,"r+") as f:
        topo_dict = json.load(f)
        links = topo_dict["topology"]["links"]
        new_links=[['s3','s2']]
        
        #print(topo_dict["topology"]["links"])
        topo_dict["topology"]["links"] =new_links+links
        print(topo_dict["topology"]["links"] )

    with open("p4app.json", "w") as f:
        json.dump(topo_dict, f)  
        
