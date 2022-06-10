import os
from datetime import datetime
from pytz import timezone

print('time zone is {0:s}/{1:s}'.format(os.environ['INPUT_TZ1'], os.environ['INPUT_TZ2']))

external_fmt = os.environ['INPUT_DATEFORMAT_OVERRIDE']
fmt = "%Y-%m-%d_%H.%M.%S_%Z%z"

if external_fmt:
    print('External format provided via environment variable INPUT_DATEFORMAT_OVERRIDE: {0:s} '.format(external_fmt))
    fmt = external_fmt
else:
    print('Using default format: {0:s}'.format(fmt))

now_utc = datetime.now(timezone('{0:s}/{1:s}'.format(os.environ['INPUT_TZ1'], os.environ['INPUT_TZ2'])))
str_temp = now_utc.strftime(fmt)

if None != str_temp:
    command = 'echo ::set-output name=datetime_str::{0:s}'.format(str_temp)
    print(command)
    print(os.popen(command).read())


