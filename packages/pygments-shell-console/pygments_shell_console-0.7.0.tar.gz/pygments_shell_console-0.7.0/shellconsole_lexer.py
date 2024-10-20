"""An example plugin lexer for Pygments."""

from pygments.lexer import Lexer
from pygments.lexer import RegexLexer, ExtendedRegexLexer, include, bygroups, \
    default, using, line_re, do_insertions
from pygments.token import Token, Punctuation, Whitespace, \
    Text, Comment, Operator, Keyword, Name, String, Number, Generic
from pygments.lexers.diff import DiffLexer
from pygments.lexers.shell import BashLexer
from pygments.lexers.diff import DiffLexer
from git_lexer import GitLexer, GitLogLexer, GitPrettyLogLexer, \
    GitStatusLexer, GitShowLexer, GitBranchLexer, GitMergeLexer
from pygments.token import STANDARD_TYPES

import re

__all__ = ['ShellConsoleLexer']

STANDARD_TYPES.update({
    Token.Generic.Prompt.Whitespace: 'gp-w',
    Token.Generic.Prompt.UserHost: 'gp-uh',
    Token.Generic.Prompt.Directory: 'gp-d',
    Token.Generic.Prompt.GitBranch: 'gp-gb',
    Token.Generic.Prompt.VirtualEnv: 'gp-ve',
})

class ShellConsoleLexer(Lexer):
    name = "Shell Console"
    aliases = ["shellconsole", "shell-console", "shell", "console"]
    filenames = ['*.sh-session', '*.shell-session']
    mimetypes = ['application/x-shell-session', 'application/x-sh-session']
    url = 'https://en.wikipedia.org/wiki/Unix_shell'
    version_added = '1.0'

    _bare_continuation = False

    _ps1_groups = [
        r'(?P<venv>\([^\)]*\))?', # Virtualenv
        r'(\s*)?', # Whitespace
        r'\[?', # Start bracketed prompt
        r'(?P<user_host>[\S @]+@[^\s]+?)', # user@host
        r'(\s*)', # Whitespace
        r'(?:(\:)|(\s+))', # Separator: colon or space
        r'(\s*)', # Whitespace
        r'(?P<current_dir>[^\s\]]+)', # Current directory
        r'(?:(\s+)(?P<git_branch>\([^)]+\)))?', # Whitespace + Git branch
        r'\]?', # End bracketed prompt
        r'(\s*)', # Whitespace
        r'([$#%]\n?)', # End of prompt
        r'(\s*)', # Whitespace
        r'(?P<command>.*\n?)' # Command
    ]
    _ps1rgx = re.compile(r''.join(_ps1_groups))
    # print(_ps1rgx.pattern)

    _ps1_tokens = [
            Token.Generic.Prompt.VirtualEnv,
            Token.Generic.Prompt.Whitespace,
            Token.Generic.Prompt.UserHost,
            Token.Generic.Prompt.Whitespace,
            Token.Generic.Prompt, # Separator: colon
            Token.Generic.Prompt.Whitespace, # Separator: space
            Token.Generic.Prompt.Whitespace,
            Token.Generic.Prompt.Directory,
            Token.Generic.Prompt.Whitespace,
            Token.Generic.Prompt.GitBranch,
            Token.Generic.Prompt.Whitespace,
            Token.Generic.Prompt,
            Token.Generic.Prompt.Whitespace,
    ]


    _ps2 = '> '
    _innerLexerCls = BashLexer


    def get_tokens_unprocessed(self, text):
        innerlexer = self._innerLexerCls(**self.options)
        difflexer = DiffLexer()
        gitlexer = GitLexer()
        git_log_lexer = GitLogLexer()
        git_pretty_log_lexer = GitPrettyLogLexer()
        gitstatuslexer = GitStatusLexer()
        gitshowlexer = GitShowLexer()
        gitbranchlexer = GitBranchLexer()
        mergelexer = GitMergeLexer()

        pos = 0
        # Bash command
        curcode = ''
        insertions = []
        backslash_continuation = False

        custom_lexer = None
        output = ""

        for match in line_re.finditer(text):
            line = match.group()

            m = self._ps1rgx.match(line)
            ## If line starts with a prompt
            if m:
                curcode = ''

                # If there is output, yield it using the custom lexer
                if output:
                    if custom_lexer:
                        for i, t, v in custom_lexer.get_tokens_unprocessed(output):
                            # print(f"\n2. yielding pos={pos+i}, t={t}, v={v}")
                            yield pos+i, t, v
                    else:
                        yield pos, Generic.Output, output

                    output = ''
                    custom_lexer = None

                if not insertions:
                    pos = match.start()

                prompt_pos = 0
                for i, t in enumerate(self._ps1_tokens):
                    if m.group(i + 1):
                        group_pos = m.start(i + 1)
                        before_content = line[prompt_pos:group_pos]
                        if before_content:
                            insertions.append((len(curcode), [(0, Generic.Prompt, before_content)]))

                        insertions.append((len(curcode), [(0, t, m.group(i + 1))]))
                        prompt_pos += len(before_content) + len(m.group(i+1))

                last_group_index = len(self._ps1_tokens) + 1
                group_pos = m.start(last_group_index)
                before_content = line[prompt_pos:group_pos]
                if before_content:
                    insertions.append((len(curcode), [(0, Generic.Prompt, before_content)]))

                curcode += m.group(last_group_index)
                backslash_continuation = curcode.endswith('\\\n')

            # If line is a continuation of a previous line
            elif backslash_continuation:
                # If there is a continuation prompt, insert it
                if line.startswith(self._ps2):
                    insertions.append((len(curcode),
                                       [(0, Generic.Prompt,
                                         line[:len(self._ps2)])]))
                    curcode += line[len(self._ps2):]
                else:
                    curcode += line
                backslash_continuation = curcode.endswith('\\\n')

            # If line is a continuation of a previous line with bare_continuation
            elif self._bare_continuation and line.startswith(self._ps2):
                insertions.append((len(curcode),
                                   [(0, Generic.Prompt,
                                     line[:len(self._ps2)])]))
                curcode += line[len(self._ps2):]

            # Otherwise, we have a normal line
            else:
                if 'diff' in curcode or curcode.startswith('git stash show -p'):
                    custom_lexer = difflexer
                elif curcode.startswith('git lg') or curcode.startswith('git log --graph'):
                    custom_lexer = git_pretty_log_lexer
                elif curcode.startswith('git log'):
                    custom_lexer = git_log_lexer
                elif curcode.startswith('git status'):
                    custom_lexer = gitstatuslexer
                elif curcode.startswith('git show'):
                    custom_lexer = gitshowlexer
                elif curcode.startswith('git branch'):
                    custom_lexer = gitbranchlexer
                elif curcode.startswith('git merge') or curcode.startswith('git pull') or curcode.startswith('git stash show'):
                    custom_lexer = mergelexer
                elif curcode.startswith('git'):
                    custom_lexer = gitlexer

                output += line

            if not backslash_continuation and insertions:
                for i, t, v in do_insertions(insertions,
                                             innerlexer.get_tokens_unprocessed(curcode)):
                    # print(f"\n4. yielding pos={pos+i}, t={t}, v={v}")
                    yield pos+i, t, v

                insertions = []

        if output:
            if custom_lexer:
                for i, t, v in custom_lexer.get_tokens_unprocessed(output):
                    # print(f"\n2. yielding pos={pos+i}, t={t}, v={v}")
                    yield pos+i, t, v
            else:
                yield pos, Generic.Output, output
