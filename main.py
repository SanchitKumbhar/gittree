from git import Repo

repo="/home/sanchit/Desktop/timecap/TimeCap/.git"

# repo=input("Repo: ")

repo=Repo(repo)

class Main:
    def __init__(self):
        self.base = "main"
        self.merge_commits = []
        self.normal_commits = []
        self.revert_commits = []
        self.branch_name = input("Enter branch: ")  # now instance-level


    '''
    Here main branch commits will be displayed with with their respective revert commits too.
    repo.iter_commits -> targeting to main branch by default,
    the commit.message[:6] is telling that check whether the first word of the revert message is Revert
    if it is then dont add it to the normal_commits add to revert_commits else u could add it ot normal_commits
    '''
    def main_branch(self):
        for commit in (repo.iter_commits("main")):
            if commit.message[:6] != "Revert":
                self.normal_commits.append({
                    "author" : commit.author.name,
                    "id" : commit.hexsha,
                    "message" : commit.message,
                })
            else:
                check=commit.message.split()
                self.revert_commits.append({
                    "author" : commit.author.name,
                    "message" : commit.message,
                    "id" : check[-1]
                })
    '''
    Here user defined branch commits will be displayed with with their respective revert commits too.
    repo.iter_commits -> targeting to main branch by default,
    the commit.message[:6] is telling that check whether the first word of the revert message is Revert
    if it is then dont add it to the normal_commits add to revert_commits else u could add it ot normal_commits
    '''
    def user_branch(self):
        print("Im here!")
        for commit in repo.iter_commits(f"{self.base}..{self.branch_name}"):
            print("commit")
            if commit.message[:6] != "Revert":
                self.normal_commits.append({
                    "author" : commit.author.name,
                    "id" : commit.hexsha,
                    "message" : commit.message,
                })
            else:
                check=commit.message.split()
                self.revert_commits.append({
                    "author" : commit.author.name,
                    "message" : commit.message,
                    "id" : check[-1]
                })

        # for commit in repo.iter_commits("main"):
        #     if len(commit.parents) > 1:   # merge commit
        #         self.merge_commits.append({
        #                 "author" : commit.author.name,
        #                 "id" : commit.hexsha,
        #                 "message" : commit.message,
        #                 "parents" : [(parent.hexsha, [head.name for head in repo.heads if parent in repo.iter_commits(head)]) for parent in commit.parents]
        #         })

        
    # print(repo.git.log("--merges", "main"))

# obj=Main()

