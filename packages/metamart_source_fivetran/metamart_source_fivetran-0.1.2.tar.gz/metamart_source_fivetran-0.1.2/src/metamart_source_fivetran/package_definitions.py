from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-fivetran"
    metadata_id = "metamart_source_fivetran"


config = Config()
