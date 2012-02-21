from mercurial import commands, extensions

def addbookmark(orig, ui, repo, *pats, **opts):
    """If there is an active bookmark, prepend it to the commit message."""
    bookmark = getattr(repo, '_bookmarkcurrent', None)
    if bookmark:
        msg = opts.get('message', None)
        opts['message'] = ' '.join([bookmark, msg]).strip()
    return orig(ui, repo, *pats, **opts)

def uisetup(ui):
    extensions.wrapcommand(commands.table, 'commit', addbookmark)
