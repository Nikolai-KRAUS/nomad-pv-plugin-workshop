from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from pvworkshop.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class containerExperimentParserEntryPoint(ParserEntryPoint):

    def load(self):
        from pvworkshop.parsers.container_batch_parser import containerExperimentParser

        return containerExperimentParser(**self.model_dump())


class containerParserEntryPoint(ParserEntryPoint):

    def load(self):
        from pvworkshop.parsers.container_measurement_parser import containerParser

        return containerParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


container_experiment_parser_entry_point = containerExperimentParserEntryPoint(
    name='containerExperimentParserEntryPoint',
    description='container experiment parser entry point configuration.',
    mainfile_name_re='^(.+\.xlsx)$',
    mainfile_mime_re='(application|text|image)/.*',
)


container_parser_entry_point = containerParserEntryPoint(
    name='containerParserEntryPoint',
    description='container parser entry point configuration.',
    mainfile_name_re='^.+\.?.+\.((eqe|jv|mppt)\..{1,4})$',
    mainfile_mime_re='(application|text|image)/.*',
)
