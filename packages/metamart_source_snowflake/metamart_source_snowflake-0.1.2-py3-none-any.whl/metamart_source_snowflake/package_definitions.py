from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-snowflake"
    metadata_id = "metamart_source_snowflake"


config = Config()
