LOCAL_APPS = (
    'core',
)

CONSTANCE_CONFIG = {}


THUMBNAIL_PRESERVE_FORMAT = True

# Autoslag handler that we need to create for make tests runnable

def auto_slag_handler():
    return 'auto_slug'

MOMMY_CUSTOM_FIELDS_GEN = {
    'django_extensions.db.fields.AutoSlugField': auto_slag_handler,
}
