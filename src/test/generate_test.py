from testslide.dsl import context
import generate
from utils import files
from pathlib import Path
import shutil
import os


@context
def Generate(context):
    @context.sub_context
    def test_generate(context):
        @context.example
        def it_will_generate_models_for_example1(self):
            output = files.clean_dir("../generate_examples/example1")
            generate.run("test/assets/example1.yml", output)

        @context.example
        def it_will_produce_compilable_code(self):
            os.chdir("../generate_examples/example1")
            result = os.system("g++ -shared -fPIC *.cpp")
            self.assertEquals(result, 0)
            os.remove("a.out")
