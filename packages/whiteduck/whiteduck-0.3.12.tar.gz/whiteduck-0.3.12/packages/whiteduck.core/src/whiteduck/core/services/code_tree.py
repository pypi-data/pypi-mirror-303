import ast
import os


class CodeTreeClass:
    def __init__(self, name):
        self.name = name
        self.called_by = []
        self.calls = []

    def __repr__(self):
        return f"CodeTreeClass(name={self.name}, called_by={self.called_by}, calls={self.calls})"


class CodeTree:
    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.classes = []

    def _is_included(self, path, include_filter=None, exclude_filter=None):
        """
        Helper function to check if a file/folder is included based on filters.
        """
        if include_filter and not any(inc in path for inc in include_filter):
            return False
        if exclude_filter and any(exc in path for exc in exclude_filter):
            return False
        return True

    def _print_tree(self, folder, indent="", include_filter=None, exclude_filter=None):
        """
        Helper function to recursively print the directory structure.
        """
        # List all files and directories in the current folder
        try:
            items = sorted(os.listdir(folder))
        except OSError as e:
            print(f"Error accessing folder: {folder}, {e}")
            return

        for i, item in enumerate(items):
            path = os.path.join(folder, item)
            if not self._is_included(path, include_filter, exclude_filter):
                continue

            # Determine if this is the last item in the current directory
            is_last = i == len(items) - 1

            if os.path.isdir(path):
                # Print the folder name and recurse
                print(f"{indent}{'└── ' if is_last else '├── '}{item}/")
                new_indent = indent + ("    " if is_last else "│   ")
                self._print_tree(path, new_indent, include_filter, exclude_filter)
            else:
                # Print the file name
                print(f"{indent}{'└── ' if is_last else '├── '}{item}")

    def visualize_file_tree(self, include_filter=None, exclude_filter=None):
        """
        Visualizes the file tree starting from the root folder, with optional inclusion and exclusion filters.
        """
        self._print_tree(self.root_folder, include_filter=include_filter, exclude_filter=exclude_filter)

    def visualize_syntax_tree(self, file_path):
        """
        Parses a Python file and visualizes its abstract syntax tree (AST).
        """
        if not file_path.endswith(".py"):
            print(f"Error: {file_path} is not a Python (.py) file")
            return

        try:
            with open(file_path, "r") as f:
                source_code = f.read()
        except Exception as e:
            print(f"Error reading file: {file_path}, {e}")
            return

        try:
            tree = ast.parse(source_code, filename=file_path)
            print(ast.dump(tree, indent=4))
        except SyntaxError as e:
            print(f"Syntax error in {file_path}: {e}")

    def visualize_syntax_trees_in_folder(self):
        """
        Visualizes syntax trees for all Python files in the folder tree.
        """
        for foldername, _, filenames in os.walk(self.root_folder):
            for filename in filenames:
                if filename.endswith(".py"):
                    file_path = os.path.join(foldername, filename)
                    print(f"Syntax Tree for {file_path}:")
                    self.visualize_syntax_tree(file_path)
                    print("-" * 40)

    def extract_classes(self):
        """
        Extracts all classes from the syntax tree of Python files within the root folder.
        """
        self.classes = []

        for foldername, _, filenames in os.walk(self.root_folder):
            for filename in filenames:
                if filename.endswith(".py"):
                    file_path = os.path.join(foldername, filename)
                    try:
                        with open(file_path, "r") as f:
                            source_code = f.read()
                        tree = ast.parse(source_code, filename=file_path)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.ClassDef):
                                self.classes.append(CodeTreeClass(name=node.name))
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")


# Example Usage:
# Let's assume that '/mock_project' is the root folder
code_tree = CodeTree("/mock_project")

# Visualize file tree with inclusion and exclusion filters
code_tree.visualize_file_tree(include_filter=[".py"], exclude_filter=["/tests"])

# Visualize syntax trees for all Python files in the folder tree
code_tree.visualize_syntax_trees_in_folder()

# Extract and get all CodeTreeClass instances
code_tree.extract_classes()
print(code_tree.classes)
