import uuid
import os
from agents.researcher import Researcher
from agents.designer import Designer
from agents.coder_executor import CoderExecutor
from agents.analyst import Analyst
from agents.writer import Writer

class Orchestrator:
    def __init__(self):
        self.researcher = Researcher()
        self.designer = Designer()
        self.coder = CoderExecutor()
        self.analyst = Analyst()
        self.writer = Writer()

    def run(self, topic, mode="demo"):
        session_id = str(uuid.uuid4())
        os.makedirs(f"artifacts/{session_id}", exist_ok=True)

        print("1. Researching topic...")
        literature = self.researcher.generate_literature(topic)

        print("2. Designing experiment...")
        plan = self.designer.create_plan(literature, topic)

        print("3. Generating and executing code...")
        code_file = self.coder.generate_code(plan, session_id)
        run_results = self.coder.execute_code(code_file, session_id)

        print("4. Analyzing results...")
        analysis = self.analyst.process(run_results, session_id)

        print("5. Creating paper + slides...")
        outputs = self.writer.create_outputs(literature, plan, analysis, session_id)

        print("Done.")
        return outputs
