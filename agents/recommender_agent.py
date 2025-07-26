# from typing import Dict, Any
# from .base_agent import BaseAgent
#
#
# class RecommenderAgent(BaseAgent):
#     def __init__(self):
#         super().__init__(
#             name="Recommender",
#             instructions="""Generate final recommendations considering:
#             1. Extracted profile
#             2. Skills analysis
#             3. Job matches
#             4. Screening results
#             Provide clear next steps and specific recommendations."""
#         )
#
#     async def run(self, message: list) -> Dict[str, Any]:
#         """Generate final recommendations"""
#         print("Recommender: Generating final recommendations")
#
#         # Parse the last message (assumed to be a dict-like context)
#         workflow_context = eval(message[-1]["content"])
#
#         # Convert the dict to string for LLM prompt
#         recommendation = self._query_ollama(str(workflow_context))
#
#         # Return final structured output
#         return {
#             "final_recommendation": recommendation,
#             "recommendations_timestamp": "2024-03-14",
#             "confidence_level": "high"
#         }


from typing import Dict, Any
from .base_agent import BaseAgent


class RecommenderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Recommender",
            instructions="""
            Generate final recommendations considering:
            1. Extracted profile
            2. Skills analysis
            3. Job matches
            4. Screening results
            Provide clear next steps and specific recommendations.
            """
        )

    async def run(self, message: list) -> Dict[str, Any]:
        print("Recommender: Generating final recommendations")

        try:
            workflow_context = eval(message[-1]["content"])
            prompt = f"Based on the following workflow context, provide clear final recommendations:\n{workflow_context}"

            recommendation = self._query_ollama(prompt)

            return {
                "final_recommendation": recommendation,
                "recommendations_timestamp": "2024-03-14",
                "confidence_level": "high"
            }
        except Exception as e:
            print(f"Recommender error: {e}")
            return {
                "error": "Failed to generate recommendations.",
                "details": str(e)
            }

