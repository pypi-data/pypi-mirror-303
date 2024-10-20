from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    """ """

    integration_name = "metamart-source-flat-file"
    metadata_id = "metamart_source_flat_file"


config = Config()
