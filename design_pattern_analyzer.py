import os
import ast
import re
from collections import defaultdict

class DesignPatternAnalyzer:
    # Initialize the analyzer with the project path
    def __init__(self, project_path):
        self.project_path = project_path
        self.patterns = defaultdict(list)
        self.total_files_analyzed = 0

    # Scan Python files and check for supported design patterns
    def analyze(self):
        """Analyze all files in the project directory to identify design patterns."""
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py"):
                    self.total_files_analyzed += 1
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        file_content = f.read()
                        tree = ast.parse(file_content)
                        self._check_singleton(file_content, file_path)
                        self._check_factory(file_content, file_path)
                        self._check_decorator(file_content, file_path)
                        self._check_state(file_content, file_path)
                        self._check_strategy(tree, file_path)
                        self._check_abstract_factory(file_content, file_path)
                        self._check_adapter(file_content, file_path)
                        self._check_bridge(file_content, file_path)
                        self._check_builder(file_content, file_path)
                        self._check_chain_of_responsibility(file_content, file_path)
                        self._check_composite(file_content, file_path)
                        self._check_facade(file_content, file_path)
                        self._check_iterator(file_content, file_path)
                        self._check_prototype(file_content, file_path)
                        self._check_proxy(file_content, file_path)
                        self._check_template(file_content, file_path)
                        self._check_interpreter(file_content, file_path)

    # Check for Singleton pattern
    def _check_singleton(self, file_content, file_path):
        if re.search(r'__new__\s*\(cls\)', file_content):
            self.patterns["Singleton"].append(file_path)
        elif re.search(r'@classmethod\s+def\s+get_instance', file_content):
            self.patterns["Singleton"].append(file_path)

    # Check for Factory pattern
    def _check_factory(self, file_content, file_path):
        if re.search(r'class\s+[A-Za-z]+Factory', file_content):
            self.patterns["Factory"].append(file_path)
        elif re.search(r'def\s+create\w*', file_content):
            self.patterns["Factory"].append(file_path)

    # Check for Decorator pattern
    def _check_decorator(self, file_content, file_path):
        if re.search(r'@.*\s+def\s+', file_content):
            self.patterns["Decorator"].append(file_path)

    # Check for State pattern
    def _check_state(self, file_content, file_path):
        if re.search(r'class\s+[A-Za-z]+State', file_content):
            self.patterns["State"].append(file_path)
        elif re.search(r'change\s+state', file_content, re.IGNORECASE):
            self.patterns["State"].append(file_path)

    # Check for Strategy pattern
    def _check_strategy(self, tree, file_path):
        strategies = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and "strategy" in node.name.lower():
                strategies.add(node.name)
        if len(strategies) >= 2:
            self.patterns["Strategy"].append(file_path)

    # Check for Abstract Factory pattern
    def _check_abstract_factory(self, file_content, file_path):
        if re.search(r'abstract.*factory', file_content, re.IGNORECASE):
            self.patterns["Abstract Factory"].append(file_path)

    # Check for Adapter pattern
    def _check_adapter(self, file_content, file_path):
        if re.search(r'adapter', file_content, re.IGNORECASE):
            self.patterns["Adapter"].append(file_path)

    # Check for Bridge pattern
    def _check_bridge(self, file_content, file_path):
        if re.search(r'bridge', file_content, re.IGNORECASE):
            self.patterns["Bridge"].append(file_path)

    # Check for Builder pattern
    def _check_builder(self, file_content, file_path):
        if re.search(r'builder', file_content, re.IGNORECASE):
            self.patterns["Builder"].append(file_path)

    # Check for Chain of Responsibility pattern
    def _check_chain_of_responsibility(self, file_content, file_path):
        if re.search(r'chain.*responsibility', file_content, re.IGNORECASE):
            self.patterns["Chain of Responsibility"].append(file_path)

    # Check for Composite pattern
    def _check_composite(self, file_content, file_path):
        if re.search(r'composite', file_content, re.IGNORECASE):
            self.patterns["Composite"].append(file_path)

    # Check for Facade pattern
    def _check_facade(self, file_content, file_path):
        if re.search(r'facade', file_content, re.IGNORECASE):
            self.patterns["Facade"].append(file_path)

    # Check for Iterator pattern
    def _check_iterator(self, file_content, file_path):
        if re.search(r'iterator', file_content, re.IGNORECASE):
            self.patterns["Iterator"].append(file_path)

    # Check for Prototype pattern
    def _check_prototype(self, file_content, file_path):
        if re.search(r'prototype', file_content, re.IGNORECASE):
            self.patterns["Prototype"].append(file_path)

    # Check for Proxy pattern
    def _check_proxy(self, file_content, file_path):
        if re.search(r'proxy', file_content, re.IGNORECASE):
            self.patterns["Proxy"].append(file_path)

    # Check for Template pattern
    def _check_template(self, file_content, file_path):
        if re.search(r'template', file_content, re.IGNORECASE):
            self.patterns["Template"].append(file_path)

    # Check for Interpreter pattern
    def _check_interpreter(self, file_content, file_path):
        if re.search(r'interpreter', file_content, re.IGNORECASE):
            self.patterns["Interpreter"].append(file_path)

    def print_results(self):
        """Display results of the design pattern analysis."""
        if not self.patterns:
            print("No design patterns were detected.")
        else:
            total_patterns = 0
            for pattern, files in self.patterns.items():
                count = len(files)
                total_patterns += count
                print(f"\nDetected {pattern} pattern in {count} files:")
                for file in files:
                    print(f"  - {file}")
            print(f"\nTotal design patterns detected: {total_patterns}")
        print(f"Total files analyzed: {self.total_files_analyzed}")

# Example usage:
project_path = "/Users/Documents/python/circle_apis"
analyzer = DesignPatternAnalyzer(project_path)
analyzer.analyze()
analyzer.print_results()
