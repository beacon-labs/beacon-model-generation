from testslide.dsl import context
from src import generate
from dependencies.utils.src import files
from pathlib import Path
import shutil


@context
def Generate(context):
    @context.sub_context
    def test_generate(context):
        @context.example
        def it_will_generate_models_for_example1(self):
            output = files.clean_dir("generate_examples/example1")
            generate.run("test/assets/example1.yml", output)
