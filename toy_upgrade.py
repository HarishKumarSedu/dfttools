import sys
import tkinter as tk
from tkinter import scrolledtext, filedialog, simpledialog
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

        # Create main components
        self.create_code_editor()
        self.create_output_area()
        self.create_menu()

        # Redirect stdout to output area
        sys.stdout = RedirectText(self.output_area)

    def create_code_editor(self):
        """Create the code editor with syntax highlighting."""
        self.code_editor = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Courier", 12), bg="#17181a", fg="#D4D4D4"
        )
        self.code_editor.pack(expand=True, fill="both")
        self.code_editor.bind("<KeyRelease>", self.highlight_syntax)

    def create_output_area(self):
        """Create the output area for displaying print statements and errors."""
        self.output_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Courier", 12), height=10, bg="#252526", fg="#D4D4D4"
        )
        self.output_area.pack(expand=False, fill="x")

    def create_menu(self):
        """Create the menu bar with options for adding tests."""
        menu_bar = tk.Menu(self.root)

        # Add menu with Test option
        add_menu = tk.Menu(menu_bar, tearoff=0)
        add_menu.add_command(label="Test", command=self.add_test_box)
        menu_bar.add_cascade(label="Add", menu=add_menu)

        self.root.config(menu=menu_bar)

    def add_test_box(self):
        """Prompt for test name and create a new test box."""
        test_name = simpledialog.askstring("Test Name", "Enter the name of the test:")
        
        if test_name:
            # Create a frame for the test box
            frame = tk.Frame(self.root)
            frame.pack(pady=5)

            # Create a text area for the test code
            test_code_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=("Courier", 12), bg="#17181a", fg="#D4D4D4")
            test_code_box.pack(side=tk.LEFT)

            # Create buttons for compiling and saving the test code
            compile_button = tk.Button(frame, text="Compile",
                                       command=lambda: self.compile_test_code(test_code_box))
            compile_button.pack(side=tk.LEFT)

            execute_button = tk.Button(frame, text="Execute",
                                       command=lambda: self.execute_test_code(test_code_box))
            execute_button.pack(side=tk.LEFT)

            save_button = tk.Button(frame, text="Save Test",
                                    command=lambda: self.save_test_code(test_name, test_code_box))
            save_button.pack(side=tk.LEFT)

    def compile_test_code(self, test_code_box):
        """Compile code written in the test code box (syntax check)."""
        code = test_code_box.get("1.0", tk.END).strip()
        
        try:
            compile(code, "<string>", "exec")  # Compile the code to check for syntax errors
            print("Compilation successful.")  # Print success message
        except SyntaxError as e:
            print(f"Compilation Error: {e}")  # Print compilation error message

    def execute_test_code(self, test_code_box):
        """Execute code written in the test code box."""
        code = test_code_box.get("1.0", tk.END).strip()
        
        try:
            exec(code)  # Execute the code
            logging.info("Executed successfully.")
            print("Executed successfully.")  # Print success message
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")  # Print error message

    def save_test_code(self, test_name, test_code_box):
        """Save the code from the test box to a .py file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                   initialfile=f"{test_name}.py",
                                                   filetypes=[("Python files", "*.py")])
        
        if file_path:
            with open(file_path, "w") as file:
                content = test_code_box.get("1.0", tk.END)
                file.write(content)

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
        
        dragan_colors = {
             "keyword": "#45A9F9",
             "keyword_custom": "#FFD700",
             "string": "#FF75B5",
             "comment": "#46fc55",
             "number": "#FFA500",
             "boolean": "#C586C0",
             "constant": "#924cee"
         }
         
        color = dragan_colors.get(tag_name,"black")
        # Add tag and configure it with a foreground color.
        self.code_editor.tag_add(tag_name,start_index,end_index)
        self.code_editor.tag_config(tag_name ,foreground=color)


if __name__ == "__main__":
    root = tk.Tk()
    ide = SimplePythonIDE(root)

    root.mainloop()
