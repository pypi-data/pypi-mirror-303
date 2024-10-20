from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-bigquery"
    metadata_id = "metamart_source_bigquery"


config = Config()
