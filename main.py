from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")

# The same path where the main.py file is
NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")
DEFAULT_MESSAGE = "No notes yet."

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        # Create the file if not exists
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str) -> str:
    # It is important to always add documentation to your functions so the mcp server knows what the tool does
    """
    Explain:
        Append a new note to the sticky note file.
    Args:
        message (str): The note content to be added
    Returns:
        str: Confirmation message indicating the note was saved.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f: # Parameter "a" stands for "append"
        f.write(message + "\n")
    return "Note saved!"

@mcp.tool()
def read_notes() -> str:
    """
    Explain:
        Read and return all notes from the sticky note file.
    Returns:
        str: All the nots as a single string separated by line breaks.
            If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or DEFAULT_MESSAGE # If content is empty, a default message will return

@mcp.tool()
def remove_notes() -> str:
    """
    Explain: 
        Remove all the notes from the sticky note file.
    Returns:
        str: Confirmation message indicating all the notes was deleted.
    """
    ensure_file()
    with open(NOTES_FILE, "w") as f:
        f.write("")  # Writing an empty string to clear the content
    return "Notes removed!"

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Explain:
        Get the most recently added note from the sticky note file.
    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else DEFAULT_MESSAGE # Returns the last line if and if it is empty, a default message will return

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Explain: 
        Generate a prompt asking the AI to summarize all current notes.
    Returns:
        str: A prompt string that includes all notes and asks for a summary.
            If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return DEFAULT_MESSAGE
    return f"Summarize the current notes: {content}"