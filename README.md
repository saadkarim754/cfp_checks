# CS50 Assignment Submission System

This repository provides the setup for implementing CS50’s automatic grading system using `submit50` and `check50`. It includes step-by-step instructions for both instructors and students on how to use the system for assignment submission and grading.


## Instructor Setup

### 1. **Create a Course on `submit50.cs50.io`**
   - Visit [submit50.cs50.io](https://submit50.cs50.io) and log in.
   - Create a new course with a unique name. This course will manage the student submissions.

### 2. **Define the Slug Format**
   - The slug follows this format:  
     ```
     github_username/github_repo/branch_name/folder
     ```
   - Example slug:  
     ```
     saadkarim754/cfp_checks/main/hello
     ```

### 3. **Set Up `.cs50.yaml`**
   - Inside the folder corresponding to your slug (`main/hello` in this case), create a `.cs50.yaml` file.
   - This file specifies the files that students need to submit:
     
     ```yaml
     name: hello
     files:
       - hello.c
       - README.md
     ```

### 4. **Write a Check for `check50`**
   - Write checks to verify the correctness of student submissions. These checks validate whether the submitted code meets the requirements.
   - Check files should reside in the path defined by the slug. For reference, you can review CS50’s check examples in the [CS50 Problems GitHub Repository](https://github.com/cs50/problems/tree/2025/x/me).

### 5. **Test the Setup**
   - Verify that the checks are working with the slug you’ve defined. Use `check50` to validate student submissions and `submit50` to ensure the correct files are collected.

---

## Student Setup

### 1. **Set Up Access on `cs50.dev`**
   - Visit [cs50.dev](https://cs50.dev) and log in using your GitHub account.
   - Authorize access to CS50 tools for seamless integration with the grading system.

### 2. **Write Your Code**
   - Implement the assignment as specified by your instructor. Ensure that your code follows the provided guidelines for coding and file structure.

### 3. **Submit Your Work**
   - Once you’ve completed your code, use the following command to submit your work:

     ```bash
     submit50 saadkarim754/cfp_checks/main/hello
     ```

   - You may need to authorize `submit50` for the submission to go through.

### 4. **Verify Submission**
   - After submitting, you’ll receive a confirmation message indicating that your files have been successfully uploaded. you can check the submissions at (https://submit.cs50.io/courses/)
---

## Example Slug

Here’s an example of how the slug is structured and the expected file setup.

**Example Slug:**
saadkarim754/cfp_checks/main/hello

---

## Troubleshooting

- **Problem: `submit50` doesn’t collect the correct files**  
  Make sure that the `.cs50.yaml` file correctly lists all the files that need to be submitted, and check that the file paths are accurate.
  
- **Problem: `check50` fails to run checks correctly**  
  Ensure that the check files are placed in the correct path and properly follow the structure outlined in the CS50 checks documentation.

