import pytest
from pygments.token import Token
from shellconsole_lexer import ShellConsoleLexer
from git_lexer import GitStatusLexer

def test_git_show():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git show\n"
        "commit 8e702933d5dbec9ee71100a1599ae4491085e1aa\n"
        "Author: Author <author@localhost>\n"
        "Date:   Fri Oct 13 16:06:59 2023 +0200\n"
        "\n"
        "    Added README.md\n"
        "\n"
        "diff --git a/README.md b/README.md\n"
        "new file mode 100644\n"
        "index 0000000..6d747b3\n"
        "--- /dev/null\n"
        "+++ b/README.md\n"
        "@@ -0,0 +1,2 @@\n"
        "+Addition\n"
        "-Deletion\n"
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
            (Token.Git.Show.Header, "commit 8e702933d5dbec9ee71100a1599ae4491085e1aa"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Author: Author <author@localhost>\n"),
            (Token.Generic.Output, "Date:   Fri Oct 13 16:06:59 2023 +0200\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "    Added README.md\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Heading, "diff --git a/README.md b/README.md"),
            (Token.Text.Whitespace, "\n"),
            (Token.Text, "new file mode 100644"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Heading, "index 0000000..6d747b3"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Deleted, "--- /dev/null"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Inserted, "+++ b/README.md"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Subheading, "@@ -0,0 +1,2 @@"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Inserted, "+Addition"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Deleted, "-Deletion"),
            (Token.Text.Whitespace, "\n"),
    ]

def test_git_show_with_refs():
    lexer = ShellConsoleLexer()
    text = (
        "user@host:~/directory (main) $ git show\n"
        "commit 8e702933d5dbec9ee71100a1599ae4491085e1aa (HEAD -> main, tag: v1, origin/main, origin/HEAD)\n"
        "Author: Author <author@localhost>\n"
        "Date:   Fri Oct 13 16:06:59 2023 +0200\n"
        "\n"
        "    Added README.md\n"
        "\n"
        "diff --git a/README.md b/README.md\n"
        "new file mode 100644\n"
        "index 0000000..6d747b3\n"
        "--- /dev/null\n"
        "+++ b/README.md\n"
        "@@ -0,0 +1,2 @@\n"
        "+Addition\n"
        "-Deletion\n"
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
            (Token.Git.Show.Header, "commit 8e702933d5dbec9ee71100a1599ae4491085e1aa"),
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
            (Token.Git.Show.Header, ","),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs.RemoteBranch, "origin/main"),
            (Token.Git.Show.Header, ","),
            (Token.Text.Whitespace, " "),
            (Token.Git.Refs.RemoteHead, "origin/HEAD"),
            (Token.Git.Show.Header, ")"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "Author: Author <author@localhost>\n"),
            (Token.Generic.Output, "Date:   Fri Oct 13 16:06:59 2023 +0200\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Output, "    Added README.md\n"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Heading, "diff --git a/README.md b/README.md"),
            (Token.Text.Whitespace, "\n"),
            (Token.Text, "new file mode 100644"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Heading, "index 0000000..6d747b3"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Deleted, "--- /dev/null"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Inserted, "+++ b/README.md"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Subheading, "@@ -0,0 +1,2 @@"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Inserted, "+Addition"),
            (Token.Text.Whitespace, "\n"),
            (Token.Generic.Deleted, "-Deletion"),
            (Token.Text.Whitespace, "\n"),
    ]
