from testslide.dsl import context
from src import config


@context
def Config(context):
    @context.sub_context
    def test_load(context):
        @context.example
        def it_will_load_and_validate_example1(self):
            c = config.load("test/assets/example1.yml")
            self.assertEquals(c["settings"]["prefix"], "BL")
