import subprocess
import re
from collections import defaultdict

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def generate_changelog():
    # Get the last tag
    last_tag = run_command("git describe --tags --abbrev=0")
    if not last_tag:
        # If no tags, get all commits
        commits_cmd = "git log --pretty=format:'%s'"
    else:
        commits_cmd = f"git log {last_tag}..HEAD --pretty=format:'%s'"
    
    commits = run_command(commits_cmd).split('\n')
    
    categories = defaultdict(list)
    
    # Keywords for categorization
    patterns = {
        "Added": r"(?i)^(feat|add|new)",
        "Fixed": r"(?i)^(fix|bug|patch)",
        "Changed": r"(?i)^(refactor|update|change|improve)",
        "Removed": r"(?i)^(remove|delete|drop)"
    }
    
    for commit in commits:
        if not commit: continue
        found = False
        for cat, pattern in patterns.items():
            if re.search(pattern, commit):
                categories[cat].append(commit)
                found = True
                break
        if not found:
            categories["Other"].append(commit)
            
    # Format output
    output = "# Changelog\n\n"
    for cat in ["Added", "Fixed", "Changed", "Removed", "Other"]:
        if categories[cat]:
            output += f"## {cat}\n"
            for item in categories[cat]:
                output += f"- {item}\n"
            output += "\n"
            
    with open("CHANGELOG.md", "w") as f:
        f.write(output)
    
    print("CHANGELOG.md generated successfully.")

if __name__ == "__main__":
    generate_changelog()
