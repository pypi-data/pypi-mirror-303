# Copyright (c) 2024 XX Xiao

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import re,ast
import networkx as nx
import numpy as np
import json
import matplotlib.pyplot as plt 

def load_chip_configuration(chip_name):
    with open('./' + chip_name + '_previous-1.json','r') as file:
        chip_info = json.load(file)
    print(f'{chip_name} configuration load done!')
    return chip_info

class Backend:
    """A class to represent a quantum hardware backend as a nx.Graph.
    """
    def __init__(self,chip_info):
        """Initialize a Backend object.

        Args:
            chip_info (dict): A dictionary containing information about the quantum chip. This includes details 
            such as the size of the chip, calibration time, priority qubits, available basic gates, and couplers 
            (e.g., CZ gates).
        """
        self.size = chip_info['chip']['size']
        self.calibration_time = chip_info['chip']['calibration_time']
        self.priority_qubits = ast.literal_eval(chip_info['chip']['priority_qubits'])
        self.basic_gates = chip_info['chip']['basic_gates']
        self.couplers  = chip_info['gate']['CZ']

        self.picknodes = []
        self.graph = self.get_graph()

    def get_graph_edges(self):
        coupler_with_fidelity = []
        for cz in self.couplers.keys():
            if cz == '__order_senstive__': 
                continue
            coupler_qubits = re.findall(r'\d+', cz)
            coupler_qubits = [int(num) for num in coupler_qubits]
            fidelity = self.couplers[cz]['fidelity']
            if fidelity != 0:
                coupler_info = (coupler_qubits[0],coupler_qubits[1],fidelity)
                coupler_with_fidelity.append(coupler_info)
        return coupler_with_fidelity
    
    def get_nodes_position(self):
        row,col = self.size
        position = {}
        idx = 0
        for i in range(row):
            for j in range(col):
                if i == 0:
                    position[idx] = (j,i)
                else:
                    position[idx] = (j,-i)
                idx += 1
        return position
        
    def get_graph(self):
        position = self.get_nodes_position()
        edges_with_weight = self.get_graph_edges()
        nodes = list(position.keys())
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_weighted_edges_from(edges_with_weight)
        return G
    
    def draw(self):
        pos = self.get_nodes_position()
        node_colors = ['#009E73' if node in self.picknodes else '#0072B2' for node in self.graph.nodes() ]
        
        plt.figure(figsize=(12, 10))
        nx.draw(self.graph, pos, with_labels=True, node_color=node_colors, node_size=600,\
                edge_color = 'k',width = 2,\
                font_size=10,font_color='white', font_weight='bold')
        edge_labels = nx.get_edge_attributes(self.graph, 'weight') 
        edge_labels_init = {}
        for k,v in edge_labels.items():
            edge_labels_init[k] = np.round(v,3)
        #print(edge_labels,edge_labels_init)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels_init,font_size=10)
        #plt.title("Baihua chip")
        plt.show()
        return None