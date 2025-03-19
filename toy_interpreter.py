import sys
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)])


class RedirectText:
    """Class to redirect stdout to a text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        """Write message to the text widget."""
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)  # Scroll to the end

    def flush(self):
        """Flush method for compatibility."""
        pass


class SimplePythonIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Dragan Theme Python IDE")

        # Create a text area for code input (with syntax highlighting)
        self.code_editor = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 12), bg="#17181a", fg="#D4D4D4")
        self.code_editor.pack(expand=True, fill="both")
        self.code_editor.bind("<KeyRelease>", self.highlight_syntax)  # Trigger syntax highlighting on key release

        # Redirect stdout to output area
        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 12), height=10, bg="#252526", fg="#D4D4D4")
        self.output_area.pack(expand=False, fill="x")
        sys.stdout = RedirectText(self.output_area)

        # Set cursor color based on background
        self.set_cursor_color()

        # Create menu bar
        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.code_editor.delete("1.0", tk.END)  # Clear current content
                self.code_editor.insert(tk.END, content)  # Insert new content

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                   filetypes=[("Python files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.code_editor.get("1.0", tk.END)
                file.write(content)

    def execute_code(self):
        """Execute the code written in the editor."""
        code = self.code_editor.get("1.0", tk.END).strip()
        
        try:
            exec(code)  # Execute the code
            logging.info("Executed successfully.")
            print("Executed successfully.")  # Print success message
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")  # Print error message

    def highlight_syntax(self, event=None):
        """Highlight syntax in the code editor using Pygments."""
        content = self.code_editor.get("1.0", tk.END)

        # Clear previous tags
        for tag in self.code_editor.tag_names():
            self.code_editor.tag_remove(tag, "1.0", tk.END)

        # Use Pygments lexer to tokenize the content
        lexer = PythonLexer()

        # Tokenize and apply colors based on token type
        for token_type, value in lex(content, lexer):
            line_number = content.count('\n', 0, content.index(value)) + 1
            column_start = content.index(value) - content.rfind('\n', 0, content.index(value)) - 1
            column_end = column_start + len(value)

            start_index = f"{line_number}.{column_start}"
            end_index = f"{line_number}.{column_end}"

            if token_type in Token.Keyword:
                if value in ["print", "in", "range", "list", "tuple", "dict"]:  # Custom keywords in yellow
                    self.apply_tag("keyword_custom", start_index, end_index)
                else:  # Standard keywords in light blue
                    self.apply_tag("keyword", start_index, end_index)
            elif token_type in Token.String:
                self.apply_tag("string", start_index, end_index)
            elif token_type in Token.Comment:
                self.apply_tag("comment", start_index, end_index)
            elif token_type in Token.Number:
                self.apply_tag("number", start_index, end_index)
            elif value in ("True", "False"):  # Booleans in red
                self.apply_tag("boolean", start_index, end_index)
            elif value == "None":  # None constant in red
                self.apply_tag("constant", start_index, end_index)

    def apply_tag(self, tag_name, start_index, end_index):
        """Apply color tags to specific text ranges."""
        
        # Define Dragan theme colors for syntax highlighting
        dragan_colors = {
            "keyword": "#45A9F9",       # Light Blue for standard keywords
            "keyword_custom": "#FFD700",# Yellow for specific keywords (print, in...)
            "string": "#FF75B5",         # Pink for strings
            "comment": "#46fc55",       # Green for comments
            "number": "#FFA500",         # Orange for numbers
            "boolean": "#C586C0",       # Red for booleans (True/False)
            "constant": "#C586C0"       # Purple for constants (None)
        }
        
        color = dragan_colors.get(tag_name, "black")

        # Add tag and configure it with a foreground color
        self.code_editor.tag_add(tag_name, start_index, end_index)
        self.code_editor.tag_config(tag_name, foreground=color)

    def set_cursor_color(self):
        """Set cursor color based on background color."""
        bg_color = "#17181a"  # Background color of code editor
        
        if bg_color == "#17181a":  # Dark background
            cursor_color = "white"
        else:                       # Light background (if applicable)
            cursor_color = "black"

        # Set cursor color using Tkinter's configuration (this may vary by platform)
        self.code_editor.config(insertbackground=cursor_color)


if __name__ == "__main__":
    root = tk.Tk()
    ide = SimplePythonIDE(root)

    # Add a button to execute code from the editor
    execute_button = tk.Button(root, text="Execute Code", command=ide.execute_code)
    execute_button.pack(side=tk.BOTTOM)

    root.mainloop()
