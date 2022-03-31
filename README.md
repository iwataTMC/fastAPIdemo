# Create React App

```
$ npx create-react-app client --template typescript
```

- The problem is both directories are git repositories in which case you would have a submodule.
- To remove git submodule but keep files follow this instructions.

-  moving to your client folder or whatever 
-  the react-app folder is called

```
$ cd client
```

- remove the git in this folder

```
$ rm -rf client/.git
```

- Now you go back to you root directory and do the add, commit, and push. You should have all your react-app folder pushed to the repository you want to.

```
$ cd ..

$ git add .

$ git commit -m "Dereted client/.git"

$ git push
```

