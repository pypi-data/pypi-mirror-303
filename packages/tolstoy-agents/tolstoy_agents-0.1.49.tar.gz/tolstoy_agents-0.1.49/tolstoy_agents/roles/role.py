PREFIX_TEMPLATE = """You are a seasoned expert Tolstoy {profile}, named {name}. Your goal is to {goal}.\n\n"""

CONSTRAINT_TEMPLATE = "Remember these constraints: {constraints}.\n\n"

class Role():
    """Role/Agent"""
    name: str = ""
    profile: str = ""
    goal: str = ""
    constraints: str = ""
    todo_action: str = ""
    desc: str = ""
    is_human: bool = False
    role_id: str = ""
    states: list[str] = []

    def _get_prefix(self):
        """Get the role prefix"""
        if self.desc:
            return self.desc

        prefix = PREFIX_TEMPLATE.format(**{"profile": self.profile, "name": self.name, "goal": self.goal})
        
        if self.constraints:
            prefix += CONSTRAINT_TEMPLATE.format(**{"constraints": self.constraints})
        
        if self.todo_action:
            prefix += f"To achieve this, you will: {self.todo_action}"

        return prefix