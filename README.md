# 📝 AI Sticky Notes – MCP Project

This project is a simple and functional application that uses the **MCP (Model Context Protocol)** to create a sticky notes system powered by AI. It leverages `FastMCP`, the `mcp[cli]` interface, and integrates with **Claude Desktop**.

---

## 🚀 Features

- Add new notes
- Read all existing notes
- Remove all notes
- Retrieve the latest note
- Generate a prompt to summarize all notes

---

## 🧰 Technologies Used

- Python
- FastMCP
- `uv` for environment management
- Claude Desktop for execution with tools, resources, and prompts

---

## 🛠️ Setup and Usage

### 1. Create and initialize the MCP environment

```bash
uv install
uv init project-folder-name
cd project-folder-name
uv add "mcp[cli]"
```

### 2. Install and use Claude Desktop

- Download and install **Claude Desktop**
- Run and interact with the defined tools, resources, and prompts

---

## 📁 File Overview

### `main.py`

This file contains all the tools and logic to manage notes using the MCP framework.

---

## 🔧 Tools

### `add_note(message: str) -> str`
Appends a new note to the `notes.txt` file.

### `read_notes() -> str`
Returns all saved notes. If no notes exist, returns a default message.

### `remove_notes() -> str`
Clears all notes in the `notes.txt` file.

---

## 🔗 Resource

### `get_latest_note() -> str`
Returns the most recently added note.

---

## 💬 Prompt

### `note_summary_prompt() -> str`
Generates a prompt asking the AI to summarize all current notes.

---

## 📄 Notes File

All notes are stored in a local `notes.txt` file, which is automatically created if it doesn't exist.

---

## ✅ Requirements

- Python 3.10+
- `uv` installed
- Claude Desktop installed

---

## 🧠 Inspiration

This project demonstrates how to use **MCP** to build intelligent agents that interact with local files and structured data. It’s easily extendable with new functionalities.

---
