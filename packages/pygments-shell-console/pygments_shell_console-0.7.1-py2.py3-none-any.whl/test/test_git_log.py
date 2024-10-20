import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer
from git_lexer import GitStatusLexer

def test_git_show():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git show\n"
        "commit c9fc6c856c2d52744b85a6f8d92feac496e60bd6 (HEAD -> main, tag: v1)\n"
        "Author: Author <author@localhost>\n"
        "Date:   Mon Oct 16 11:43:20 2023 +0200\n"
        "\n"
        "    Added another line to README.md\n"
        "\n"
        "commit 8e702933d5dbec9ee71100a1599ae4491085e1aa\n"
        "Author: Author <author@localhost>\n"
        "Date:   Fri Oct 13 16:06:59 2023 +0200\n"
        "\n"
        "    Added README.md\n"
)

    tokens = list(lexer.get_tokens(text))

    assert tokens == [
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/directory"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Text, "git"),
            (Token.Text.Whitespace, " "),
            (Token.Text, "show"),
            (Token.Text.Whitespace, "\n"),
            # First commit
            (Token.Git.Show.Header, "commit c9fc6c856c2d52744b85a6f8d92feac496e60bd6"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Show.Header, "("),
            (Token.Git.Refs.Head, "HEAD"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Show.Header, "->"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs.Branch, "main"),
            (Token.Git.Show.Header, ","),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs.Tag, "tag: v1"),
            (Token.Git.Show.Header, ")"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Author: Author <author@localhost>\n"),
            (Token.Generic.Output, "Date:   Mon Oct 16 11:43:20 2023 +0200\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "    Added another line to README.md\n"),
            (Token.Text.Whitespace, "\n"),
            # Second commit
            (Token.Git.Show.Header, "commit 8e702933d5dbec9ee71100a1599ae4491085e1aa"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Author: Author <author@localhost>\n"),
            (Token.Generic.Output, "Date:   Fri Oct 13 16:06:59 2023 +0200\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "    Added README.md\n"),
    ]
