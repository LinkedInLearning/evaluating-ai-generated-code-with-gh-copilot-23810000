# Evaluating AI-Generated Code with GitHub Copilot
This is the repository for the LinkedIn Learning course `Evaluating AI-Generated Code with GitHub Copilot`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

## Course Description

AI coding assistants can generate working code quickly, but working code isn't necessarily correct code. In this course, discover a practical process for evaluating AI-generated Python code before relying on it in your projects. Join instructor Eduardo Corpeño, electrical engineer, computer programmer, and teacher, as he shows you how to use GitHub Copilot with a five-step framework: generate, inspect, test, verify, and improve. Explore practical examples involving intent mismatches, edge cases, hidden assumptions, fabricated methods, sensitive data, and incomplete test suites. Along the way, learn how to apply the complete evaluation loop in hands-on challenges and build a more systematic approach to reviewing AI-generated code before you use it.

## Learning Objectives

- Apply a five-step framework to generate, inspect, test, verify, and improve AI-generated Python code.
- Identify intent mismatches, edge cases, hidden assumptions, and fabricated functionality in AI-generated code.
- Identify hard-coded sensitive data and evaluate approaches for keeping credentials out of source code.
- Evaluate AI-generated test suites for missing cases that can allow defects to go undetected.
- Use testing and verification results to improve AI-generated code and confirm that the revised code meets the intended behavior.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"

## Installing
1. To use these exercise files, you must have the following installed:
	- [list of requirements for course]
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.
3. [Course-specific instructions]

## Instructor

Eduardo Corpeño
Electrical Engineer, Computer Programmer, and Teacher for 15+ years

Eduardo is a proud graduate of the Online Master of Science in Computer Science program from Georgia Tech. He has published over 20 online courses on topics such as microcontrollers, embedded systems, and solving engineering problems. At Galileo University, Guatemala City, he teaches a variety of subjects, including electrical circuit theory, computer architecture, microcontrollers, and printed circuit board design. Along with some colleagues, Eduardo created one of the first MOOCs in Spanish in 2013—an introduction to the Raspberry Pi— and later translated to Spanish The RISC-V Reader: An Open Architecture Atlas by Turing Award laureate David Patterson and Andrew Waterman.

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/eduardo-corpeno?u=104).


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/evaluating-ai-generated-code-with-github-copilot/catching-a-scope-mismatch-in-github-copilot-s-code?u=104
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D560DAQFRiZ-39RIipQ/learning-public-crop_675_1200/B56aDqFIQUIEAY-/0/1790633608528?e=2147483647&v=beta&t=YjbIdybPMHDBLgie3SDu0VC5VMUg6AqIFv2zoaHiR5E

