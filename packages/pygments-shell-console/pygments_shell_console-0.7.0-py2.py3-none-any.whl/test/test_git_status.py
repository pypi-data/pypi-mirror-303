import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer
from git_lexer import GitStatusLexer

def test_git_status_modified():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git status\n"
        "On branch main\n"
        "\n"
        "Changes not staged for commit:\n"
        "  (use \"git add <file>...\" to update what will be committed)\n"
        "  (use \"git restore <file>...\" to discard changes in working directory)\n"
        "        modified:   README.md\n"
        "\n"
        "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n"
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
        (Token.Text, "status"),
        (Token.Text.Whitespace, "\n"),
        # Status
        (Token.Generic.Output, "On branch main\n"),
        (Token.Text.Whitespace, "\n"),
        (Token.Generic.Output, "Changes not staged for commit:\n"),
        (Token.Generic.Output, "  (use \"git add <file>...\" to update what will be committed)\n"),
        (Token.Generic.Output, "  (use \"git restore <file>...\" to discard changes in working directory)\n"),
        (Token.Text.Whitespace, "        "),
        (Token.Git.Modified, "modified:   README.md"),
        (Token.Text.Whitespace, "\n"),
        (Token.Text.Whitespace, "\n"),
        (Token.Generic.Output, "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n"),
    ]


def test_full_git_status():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git status\n"
        "On branch main\n"
        "\n"
        "No commits yet\n"
        "\n"
        "Untracked files:\n"
        "  (use \"git add <file>...\" to include in what will be committed)\n"
        "        README.md\n"
        "\n"
        "Changes not staged for commit:\n"
        "  (use \"git add <file>...\" to update what will be committed)\n"
        "  (use \"git restore <file>...\" to discard changes in working directory)\n"
        "        deleted:    README.md\n"
        "        modified:   mkdocs.yml\n"
        "        modified:   requirements.txt\n"
        "\n"
        "Changes to be committed:\n"
        "  (use \"git rm --cached <file>...\" to unstage)\n"
        "        new file:   README.md\n"
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
            (Token.Text, "status"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "On branch main\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "No commits yet\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Untracked files:\n"),
            (Token.Generic.Output, "  (use \"git add <file>...\" to include in what will be committed)\n"),
            (Token.Text.Whitespace, "        "),
            (Token.Git.Untracked, "README.md"),
            (Token.Text.Whitespace, "\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Changes not staged for commit:\n"),
            (Token.Generic.Output, "  (use \"git add <file>...\" to update what will be committed)\n"),
            (Token.Generic.Output, "  (use \"git restore <file>...\" to discard changes in working directory)\n"),
            (Token.Text.Whitespace, "        "),
            (Token.Git.Modified, "deleted:    README.md"),
            (Token.Text.Whitespace, "\n"),
            (Token.Text.Whitespace, "        "),
            (Token.Git.Modified, "modified:   mkdocs.yml"),
            (Token.Text.Whitespace, "\n"),
            (Token.Text.Whitespace, "        "),
            (Token.Git.Modified, "modified:   requirements.txt"),
            (Token.Text.Whitespace, "\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Changes to be committed:\n"),
            (Token.Generic.Output, "  (use \"git rm --cached <file>...\" to unstage)\n"),
            (Token.Text.Whitespace, "        "),
            (Token.Git.Staged, "new file:   README.md"),
            (Token.Text.Whitespace, "\n"),
    ]

def test_git_status_after_empty_command():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git add README.md\n"
        "user@host:~/directory (main) $ git status\n"
        "On branch main\n"
        "\n"
        "Changes not staged for commit:\n"
        "  (use \"git add <file>...\" to update what will be committed)\n"
        "  (use \"git restore <file>...\" to discard changes in working directory)\n"
        "        modified:   README.md\n"
        "\n"
        "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n"
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
        (Token.Text, "add"),
        (Token.Text.Whitespace, " "),
        (Token.Text, "README.md"),
        (Token.Text.Whitespace, "\n"),
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
        (Token.Text, "status"),
        (Token.Text.Whitespace, "\n"),
        # Status
        (Token.Generic.Output, "On branch main\n"),
        (Token.Text.Whitespace, "\n"),
        (Token.Generic.Output, "Changes not staged for commit:\n"),
        (Token.Generic.Output, "  (use \"git add <file>...\" to update what will be committed)\n"),
        (Token.Generic.Output, "  (use \"git restore <file>...\" to discard changes in working directory)\n"),
        (Token.Text.Whitespace, "        "),
        (Token.Git.Modified, "modified:   README.md"),
        (Token.Text.Whitespace, "\n"),
        (Token.Text.Whitespace, "\n"),
        (Token.Generic.Output, "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n"),
    ]

def test_git_status_whit_hint():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git status\n"
        "hint: You've added another git status command\n"
        "On branch main\n"
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
        (Token.Text, "status"),
        (Token.Text.Whitespace, "\n"),
        (Token.Git.Hint, "hint: You've added another git status command\n"),
        (Token.Generic.Output, "On branch main\n"),
    ]

def test_git_status_unmerged():
        lexer = ShellConsoleLexer()
        text = (
            "user@host:~/directory (main) $ git status\n"
            "On branch main\n"
            "You have unmerged paths.\n"
            "  (fix conflicts and run \"git commit\")\n"
            "  (use \"git merge --abort\" to abort the merge)\n"
            "\n"
            "Unmerged paths:\n"
            "  (use \"git restore --staged <file>...\" to unstage)\n"
            "  (use \"git add <file>...\" to mark resolution)\n"
            "        both modified:   README.md\n"
            "\n"
            "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n"
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
            (Token.Text, "status"),
            (Token.Text.Whitespace, "\n"),
            # Output
            (Token.Generic.Output, "On branch main\n"),
            (Token.Generic.Output, "You have unmerged paths.\n"),
            (Token.Generic.Output, "  (fix conflicts and run \"git commit\")\n"),
            (Token.Generic.Output, "  (use \"git merge --abort\" to abort the merge)\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Unmerged paths:\n"),
            (Token.Generic.Output, "  (use \"git restore --staged <file>...\" to unstage)\n"),
            (Token.Generic.Output, "  (use \"git add <file>...\" to mark resolution)\n"),
            (Token.Text.Whitespace, "        "),
            (Token.Git.Unmerged, "both modified:   README.md"),
            (Token.Text.Whitespace, "\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "no changes added to commit (use \"git add\" and/or \"git commit -a\")\n"),
        ]
