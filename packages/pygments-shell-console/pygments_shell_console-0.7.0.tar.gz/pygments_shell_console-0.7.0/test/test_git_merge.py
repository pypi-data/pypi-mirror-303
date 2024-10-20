import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer

def test_git_stash_show():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git stash show\n"
        " README.md | 2 ++--\n"
        " 1 file changed, 2 insertions(+)\n"
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
            (Token.Text, "stash"),
            (Token.Text.Whitespace, " "),
            (Token.Text, "show"),
            (Token.Text.Whitespace, "\n"),
            # First line
            (Token.Generic.Output, " README.md | 2 "),
            (Token.Generic.Inserted, "++"),
            (Token.Generic.Deleted, "--"),
            (Token.Text.Whitespace, "\n"),
            # Second line
            (Token.Generic.Output, " 1 file changed, 2 insertions(+)\n"),
    ]
