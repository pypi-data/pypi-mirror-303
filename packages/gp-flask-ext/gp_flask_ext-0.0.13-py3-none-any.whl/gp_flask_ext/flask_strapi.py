from flask import Flask, Blueprint
from loguru import logger
from .strapi import StrapiClient


def init_app(app: Flask, config=None):
    # Check if the provided config is valid
    if not (config is None or isinstance(config, dict)):
        raise ValueError("`config` must be an instance of dict or None")

    # Merge the default config with the provided config
    base_config = app.config.get("STRAPI_CONFIG", {})
    if config:
        base_config.update(config)
    config = base_config

    # Initialize the StrapiAPI
    _strapi = StrapiClient(
        **config
    )

    # Add the StrapiAPI to the app context
    ext_name = config.get("ext_name", "strapi")
    app.extensions[ext_name] = _strapi
    logger.info("Initialized the StrapiAPI")

    if config.get("blueprint", True):
        # Register the blueprint
        bp_name = base_config.get("blueprint_name", "strapi")
        bp_url_prefix = base_config.get("blueprint_url_prefix", "/strapi")
        bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix, template_folder="templates")

        app.register_blueprint(bp)
        logger.info("Registered the Strapi blueprint")

