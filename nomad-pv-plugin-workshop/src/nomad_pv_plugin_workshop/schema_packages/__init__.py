from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_pv_plugin_workshop.schema_packages.schema_package import m_package

        return m_package


class fooPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_pv_plugin_workshop.schema_packages.foo_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)


foo_schema_package_entry_point = fooPackageEntryPoint(
    name='fooPackage',
    description='foo package entry point configuration.',
)
