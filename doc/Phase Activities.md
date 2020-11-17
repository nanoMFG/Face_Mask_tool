# nanoMFG Software Development Phase Activities

* [phase: 1](#phase-1)<br/>
  - [Review GitHub Accounts and Team Membership](#review-github-accounts-and-team-membership)<br/>
  - [Provide Summary and Team Info for Next Release](#provide-summary-and-team-info-for-next-release)<br/>
  - [Identify Potential Users](#identify-potential-users)<br/>
  - [Draft and Update User Requirements](#draft-and-update-user-requirements)<br/>
  - [Add License Documents](#add-license-documents)<br/>
  - [Complete Phase 1 Planning (Draft)](#complete-phase-1-planning-draft)<br/>
  - [Update Project Goals and Mission Statement](#update-project-goals-and-mission-statement)<br/>
  - [Plan User Outreach Activities](#plan-user-outreach-activities)<br/>
* [phase: 2](#phase-2)<br/>
  - [Document Software and Architecture Components](#document-software-and-architecture-components)<br/>
  - [Document System Environment and Known Constraints](#document-system-environment-and-known-constraints)<br/>
  - [Develop a Testing, Verification and Validation Plan](#develop-a-testing,-verification-and-validation-plan)<br/>
  - [Develop a Documentation Plan](#develop-a-documentation-plan)<br/>
  - [Complete Phase 2 Planning (Draft)](#complete-phase-2-planning-draft)<br/>
* [phase: 3](#phase-3)<br/>
  - [Develop Contributer Guidelines and Procedures](#develop-contributer-guidelines-and-procedures)<br/>
  - [Create Issues for Planned Activities](#create-issues-for-planned-activities)<br/>
  - [Complete Phase 3 Activities (Draft)](#complete-phase-3-activities-draft)<br/>
* [phase: 4](#phase-4)<br/>
  - [Complete Phase 4 Activities (Draft)](#complete-phase-4-activities-draft)<br/>
* [phase: 5](#phase-5)<br/>
  - [Complete Phase 5 Activities (Draft)](#complete-phase-5-activities-draft)<br/>

# phase: 1
## Review GitHub Accounts and Team Membership
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | 1 
### Summary
Review GitHub account details for team members and create a project development team.  A GitHub team should to be created for each group of collaborators developing one or more nanoHUB tool(s).

### Details
Note: this is best completed by the project PI and/or repository admin (creator).<br/>

- [ ] If possible, ask all of your team members to update their GitHub profile to include: full name, email and home institution.
- [ ] Create a GitHub team using all of your project team member's GitHub accounts (including the PI's) in the nanoMFG organization (see below).
- [ ] Add your project repository to the team.

### References
Here are GitHub's docs on teams:
* [about teams](https://help.github.com/en/articles/about-teams)
* [creating a team]( https://help.github.com/en/articles/creating-a-team)
* [team access to repositories](https://help.github.com/en/articles/managing-team-access-to-an-organization-repository)

## Provide Summary and Team Info for Next Release
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | 2 
### Summary
Begin a Software Planning Document (SPD) and provide project information for the next upcoming release. The preliminary project information described in the checklist below should go into the subtitle and section 1 of the SPD.  In this planning task you will:
* Create a draft SPD from the [SPD template](https://github.com/nanoMFG/Face_Mask_tool/blob/planning/doc/templates/SPD_template.md).
* Add requested information and commit a new document to a separate  branch of your project repository.
* Open a pull request to merge your new document into `doc/SPD` on your project repository's `planning` branch.

### Details
**Only** the following SPD items are required for this issue: 
- [ ] Title and (short)name for the software project (tool).
    - The "short name" should be the same as will be used for short name on nanoHUB tool page.
- [ ]  Documentation for team members
    - Please provide names platform usernames, project roles and current status for all team members
    - Use the provided table in the SPD template to document members of your development team.
- [ ] Version number to be used for the next release(eg 1.0.0) and an approximate target date for the release.
- [ ] GitHub nanoMFG org. team names.
- [ ] nanoHUB group names (if applicable).
- [ ] Brief synopsis/abstract to outline this release under "Introduction".

Once a pull request is opened, the nanoMFG `@dev-review` team will review the document and issue any feedback to the pull request and/or this issue.  Refer to the links in the references below for detailed instructions  on creating and submitting an SPD revision.

### References
 [Instructions to Create SPD from Template](https://github.com/nanoMFG/Face_Mask_tool/tree/planning/doc/SPD#create-a-draft-spd-from-template)
[Submitting SPD Updates for Review](https://github.com/nanoMFG/Face_Mask_tool/tree/planning/doc/SPD#submitting-spd-updates-for-review)


## Identify Potential Users
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | 3 
### Summary
Identify classes (types) of users that you anticipate will use the product and document them in section 3.1 of the SPD.  Provide any relevant context about each class that may influence how the product is used.

### Details
Consider the following criteria when classifying potential users:
* The tasks the class of users will perform
* Access and privilege level (if relevant).
* Features used
* Experience/knowledge level
* Type of interaction (education, research, other...)

Provide links to and/or summaries of any user surveys, questionnaires, interviews, feedback or other relevant information.

### References

## Draft and Update User Requirements
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | 8 
### Summary
Develop and/or revise the set of user requirement issues for your project.  List links to the issues in sec. 3.2 of the SPD.  A template to [create a user requirement issue]() has been added to your repository.   A well written user requirement should be easy to justify (Rational) and should be testable.  

### Details
User requirements should be "user facing" and serve as top-level drivers for other development your project.  Not all iterations through the development phases will generate additional user requirements.  A good strategy for the first planning pass is to determine a set of user requirements that comprises a _minimum viable product_ (MVP) and label them as `must have`.

- [ ] Create issues for each use case using the [User Requirement]() issue template.
- [ ] Review draft use case with your team and refine their descriptions.
- [ ] Label each issue to indicate the priority as either: `must have`, `should have` or `nice to have`.
- [ ] Update section 3.2 of your SPD with a list of links to each user requirement issue.

**Note:** If no user-facing updates are planned for this iteration indicate as such in Sec 3.2.

When planning specific development activities, refer back to user requirements when appropriate.

### References
[Requirements Checklist](https://github.com/nanoMFG/DevTeam/wiki/Requirements-Checklist)

## Add License Documents
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | 2 
### Summary
The nanoMFG node encourages contributions to the open source community. Open source contribution give our project a chance to have a larger impact and build a community of users and contributors.  A first step in preparing for an open source release is to choose a license add the necessary documentation to your project.

### Details
Apache 2 is the default license choice for nanoMFG projects.  
- [ ] Choose an open source license. Add a LICENSE file to your project using the GitHub interface.
- [ ] Add a COPYRIGHT file.
- [ ] Add an AUTHORS file
- [ ] Update License section of Project README.md

### References
[starting and open source project](https://opensource.guide/starting-a-project/)
[adding a license to a repository](https://help.github.com/en/articles/adding-a-license-to-a-repository)

## Complete Phase 1 Planning (Draft)
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | None 
### Summary
Track progress on Phase 1 activities here.   Submit SPD for review when completed

### Details
Note, To see enhanced features for this (and other) issues refer to the Zenhub documentation link below.
- [ ] Submit SPD draft with all phase 1 activities.

### References

 [Instructions to Create SPD from Template](https://github.com/nanoMFG/Face_Mask_tool/tree/planning/doc/SPD#create-a-draft-spd-from-template)
[Submitting SPD Updates for Review](https://github.com/nanoMFG/Face_Mask_tool/tree/planning/doc/SPD#submitting-spd-updates-for-review)
[Adding ZenHub Extensions](https://github.com/nanoMFG/DevTeam/wiki/Reference-Material-and-Links-for-Developers#zenhub-extensions-to-github)
## Update Project Goals and Mission Statement
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | 2 
### Summary
Develop or review your project goals and mission statement in sec 1.1 of your SPD draft.
.
### Details
Add a concise mission statement and summarize your project goals 
* Why are we building this tool? 
* What is the key benefit? 
* How does this tool relate to existing tools and existing software? 
* How does it fit into the overall objectives for the nanoMFG node? 
* Who will use it?

### References

## Plan User Outreach Activities
Phase | Activity Type | Work Estimate
---|---|---
phase: 1 | None | 3 
### Summary
Determine efforts directed at eliciting user feedback.  Update section 3.5 of the SPD with planned activities.

### Details
As for other activities, create issues for specific activities.  For other, more general efforts document the plan in section 3.5.
- [ ] Reaching out to specific lists of users
- [ ] Conducting surveys
- [ ] Data collection (eg. for validation)

### References

# phase: 2
## Document Software and Architecture Components
Phase | Activity Type | Work Estimate
---|---|---
phase: 2 | None | 2 
### Summary
Identify the major components of your system whether they be functions, databases, models, etc.  Provide and overview as an introduction to section 2 of the SPD

### Details
A good way to document this is with a flowchart or high level diagram.  Add a brief synopsis of how that major planned activities fit into this architecture.

### References
## Document System Environment and Known Constraints
Phase | Activity Type | Work Estimate
---|---|---
phase: 2 | None | 2 
### Summary
Identify the relevant factors that will affect your software on in the target environment.  Update section 2.3 with any new constraints.

### Details
Use this activity to review and accumulate knowledge about the target environment.
- [ ] Known constraints of the target operation environment (nanoHUB)
- [ ] Factors affecting installation, runtime behavior etc.

### References
None yet.
## Develop a Testing, Verification and Validation Plan
Phase | Activity Type | Work Estimate
---|---|---
phase: 2 | None | 5 
### Summary
Develop or revise a set of planned activities for testing validation and verification of the application in sec 4.3 of the SPD.  If no testing activities are planned for this release, indicate as such in sec 4.3 and provide any context/status and/or future plans/timelines.

### Details
**Each tool is required to (at a minimum) develop tests to verify the correct functionality of core functions and/or the entire application and provide documentation on how to run them.**

**Create an issue** for each planned activity in your repository and provide a list of links to them in sec 4.3 of the SPD along with any other relevant context and/or explanation.  Use [task lists](https://help.github.com/en/articles/about-task-lists) in the issue to list more granular sub-tasks.

Planned activities may include (but are not limited to):
* Identify data sets to serve as validation and/or verification
* Identify critical functions to be tested
* Implement specific tests
* Refactor application code to allow testing
* Collect validation data
* Document inputs and expected outputs for validation
* Adopt a unit test framework
* Integrate Travis CI automation

### References
[PyUnit](https://wiki.python.org/moin/PyUnit)
[python testing style guidelines](https://jrsmith3.github.io/python-testing-style-guidelines.html)

## Develop a Documentation Plan
Phase | Activity Type | Work Estimate
---|---|---
phase: 2 | None | 3 
### Summary
List the planned components of the documentation for your project in section 3.4 of the SPD.  If already completed, indicate version in which it was completed.  Revise if necessary.

### Details
List planned documents and develop conventions for maintaining them.  Update you CONTRIBUTOR guidelines if needed to communicate desired documentation practices with your team
Some Documents include:
* In code documentation conventions and requirements
* In-app documentation for users
* Web documentation
  - nanoHUB web page
  - GitHub README.md
  - other webpage (github pages etc.)

Create issues for any specific documentation tasks using the documentation issue template.

## Complete Phase 2 Planning (Draft)
Phase | Activity Type | Work Estimate
---|---|---
phase: 2 | None | None 
### Summary
Track progress on Phase 1 activities here.   Submit SPD for review when completed

### Details
Note, To see enhanced features for this (and other) issues refer to the Zenhub documentation link below.
- [ ] Submit SPD draft with all phase 2 activities.

### References

 [Instructions to Create SPD from Template](https://github.com/nanoMFG/Testing/tree/planning/doc/SPD#create-a-draft-spd-from-template)
[Submitting SPD Updates for Review](https://github.com/nanoMFG/Testing/tree/planning/doc/SPD#submitting-spd-updates-for-review)
[Adding ZenHub Extensions](https://github.com/nanoMFG/DevTeam/wiki/Reference-Material-and-Links-for-Developers#zenhub-extensions-to-github)
# phase: 3
## Develop Contributer Guidelines and Procedures
Phase | Activity Type | Work Estimate
---|---|---
phase: 3 | None | 3 
### Summary
Develop or revise your project's set of Contribution guidelines, standards and procedures.  Indicate any applicable activities as comments below,  and/or reference this issue in any relevant commits before closing this issue.

### Details
Update policies and guidelines in a file named : CONTRIBUTING.md and link to this document somewhere in README.md.  Review and/or update these practices with your team as you begin this iteration coding and construction activities.

* Version control practices
  - Conventions on using branches and pull requests
  - Issues and issue tracking for your project

•Conventions for using issue tracking
  - Explanation of use of labels
  - Description of Issue Templates or kind of issues to submit

•Coding conventions including style guidelines for each relevant programming language
* Conventions for writing and running tests
* Conventions for documenting new features
* Acceptance criteria for API changes


### References
More to come...

## Create Issues for Planned Activities
Phase | Activity Type | Work Estimate
---|---|---
phase: 3 | None | 8 
### Summary
Develop a set of issues needed to complete the activities planned in Phases 1 and 2.   Add these issues to the **Complete Phase 3 Activities** Epic issue.

### Details
#### Document the work that needs to be done including:
* Code development
* Writing Tests
* User outreach
* Documentation
* Other

#### Add finishing touches to your issues:
* Apply appropriate labels for each issue (create new ones for your project if needed). 
  - This could include a "help wanted" label and/or `@mentions` to solicit help from others in the node.
* Assign issues to the right people
* Use task lists to detail more granular steps to complete the issue

#### Organize your Board
* Once issues are ready to go, drag them into your `Backlog` pipeline.
* Order by priority
* Use a milestone to set target completion dates for sets of issues
* Assign and drag to `In Progress`.

### References

## Complete Phase 3 Activities (Draft)
Phase | Activity Type | Work Estimate
---|---|---
phase: 3 | None | None 
### Summary
Use this issue as a container for all planned phase development activities planning in phases 1-3.  In addition to `nanoMFG` activities, add your planned activities to this Epic.  Upon completion, update section 2.2.2 "Release Notes" of the SPD with the version # and completed activities, then submit for review. 

### Details
 * If this issue is used as a tracking (Epic) issue, you can just add a link to this issue in the SPD, along with notes on any other relevant activities or features added.
* Submit the updated SPD wit hrelease notes for reveiw:

### References
[submitting SPD updates for review](https://github.com/nanoMFG/Face_Mask_tool/tree/planning/doc/SPD#submitting-spd-updates-for-review)
[getting started with Epics](https://help.zenhub.com/support/solutions/articles/43000500733-getting-started-with-epics)



# phase: 4
## Complete Phase 4 Activities (Draft)
Phase | Activity Type | Work Estimate
---|---|---
phase: 4 | None | None 

# phase: 5
## Complete Phase 5 Activities (Draft)
Phase | Activity Type | Work Estimate
---|---|---
phase: 5 | None | None 
