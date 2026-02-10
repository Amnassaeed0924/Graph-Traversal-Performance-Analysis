# Comparative Analysis of Graph Traversal Algorithms (BFS vs DFS)

## 📋 Project Overview
This project provides an empirical performance analysis of **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. The study focuses on how different graph representations—**Adjacency Matrix** and **Adjacency List**—impact execution speed and memory consumption.

> **Key Discovery:** Adjacency Lists can be over **100x more memory-efficient** in sparse graph scenarios compared to Adjacency Matrices.

---

## 🚀 Key Objectives
* **Implementation:** Iterative BFS and DFS algorithms developed in C++.
* **Benchmarking:** Measured execution time using `clock()` and memory via peak auxiliary storage.
* **Comparison:** Evaluated $O(V^2)$ vs. $O(V + E)$ space complexities.
* **Visualization:** Data recorded across varying node sizes to observe scaling trends.

---

## 📊 Comparison Summary

| Feature | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Data Structure** | 2D Array | Array of Lists/Vectors |
| **Space Complexity** | $O(V^2)$ | $O(V + E)$ |
| **Memory Efficiency** | Low (Static) | **High (Dynamic)** |
| **Edge Lookup** | $O(1)$ | $O(degree(v))$ |
| **Best Use Case** | Dense Graphs | Sparse Graphs / Large Networks |

---

## 🛠️ Methodology
1. **Graph Generation:** Randomly generated connected graphs ensure full traversal.
2. **Uniform Testing:** The same graph structure is applied to both representations for a fair comparison.
3. **Memory Tracking:** We measure **Peak Auxiliary Space**:
   * **DFS:** Maximum Stack size.
   * **BFS:** Maximum Queue size.
4. **Environment:** * **Language:** C++
   * **IDE:** Dev C++ / Online Compiler
   * **OS:** Windows

---

## 🔍 Assumptions & Constraints
* **Connectivity:** All graphs are connected to prevent early termination.
* **Source Node:** All traversals begin from the same initial vertex.
* **Matrix Scanning:** The algorithm assumes a full row scan ($O(V)$) for neighbor identification in matrices.

---

## 📈 Results Highlights
* **Memory:** Adjacency Lists showed a massive advantage in memory scaling as nodes ($V$) increased.
* **Execution Time:** Adjacency Lists outperformed Matrices in neighbor discovery by skipping "empty" edges.
