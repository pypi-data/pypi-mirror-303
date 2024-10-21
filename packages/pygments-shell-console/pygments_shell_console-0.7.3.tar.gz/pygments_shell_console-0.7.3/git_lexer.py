"""An example plugin lexer for Pygments."""

from pygments.lexer import Lexer
from pygments.lexer import RegexLexer, ExtendedRegexLexer, include, bygroups, \
    default, using, line_re, do_insertions, inherit
from pygments.token import Token, Punctuation, Whitespace, \
    Text, Comment, Operator, Keyword, Name, String, Number, Generic
from pygments.lexers.diff import DiffLexer
from pygments.token import STANDARD_TYPES

import re

__all__ = [
    'GitLexer',
    'GitStatusLexer',
    'GitPrettyLogLexer',
    'GitLogLexer',
    'GitShowLexer',
]

STANDARD_TYPES.update({
    Token.Git: 'git',
    Token.Git.BranchLine: 'git-bl',
    Token.Git.CommitHash: 'git-ch',
    Token.Git.CommitDate: 'git-cd',
    Token.Git.CommitMessage: 'git-cm',
    Token.Git.CommitAuthor: 'git-ca',
    Token.Git.Hint: 'git-hint',
    Token.Git.Warning: 'git-warning',
    Token.Git.Error: 'git-error',
    Token.Git.Fatal: 'git-fatal',
    Token.Git.Refs: 'git-r',
    Token.Git.Untracked: 'git-untr',
    Token.Git.Modified: 'git-mod',
    Token.Git.Unmerged: 'git-unm',
    Token.Git.Staged: 'git-stg',
    Token.Git.Show: 'git-show',
    Token.Git.Show.Header: 'git-show-h',
    Token.Git.Refs.RemoteHead: 'git-rh',
    Token.Git.Refs.Head: 'git-h',
    Token.Git.Refs.Tag: 'git-t',
    Token.Git.Refs.RemoteBranch: 'git-rb',
    Token.Git.Refs.Branch: 'git-b',
})

class GitLexer(RegexLexer):
    name = "Git"
    aliases = ["git"]
    filenames = ['*.git']
    version_added = '1.0'

    tokens = {
        'root': [
            (r'\n', Whitespace),
            (r'^error:(.*?)\n', Token.Git.Error),
            (r'^fatal:(.*?)\n', Token.Git.Fatal),
            (r'^hint:(.*?)\n', Token.Git.Hint),
            (r'^warning:(.*?)\n', Token.Git.Warning),
            (r'^.*$\n', Generic.Output),
            (r'[^\n]+', Generic.Output),
        ]

    }

class GitPrettyLogLexer(Lexer):
    _branch_line_rgx = r'([\|\\\/ _]*)'
    _logrgx_groups = [
      _branch_line_rgx,     # 1. Branch line
      r'(\*)',              # 2. Commit asterisk
      _branch_line_rgx,     # 3. Branch line
      r'( +)',              # 4. Space
      r'([a-f0-9]+)',       # 5. Commit hash
      r'( +)',              # 6. Space
      r'(-)',               # 7. Commit separator
      r'( +)',              # 8. Space
      r'(\([0-9A-Za-zÀ-ÖØ-öø-ÿ ]+\))',  # 9. Date
      r'(\s+)',    # 10. Space
      r'([^\n]+)', # 11. Commit message
      r'( +)',     # 12. Space
      r'(-)',      # 13. Commit separator
      r'( +)',     # 14. Space
      r'([0-9A-Za-zÀ-ÖØ-öø-ÿ ]*[0-9A-Za-zÀ-ÖØ-öø-ÿ]+)',  # 15. Author
      r'( *)',                        # 16. Space
      r'((\([\w ->,:]+\))?)',         # 17. Refs
      r'\n', # End
    ]

    # Combine the regex patterns into a single pattern
    _logrgx = re.compile(r''.join(_logrgx_groups))

    _log_tokens = {
      1: Token.Git.BranchLine,
      3: Token.Git.BranchLine,
      4: Whitespace,
      5: Token.Git.CommitHash,
      6: Whitespace,
      8: Whitespace,
      9: Token.Git.CommitDate,
      10: Whitespace,
      11: Token.Git.CommitMessage,
      12: Whitespace,
      14: Whitespace,
      15: Token.Git.CommitAuthor,
      16: Whitespace,
      17: Token.Git.Refs,
    }

    def get_tokens_unprocessed(self, text):
        pos = 0

        for match in line_re.finditer(text):
            line = match.group()

            match_log = self._logrgx.match(line)
            match_branch_line = re.match(r'^' + self._branch_line_rgx + r'$', line)

            ## Line is log
            if match_log:
                for i in range(1, len(match_log.groups())):
                    if match_log.group(i):
                        if self._log_tokens.get(i):
                            yield match_log.start(i), self._log_tokens[i], match_log.group(i)
                        else:
                            yield match_log.start(i), Generic.Output, match_log.group(i)
                yield match.end(), Whitespace, '\n'
            elif match_branch_line:
                yield match.start(), Token.Git.BranchLine, line

            else:
                yield match.start(), Generic.Output, line

