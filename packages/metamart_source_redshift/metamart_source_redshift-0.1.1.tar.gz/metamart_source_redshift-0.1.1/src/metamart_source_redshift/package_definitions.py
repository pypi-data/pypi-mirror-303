from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-redshift"
    metadata_id = "metamart_source_redshift"


config = Config()
