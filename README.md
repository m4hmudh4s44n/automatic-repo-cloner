# GitHub Automatic Repo Cloner

A simple Python automation script that lets you copy (clone) any public GitHub repository, remove its original history, and prepare it for upload to your own GitHub account.

This tool helps you:
- Clone any GitHub project
- Remove the original `.git` history
- Re-initialize Git
- Prepare the project for pushing into your own GitHub repository

> ⚠️ This script does **NOT** automatically create a GitHub repository online.  
> You must create an empty repo manually and then push.

---

## Features

- Clone any public GitHub repository
- Auto-detect folder name
- Remove original Git history
- Reinitialize your own Git repository
- Helpfully instructs you to create a GitHub repo
- Pushes to your GitHub with one command

---

## 📌 Requirements

- Must have to do this on your **git bash**
- Python 3.x
- Git installed  
- Internet connection  
- GitHub account  

---

## 📂 How to Use

Run the script:

```bash
python copy_repo.py
```

## 📜 Example
Enter the GitHub repository URL to clone:
```
https://github.com/someuser/someproject.git
```
Enter your GitHub username:


Enter NEW repo name:
my-copied-project

## 🛠 Technology Stack

Python

Git (CLI)

## 📄 License

MIT License – You are free to use and modify.
