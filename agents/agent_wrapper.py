# # agents/agent_wrapper.py
# class Agent:
#     def __init__(self, name, model, instructions, functions):
#         self.name = name
#         self.model = model
#         self.instructions = instructions
#         self.functions = functions  # Should be a list of callable functions
#
#     def run(self, input_data):
#         # Just a basic executor for now
#         for fn in self.functions:
#             input_data = fn(input_data)
#         return input_data


class Agent:
    def __init__(self, name, model, instructions, functions):
        self.name = name
        self.model = model
        self.instructions = instructions
        self.functions = functions  # List of callable functions

    def run(self, input_data):
        for fn in self.functions:
            input_data = fn(input_data)
        return input_data
