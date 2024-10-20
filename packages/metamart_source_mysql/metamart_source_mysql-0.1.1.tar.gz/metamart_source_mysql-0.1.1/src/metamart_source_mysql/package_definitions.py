from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-mysql"
    metadata_id = "metamart_source_mysql"


config = Config()
