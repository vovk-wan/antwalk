
config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "ant_walk": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "ant_walk"
        },
    },
    "loggers": {
        "ant_logger": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    },
}
