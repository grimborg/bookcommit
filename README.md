Mercurial extension to automatically prepend the current bookmark name to the commit message.

=== Overview ===

Whenever you commit, if you have an active bookmark, it will be prepended to the commit message that you provide. Otherwise, the message will stay as you entered it:

{{{
hg ci -m "message"`
}}}

If you have an active bookmark, the resulting message will be "BOOKMARK message". Otherwise, it will be just "message".

