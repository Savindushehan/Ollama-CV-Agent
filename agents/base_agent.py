
from typing import Dict, Any
import json
from openai import OpenAI


class BaseAgent:
    def __init__(self,name: str, instructions:str):
        self.name = name
        self.instructions = instructions
        self.Ollama_client = OpenAI(
            base_url = "http:/localhost:11434/v1",
            api_key="ollama",
        )
    async  def run(self, message:list) -> Dict[str, Any] :
        """Default run method to be overidden by child classses"""
        raise  NotImplementedError("Subclasses mujst implement run()")