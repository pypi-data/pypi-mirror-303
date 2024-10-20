from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-postgres"
    metadata_id = "metamart_source_postgres"


config = Config()
