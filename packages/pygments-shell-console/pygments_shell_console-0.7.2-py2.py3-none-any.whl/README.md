# Pygments Shell Console
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![PyPi](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/pygments-shell-console/)

This Pygments plugin adds new lexers for `shellconsole` output.

The lexers are:
- `ShellConsoleLexer`: Based in [`ShellSessionBaseLexer`](https://github.com/pygments/pygments/blob/master/pygments/lexers/shell.py#L151C7-L151C28),
    extends its behavior to recognize the prompt elements and highlight them.

    Also, it adds support for highlighting the following commands output:
    - Uses `DiffLexer` to highlight `diff` and `git diff` output.
    - `GitStatusLexer`: Adds support for highlighting `git status` output.
    - `GitShowLexer`: Adds support for highlighting `git show` output.
    - `GitLogLexer`: Adds support for highlighting `git log` output.
    - `GitPrettyLogLexer`: Adds support for highlighting `git log` output, following the format:
        ```
        log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
        ```

Examples of the result can be found [here](https://joapuiib.github.io/mkdocs-material-joapuiib/features/code_blocks/#shell-block).
