from pystrict3lib import FuncDocVerifier

class OutStreamListener:
	def __init__(self):
		self.reset()
	def write(self, s):
		self.lines.append(s)
	def reset(self):
		self.lines = []

def test_rst_urls():
	nodename, lineno = 'mock', 123
	outstream = OutStreamListener()
	fdv = FuncDocVerifier("hello")
	fdv.find_directives("`link <http://example.com>` with no \_ at the end.", nodename, lineno, outstream)
	assert len(outstream.lines) == 1
	assert 'rst link should end with _' in outstream.lines[0]

	outstream.reset()
	fdv.find_directives("`link<http://example.com>`_ with no space in between.", nodename, lineno, outstream)
	assert len(outstream.lines) == 1
	assert 'rst link needs space before <url>' in outstream.lines[0]

def test_rst_unknown_directives():
	nodename, lineno = 'mock', 123
	outstream = OutStreamListener()
	fdv = FuncDocVerifier("hello")
	fdv.find_directives("""
:py:unknown, a unknown directive
:pyclass:`Foo`, a unknown directive
:py:method:`NoQuotes.foo` which should be `meth`.

Something else::

	is unrelated

""", nodename, lineno, outstream)
	assert len(outstream.lines) == 3
	assert all(('unknown directive' for line in outstream.lines))
            
	outstream.reset()
	fdv.find_directives("""
:class:TreeNode which should be be in the `py` domain
children: list of :class:TreeNode objects
:func:bla which should be be in the `py` domain
but referencing :py:meth:`FuncDocVerifier.find_directives` is fine.
""", nodename, lineno, outstream)
	assert len(outstream.lines) == 3
	assert all(('should be ":py' for line in outstream.lines))
            
	outstream.reset()
	fdv.find_directives(""":py:class:NoQuotes without `quotes`""", nodename, lineno, outstream)
	assert len(outstream.lines) == 1
	assert 'directive should continue with `quotes`' in outstream.lines[0]
