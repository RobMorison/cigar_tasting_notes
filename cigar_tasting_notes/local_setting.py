# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4%$6hxg9km*f@unyxqs1n=*5le*)h%=8c%mxzkzpo7*svfp^9v'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cigar_tasting_notes',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Football1!'
    }
}
