from typing import Dict, Any
from agent_wrapper import Agent

# Profile Enhancer function: Enhances the candidate's profile summary
def profile_enhancer_agent_function(extracted_info: Dict[str, Any]) -> Dict[str, Any]:
    enhanced_profile = extracted_info.copy()

    # Safely calculate total years of experience
    experience_entries = extracted_info.get("experience", [])
    total_experience_years = sum(item.get("years", 0) for item in experience_entries if isinstance(item, dict))

    name = extracted_info.get("name", "The candidate")

    # Add a summary based on the extracted data
    enhanced_profile["summary"] = (
        f"{name} has approximately {total_experience_years} year(s) of experience across relevant roles."
    )

    return enhanced_profile

# Define the agent using the Swarm framework
profile_enhancer_agent = Agent(
    name="Profile Enhancer Agent",
    model="llama3:latest",
    instructions="Enhance the candidate's profile based on the extracted information.",
    functions=[profile_enhancer_agent_function]
)
