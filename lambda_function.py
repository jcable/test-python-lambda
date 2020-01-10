import os
from datetime import datetime
from urllib.request import Request, urlopen
import requests

SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable
EXPECTED = os.environ['expected']  # String expected to be on the page, stored in the expected environment variable


def validate(res):
    '''Return False to trigger the canary

    Currently this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of arbitrary
    checks on the contents of SITE.
    '''
    return EXPECTED in res


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        r = requests.get(SITE, cert=('cosmos/client.crt', 'cosmos/client.key'))
        print(r.text)
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
