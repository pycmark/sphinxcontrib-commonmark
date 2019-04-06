"""
    test_commonmark
    ~~~~~~~~~~~~~~~

    :copyright: Copyright 2017-2019 by Takeshi KOMIYA
    :license: Apache License 2.0, see LICENSE for details.
"""

import pytest


def test_build(app, status, warning):
    app.build()
    assert app.statuscode == 0
    assert warning.getvalue() == ''

    content = (app.outdir / 'index.html').text()

    # heading
    assert ('<div class="section" id="id1">\n'
            '<h1>sphinxcontrib-commonmark examples<a class="headerlink" href="#id1" '
            'title="Permalink to this headline">¶</a></h1>' in content)

    # paragraph and inline markups
    assert ('<p>Hello markdown world!\n'
            'You can write <em>emphasis</em>, <strong>strong</strong> and '
            '<code class="docutils literal notranslate"><span class="pre">literal</span></code> '
            'text.</p>' in content)

    # bullet list
    assert ('<ul class="simple">\n'
            '<li>item1</li>\n'
            '<li>item2</li>\n'
            '<li>item3</li>\n'
            '</ul>\n' in content)

    # enumerated list
    assert ('<ol class="arabic simple" start="1">\n'
            '<li>item1</li>\n'
            '<li>item2</li>\n'
            '<li>item3</li>\n'
            '</ol>\n' in content)

    # code-block
    assert ('<div class="code highlight-default notranslate"><div class="highlight">'
            '<pre><span></span><span class="nb">print</span> '
            '<span class="s2">&quot;hello world&quot;</span>\n'
            '</pre></div>\n'
            '</div>' in content)

    # blockquote
    assert ('<blockquote>\n'
            '<div><p>Of course, you can write quoted text\n'
            'using “&gt;” mark.</p>\n'
            '</div></blockquote>\n' in content)


@pytest.mark.sphinx('html', testroot='hardlinebreak')
def test_hardlinebreak_html(app):
    app.build()

    content = (app.outdir / 'index.html').text()
    assert ('<p>Hello markdown world!<br />\n'
            'hard line<br />\n'
            'break in Sphinx.</p>' in content)


@pytest.mark.sphinx('latex', testroot='hardlinebreak')
def test_hardlinebreak_latex(app):
    app.build()

    content = (app.outdir / 'python.tex').text()
    assert ('Hello markdown world!\\linebreak\n'
            'hard line\\linebreak\n'
            'break in Sphinx.\n' in content)


@pytest.mark.sphinx('text', testroot='hardlinebreak')
def test_hardlinebreak_text(app):
    app.build()

    content = (app.outdir / 'index.txt').text()
    assert 'Hello markdown world! hard line break in Sphinx.\n' in content
