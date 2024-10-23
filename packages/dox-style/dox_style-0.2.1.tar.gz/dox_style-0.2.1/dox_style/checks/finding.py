class Finding:
    NAME = "Finding"

    def __init__(self, file, line, **kwargs):
        self.file = file
        self.line = line

    def msg(self):
        return "<Missing description>"

    def excerpt_lines(self, n):
        lines = []
        try:
            with open(self.file, "r", encoding="utf-8") as rst_file:
                all_lines = rst_file.readlines()

            if self.line > len(all_lines):
                raise IndexError

            start = max(0, self.line - n - 1)
            end = min(len(all_lines), self.line + n)

            for i in range(start, end):
                lines.append((i + 1, all_lines[i]))

        except FileNotFoundError:
            lines = [(self.line, self.file)]
        except IndexError:
            lines = [(self.line, self.file)]
        return lines

    def as_str(self, show_excerpt=0):
        display = f"[{self.NAME}] {self.msg()}\n"
        if show_excerpt > 0:
            for i, line in self.excerpt_lines(show_excerpt):
                if i == self.line:
                    display += f"{i:3d} -> {line}"
                else:
                    display += f"{i:3d}:  {line}"
        return display
