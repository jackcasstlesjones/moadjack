# CHIRPdb Tranche 2: release descriptions

Tranche 2 is delivered in five releases. Each one leaves CHIRP with something people can use, and each builds on the one before. The work is grouped into eight user activities (the epics): Get access, Ask a question, Check the evidence, Spot patterns across reports, Learn from similar incidents, Report a problem, Keep the data accurate, and Run the service safely.

Estimates are build days, before contingency. Anything in [brackets] is a value CHIRP still needs to agree.

---

## Release 1: Staff chat

**16 November to 18 December 2026 · 15 stories · 26 days**

### Outcome

CHIRP staff can answer "how many" questions about UK and US marine accidents themselves, in minutes rather than by searching reports by hand, and they can trust each answer because every claim links to the page it came from.

### Who it's for

CHIRP staff only, signing in with their existing CHIRPdb accounts. Nothing is open to the public yet.

### What people can do

**Ask a question**

- Open a basic chat page, sign in with a staff account and type a question in plain English.
- Watch the answer appear as it is written, rather than waiting on a blank screen.
- Get answers drawn from the CHIRPdb database, not the AI's general knowledge.
- Ask for comparisons, such as UK against US collisions since 2015, and get the figures side by side with the biggest differences pointed out.
- Read answers in plain maritime English, with lessons that come only from the reports cited.
- Use the chat on a phone, in the main browsers, with a layout that works on small screens and with a keyboard or screen reader.

**Spot patterns across reports**

- Ask how many incidents match some criteria, such as fishing vessels that sank since 2016, and get one exact number that matches a direct database query.
- Combine several filters at once, such as vessel type, country, date range and deaths.
- Split counts into groups, such as by country or by vessel type, and count reports that mention particular words, such as "enclosed space".

**Check the evidence**

- Click any claim in an answer and open the source PDF at the right page.
- Rely on every claim having been checked against the passage it cites before the answer is shown. Figures are checked against the counting tool's result.
- See unsupported claims removed, after one retry, with a note saying so. If nothing useful is left, the chat says the question couldn't be answered from the reports.
- Know that answers are tested against a fixed set of questions with known right answers after every change, and that a failure stops the change going live.

**Learn from similar incidents**

- Ask for a toolbox talk or briefing on a task, and get one that fits on a page and cites real cases.
- Describe a near miss and be pointed to CHIRP's reporting form.

**Run the service safely**

- Use the chat at a secure web address, deployed automatically when changes pass their tests.
- See a clear message if something fails, such as the AI timing out or the provider being down, rather than a broken reply.
- Switch AI model by configuration, but only once the test set passes on the new model.
- CHIRP staff can see a log of every question, who asked it, which reports were used, how long it took and what it cost.

### Not in this release

Only UK and US reports are included, and only the basic fields compare like for like between them. There is no "find similar incidents" search, no follow-up questions, no SHIELD code review, and no public access.

### CHIRP to agree

Answer speed targets, the maximum number of tool calls per question, the size of the test set, the accessibility standard, the near-miss form address, and how long the question log is kept.

---

## Release 2: Full answers

**4 January to 29 January 2027 · 10 stories · 18 days**

### Outcome

Staff can compare UK and US accidents on any field with confidence that like is being compared with like, find past incidents similar to one they describe, and start building a checked set of SHIELD codes.

### Who it's for

CHIRP staff, including the people who review SHIELD codes.

### What people can do

**Ask a question**

- Ask a follow-up, such as "and in the US?", without repeating the original question.

**Spot patterns across reports**

- Compare UK and US reports on vessel type and accident type using one shared list of terms, so "fishing vessel", "fishing" and "trawler" count as the same thing.
- Do the same for outcome, severity and the remaining incident fields.
- Filter and group counts by the extra detail extracted from every UK and US report.

**Check the evidence**

- Rely on test-set questions covering every shared field.

**Learn from similar incidents**

- Describe what happened in your own words, such as "bulk carrier grounded at night, one person on watch", and get the most similar past incidents, closest first, each with a summary and a link.
- Ask for near-miss answers and task briefings that bring similar incidents together with their shared factors.

**Keep the data accurate**

- Review proposed SHIELD codes for every UK and US report in the review tool, and confirm or reject each one.
- Count by SHIELD code, using only codes a person has confirmed.

**Run the service safely**

- Have the chat monitored, with alerts on errors, tested backups, and visible usage and AI costs. A load test confirms it copes with the agreed number of users.

### Not in this release

The six other countries and CHIRP's own reports are not in answers yet, and duplicate reports of the same accident are still counted separately.

### CHIRP to agree

The load level for the load test.

---

## Release 3: All countries

**27 January to 12 March 2027 · 16 stories · 21 days**

### Outcome

Answers draw on every source CHIRP cares about, which means all eight countries plus CHIRP's own reports. Each accident counts once, the database keeps itself up to date, and useful patterns the AI finds are kept and reused rather than lost.

### Who it's for

CHIRP staff.

