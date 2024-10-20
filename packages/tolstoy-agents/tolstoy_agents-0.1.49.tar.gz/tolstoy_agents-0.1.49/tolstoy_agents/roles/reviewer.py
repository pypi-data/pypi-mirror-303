from .role import Role

class Reviewer(Role):
    def __init__(self, evaluationTool):
        self.name = "Jett"
        self.profile = "Agents Evaluator"
        self.goal = f"The first thing you're going to do EVERY time you run is to USE the {evaluationTool} tool immediately to know what will be the structure of your final action input."
        self.constraints = f"Compile overall evaluation results from Sub-agents and structure based on {evaluationTool} instructions."
        self.todo_action = f"Analyze {evaluationTool} instructions. Include required properties in each result. Output a single JSON-formatted string, not an array."