#
# from typing import Dict, Any
# import json
# from openai import OpenAI
#
#
# class BaseAgent:
#     def __init__(self,name: str, instructions:str):
#         self.name = name
#         self.instructions = instructions
#         self.Ollama_client = OpenAI(
#             base_url="http://localhost:11434/v1",
#             api_key="ollama",
#         )
#     async  def run(self, message:list) -> Dict[str, Any] :
#         """Default run method to be overidden by child classses"""
#         raise  NotImplementedError("Subclasses must implement run()")
#
#     def _query_ollama(self, prompt:str)-> str:
#         """Query Ollama model with the given prompt"""
#
#         try:
#             response = self.Ollama_client.chat.completions.create(
#                 model = "gemma3:latest",
#             messages=[
#                     {"role":"system","content":self.instructions},
#                     {"role":"user","content":prompt},
#                 ],
#                 temperature=0.7,
#                 max_tokens=2000
#             )
#             return response.choices[0].message.content
#         except Exception as e:
#             print(f"Error Querying Ollama:{str(e)}")
#             raise
#
#     def _parse_json_safely(self, text:str) -> Dict[str, Any]:
#         """Safely parse JSON from text, handling potential errors"""
#
#         try:
#             # Try to find Json like content between curly braces
#             start = text.find("{")
#             end = text.rfind("}")
#             if start != -1 and end != -1:
#                 json_str = text[start : end +1]
#                 return json.loads(json_str)
#             return {"error": "No JSON content found"}
#         except json.JSONDecodeError:
#             return {"error": "Invalid JSON copntent"}


from typing import Dict, Any
import json
from openai import OpenAI


class BaseAgent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        self.Ollama_client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",
        )
        self.model = "gemma3:latest"

    async def run(self, message: list) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement run()")

    def _query_ollama(self, prompt: str) -> str:
        try:
            response = self.Ollama_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=2000,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error Querying Ollama: {str(e)}")
            raise

    def _parse_json_safely(self, text: str) -> Dict[str, Any]:
        try:
            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1:
                json_str = text[start : end + 1]
                return json.loads(json_str)
            return {"error": "No JSON content found"}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON content"}
