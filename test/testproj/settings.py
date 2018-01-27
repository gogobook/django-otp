from os.path import dirname, join, abspath

import django


def project_path(path):
    return abspath(join(dirname(__file__), path))


USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django_otp',
    'django_otp.plugins.otp_hotp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_email',

    'otp_yubikey',
    'otp_twilio',

    'django_agent_trust',
    'otp_agents',
]

if django.VERSION < (1, 10):
    MIDDLEWARE_CLASSES = [
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django_otp.middleware.OTPMiddleware',
        'django_agent_trust.middleware.AgentMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]
else:
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django_otp.middleware.OTPMiddleware',
        'django_agent_trust.middleware.AgentMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            project_path('templates'),
        ]
    },
]

SECRET_KEY = 'cI4AHyAcIKQxcq2hI54YS7Bnn6vbojTxxlTWQdRiA2pky5oz8IEgJ1DcyvCDXnXn'

ROOT_URLCONF = 'urls'
