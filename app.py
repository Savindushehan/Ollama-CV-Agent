import asyncio
from agents.orchestrator import OrchestratorAgent

async def main():
    print("🚀 CV Analysis AI Agent System")

    # Sample resume input (replace the file_path with a real file if available)
    resume_input = {
        "file_path": "./resumes/Savindu_Shehan_CV.pdf"
        # Or use raw text instead:
        # "text": "John Doe\nSoftware Engineer\n5 years experience in Python and ML..."
    }

    # Initialize orchestrator agent
    orchestrator = OrchestratorAgent()

    # Process the resume through the full workflow
    results = await orchestrator.process_application(resume_input)

    print("\n✅ Final Recommendation and Workflow Results:")
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
