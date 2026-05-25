# 🧠 Python Heap 

## From-scratch implementation of **Min Heap** in Python.
- Heap from scratch
- Heap depinding in List implementation
---
## 📦 Project Structure
```
heaps/
├── heap.py
├── heap_list.py
└── README.md
```
## 📦 Time And Space Complexity To Functions
| function name       | Time complexity | Space complexity |
|---------------------|-----------------|------------------|
| insert              |  O(log n)       | O(log n)         |
| heapify_up          |  O(log n)       | O(1)             |
| search              |  O(n)           | O(log n)         |
| index_of            |  O(n)           | O(log n)         |
| find_node           |  O(n)           | O(log n)         |
| get_height          |  O(n)           | O(log n)         |
| find_last_node      |  O(n log n)     | O(log n)         |
| delete              |  O(n log n)     | O(log n)         |
| heapify_down        |  O(log n)       | O(1)             |
| for_each            |  O(n)           | O(1)             |
|convert_array_to_heap|  O(n log n)     | O(n)             |