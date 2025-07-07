from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_pv_plugin_template.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class fooExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_pv_plugin_template.parsers.foo_batch_parser import fooExperimentParser

        return fooExperimentParser(**self.model_dump())


class fooParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_pv_plugin_template.parsers.foo_measurement_parser import fooParser

        return fooParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


foo_experiment_parser_entry_point = fooExperimentParserEntryPoint(
    name='fooExperimentParserEntryPoint',
    description='foo experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


foo_parser_entry_point = fooParserEntryPoint(
    name='fooParserEntryPoint',
    description='foo parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
