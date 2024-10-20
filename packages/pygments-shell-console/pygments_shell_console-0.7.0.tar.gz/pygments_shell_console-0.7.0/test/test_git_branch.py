import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer
from git_lexer import GitStatusLexer

def test_git_branch():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git branch\n"
        "* main\n"
        "  desc\n"
    )

    tokens = list(lexer.get_tokens(text))

    assert tokens == [
        # Prompt
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
        (Token.Text, "branch"),
        (Token.Text.Whitespace, "\n"),
        # Output
        (Token.Generic.Output, "* "),
        (Token.Git.Refs.Branch, "main"),
        (Token.Text.Whitespace, "\n"),
        (Token.Generic.Output, "  desc\n"),
    ]