class GitStatusLexer(RegexLexer):
    tokens = {
        'root': [
            (r'^\n', Whitespace),
            (r'\s*Untracked files:\n', Generic.Output, 'untracked'),
            (r'\s*Changes not staged for commit:\n', Generic.Output, 'modified'),
            (r'\s*Changes to be committed:\n', Generic.Output, 'staged'),
            (r'\s*Unmerged paths:\n', Generic.Output, 'unmerged'),
            (r'^.*\n', using(GitLexer)),
        ],
        'untracked': [
            (r'^\s*\n', Whitespace, '#pop'),
            (r'^\s+\(.*\)\n', Generic.Output),
            (r'^(\s*)([^\n]+)(\n)', bygroups(
                Whitespace,
                Token.Git.Untracked,
                Whitespace
            )),
        ],
        'modified': [
            (r'^\s*\n', Whitespace, '#pop'),
            (r'^\s+\(.*\)\n', Generic.Output),
            (r'^(\s*)([^\n]+)(\n)', bygroups(
                Whitespace,
                Token.Git.Modified,
                Whitespace
            )),
        ],
        'staged': [
            (r'^\s*\n', Whitespace, '#pop'),
            (r'^\s+\(.*\)\n', Generic.Output),
            (r'^(\s*)([^\n]+)(\n)', bygroups(
                Whitespace,
                Token.Git.Staged,
                Whitespace
            )),
        ],
        'unmerged': [
            (r'^\s*\n', Whitespace, '#pop'),
            (r'^\s+\(.*\)\n', Generic.Output),
            (r'^(\s*)([^\n]+)(\n)', bygroups(
                Whitespace,
                Token.Git.Unmerged,
                Whitespace
            )),
        ],
    }

class GitLogLexer(RegexLexer):
    tokens = {
        'root': [
            (r'^\n', Whitespace),
            (r'^(commit [0-9a-f]+)', Token.Git.Show.Header, 'header'),
            (r'^.*\n', using(GitLexer)),
        ],
        'header': [
            (r' +', Whitespace),
            (r'(\(|\)|->|,)', Token.Git.Show.Header),
            (r'origin/HEAD', Token.Git.Refs.RemoteHead),
            (r'HEAD', Token.Git.Refs.Head),
            (r'tag: [\w.-]+', Token.Git.Refs.Tag),
            (r'origin/[\w/_-]+', Token.Git.Refs.RemoteBranch),
            (r'[\w/_-]+', Token.Git.Refs.Branch),
            (r'\n', Whitespace, '#pop'),
        ],
    }


class GitShowLexer(GitLogLexer):
    tokens = {
        'root': [
            (r'^diff .*\n', using(DiffLexer), 'diff'),
            inherit
        ],
        'diff': [
            (r'^.*\n', using(DiffLexer)),
        ],
    }

class GitBranchLexer(RegexLexer):
    tokens = {
        'root': [
            (r'^\n', Whitespace),
            (r'^(\* )(.*?)(\n)', bygroups(
                using(GitLexer),
                Token.Git.Refs.Branch,
                Whitespace,
            )),
            (r'^.*\n', using(GitLexer)),
        ],
    }

class GitMergeLexer(RegexLexer):
    tokens = {
        'root': [
            (r'^\n', Whitespace),
            (r'^( \S+ +\| +\d+ )(\+*)(\-*)(\n)', bygroups(
                Generic.Output,
                Generic.Inserted,
                Generic.Deleted,
                Whitespace,
            )),
            (r'^.*\n', using(GitLexer)),
        ],
    }
