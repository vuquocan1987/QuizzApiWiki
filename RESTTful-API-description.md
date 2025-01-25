# Important information for Deadline 1


:bangbang:&nbsp;&nbsp;**This chapter should be completed by Deadline 1** *(see course information at [Lovelace](http://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/))*

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Chapter summary</strong>
</summary>

<bloquote>
This chapter must provide a good overview of the Web API that your group is going to develop during the course, and some insight into the (imaginary) microservice architecture it will be a part of. You should not focus in implementation aspects such as database structure,  interfaces or the request/responses formats. We recommend that you look into existing APIs (see Related work below) before writing the description for your own API.

<h3>Chapter GOALS:</h3>
<ol>
<li>Understand what is an API</li>
<li>Describe the project topic API</li>
<li>Describe how the API would be used as part of a larger architecture</li>
</ol>
</bloquote>

</details>

---

<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Chapter evaluation (max 5 points)</strong>
</summary>

<bloquote>
You can get a maximum of 5 points after completing this Chapter. More detailed evaluation is provided in the evaluation sheet in Lovelace.
</bloquote>

</details>

---

# RESTful API description
## Overview
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>

Describe the API you are going to implement. Also describe the larger imaginary architecture that would exist around that API - while you do not need to implement these other components, they will be helpful in imagining context for your API. Your API will be a component that stores, and offers an interface to, some important data in the larger ecosystem. Think about a larger system, and then take out one key piece to examine - this will be your API.

Describe the API briefly and comment what is the main functionality that it exposes. Focus in the API not in any specific application that is using this API. Take into account that in the end, a WEB API is an encapsulated functionality as well as the interface to access that functionality. Remember that your API is just one part of a larger machine. It does not need to do everything. There will be other components in the system to do those things. This course focuses on creating a small API in detail - thinking too big from the start will drown you in work later. 

A really short version of an overview for the RESTful Web API could be: 

<em>“The discussion forum Web API offers different functionalities to structure non-real-time conversations among the people of a group about topics they are interested in certain topic. Messages are grouped in Threads, that at the same time are grouped in Topics. The messages are accessible to anyone, but posts can only be created by providing credentials of a registered user [...] This API could exist as part of an online learning environment system where it is responsible for offering discussion forum features that can be included in other components of the learning environment. For example, a programming task (managed by a different component) can include its own discussion board managed by the discussion forum API[...]“</em>

</bloquote>

</details>

---

:pencil2: The Quiz API is a tool for managing and using quizzes in a structured way. It provides functionalities to query, update, and manage quizzes within the system. It helps store quiz data, allows users to retrieve it, and lets authorized administrators make changes.

### Motivation
Quizzes are a great way to help people learn by testing their knowledge and analyzing what they’ve studied. This API is designed to support active learning by  providing quizzes on different topics while managing quizzes and having a clear system in place. 

    1.Making it easy to organize quizzes by category and level.
    
    2.Providing a simple way to access and update quiz data.
    
    3.Ensuring only authorized people can make changes to the quizzes.

### Structure of the Quiz API
Quizzes are organized into categories and levels to serve to users and their difficulty preferences.

Each quiz contains a multiple-choice question, multiple options for answers and one or more correct answers. 

### Role in the Larger System
#### Accessibility and Security
A separate authentication system is used to control the access to the Quiz API. 
Entities with admin access level are authorized to do the below functions.

    Add new quizzes.
    
    Update existing quizzes.
    
    Delete quizzes. 

#### Recommendation System
Suggests quizzes to users based on what they’ve done so far.

#### User Interface
Web application that show quizzes to users.

#### Data consistency
Quizzes are complete with clear questions, options, and answers.


---


## Main concepts and relations
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
<strong>Define</strong> the <strong>main concepts</strong> and describe the <strong>relations</strong> among them textually. Roughly, a concept is a real-world entity that is expected to be of interest to users or other services. This section will be a guideline for choosing your resources to implement in Deadline 3. Students should remember that some of the concepts might not be a resource by themselves, but just a part of it (resource property). In this section, students should not describe the RESTful resources, but identify which are the main ideas of the API. Do not forget to include the relations among the concepts.

A description of the main concepts for the Forum API could be: 

<em>"The API permits users send messages. The forum contains a list of categories and a list of users. Each category specifies a name, a description and a thread. A thread is [...]The forum may contain 0 or more categories… Each category may have 0 or more threads… Users can write and read messages to a forum thread. A user has a profile, basic information, activity information (stores, for instance, all the messages sent by a user, the messages marked as favorites). [...]The user history contains information of the last 30 messages sent by the user.[…]"</em>

Include a diagram which shows the relations among concepts.

This section is important because it outlines the concepts that you will later implement. In particular, the diagram defined here will follow you throughout the project report and you will be adding more details to it. 


</bloquote>

</details>

---

:pencil2: The Quiz API is designed for managing quizzes and their associated categories.

### Quiz Category
   
Quizzes are categorized by a specific topic or subject.

#### Attributes

Name: The title of the category (e.g., "Programmable Web Project," "Mobile Computing").

Level Range: Minimum and maximum difficulty levels of quizzes in the category (e.g., 1–5).

#### Relationships
A category can contain one or more quizzes.

### Quiz
Multiple-choice questions with options and correct answers.

#### Attributes

Question

A list of answer choices.

The correct option(s) among the choices.

Difficulty level

Specifies whether the quiz is available to a specific group of users.

#### Relationships

A quiz question belongs to one category.

### Authentication 
An authenticated user with an access to manage quizzes and categories.

#### Attributes

Role: Specifies the level of access (e.g., "admin").

#### Responsibilities

Can create, edit, or delete categories and quizzes.
 
### User
An user accessing the quizzes to participate in the learning system.

#### Responsibilities
Users can access quizzes  but cannot modify them.


![image](https://github.com/user-attachments/assets/9359293e-e4c6-49fb-ad6b-2275639accee)


---

## API uses
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Describe at least one client and one service that could use your Web API. You must explain here what is the functionality provided by the client/service, and how it uses the Web API to implement this functionality. 
</bloquote>

</details>

---

:pencil2: The Quiz API can be utilized by various clients and services to achieve specific functionalities within a larger learning system.
### Client: Web Application
A web application designed for users serves as a client for accessing the Quiz API.

#### Functionality

Allows users to browse quiz categories and take individual quizzes.

Provides an interactive interface for selecting quizzes based on topics or difficulty levels.

#### API Usage

Queries the API to retrieve a list of quiz categories.

Fetches individual quiz data, including questions and options, for display.

Ensures users can only view the quizzes by using API's accessibility settings.

Client-side logic handles hidden answers, scoring, and presenting feedback.

### Service: Quiz Generating System

A backend service acts as an automated quiz management system, integrating with the Quiz API to maintain and update quiz content.

#### Functionality

Manages quizzes by adding, updating, or deleting content.

Automates bulk operations and ensures quiz data integrity.

#### API Usage

Authenticates access to modify quizzes and categories.

Validates and synchronizes quiz data for consistency.



## Related work
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Find at least one API that resembles the functionality provided by yours. Explain in detail the functionality provided by the API. Classify the API according to its type (RPC, CRUD REST, pure REST, hypermedia driven ...) justifying your selection. Provide at least one example client that uses this API.

The purpose of this task is to get more familiar with what an API is. This will be helpful in describing your own API. Therefore, it is recommended to do this section after you have decided the topic of your project but before writing your API description.
</bloquote>

</details>

---



:pencil2: 
### Trivia API

The Open Trivia Database API is a free API that provides questions across various topics. It allows users to fetch  questions by category and difficulty level, making it similar to the functionality we intend to offer with our Quiz API.

#### Functionality

Retrieve trivia questions by specific categories. 

Filter by difficulty of the questions.

Multiple-choice questions with options.

#### API Type

This is a REST API because it only supports Read operations like retrieving questions and does not involve data creation or modification.

The API uses HTTP GET requests to fetch quiz data.

#### Example Client

Trivia quiz apps often use this API. They retrieve questions based on the user's selected category and difficulty and display them in a quiz format.

### Quizlet 

The Quizlet API is a widely used service for managing and accessing flashcards and study sets. While its primary focus is on flashcards, it provides similar functionality related to quizzes and learning.

#### Functionality

Create and retrieve study sets of terms and definitions.

Organize study sets by categories or subjects.

API allows users to retrieve sets by keyword, difficulty, and more.

#### API Type

The Quizlet API is a REST API which supports Create, Read, Update, and Delete operations.

#### Example Client

The Quizlet API is used by mobile and web apps designed for learning, where users can practice with flashcards or quizzes across different subjects.


---


## Resources allocation
|**Task** | **Student**|**Estimated time**|
|:------: |:----------:|:----------------:|
|Initilize Git|An Vu|30 minutes| 
|Rough API describe,overall idea |An Vu|90 minutes| 
|||| 
|||| 
|||| 
