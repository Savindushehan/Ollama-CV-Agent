# from typing import Dict, Any
# from .base_agent import BaseAgent
#
#
# class AnalyzerAgent(BaseAgent):
#     def __init__(self):
#         super().__init__(
#             name="Analyzer",
#             instructions="""
#             Analyze the extracted resume data and provide:
#             - A breakdown of technical and soft skills.
#             - Estimated total experience in years.
#             - Summary of education and certifications.
#             - Key strengths and potential weaknesses.
#             - Return output in structured JSON format.
#             """
#         )
#
#     async def run(self, message: list) -> Dict[str, Any]:
#         """Analyze the extracted resume information"""
#         print("Analyzer: Analyzing extracted resume data")
#
#         try:
#             extracted_data = eval(message[-1]["content"])
#             analysis_input = str(extracted_data)
#             analysis_response = self._query_ollama(analysis_input)
#             return {
#                 "skills_analysis": analysis_response,
#                 "analysis_status": "completed"
#             }
#         except Exception as e:
#             print(f"Analyzer error: {e}")
#             return {
#                 "error": str(e),
#                 "analysis_status": "failed"
#             }


from typing import Dict, Any
from .base_agent import BaseAgent


class AnalyzerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Analyzer",
            instructions="""
            Analyze the extracted resume data and provide:
            - A breakdown of technical and soft skills.
            - Estimated total experience in years.
            - Summary of education and certifications.
            - Key strengths and potential weaknesses.
            - Return output in structured JSON format.
            """
        )

    async def run(self, message: list) -> Dict[str, Any]:
        print("Analyzer: Analyzing extracted resume data")

        try:
            extracted_data = eval(message[-1]["content"])
            analysis_input = str(extracted_data)
            analysis_response = self._query_ollama(analysis_input)
            return {
                "skills_analysis": analysis_response,
                "analysis_status": "completed"
            }
        except Exception as e:
            print(f"Analyzer error: {e}")
            return {
                "error": str(e),
                "analysis_status": "failed"
            }

