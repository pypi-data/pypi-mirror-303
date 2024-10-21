import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer
from git_lexer import GitPrettyLogLexer

def test_full_git_log():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git lga\n"
        "* f853946 - (7 minutes ago) README: Afegits autors - Mar (origin/feature/author)\n"
        "| * cc8c388 - (9 minutes ago) LICENSE: Afegida llicència - Pau (origin/feature/license)\n"
        "* | 9e34bb0 - (15 minutes ago) README: Afegida descripció del projecte - Anna (HEAD -> develop, origin/develop, feature/readme, origin/feature/readme)\n"
        "|/\n"
        "* 0fb88ef - (29 minutes ago) 1. Primer commit - Joan Puigcerver (origin/main, origin/HEAD, main)\n"
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
            (Token.Text, "lga"),
            (Token.Text.Whitespace, "\n"),
            # First commit
            (Token.Generic.Output, "*",),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "f853946"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(7 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "README: Afegits autors"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Mar"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs, "(origin/feature/author)"),
            (Token.Text.Whitespace, "\n"),
            # Second commit
            (Token.Git.BranchLine, "| "),
            (Token.Generic.Output, "*"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "cc8c388"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(9 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "LICENSE: Afegida llicència"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Pau"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs, "(origin/feature/license)"),
            (Token.Text.Whitespace, "\n"),
            # Third commit
            (Token.Generic.Output, "*"),
            (Token.Git.BranchLine, " |"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "9e34bb0"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(15 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "README: Afegida descripció del projecte"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Anna"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs, "(HEAD -> develop, origin/develop, feature/readme, origin/feature/readme)"),
            (Token.Text.Whitespace, "\n"),
            # Branch line
            (Token.Git.BranchLine, "|/\n"),
            # Fourth commit
            (Token.Generic.Output, "*"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "0fb88ef"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(29 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "1. Primer commit"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Joan Puigcerver"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs, "(origin/main, origin/HEAD, main)"),
            (Token.Text.Whitespace, "\n"),
    ]

def test_git_log_with_other_command():

    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git lga\n"
        "* f853946 - (7 minutes ago) README: Afegits autors - Mar (origin/feature/author)\n"
        "(venv) [user@host ~ (main)] $ echo 'Hello, world!'\n"
    )

    tokens = list(lexer.get_tokens(text))

    assert tokens == [
            # First command
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
            (Token.Text, "lga"),
            (Token.Text.Whitespace, "\n"),
            # First commit
            (Token.Generic.Output, "*",),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "f853946"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(7 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "README: Afegits autors"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Mar"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs, "(origin/feature/author)"),
            (Token.Text.Whitespace, "\n"),
            # Second command
            (Token.Generic.Prompt.VirtualEnv, "(venv)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "["),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.Directory, "~"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt, "]"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Name.Builtin, "echo"),
            (Token.Text.Whitespace, " "),
            (Token.Literal.String.Single, "'Hello, world!'"),
            (Token.Text.Whitespace, "\n"),
    ]

def test_simple_git_log():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git lg\n"
        "* f853946 - (7 minutes ago) README: Afegits autors - Mar (main)\n"
        "* 0fb88ef - (29 minutes ago) 1. Primer commit - Joan Puigcerver"
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
            (Token.Text, "lg"),
            (Token.Text.Whitespace, "\n"),
            # First commit
            (Token.Generic.Output, "*",),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "f853946"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(7 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "README: Afegits autors"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Mar"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs, "(main)"),
            (Token.Text.Whitespace, "\n"),
            # Second commit
            (Token.Generic.Output, "*"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "0fb88ef"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(29 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "1. Primer commit"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Joan Puigcerver"),
            (Token.Text.Whitespace, "\n"),
    ]

def test_git_log_with_commit_message_commas():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git lg\n"
        "* f853946 - (7 minutes ago) README: Afegits autors - Mar (main)\n"
        "* 0fb88ef - (29 minutes ago) Canvis A, B i C - Joan Puigcerver"
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
            (Token.Text, "lg"),
            (Token.Text.Whitespace, "\n"),
            # First commit
            (Token.Generic.Output, "*",),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "f853946"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(7 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "README: Afegits autors"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Mar"),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs, "(main)"),
            (Token.Text.Whitespace, "\n"),
            # Second commit
            (Token.Generic.Output, "*"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitHash, "0fb88ef"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitDate, "(29 minutes ago)"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitMessage, "Canvis A, B i C"),
            (Token.Text.Whitespace, " "),
            (Token.Generic.Output, "-"),
            (Token.Text.Whitespace, " "),
            (Token.Git.CommitAuthor, "Joan Puigcerver"),
            (Token.Text.Whitespace, "\n"),
    ]
