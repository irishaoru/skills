## Task used on:
Finding summer 2027 internships relevant to my background and organizing the results into an Excel spreadsheet.

## Run #1 - MCP Tool:
**Prompts**:
Me: 
find me internships using the mcp tool
Agent Output:
Before searching, tell me:
1. Education: level, major, expected graduation date.
2. Skills and experience: languages, projects, or past work.
3. Target roles: software engineering, data, product, etc.
4. Location: preferred cities/countries and remote preference.
5. Availability: start date and how many weeks/months.
6. Companies: any preferences? We can start with Stripe.
You can leave anything unspecified. I’ll use your answers to review the listings and provide an .xlsx file.
Me:
grad date: 2029, major: business administration, sophomore. 3. product, strategy, data analytics. 4. NYC, hybrid, remote, CA, 5. May - September 2027. I have done consulting projects through 180 degrees consulting and tartan marketing association, competed in multiple case competitions, including 2nd place for BNY x 180 degrees and 1st place in Deloitte CMU roudn and 4th place Deloitte Naitonals. Python, excel, canva, powerpoint, HTML, JavaScript, CSS are my skills
Agent output:
I used the internship MCP tool and found these promising options for summer 2027. My fit assessment prioritizes your consulting projects, case competition results, and Excel/Python skills.
All five specify 12 weeks in summer 2027; exact start dates need confirmation. Their descriptions don’t state a graduation-year restriction, so your 2029 graduation isn’t explicitly excluded, but eligibility remains unconfirmed.

I’d prioritize Strategic Sourcing, Acceleration Programs, and People Analytics. Coinbase limits candidates to three applications within six months, so choose carefully.

I also checked Stripe’s Data Analyst internship, but it requires graduation in December 2027 or spring/summer 2028, which conflicts with your 2029 date.

[Download the spreadsheet](../evidence/internships-run1.xlsx) It contains search candidates, including roles outside your preferences—not a verified eligibility shortlist.

## Run #1 - Checker review (Ran in a separate, fresh session):
Me:
use the assignment check skill to check this spreadsheet result mets the requirements of the MCP tool: (attached the file named: internships-MCP server.xlsx - renamed from before)
Agent Output: 
The spreadsheet meets the MCP’s export structure, but full compliance is only partially verified. It contains 50 candidates, including education mismatches, without individual fit assessments.
Broad candidates are permitted by the MCP contract, so mismatches alone do not establish a filtering failure. The missing evidence is whether those mismatches were explained to the user.

| Requirement | Status | Evidence or gap |
| --- | --- | --- |
| Export nine specified columns | MET | `Internships!A1:I51` contains all nine columns and 450 nonempty data cells. |
| Return internship titles; maximum 50 rows | MET | Exactly 50 candidates. Every title contains “Intern” or “Internship.” |
| Include application links | MET | `Internships!G2:G51` contains 50 unique URLs with matching native hyperlinks. |
| Preserve five profile fields | MET | `Search context!A6:B10` records education, skills, interests, locations, and availability. |
| Identify source and explain date meaning | MET | Every source is Greenhouse. `Search context!B3:B4` explains board identifiers and last-updated dates. |
| Include pay, duration, and qualification excerpts | MET | All three evidence columns exist. Missing evidence uses “Not specified.” |
| Interpret evidence accurately | PARTIAL | `Internships!E2` includes an application-limit period unrelated to internship duration. `Internships!F5` describes a responsibility rather than a qualification. Raw excerpts require interpretation. |
| Assess every candidate’s fit and unknown requirements | PARTIAL | The workbook warns that eligibility is unverified but contains no individual assessments. `Internships!F50:F51` requires master’s study and graduation in 2027–28, conflicting with the undergraduate profile graduating in 2029. An accompanying assessment could satisfy this requirement. |
| Apply supplied board, keyword, location, and limit arguments | UNVERIFIED | Original tool-call arguments are unavailable. Singapore, Toronto, and other locations appear, but profile preferences alone do not establish which filter was passed. |
| Report failed boards separately | UNVERIFIED | No board errors appear in the context sheet. The original response is needed to establish whether any boards failed. |
| Collect profile before searching | UNVERIFIED | The profile is saved, but its presence does not prove intake occurred before this search. |
| Keep profile local | UNVERIFIED | Current code sends only `content=true` to Greenhouse, but this workbook cannot establish the originating execution’s behavior. |
| Return `xlsx_path` and deliver a link or attachment | PARTIAL | The XLSX exists. The originating response is needed to verify the returned path and delivery. |
| Submit no applications | UNVERIFIED | The workbook cannot establish execution history. |

Highest-priority next actions:
1. Supply the original tool arguments and response to verify filters, errors, and delivery.
2. Supply the accompanying candidate assessments, or flag education, location, and availability conflicts individually.
3. Interpret noisy excerpts before presenting them as confirmed pay, duration, or qualifications.
Checks performed: read-only Python inspection of XLSX XML, ZIP integrity, cell completeness, title matching, URL uniqueness, and hyperlink targets. No files changed.
Not checked: live listing availability, visual rendering in Excel/Sheets, or the original search execution.

