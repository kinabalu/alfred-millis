import sys
import datetime
import time
import pytz
from workflow import Workflow3, ICON_CLOCK

GITHUB_UPDATE_CONF = {'github_slug': 'kinabalu/alfred-millis'}
# GitHub Issues
HELP_URL = 'https://github.com/kinabalu/alfred-millis/issues'

DATE_FORMAT = "%b %d %Y %H:%M:%S %Z"

log = None


def get_utc_time_in_millis():
    return round(time.time()) * 1000


def main(wf):

    log.debug(wf.args)
    if len(wf.args) == 0:
        utc_time_in_millis = get_utc_time_in_millis()
        wf.add_item(
            title='Unix Time',
            subtitle=utc_time_in_millis,
            copytext=utc_time_in_millis,
            icon=ICON_CLOCK
        )
    elif len(wf.args) == 1 and wf.args[0] != 'utc' and wf.args[0].isnumeric():
        milliseconds = int(wf.args[0])
        current_datetime = datetime.datetime.fromtimestamp(
            milliseconds / 1000.0)

        wf.add_item(
            title='Date is %s' % current_datetime.strftime(
                DATE_FORMAT),
            subtitle="Milliseconds entered: %s" % wf.args[0],
            icon=ICON_CLOCK
        )
    elif len(wf.args) == 2 and wf.args[0].lower() == 'utc' and wf.args[1].isnumeric():
        milliseconds = int(wf.args[1])
        utc_datetime = datetime.datetime.fromtimestamp(
            milliseconds / 1000.0, tz=pytz.timezone("UTC"))
        log.debug("utc_datetime: %s" % utc_datetime)
        wf.add_item(
            title='Date is %s' % utc_datetime.strftime(
                DATE_FORMAT),
            subtitle="Milliseconds entered for UTC: %s" % wf.args[1],
            icon=ICON_CLOCK
        )
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))
