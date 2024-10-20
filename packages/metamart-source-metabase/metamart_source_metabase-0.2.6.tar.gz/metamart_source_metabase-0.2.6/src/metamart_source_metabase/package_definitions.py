from metamart_schemas.generics import PackageConfig


class Config(PackageConfig):
    integration_name = "metamart-source-metabase"
    metadata_id = "metamart_source_metabase"


config = Config()
