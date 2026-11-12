## What the skill does:
It is an assignment criteria checker that checks the user's current HW/project against the criteria posted online. It triggers whenever the user asked to check against assignment criteria, find missing deliverables, or review readiness to submit. It's also prompted if the user simply types in "assignment check" along with the appropriate link, text or document file. 

## What the MCP tool does:
The MCP tool uses Greenhouse company boards to find a list of internships and give it back to the users in the form of an .xlsx file that they can open in Excel or import it into Google Sheets.

## Motivations for the skill:
Previously having to ask the agent to check my work against the assignment criteria repeatedly. 
Prompt log from vector database project: "is that still under chroma/abiding by assignment requirements?"
Prompt log from HW7: "do i have all of these in my readme to hand off: 
README.md This serves both someone who wants to run the game and the developer taking over. Include: How to install and run it on a machine that isn't yours
Controls, and anything else a player needs to know
Which acceptance criteria are already met, and which aren't
A map of the code: what each file, class, or major function is responsible for, so someone knows where to go to change a given behavior
What you'd do next, in priority order
Known bugs and traps (e.g. the thing that breaks when you resize the window, the function that looks reusable but isn't)
Where you cut corners, and why"


## Motivations for the MCP:
Time consuming and tedious for find internships one by one that are relevant and organize it in a spreadsheet. It would make my life a lot easier to have AI automate this process for me so that I can focus on the important part like actually applying for the roles.

## How to install both:
**Skill**:
1. Copy the assignment-check folder into the project you want checked. 
2. Start a fresh Codex session in that project. Reload VS Code if the skill doesn’t appear.

**MCP**:
1. Install Python and download or clone your toolkit repository.
2. Open a terminal in the toolkit repository and run:
python3 -m venv internship-mcp/.venv
internship-mcp/.venv/bin/python -m pip install -r internship-mcp/requirements.txt
3. Register it with Codex. Replace /absolute/path/to with the location of the downloaded repository:
codex mcp add internship-search -- /absolute/path/to/internship-mcp/.venv/bin/python /absolute/path/to/internship-mcp/server.py
4. Reload VS Code and start a fresh Codex session
5. Ask smething like: Help me find intenrships using the MCP tool.

## Which tools I confirmed it works in:
Assignment checker: Codex in VS Code.
Internship MCP server: Codex in VS Code - tool successfully returned Stripe internships 

## How AI was used in the assignment:
Codex drafted the SKILL.md and implemented the internship-search MCP server.
I managed changes in the MCP server such as switching from Adzuna to Greenhouse, adding profile questions, and exporting .xlsx files.

