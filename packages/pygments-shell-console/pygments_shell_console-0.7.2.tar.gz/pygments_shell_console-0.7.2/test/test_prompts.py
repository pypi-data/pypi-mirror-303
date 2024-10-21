import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer

def test_basic_bash_prompt():
    lexer = ShellConsoleLexer()
    prompt = "user@host:~$"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~"),
            (Token.Generic.Prompt, "$\n"),
    ]

def test_basic_bash_prompt_with_space():
    lexer = ShellConsoleLexer()
    prompt = "user@host:~ $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]

def test_bash_prompt_with_git_branch():
    lexer = ShellConsoleLexer()
    prompt = "user@host:~/project (main) $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]

def test_bash_prompt_with_virtualenv():
    lexer = ShellConsoleLexer()
    prompt = "(venv) user@host:~/project $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.VirtualEnv, "(venv)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]

def test_bash_prompt_with_virtualenv_and_git_branch():
    lexer = ShellConsoleLexer()
    prompt = "(venv) user@host:~/project (main) $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.VirtualEnv, "(venv)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]
def test_bracketed_bash_prompt():
    lexer = ShellConsoleLexer()
    prompt = "[user@host:~/project] $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt, "["),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt, "]"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]

def test_bracketed_bash_prompt_with_git_branch():
    lexer = ShellConsoleLexer()
    prompt = "[user@host:~/project (main)] $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt, "["),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt, "]"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]

def test_bracketed_bash_prompt_with_virtualenv():
    lexer = ShellConsoleLexer()
    prompt = "(venv) [user@host:~/project] $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.VirtualEnv, "(venv)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "["),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt, "]"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]

def test_bash_prompt_with_virtualenv_and_git_branch_and_command():
    lexer = ShellConsoleLexer()
    prompt = "(venv) user@host:~/project (main) $ echo 'Hello world!'\n"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.VirtualEnv, "(venv)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Name.Builtin, "echo"),
            (Token.Text.Whitespace, " "),
            (Token.Literal.String.Single, "'Hello world!'"),
            (Token.Text.Whitespace, "\n"),
    ]

def test_bash_prompt_with_virtualenv_and_git_branch_and_command_backslash():
    lexer = ShellConsoleLexer()
    prompt = (
        "(venv) user@host:~/project (main) $ echo 'Hello world!' && \\\n"
        "cd /tmp\n"
    )

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.VirtualEnv, "(venv)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Name.Builtin, "echo"),
            (Token.Text.Whitespace, " "),
            (Token.Literal.String.Single, "'Hello world!'"),
            (Token.Text.Whitespace, " "),
            (Token.Operator, "&&"),
            (Token.Text.Whitespace, " "),
            (Token.Literal.String.Escape, "\\\n"),
            (Token.Name.Builtin, "cd"),
            (Token.Text.Whitespace, " "),
            (Token.Text, "/tmp"),
            (Token.Text.Whitespace, "\n"),
    ]

def test_bash_prompt_with_virtualenv_and_git_branch_and_command_output():
    lexer = ShellConsoleLexer()
    prompt = (
        "(venv) user@host:~/project (main) $ echo 'Hello world!'\n"
        "Hello world!\n"
    )

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.VirtualEnv, "(venv)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.UserHost, "user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt.GitBranch, "(main)"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Name.Builtin, "echo"),
            (Token.Text.Whitespace, " "),
            (Token.Literal.String.Single, "'Hello world!'"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Hello world!\n"),
    ]

def test_bash_prompt_with_spaces():
    lexer = ShellConsoleLexer()
    prompt = "Fri Sep 13 09:30:00 user@host:~/project $"

    tokens = list(lexer.get_tokens(prompt))

    assert tokens == [
            (Token.Generic.Prompt.UserHost, "Fri Sep 13 09:30:00 user@host"),
            (Token.Generic.Prompt, ":"),
            (Token.Generic.Prompt.Directory, "~/project"),
            (Token.Generic.Prompt.Whitespace, " "),
            (Token.Generic.Prompt, "$\n"),
    ]
