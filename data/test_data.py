import os
users = {
    'nonadmin': {
        'login_name': os.environ['NONADMIN_USER_NAME'],
        'password': os.environ['NONADMIN_USER_PASSWORD'],
        'name': 'Katie Clausman',
        'email': 'katie@nd.com'
    },
    'admin': {
        'login_name': os.environ['ADMIN_USER_NAME'],
        'password': os.environ['ADMIN_USER_PASSWORD'],
        'name': 'Steve Thomsons',
        'email': 'sthompson@nd.com'
    },
    'expired': {
        'login_name': os.environ['EXPIRED_USER_NAME'],
        'password': os.environ['EXPIRED_USER_PASSWORD'],
        'name': 'Expired User'
    },
    'disabled': {
        'login_name': os.environ['DISABLED_USER_NAME'],
        'password': os.environ['DISABLED_USER_PASSWORD'],
        'name': 'Disabled User'
    }
}