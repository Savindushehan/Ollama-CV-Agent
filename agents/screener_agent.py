# from typing import Dict, Any
# from .base_agent import BaseAgent
# from datetime import datetime
#
#
# class ScreenerAgent(BaseAgent):
#     def __init__(self):
#         super().__init__(
#             name="Screener",
#             instructions="""
#             Screen candidates based on:
#             - Qualification alignment
#             - Experience relevance
#             - Skill match percentage
#             - Cultural fit indicators
#             - Red flags or concerns
#
#             Provide a comprehensive and structured screening report in JSON format.
#             """
#         )
#
#     async def run(self, message: list) -> Dict[str, Any]:
#         """Screen the candidate"""
#         print("Screener: Conducting initial screening...")
#
#         try:
#             # Assume message[-1]["content"] is a dict in string format
#             workflow_context = eval(message[-1]["content"])  # Safer with json.loads if it's actually JSON
#             prompt = f"Screen this candidate:\n{workflow_context}"
#
#             raw_output = self._query_ollama(prompt)
#             parsed_output = self._parse_json_safely(raw_output)
#
#             return {
#                 "screening_report": parsed_output,
#                 "screening_timestamp": datetime.now().isoformat(),
#                 "screening_score": 85  # Hardcoded for now, or could be extracted from parsed_output
#             }
#
#         except Exception as e:
#             print(f"Error during screening: {str(e)}")
#             return {
#                 "error": "Failed to complete screening.",
#                 "details": str(e)
#             }


from typing import Dict, Any
from .base_agent import BaseAgent
from datetime import datetime
import json


class ScreenerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Screener",
            instructions="""
            Screen candidates based on:
            - Qualification alignment
            - Experience relevance
            - Skill match percentage
            - Cultural fit indicators
            - Red flags or concerns

            Provide a comprehensive and structured screening report in JSON format.
            """
        )

    async def run(self, message: list) -> Dict[str, Any]:
        print("Screener: Conducting initial screening...")

        try:
            workflow_context = json.loads(message[-1]["content"])
            prompt = f"Screen this candidate based on the following data:\n{json.dumps(workflow_context, indent=2)}"

            raw_output = self._query_ollama(prompt)
            parsed_output = self._parse_json_safely(raw_output)

            return {
                "screening_report": parsed_output,
                "screening_timestamp": datetime.now().isoformat(),
                "screening_score": parsed_output.get("score", 85)
            }

        except Exception as e:
            print(f"Error during screening: {e}")
            return {
                "error": "Failed to complete screening.",
                "details": str(e)
            }

