import tkinter as tk
import math
import random
from tkinter import Tk

filename = "graph_data.txt"
with open(filename, "r") as file:
    content = file.readlines()
    data_dict = {}
    for line in content:
        values = line.split(" ")
        key = values[0]
        dictionary_values = values[1:]
        data_dict[key] = dictionary_values

spname = "shortpath.txt"

with open(spname, "r") as file:
    nums = [int(num) for num in file.read().split()]
print(nums)



class GraphDisplay(tk.Canvas):
    def __init__(self, master, graph, sp, **kwargs):
        super().__init__(master, **kwargs)
        self.graph = graph
        self.sp = sp
        self.node_radius = 20
        self.edge_width = 2
        self.node_positions = {}  # dictionary to store node positions

    def draw_graph(self):
        self.delete(tk.ALL)  # clear canvas
        # Calculate node positions
        self.calculate_node_positions()
        # Draw edges
        for node, edges in self.graph.items():
            x1, y1 = self.node_positions[node]
            for alph in edges:
                if alph == '\n':
                    break
                x2, y2 = self.node_positions[alph]
                if( (node == '3' and alph == '8') or (node == '8' and alph == '3')):
                    self.create_line(x1, y1, x2, y2, width=self.edge_width, fill="blue")
                    continue

                self.create_line(x1, y1, x2, y2, width=self.edge_width)
        # Draw nodes
        for node, position in self.node_positions.items():
            x, y = position
            count = 0
            n=0
            for snode in self.sp :       
                if node == snode:
                    count += 1
                    break
                   
            if(count == 1):
                self.create_oval(x - self.node_radius, y - self.node_radius,x + self.node_radius, y + self.node_radius,
                            fill='yellow', outline='black')
                
            else:
                self.create_oval(x - self.node_radius, y - self.node_radius,x + self.node_radius, y + self.node_radius,
                            fill='white', outline='black')
            self.create_text(x, y, text=str(node))




    def calculate_node_positions(self):
        arr = [600,600,    #0
               720,650,    #1
               960,590,   #2
               790,490,   #3
               920,470,     #4
               590,350,     #5
               400,630,     #6
               740,270,     #7
               250,440,     #8
               290,200,     #9
               590,470,     #10
               850,70,     #11
               870,680,     #12
               935,770,     #13
               1170,470,     #14
               600,740,     #15
               950,320,     #16
               530,160,     #17
               1190,70,     #18
               950, 190 ]    #19
            
        width = self.winfo_width()
        height = self.winfo_height()
        num_nodes = len(self.graph)
        if num_nodes == 0:
            print("empty path")
            return 

        radius = min(width, height) * 0.4
        j=0
        for i, node in enumerate(self.graph.keys()):        
            x = arr[j] 
            y = arr[j+1]
            j+=2
            self.node_positions[node] = (x, y)

    def resize(self, event):
        self.draw_graph()

# Example usage
if __name__ == "__main__":
    graph = data_dict
    sp = {}
    k = 0
    while(k < len(nums)):
        if(k+1 == len(nums)):
            sp[str(nums[k])] = ""
            break
        sp[str(nums[k])] = str(nums[k+1])
        k += 1
    print(sp)

    print("\n")
    root = Tk()

    canvas = GraphDisplay(root, graph, sp, width=400, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.draw_graph()
    canvas.bind("<Configure>", canvas.resize)
    
    root.mainloop()