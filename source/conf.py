# for custom dScript lexer
from pygments.lexer import RegexLexer, include
from pygments import token
from sphinx.highlighting import lexers

# for markdown support
import recommonmark
from recommonmark.transform import AutoStructify

# Project Info
project = "Denizen Beginner's Guide"
copyright = '2019-2020 The DenizenScript Team'
author = 'The DenizenScript Team'
version = '0.4'
release = '0.4'

# General Config
extensions = ['recommonmark']
templates_path = ['_templates']
source_suffix = '.md'
master_doc = 'index'
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Changes to HTML format
html_title = "Denizen Beginner's Guide"
html_extra_path = ['_static_extra']

# Disabled stuff
smartquotes = False

templates_path = ['_templates']

reusable_tokens = {
    'spaces_patch': [
        (r'\s', token.Text ) #                                                    spaces
    ],
    'inside_brackets': [
        (r'\[', token.Name.Variable, '#push'), #                                  [
        (r'\]', token.Name.Variable, '#pop'), #                                   ]
        include('tag_finder'),
        (r'$', token.Text, '#pop'),
        (r'.', token.Name.Variable) #                                             anything else
    ],
    'inside_tag': [
        (r'\[(?=([^\s]+)\])', token.Name.Variable, 'inside_brackets' ), #         [brackets]
        (r'\.', token.Operator ), #                                               .
        (r'>', token.Name.Tag, '#pop'), #                                         >
        (r'$', token.Text, '#pop'),
        (r'.', token.Name.Tag) #                                                  anything else
    ],
    'tag_finder': [
        (r'<(?=([^\s]+)>)', token.Name.Tag, 'inside_tag' ), #                     <tag>
        (r'%.*%', token.Generic.Error ) #                                         %old_def%
    ],
    'double_quoted': [
        include('tag_finder'),
        (r'"', token.Literal.String, '#pop'), #                                   ]
        (r'.', token.Literal.String ) #                                           anything else
    ],
    'single_quoted': [
        include('tag_finder'),
        (r'\'', token.Literal.String.Backtick, '#pop'), #                         ]
        (r'.', token.Literal.String.Backtick ) #                                  anything else
    ],
    'code_line': [
        (r'"(?=([^"]+)")', token.Literal.String, 'double_quoted' ), #             "text"
        (r'\'(?=([^\']+)\')', token.Literal.String.Backtick, 'single_quoted' ), # 'text'
        (r'$', token.Text, '#pop'),
        include('tag_finder'),
        (r'.', token.Text ) #                                                     anything else
    ],
    'root': [
        (r'^\s*#\s*[\|+=].*$', token.Comment.Hashbang ), #                        # +--- header comment
        (r'^\s*#\s*-.*$', token.Comment.Single ), #                               # - code comment
        (r'^\s*#.*$', token.Comment ), #                                          # regular comment
        (r'^[^-#\n]*:', token.Name.Class ), #                                       yaml key:
        (r'^\s*-\s[^\s]+$', token.Keyword ), #                                    - somecommand
        (r'^\s*-\s[^\s]+\s', token.Keyword, 'code_line' ), #                      - somecommand someargs
        include('spaces_patch'),
        (r'.', token.Text ) #                                                     anything else
    ]
}

class dScriptLexerRed(RegexLexer):
    name = 'dscript_red'
    tokens = reusable_tokens
class dScriptLexerGreen(RegexLexer):
    name = 'dscript_green'
    tokens = reusable_tokens
class dScriptLexerBlue(RegexLexer):
    name = 'dscript_blue'
    tokens = reusable_tokens

lexers['dscript_red'] = dScriptLexerRed(startinline=True)
lexers['dscript_green'] = dScriptLexerGreen(startinline=True)
lexers['dscript_blue'] = dScriptLexerBlue(startinline=True)

# For markdown
def setup(app):
    app.add_stylesheet('css/stylesheet.css')
    app.add_config_value('recommonmark_config', {
            'auto_toc_tree_section': 'Contents',
            'enable_eval_rst': True,
            }, True)
    app.add_transform(AutoStructify)
