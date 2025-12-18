# 🚀 Geo Isolation Tool Using UserData (Softimage / Maya Style)

Let’s get started! This tool recreates the **Isolate Selection** behavior from **Softimage** and **Maya** in **Houdini**, but with a twist: it uses **each node's `userData`** to store previous visibility states instead of global session variables. This makes the tool safer and avoids session-wide variables.


## 📦 What does this tool do?

* Toggles isolation mode for selected nodes under `/obj`.
* Stores each node's previous display state in `userData`.
* Restores the previous visibility state when exiting isolation.
* Works on all object nodes under `/obj`.
* Can be mapped to a hotkey for quick workflow.


## ✨ Features

* Toggle-based isolate tool
* Stores previous visibility in node `userData`
* No global session variables needed
* Works on all nodes under `/obj`
* Mimics Maya / Softimage isolate selection
* Ideal for hotkeys and shelf tools


## 💡 Recommended usage

* Perfect for quick object isolation during modeling, rigging, or lookdev.
* Assign to a shelf tool or hotkey for maximum efficiency.
* Safely isolates objects without affecting other nodes’ session data.


## ⚠️ Notes & limitations

* Works only at the **OBJ (geometry) level**.
* Can be extended to include other node types by modifying the filter.
* The isolation state is saved per node and does not persist across Houdini sessions unless the scene is saved.
