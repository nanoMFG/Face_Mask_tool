# nanoMFG Software Planning Document
<!-- Replace text below with long title of project:short-name -->
## FaceMask tool 
### Target Release: 1.0.0 : August 2020

## Development Team
<!-- Complete table for all team members 
 roles: PI, developer, validation
 status: active, inactive
-->
Name | Role | github user | nanohub user | email | status
---|---|---|---|---|---
Jeffrey Asubonteng | member | jasubon3 | jasubon3 | jeffreyasubonteng2010@gmail.com | active
QuoVadis Savoy | member | qsavoy | qsavoy | quovadis_savoy_00@subr.edu| active
Darren Adams | software Developer | dadamsncsa | dadamsncsa | dadams@illinois.edu | active
Elif Ertekin | Developer | elif | elif | ertekin@illinois.edu | active


**nanoMFG Github Team(s):** @face_mask_toolteam
**nanoHUB Group(s):**

## 1. Introduction
<!-- A  concise description of the current iteration of work. -->

### 1.1 Purpose and Vision Statement
<!--Why are we building this tool? What is the key benefit? How does it relate to existing tools and existing software? How does it fit into the overall objectives for the nanoMFG node? Who will use it?-->
The FaceMask tool is designed to help analyze face mask wearing habits of the public. It uses neural networks to analyze publically available images to detect whether masks are being worn, and if so, whether they are being worn properly. 

### 1.2 References
<!--List any documents or background material that are relevant.  Links are useful. For instance, a link to a wiki or readme page in the project repository, or link to a uploaded file (doc, pdf, ppt, etc.).-->
This tool is based on the [COVID-19: Face Mask Detector](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/) and uses OpenCV, Keras/Tensorflow, and Deep Learning. The main source code has been implemented in a jupyter notebook. 

## 2 Overview and Major Planned Features
<!--Provide and overview characterising this proposed release.  Describe how users will interact with each proposed feature. Include a schematic/diagram to illustrate an overview of proposed software and achitecture componets for the project-->
Users will be able to assess the accuracy and precision of the face mask detector by training and testing the framework on datasets of images. Users can upload their own images and use the tool to analyze them. 

### 2.1 Product Background and Strategic Fit
<!--Provide context for the proposed product.  Is this a completely new projects, or next version of an existing project? This can include a description of any contextual research, or the status of any existing prototype application.  If this SPD describes a component, describe its relationship to larger system. Can include diagrams.-->

### 2.2 Scope and Limitations for Current Release
<!--List the all planned goals/features for this release.  These should be links to issues.  Add a new subsection for each release.  Equally important, document feature you explicity are not doing at this time-->


##### 2.2.1 Planned Features
Users will be able to assess the accuracy and precision of the face mask detector by training and testing the framework on datasets of images. Users can upload their own images and use the tool to analyze them. 

#### 2.2.2 Release Notes 
##### v#.#.#

### 2.3 Scope and Limitations for Subsequent Releases
<!--Short summary of  future envisioned roadmap for subsequent efforts.-->

### 2.3 Operating Environment
<!--Describe the target environment.  Identify components or application that are needed.  Describe technical infrastructure need to support the application.-->

### 2.4 Design and Implementation Constraints
<!--This could include pre-existing code that needs to be incorporated ,a certain programming language or toolkit and software dependencies.  Describe the origin and rationale for each constraint.-->

## 3 User Interaction and Design

### 3.1 Classes of Users
<!--Identify classes (types) of users that you anticipate will use the product.  Provide any relevant context about each class that may influence how the product is used: 
The tasks the class of users will perform
Access and privilege level
Features used
Experience level
Type of interaction
Provide links to any user surveys, questionnaires, interviews, feedback or other relevant information.-->
This tool could be used by public health department or city planners interested in understanding the face mask wearing habits in their region.  Individuals who use this tool apply different features to get an accurate results. This product is free and can be accessed by anyone or organization for their research.

This tool may also be used for educational purposes.  It can be used to explore concepts such as computer vision and neural networks. 

### 3.2 User Requirements
<!-- Provide a list of issue links to document the main set of user requirements to be satisfied by this release.  Use the user requirement template to draft thense issues.  A well written user requirement should be easy to justify (Rational) and should be testable.  List in order of priority as must have, should have or nice to have for each use case. -->

### 3.3 Proposed User Interface
<!--Could include drawn mockups, screenshots of prototypes, comparison to existing software and other descriptions.--> 
Jupyter Notebook. 

### 3.4 Documentation Plan
<!-- List planned documentation activities -->

### 3.5 User Outreach Plan
<!-- List upcoming activities designed to elicit user feedback and/or engage new users.  Use issues for activities that will be completed this iteration-->

## 4. Data And Quality Attributes

### 4.1 Data Dictionary
<!--Summarize inputs and outputs for the application.-->

### 4.2 Usability and Performance
<!--Summarize usability requirements such as easy of adoption for new users (eg example data),  inline documentation, avoiding errors, efficient interaction, etc.  Describe performance expectations  and/or document challenges.  Note you can reference user requirements from above if needed. -->

### 4.3 Testing, Verification and Validation
<!--Describe What data is necessary to verify the basic functionality of the application.  Provide a testing plan that includes a list of issues for each planned activity.  Describe data sets that are needed to test validation.-->

### 4.4 Uncertainty Quantification
<!--Identify and document possible sources of uncertainty. Categorize with standard labels, such as parametric, structural, algorithmic, experimental, interpolation.

Develop a plan for measuring and documenting uncertainty, e.g., using forward propagation or inverse UQ, and showing it in the application, if applicable.-->
