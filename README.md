# Create React App

```
npx create-react-app client --template typescript
```

- The problem is both directories are git repositories in which case you would have a submodule.
- To remove git submodule but keep files follow this instructions.

```
mv client subfolder_tmp
git submodule deinit subfolder_tmp
git rm --cached subfolder_tmp
mv subfolder_tmp client
git add client
```

// moving to your client folder or whatever 
// the react-app folder is called
cd client
// remove the git in this folder
rm -rf client/.git
// moving to your root folder of git
cd ..

git add .

git commit -m "Dereted `client/.git`"