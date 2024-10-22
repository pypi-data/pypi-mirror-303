
def main():
    from crewai import Agent, Task, Crew
    from crewai_tools import (
      FileReadTool,
      ScrapeWebsiteTool,
      MDXSearchTool,
      SerperDevTool
    )

    from IPython.display import Markdown, display

    import os
    os.environ['OPENAI_API_KEY'] = input("Enter your OPENAI_API_KEY")
    os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'

    import os
    os.environ['SERPER_API_KEY'] = input('Enter your SERPER_API_KEY')

    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()


    # Agent 1: Researcher
    researcher = Agent(
        role="Grant funding researcher",
        goal="Make sure to do amazing analysis on "
             "the grant funding opportunity at {grant_funding_url} to help {faculty}.",
        tools = [scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "As a Researcher, your prowess is in "
            "navigating and extracting critical "
            "information from the grant funding opportunity at {grant_funding_url} is unmatched."
            "Your skills help pinpoint the necessary "
            "qualifications and requirements as posted by the"
            "funding organizer at {grant_funding_url}, forming the foundation for "
            "effective grant funding application."
        )
    )

    # Agent 2: Profiler
    profiler = Agent(
        role="Personal Profiler for {faculty}",
        goal="Do increditble research on {faculty}"
             "to help them stand out among the grant funding applications.",
        tools = [scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "Equipped with analytical prowess, you dissect "
            "and synthesize information "
            "from diverse sources to craft comprehensive "
            "grant funding proposal, laying the "
            "groundwork for an amazing grant application for {faculty} and their lab."
        )
    )

    research_project_creator= Agent(
        role="Senior research project creator for {faculty}",
        goal="Find all the best projects that {faculty}"
             "can start in their lab for which they can successfully secure the grant funding as indicated in {grant_funding_url}.",
        tools = [scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "With an exceptional performance in finding new research ideas for which the grant funding agency at {grant_funding_url} will approve the grant funding."
            "You are exceptional in coordinating with the profiler agent to see which new research projects/ideas that {faculty} and their lab can start working on."
            "you ensure that the new research idea resonate perfectly with the funding requirements."
            "You back your new research idea based on past research work done by {faculty} with their **collaborators**."
            "You always cite any idea you are collecting from other research work."

        )
    )

    # Agent 3: Resume Strategist
    proposal_strategist = Agent(
        role="Proposal Strategist for securing grant funding at {grant_funding_url} for {faculty}",
        goal="Find all the best ways to make the "
             "grant proposal stand out among all the past successful grant proposals at {grant_funding_url}.",
        tools = [scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "With a strategic mind and an eye for detail, you "
            "excel at refining proposals to highlight the most "
            "relevant skills and resaerch work done by the {faculty}, ensuring they "
            "resonate perfectly with the funding requirements."
            "You also excel in finding past successful grant applications which secured funding from {grant_funding_url}."

        )
    )

    researcher_task = Task(
        description=(
            "Analyze the grant funding posting URL provided ({grant_funding_url}) "
            "to extract all key requirements for securing the funding."
            "You also collect any other links you find in the website and analyse the content in those links to extract any information neccesary."

        ),
        expected_output=(
            "A structured list of all the requirements for securing funding at {grant_funding_url}."

        ),
        agent=researcher,
        async_execution=True
    )

    profiler_task = Task(
        description=(
            "Compile a detailed personal and professional profile of {faculty}"
            "using the Google Scholar link: ({scholar_link}), and personal write-up "
            "({writeup}) and website ({website}). Utilize tools to extract and "
            "synthesize information from these sources."
        ),
        expected_output=(
            "A comprehensive profile document on {faculty}'s work."

        ),
        agent=profiler,
        async_execution=True
    )

    research_project_creator_task = Task(
        description=(
            "Using the profile and proposal requirements obtained from the "
            "previous tasks, find new research projects/ideas that {faculty} can start working on."
            "Ensure that the new research idea resonate perfectly with the funding requirements."
            "Back your new research idea based on past research work done by {faculty} with their collaborators."
            "Always cite any idea you are collecting from other research work."
            "don't make up any information. The new research idea should be backed by a thorough literature survey."
        ),
        expected_output=(
            "Confirmation of a well proposed and well documented research idea which {faculty} can start working on."
        ),
        human_input=True,
        output_file="List_of_projects.md",
        context=[researcher_task, profiler_task],
        agent=research_project_creator
    )


    proposal_strategist_task = Task(
        description=(
            "Using the gatheres info on {faculty}, the grant funding opportunity at {grant_funding_url}, and the agreed upon research project from the previous task,"
            "tailor the proposal so that it is the best proposal for funding opportunity at {grant_funding_url}."
        ),
        expected_output=(
            "A final proposal for successfully securing funding at {grant_funding_url}."
        ),
        output_file="proposal.md",
        context=[researcher_task, profiler_task,research_project_creator_task],
        agent=proposal_strategist
    )

    crew = Crew(
        agents=[researcher,profiler,research_project_creator,proposal_strategist],

        tasks=[researcher_task,
               profiler_task,
               research_project_creator_task,
               proposal_strategist_task],

        verbose=True
    )


    proposal_inputs = {
        'faculty' : input("Enter your name with designation: eg: Prof. Thomas..."),
        'grant_funding_url': input("Enter the funding opportunity website"),
        'scholar_link': input("Enter your Google scholar link"),
        'writeup': input("Enter any specification for creating the proposal:"),
        'website': input("Enter your personal website")
    }


    result = crew.kickoff(inputs=proposal_inputs)


    display(Markdown("./List_of_projects.md"))


    display(Markdown("./proposal.md"))

if __name__ == '__main__':
    main()