import os
import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

print("=== GitHub Project Copier ===")

# Step 1: Ask for repo URL
repo_url = input("Enter the GitHub repository URL to clone: ").strip()

# Extract folder name from URL
folder_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")

# Step 2: Clone the repo
print("\nCloning the repository...")
run(f"git clone {repo_url}")

# Step 3: Navigate into the folder
os.chdir(folder_name)

# Step 4: Remove old .git history
print("Removing old .git history...")
run("rm -rf .git")

# Step 5: Initialize your own git repo
print("Reinitializing git repository...")
run("git init")
run("git add .")
run('git commit -m "Initial commit: copied project"')

# Step 6: Ask for your GitHub details
github_user = input("\nEnter your GitHub username: ").strip()
new_repo_name = input("Enter NEW repo name (no spaces, no special chars): ").strip()

new_repo_url = f"https://github.com/{github_user}/{new_repo_name}.git"

print("\n============================")
print("⚠️ IMPORTANT: Create a new EMPTY repo on GitHub:")
print(f"➡️  {new_repo_url}")
print("Do NOT add README, LICENSE, or .gitignore.")
print("============================\n")

input("Press ENTER after creating the GitHub repo...")

# Step 7: Add new remote and push
print("Adding remote and pushing to your GitHub...")
run(f"git remote add origin {new_repo_url}")
run("git branch -M main")
run("git push -u origin main")

print("\n🎉 Done! Your project has been copied to your GitHub.")

