import sys
from workflow import Workflow3, ICON_WEB, web


GITHUB_UPDATE_CONF = {'github_slug': 'kinabalu/alfred-chess.com'}
# GitHub Issues
HELP_URL = 'https://github.com/kinabalu/alfred-chess.com/issues'


def main(wf):
    print("Running chess.com!")

    # wf.add_item(u"Hi there", u"Woah", valid=True, icon=ICON_WEB)
    # wf.add_item(u"Ho there", u"Doah", valid=True, icon=ICON_WEB)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