The checker noted that the iniitail fit assessment was unverified just based on the spreadsheet I uploaded. I didn't include the initial conversations of me requesting for internships and the agent asking for my relevant background as that was part of how the MCP server was supposed to work. I agree with this and will provide it more info next time I test the tool. The checker has pointed out that there was "noisy duration." For example, some things like the application limit and benefits came in numbers, which the server interpreted as the duration of the internship and incorrectly used those figures in the spreadsheet. 

## Run #2 - MCP Tool:
Inserted the same initial prompts to get the conversation started.
Agent Output:
I searched 10 companies’ Greenhouse boards using the internship MCP tool. These are your strongest matches from the listings reviewed, based on your consulting experience, business major, and Excel/Python skills.

All five are 12-week summer 2027 internships. Exact start dates and work-authorization eligibility still need confirmation.
Opportunity	Location / pay	Fit and requirements to check
Coinbase — Strategic Sourcing Intern	Hybrid NYC · $40/hr	Strong fit: accepts business majors; involves vendor research, pricing analysis, and strategic recommendations. Requires interest in digital assets.
Coinbase — Institutional Operations Intern	Hybrid NYC · $40/hr	Strong fit: accepts business majors; combines data analysis, process improvement, and collaboration with Product and Engineering. Banking knowledge and crypto interest required.
Coinbase — Acceleration Programs Intern	Hybrid NYC · $40/hr	Your consulting projects align with project management, program evaluation, and presenting recommendations. Work focuses on employee programs.
Coinbase — People Analytics Intern	Hybrid NYC · $40/hr	Excel analysis and presentations align well. Requires an analytical degree or related field; confirm whether your business coursework qualifies.
Coinbase — Associate Product Manager Intern	Hybrid SF; description also lists an NYC team · $55/hr	Stretch: directly matches your product interests, but requires experience shipping a product/feature and demonstrated crypto experience—neither is established by your profile yet.


None of these descriptions specifies a graduation-year restriction, so 2029 is not explicitly excluded. That does not establish full eligibility.

I excluded Stripe’s Data Analyst internship because it requires graduation in December 2027 or spring/summer 2028, and Airbnb’s Advanced Analytics internship because it requires a master’s student.

Prioritize Strategic Sourcing and Institutional Operations. Coinbase limits candidates to three applications within six months, so choose your third carefully.

[Download the 50-listing search workbook](../evidence/internships-run2.xlsx). It contains search candidates, including roles outside your preferences; the table above is the reviewed shortlist.

## Run #2 - Checker review (in the same session)
Gave it the same input as Run #1.
Agent Output:
The spreadsheet partially meets the MCP tool’s requirements. It is a valid export of search candidates, but the required candidate-by-candidate fit review is incomplete.

Reviewed: [Run 2 spreadsheet](../evidence/internships-run2.xlsx) (repository copy of `internships-3d74c4e9bb6d.xlsx`).

Requirements source: the MCP tool contract in [server.py (line 53)](/Users/irishao/Documents/GitHub/skills/internship-mcp/server.py:53). A separate agent independently inspected the workbook because this session produced it.

| Requirement | Status | Evidence or gap |
| --- | --- | --- |
| Collect education, skills, interests, locations, and availability before searching | MET | Transcript confirms intake; all five fields appear in `Search context!B6:B10`. |
| Search 1–10 selected Greenhouse boards | MET | Recorded call supplied 10 boards; response reported no board errors. |
| Return 1–50 internship listings | MET | `Internships!A2:I51` contains 50 records; every title passes the internship-title check. |
| Apply supplied keyword and location filters | MET | Both filters were blank, so broad results comply with the call. Your profile itself does not filter results. |
| Supply spreadsheet-ready records and application links | MET | Nine populated columns, 50 hyperlink records, no duplicate application URLs; XLSX integrity check passed. |
| Save the XLSX and provide a clickable link | MET | File exists and was linked in the previous response. |
| Explain uncertainty without guaranteeing eligibility | MET | `Search context!B1:B4` contains caveats; previous response explicitly qualified eligibility. |
| Assess **each candidate** against the profile using description evidence | PARTIAL | Previous response assessed five shortlisted candidates, not all 50. The workbook has no individual fit assessments. |
| Verify eligibility at each listing | PARTIAL | Some requirements were checked using returned descriptions; individual verification for all 50 listings is not documented. |
| Keep profile local; submit no applications | MET | Recorded workflow only searched; server code sends board requests without profile data. |

The independent review also found evidence-extraction limitations:
- F2 says “Not specified” despite required skills in the returned description.
- F5 omits the APM role’s required shipped-product and crypto experience.
- E48 says “Not specified” despite summer 2027 timing in the description.
These omissions make the workbook insufficient for deciding eligibility by itself.

The highest-priority next actions are to assess all 50 candidates, verify eligibility from their linked listings, and correct incomplete qualification/timing excerpts. The 86 total matches and board-order truncation should also be recorded for clarity.

Not checked: visual rendering or opening/importing in Excel or Google Sheets. No files were changed.

The checker noted that both assessment fit and verifying eligibility were not done for all 50 job opportunities included in the spreadsheet. The AI agent itself told me it only checked a subset of the jobs for both of these criteria baseed on the server code and our conversation.