### What people can do

**Spot patterns across reports**

- Compare accidents across all eight countries on the same shared terms, one country added at a time. Any term that doesn't match is listed for CHIRP to map, rather than guessed.
- See reports of the same accident from different sources grouped together, matched on vessel name or IMO number, date and location. Uncertain matches go to staff to confirm.
- Get counts that treat each accident once, however many reports describe it, with a note on how many were combined. Counting by report is still possible on request.
- See patterns the AI finds in report text, such as "fatigue mentioned", saved for staff to approve, rename, edit or reject.
- Get the same, approved answer every time a known pattern comes up, including in reports added later.

**Ask a question**

- Get answers and counts that include CHIRP's own reports, labelled as CHIRP reports, with an option to leave them out.

**Keep the data accurate**

- Review proposed SHIELD codes for the six new countries in the same review tool, filtered by country.
- Have CHIRP's own reports imported, with confidential fields left out and no duplicates if the import is run again.
- Have every source checked for newly published reports on a schedule. New reports are processed and added to answers automatically, and staff can see what was added. If a source can't be reached, staff are told.

**Check the evidence**

- Rely on a test set that covers every country, CHIRP's reports, duplicate accidents and approved patterns. Every Release 2 question must still pass.

### Not in this release

There is still no public access.

### CHIRP to agree

The acceptable share of unmapped reports per country, SHIELD spot-check sizes and accuracy, the export format and confidential fields for CHIRP reports, the date window for duplicate matching and a list of known duplicates, how often to check for new reports and who is alerted, and the test-set size and pass rate.

---

## Release 4: Public access

**11 March to 9 April 2027 · 14 stories · 21.5 days**

### Outcome

The chat is ready for seafarers to use safely. They can sign up, use it within limits that protect CHIRP's budget, and control their own data. CHIRP can catch and correct a wrong answer before it spreads.

### Who it's for

Members of the public, starting with seafarers. Nobody outside CHIRP sees it until the beta in Release 5.

### What people can do

**Get access**

- Sign up with an email address, verify it, and get a public account that has no access to staff tools.
- Sign in, stay signed in on a device, reset a forgotten password and sign out.
- Accept CHIRP's terms and privacy notice before the first question, and again when they change.
- Keep past conversations, reopen them and carry on, or delete them.
- Download a copy of everything the service holds about you.
- Delete your account and all your data.

**Report a problem**

- Flag an answer you think is wrong, pick a reason and add a note.
- CHIRP staff see flagged answers with the full conversation and sources, mark each one right or wrong, and get a regular email of new flags.
- CHIRP staff can withdraw a wrong answer, so the person who got it sees a notice, or hide a bad report or field so it isn't used again. Every change is recorded, and can be undone.

**Run the service safely**

- Public users get a daily question limit, with a warning before they reach it. Staff have no limit.
- The AI bill has a monthly cap. CHIRP is warned as it approaches, public questions pause when it is reached, and they start again the next month.
- Off-topic questions and attempts to manipulate the chat are refused politely and logged.
- Public accounts can't reach staff pages, staff tools or staff-only data, and an automated test checks this.
- Before anyone outside CHIRP sees it, the public setup is tested for misuse, heavy use and every step a user takes, on desktop and mobile.

### Not in this release

There are no outside users yet, and no landing page or help pages.

### CHIRP to agree

Password rules and sign-in timings, the daily question limit, the spending cap and warning level, how deleted users' questions are handled in the log, how long backups keep deleted data, the refusal test set, and load test targets.

---

## Release 5: Launch

**7 April to 16 April 2027 · 6 stories · 7 days**

### Outcome

Real seafarers have tried the chat and their most important problems are fixed. It is open to anyone, easy to find, and explains what it can and can't do.

### Who it's for

A closed group of invited seafarers first, then the public.

### What people can do

**Get access**

- Invited seafarers sign up during a closed beta. Anyone else can leave their email to hear when it opens.
- Find the chat from a public landing page that explains what it does, where its information comes from and who funds it.
- Read short help pages on asking good questions, how source links work, what is covered, what the chat can't do, and how to flag a wrong answer. CHIRP staff get a guide to every staff tool.

**Report a problem**

- Beta testers give feedback through a short form. CHIRP sees a summary of feedback, flags and usage, and agrees a ranked list of fixes with Tandem.

**Run the service safely**

- The top issues from the beta are fixed within a two-day budget. Anything left over is written up for after launch.
- On launch day sign-up opens to everyone, the waiting list is emailed, and monitoring, limits and the spending cap are confirmed. Sign-up can be closed again within minutes if something goes wrong.

### Known risk

The current dates give the beta about one day between invitations and feedback, which isn't enough for real use. The Statement of Work had beta seafarers due on 19 March. Running the beta alongside the end of Release 4 would give testers several weeks. This needs agreeing with ZigZag.

### CHIRP to agree

The number of beta testers, the landing page address and copy, the wording on the chat's limits, and the launch-day spending cap.
