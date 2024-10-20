from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-mssql"
    metadata_id = "metamart_source_mssql"


config = Config()
