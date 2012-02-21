Mercurial extension to automatically prepend the current bookmark name to the commit message.

Whenever you commit, if you have an active bookmark, it will be prepended to the commit message that you provide. Otherwise, the message will stay as you entered it.

For example, if you execute this::

	hg ci -m "message"`

Then, if you have an active bookmark B123, the resulting message will be "B123 message". Otherwise, it will be just "message".

To use this extension, add it to your .hgrc::

	[extensions]
	bookcommit=
