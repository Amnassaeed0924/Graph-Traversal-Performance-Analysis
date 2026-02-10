#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\Bilal\Documents\daafsdfs.txt"

# Your data is space-separated, so use delim_whitespace=True
data = pd.read_csv(file_path, delim_whitespace=True)

plt.plot(data["Nodes"], data["DFS_Time"], 'b-o', label="DFS")
plt.plot(data["Nodes"], data["BFS_Time"], 'r--s', label="BFS")

plt.xlabel("Nodes")
plt.ylabel("Time (seconds)")
plt.title("DFS vs BFS Performance (Adjacency Matrix)")
plt.legend()
plt.grid(True)
plt.show()


# In[14]:


#Adacency List BFS And DFS
import pandas as pd
import matplotlib.pyplot as plt

# Read adjacency list results
file_path = r"C:\Users\Bilal\Documents\listdfsbfs.txt"  
data = pd.read_csv(file_path, delim_whitespace=True)  

# Plot Nodes vs Time
plt.figure(figsize=(8,6))
plt.plot(data["Nodes"], data["DFS_Time"], marker='o', label="DFS (Adjacency List)")
plt.plot(data["Nodes"], data["BFS_Time"], marker='s', label="BFS (Adjacency List)")

plt.xlabel("Number of Nodes")
plt.ylabel("Time (seconds)")
plt.title("BFS and DFS Performance using Adjacency List")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# In[21]:


import pandas as pd
import matplotlib.pyplot as plt

# File paths
matrix_file = r"C:\Users\Bilal\Documents\daafsdfs.txt"
list_file   = r"C:\Users\Bilal\Documents\listdfsbfs.txt"

# Read data
matrix_data = pd.read_csv(matrix_file, delim_whitespace=True)
list_data = pd.read_csv(list_file, delim_whitespace=True)

# Plot DFS
plt.plot(matrix_data["Nodes"], matrix_data["DFS_Time"],
         'b-o', label="DFS (Adjacency Matrix)")
plt.plot(list_data["Nodes"], list_data["DFS_Time"],
         'b--o', label="DFS (Adjacency List)")

# Plot BFS
plt.plot(matrix_data["Nodes"], matrix_data["BFS_Time"],
         'r-s', label="BFS (Adjacency Matrix)")
plt.plot(list_data["Nodes"], list_data["BFS_Time"],
         'r--s', label="BFS (Adjacency List)")

plt.xlabel("Nodes")
plt.ylabel("Time (seconds)")
plt.title("DFS vs BFS Performance: Matrix vs List")
plt.legend()
plt.grid(True)
plt.show()


# In[22]:


import pandas as pd
import matplotlib.pyplot as plt

matrix_file = r"C:\Users\Bilal\Documents\daafsdfs.txt"
list_file   = r"C:\Users\Bilal\Documents\listdfsbfs.txt"

matrix_data = pd.read_csv(matrix_file, delim_whitespace=True)
list_data = pd.read_csv(list_file, delim_whitespace=True)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Adjacency Matrix
axes[0].plot(matrix_data["Nodes"], matrix_data["DFS_Time"], 'b-o', label="DFS")
axes[0].plot(matrix_data["Nodes"], matrix_data["BFS_Time"], 'r-s', label="BFS")
axes[0].set_title("Adjacency Matrix")
axes[0].set_xlabel("Nodes")
axes[0].set_ylabel("Time (seconds)")
axes[0].legend()
axes[0].grid(True)

# Adjacency List
axes[1].plot(list_data["Nodes"], list_data["DFS_Time"], 'b-o', label="DFS")
axes[1].plot(list_data["Nodes"], list_data["BFS_Time"], 'r-s', label="BFS")
axes[1].set_title("Adjacency List")
axes[1].set_xlabel("Nodes")
axes[1].set_ylabel("Time (seconds)")
axes[1].legend()
axes[1].grid(True)

plt.suptitle("DFS vs BFS Performance Comparison")
plt.tight_layout()
plt.show()


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

matrix_file = r"C:\Users\Bilal\Documents\daafsdfs.txt"
list_file   = r"C:\Users\Bilal\Documents\listdfsbfs.txt"

matrix_data = pd.read_csv(matrix_file, delim_whitespace=True)
list_data = pd.read_csv(list_file, delim_whitespace=True)

# Ensure same node ordering
nodes = matrix_data["Nodes"]

matrix_mem = matrix_data["DFS_Mem(Bytes)"]
list_mem = list_data.filter(like="DFS").iloc[:, 0]

x = np.arange(len(nodes))
width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(x - width/2, matrix_mem, width,
        label="DFS Memory (Adjacency Matrix)", color="red")
plt.bar(x + width/2, list_mem, width,
        label="DFS Memory (Adjacency List)", color="navy")

plt.xlabel("Nodes")
plt.ylabel("Memory (Bytes)")
plt.title("DFS Memory Usage: Adjacency Matrix vs Adjacency List")
plt.xticks(x, nodes)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)

# 🔑 CRITICAL FIX
plt.yscale("log")

plt.show()






# In[32]:


import pandas as pd
import matplotlib.pyplot as plt

# File paths
matrix_file = r"C:\Users\Bilal\Documents\daafsdfs.txt"
list_file   = r"C:\Users\Bilal\Documents\listdfsbfs.txt"

matrix_data = pd.read_csv(matrix_file, delim_whitespace=True)
list_data = pd.read_csv(list_file, delim_whitespace=True)

nodes = matrix_data["Nodes"]
matrix_mem = matrix_data["DFS_Mem(Bytes)"]
list_mem = list_data["DFS_Mem(Bytes)"]

plt.figure(figsize=(8, 6))


plt.plot(nodes, matrix_mem, 'r-o', label="DFS Memory (Adjacency Matrix)", markersize=6)
plt.plot(nodes, list_mem, 'b-s', label="DFS Memory (Adjacency List)", markersize=6)

-
plt.xlim(left=0) 


plt.xlabel("Nodes")
plt.ylabel("Memory (Bytes)")
plt.title("DFS Memory Usage For Graph Traversal (Adjacency Matrix vs Adjacency List)")
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5) # 'both' grid for log scale visibility

plt.yscale("log")

plt.tight_layout() # Ensures everything fits perfectly
plt.show()


# In[33]:


import pandas as pd
import matplotlib.pyplot as plt

# File paths
matrix_file = r"C:\Users\Bilal\Documents\daafsdfs.txt"
list_file   = r"C:\Users\Bilal\Documents\listdfsbfs.txt"

matrix_data = pd.read_csv(matrix_file, delim_whitespace=True)
list_data = pd.read_csv(list_file, delim_whitespace=True)

nodes = matrix_data["Nodes"]
matrix_mem_bfs = matrix_data["BFS_Mem(Bytes)"]
list_mem_bfs = list_data["BFS_Mem(Bytes)"]

plt.figure(figsize=(8, 6))

plt.plot(nodes, matrix_mem_bfs, 'r-o', label="BFS Memory (Adjacency Matrix)", markersize=6)
plt.plot(nodes, list_mem_bfs, 'b-s', label="BFS Memory (Adjacency List)", markersize=6)

plt.xlim(left=0)

plt.xlabel("Nodes")
plt.ylabel("Memory (Bytes)")
plt.title("BFS Memory Usage For Graph Traversal (Adjacency Matrix vs Adjacency List)")
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)

plt.yscale("log")

plt.tight_layout()
plt.show()


# In[ ]:




