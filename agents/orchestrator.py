# from typing import Dict, Any
# from .base_agent import BaseAgent
# from .extractor_agent import ExtractorAgent
# from .analyzer_agent import AnalyzerAgent
# from .matcher_agent import MatcherAgent
# from .screener_agent import ScreenerAgent
# from .recommender_agent import RecommenderAgent
#
# class OrchestratorAgent(BaseAgent):
#     def __init__(self):
#         super().__init__(
#             name="Orchestrator",
#             instructions="""Coordinate the recruitment workflow and delegate tasks to specialized agents.
#             Ensure proper flow of information between extraction, analysis, matching, screening, and recommendation phases.
#             Maintain context and aggregate results from each stage."""
#         )
#         self._setup_agents()
#
#     def _setup_agents(self):
#         """Initialize all specialized agents"""
#         self.extractor = ExtractorAgent()
#         self.analyzer = AnalyzerAgent()
#         self.matcher = MatcherAgent()
#         self.screener = ScreenerAgent()
#         self.recommender = RecommenderAgent()
#
#     async def run(self, messages: list) -> Dict[str, Any]:
#         """Process a single message through the Orchestrator agent"""
#         prompt = messages[-1]["content"]
#         response = self._query_ollama(prompt)
#         return self._parse_json_safely(response)
#
#     async def process_application(self, resume_data: Dict[str, Any]) -> Dict[str, Any]:
#         """Main workflow orchestrator for processing job applications"""
#         print("Orchestrator: Starting application process")
#
#         workflow_context = {
#             "resume_data": resume_data,
#             "status": "initiated",
#             "current_stage": "extraction"
#         }
#
#         try:
#             # Extract resume information
#             extracted_data = await self.extractor.run(
#                 [{"role": "user", "content": str(resume_data)}]
#             )
#             workflow_context.update({
#                 "extracted_data": extracted_data,
#                 "current_stage": "analysis"
#             })
#
#             # Analyze candidate profile
#             analysis_results = await self.analyzer.run(
#                 [{"role": "user", "content": str(extracted_data)}]
#             )
#             workflow_context.update({
#                 "analysis_result": analysis_results,
#                 "current_stage": "matching"
#             })
#
#             # Match with jobs
#             job_matches = await self.matcher.run(
#                 [{"role": "user", "content": str(analysis_results)}]
#             )
#             workflow_context.update({
#                 "job_matches": job_matches,
#                 "current_stage": "screening"
#             })
#
#             # Screen candidate
#             screening_report = await self.screener.run(
#                 [{"role": "user", "content": str(workflow_context)}]
#             )
#             workflow_context.update({
#                 "screening_report": screening_report,
#                 "current_stage": "recommendation"
#             })
#
#             # Generate recommendation
#             recommendations = await self.recommender.run(
#                 [{"role": "user", "content": str(workflow_context)}]
#             )
#             workflow_context.update({
#                 "recommendations": recommendations,
#                 "current_stage": "completed",
#                 "status": "done"
#             })
#
#             return workflow_context
#
#         except Exception as e:
#             print(f"Orchestrator error: {e}")
#             workflow_context["status"] = "error"
#             workflow_context["error_message"] = str(e)
#             return workflow_context

from typing import Dict, Any
from .base_agent import BaseAgent
from .extractor_agent import ExtractorAgent
from .analyzer_agent import AnalyzerAgent
from .matcher_agent import MatcherAgent
from .screener_agent import ScreenerAgent
from .recommender_agent import RecommenderAgent

from typing import Dict, Any
from .base_agent import BaseAgent
from .extractor_agent import ExtractorAgent
from .analyzer_agent import AnalyzerAgent
from .matcher_agent import MatcherAgent
from .screener_agent import ScreenerAgent
from .recommender_agent import RecommenderAgent
import json


class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Orchestrator",
            instructions="""Coordinate the recruitment workflow and delegate tasks to specialized agents.
            Ensure proper flow of information between extraction, analysis, matching, screening, and recommendation phases.
            Maintain context and aggregate results from each stage."""
        )
        self._setup_agents()

    def _setup_agents(self):
        """Initialize all specialized agents"""
        self.extractor = ExtractorAgent()
        self.analyzer = AnalyzerAgent()
        self.matcher = MatcherAgent()
        self.screener = ScreenerAgent()
        self.recommender = RecommenderAgent()

    async def run(self, messages: list) -> Dict[str, Any]:
        """Process a single message through the Orchestrator agent"""
        prompt = messages[-1]["content"]
        response = self._query_ollama(prompt)
        return self._parse_json_safely(response)

    async def process_application(self, resume_data: Dict[str, Any]) -> Dict[str, Any]:
        """Main workflow orchestrator for processing job applications"""
        print("Orchestrator: Starting application process")

        workflow_context = {
            "resume_data": resume_data,
            "status": "initiated",
            "current_stage": "extraction"
        }

        try:
            # Extract resume information
            extracted_data = await self.extractor.run(
                [{"role": "user", "content": json.dumps(resume_data)}]
            )
            workflow_context.update({
                "extracted_data": extracted_data,
                "current_stage": "analysis"
            })

            # Analyze candidate profile
            analysis_results = await self.analyzer.run(
                [{"role": "user", "content": json.dumps(extracted_data)}]
            )
            workflow_context.update({
                "analysis_result": analysis_results,
                "current_stage": "matching"
            })

            # Match with jobs
            job_matches = await self.matcher.run(
                [{"role": "user", "content": json.dumps(analysis_results)}]
            )
            workflow_context.update({
                "job_matches": job_matches,
                "current_stage": "screening"
            })

            # Screen candidate
            screening_report = await self.screener.run(
                [{"role": "user", "content": json.dumps(workflow_context)}]
            )
            workflow_context.update({
                "screening_report": screening_report,
                "current_stage": "recommendation"
            })

            # Generate recommendation
            recommendations = await self.recommender.run(
                [{"role": "user", "content": json.dumps(workflow_context)}]
            )
            workflow_context.update({
                "recommendations": recommendations,
                "current_stage": "completed",
                "status": "done"
            })

            return workflow_context

        except Exception as e:
            print(f"Orchestrator error: {e}")
            workflow_context["status"] = "error"
            workflow_context["error_message"] = str(e)
            return workflow_context
