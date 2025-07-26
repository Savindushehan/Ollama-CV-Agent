from typing import Dict, Any
from .base_agent import BaseAgent
from datetime import datetime
import json


class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Matcher",
            instructions="""
            Match candidate profile with job positions.
            Consider:
              - Skill match
              - Experience level
              - Location preferences

            Provide detailed reasoning and compatibility scores.
            Return matches in JSON format with fields:
              - title
              - match_score
              - location
            """
        )

    async def run(self, messages: list) -> Dict[str, Any]:
        """Match candidate with available positions"""
        print("Matcher: Finding suitable job matches...")

        try:
            # Load structured candidate analysis results from previous step
            analysis_result = json.loads(messages[-1]["content"])

            # Sample jobs for matching (can be loaded from external source in future)
            sample_jobs = [
                {
                    "title": "Senior Software Engineer",
                    "requirements": "Python, Cloud, 5+ years experience",
                    "location": "Remote"
                },
                {
                    "title": "Data Scientist",
                    "requirements": "Python, ML, Statistics, 3+ years experience",
                    "location": "New York"
                }
            ]

            # Create a prompt for the LLM
            prompt = f"""
Analyze the following candidate profile and match it against available job listings.
Return ONLY a JSON object with the exact structure:

{{
  "matched_jobs": [
    {{
      "title": "job title",
      "match_score": "85%",
      "location": "job location"
    }}
  ],
  "match_timestamp": "{datetime.now().isoformat()}",
  "number_of_matches": <number>
}}

Candidate Profile:
{json.dumps(analysis_result)}

Available Jobs:
{json.dumps(sample_jobs)}
"""

            # Query Ollama
            raw_response = self._query_ollama(prompt)
            parsed_result = self._parse_json_safely(raw_response)

            return parsed_result

        except Exception as e:
            print(f"Error during matching: {str(e)}")
            return {
                "error": "Failed to match candidate with jobs.",
                "details": str(e)
            }
