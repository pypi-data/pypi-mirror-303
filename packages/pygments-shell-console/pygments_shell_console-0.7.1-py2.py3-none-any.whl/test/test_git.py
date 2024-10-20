import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer
from git_lexer import GitStatusLexer

def test_git_command_with_hint():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git branch -d desc\n"
        "error: the branch 'desc' is not fully merged.\n"
        "hint: If you are sure you want to delete it, run 'git branch -D desc'.\n"
        "hint: Disable this message with \"git config advice.forceDeleteBranch false\".\n"
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
        (Token.Text.Whitespace, " "),
        (Token.Text, "-d"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "desc"),
        (Token.Text.Whitespace, "\n"),
        # Output
        (Token.Git.Error, "error: the branch 'desc' is not fully merged.\n"),
        (Token.Git.Hint, "hint: If you are sure you want to delete it, run 'git branch -D desc'.\n"),
        (Token.Git.Hint, "hint: Disable this message with \"git config advice.forceDeleteBranch false\".\n"),
    ]

def test_git_command_with_empty_hint():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory $ git init\n"
        "hint: Using 'master' as the name for the initial branch. This default branch name\n"
        "hint: is subject to change. To configure the initial branch name to use in all\n"
        "hint: of your new repositories, which will suppress this warning, call:\n"
        "hint:\n"
        "hint:   git config --global init.defaultBranch <name>\n"

    )

    tokens = list(lexer.get_tokens(text))

    assert tokens == [
        # Prompt
        (Token.Generic.Prompt.UserHost, "user@host"),
        (Token.Generic.Prompt, ":"),
        (Token.Generic.Prompt.Directory, "~/directory"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Generic.Prompt, "$"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Text, "git"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "init"),
        (Token.Text.Whitespace, "\n"),
        # Output
        (Token.Git.Hint, "hint: Using 'master' as the name for the initial branch. This default branch name\n"),
        (Token.Git.Hint, "hint: is subject to change. To configure the initial branch name to use in all\n"),
        (Token.Git.Hint, "hint: of your new repositories, which will suppress this warning, call:\n"),
        (Token.Git.Hint, "hint:\n"),
        (Token.Git.Hint, "hint:   git config --global init.defaultBranch <name>\n"),
    ]

def test_git_command_with_warning():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory $ git push origin main\n"
        "warning: redirecting to url\n"
    )

    tokens = list(lexer.get_tokens(text))
    assert tokens == [
        # Prompt
        (Token.Generic.Prompt.UserHost, "user@host"),
        (Token.Generic.Prompt, ":"),
        (Token.Generic.Prompt.Directory, "~/directory"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Generic.Prompt, "$"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Text, "git"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "push"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "origin"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "main"),
        (Token.Text.Whitespace, "\n"),
        # Output
        (Token.Git.Warning, "warning: redirecting to url\n"),
    ]

def test_git_command_with_error():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory $ git push origin main\n"
        "error: src refspec main does not match any.\n"
    )

    tokens = list(lexer.get_tokens(text))
    assert tokens == [
        # Prompt
        (Token.Generic.Prompt.UserHost, "user@host"),
        (Token.Generic.Prompt, ":"),
        (Token.Generic.Prompt.Directory, "~/directory"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Generic.Prompt, "$"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Text, "git"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "push"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "origin"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "main"),
        (Token.Text.Whitespace, "\n"),
        # Output
        (Token.Git.Error, "error: src refspec main does not match any.\n"),
    ]

def test_git_command_with_fatal():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory $ git push origin main\n"
        "fatal: src refspec main does not match any.\n"
    )

    tokens = list(lexer.get_tokens(text))
    assert tokens == [
        # Prompt
        (Token.Generic.Prompt.UserHost, "user@host"),
        (Token.Generic.Prompt, ":"),
        (Token.Generic.Prompt.Directory, "~/directory"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Generic.Prompt, "$"),
        (Token.Generic.Prompt.Whitespace, " "),
        (Token.Text, "git"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "push"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "origin"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "main"),
        (Token.Text.Whitespace, "\n"),
        # Output
        (Token.Git.Fatal, "fatal: src refspec main does not match any.\n"),
    ]
