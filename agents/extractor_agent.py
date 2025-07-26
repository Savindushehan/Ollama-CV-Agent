# from typing import Dict, Any
# from pdfminer.high_level import extract_text
# from .base_agent import BaseAgent
# import json
#
#
# class ExtractorAgent(BaseAgent):
#     def __init__(self):
#         super().__init__(
#             name="Extractor",
#             instructions="""
#             Extract and structure information from resumes. Focus on:
#             - Personal information (Name, Email, Phone)
#             - Work experience (Companies, Roles, Duration)
#             - Education (Degrees, Institutions, Years)
#
#             Provide output in a clear, structured JSON format.
#             """
#         )
#
#     async def run(self, message: list) -> Dict[str, Any]:
#         """Process the resume and extract structured information"""
#         print("Extractor: Processing resume...")
#
#         try:
#             # Safely load resume data (expecting JSON string in message content)
#             resume_data = json.loads(message[-1]["content"])
#
#             # Extract text from PDF if file path is provided
#             if resume_data.get("file_path"):
#                 raw_text = extract_text(resume_data["file_path"])
#             else:
#                 raw_text = resume_data.get("text", "")
#
#             # Query Ollama to extract structured info
#             extract_info = self._query_ollama(raw_text)
#             structured_data = self._parse_json_safely(extract_info)
#
#             return {
#                 "raw_text": raw_text,
#                 "structured_data": structured_data,
#                 "extraction_status": "completed"
#             }
#
#         except Exception as e:
#             print(f"Error during extraction: {str(e)}")
#             return {
#                 "error": "Failed to extract resume information",
#                 "details": str(e)
#             }


from typing import Dict, Any
from pdfminer.high_level import extract_text
from .base_agent import BaseAgent
import json


class ExtractorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Extractor",
            instructions="""
            Extract and structure information from resumes. Focus on:
            - Personal information (Name, Email, Phone)
            - Work experience (Companies, Roles, Duration)
            - Education (Degrees, Institutions, Years)

            Provide output in a clear, structured JSON format.
            """
        )

    async def run(self, message: list) -> Dict[str, Any]:
        print("Extractor: Processing resume...")

        try:
            resume_data = json.loads(message[-1]["content"])

            if resume_data.get("file_path"):
                raw_text = extract_text(resume_data["file_path"])
            else:
                raw_text = resume_data.get("text", "")

            extract_info = self._query_ollama(raw_text)
            structured_data = self._parse_json_safely(extract_info)

            return {
                "raw_text": raw_text,
                "structured_data": structured_data,
                "extraction_status": "completed"
            }

        except Exception as e:
            print(f"Error during extraction: {str(e)}")
            return {
                "error": "Failed to extract resume information",
                "details": str(e)
            }

