## What went wrong:
1. the criteria for what was considered "duration" of the role was unclear. In one case, the AI mistook the job's application limit period for the internship duration. 
2. The original tool-call arguments were also not included, which meant that things like profile fit were unverified. 
3. there was some mistmatch the role's qualification requirements and the user's profile. Ex: one of the roles required master’s study and graduation in 2027–28, conflicting with the undergraduate profile graduating in 2029.

## Diagnosis of why:
For the unclear criteria, I think it was the fact that a lot of the raw excerpts required interpretation which got fuzzy with AI. 
For the original tool-call arguments, I used a separate session for this and didn't paste the previous info. 
For the mismatch, it was because AI didn't verify every role individually and only hcecked against a subset of the. 

## What I changed and rerun results:
I updated the MCP server to include individual assessments of all the roles, not just a subset of them. I also gave it more specific guidelines to follow when it came to what was considered duration vs. not. The  duration extractor now requires internship-related timing and excludes application limits, leave benefits, experiment requirements, and graduation dates, with all four regression tests passing. I used the same session for the checker so that the original tool-call prompts and responses were preserved.

The result after the 3rd run was that all of the requirements were MET after rerunning with the same user profile. 