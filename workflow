Git workflow.
 
This is one of the workflows we can follow while working on Git. This is *NOT* the only workflow, and you can try others. But since most of us here are new with VCS, I thought I'll loosely fix some guidelines that could help:
 
# Before you start to work on any issue
 
1. git checkout master
2. git pull upstream master
 
This will bring your local master branch to the same state as our main branch. If there is any conflict or git tries to make a new commit (i.e., it does a recursive merge strategy), please reset your master branch as follows:
 
3. git fetch upstream
4. git reset --hard upstream/master
 
Do steps 3. and 4. only if a fast-forward merge fails. (You can still do it, even if fast-forward merge was successful, just that it wouldn't matter).
 
Now begin your work by checking out a new branch as follows:
 
1. git checkout -b <new_branch_name>
 
Avoid working from master branch directly, in case you run into tangled git commits, I will ask you to redo your entire work, won't accept badly commited pull requests.
 
Now once you are on a new branch, continue with your work. Keep making commits often while working (one logical change = one commit). Once you're done, you need to squash your commits into a single commit. *Always* squash your commits into a single commit. Again, I will not allow PR's with multiple commits. Here are the steps:
 
**NOTE: Before you do this, and the steps after this, please ensure you have followed the steps above or you will run into conflicts.
 
1. git log --> now count the number on commits you made while working. Say you made n commits
2. git rebase -i HEAD~n --> This will open an editor. each commit will have a 'pick' written before it. Replace 'pick' --> 's' in all commits except the first one. Now close the editor. Another one should open up immediately, where it will give you chance to redo your commit message. Dont just skip it, remove all your prevous commit msgs and replace it with the following format of msg (This is a MUST):
 
Fixes #<issue_number>
 
where <issue_number> is the one one which you are working (go to GitHub to get that)
Now close the editor and you are done.
 
# After you are done
 
Go to your master branch again. You want to fetch the latest commits done on our main repo while you were working.
 
1. git checkout master
2. git pull upstream master
 
This will almost 100% be a fast forward merge since you haven't done anything on the master branch (you were on the other branch). Now switch back to your branch and rebase your work (i.e., the single commit you made) on top of all the commits so  far:
 
3. git checkout <branch_name>
4. git rebase master
 
In case there is no merge conflict, you are done and can skip to section below. If there are merge conflicts:
 
5. git status --> This will show you all the files where there is conflict.
 
Open each of that file one by one, and resolve conflicts. As soon as you resolve conflict for one file, do:
 
6. git add <file_name>
 
Repeat till all files are conflict free. Now do the following:
 
7. git rebase --continue
 
In case you get conflicts again, repeat the process above.
 
# How to push changes
 
Once conflicts are gone (or you never had them) push your work to your fork
 
8. git push origin <branch_name>
 
here origin is assumed to be the name of your fork (if not, change accordingly) and <branch_name> is the name of your branch on which you were working.
 
And done!