# Instructions for submitting assignments on GitHub

open terminal/gitbash

navigate to repository
```
cd {{path_to_your_folder_in_class_repo}}
```

ensure you are on the MASTER branch
```
git checkout master
```

update your repository
```
git fetch upstream
git merge upstream/master
```

After merging you may enter VIM, the terminal text-editor.  If so type `:q`, then press `Enter`.

add and commit your new files/folders
```
git add .
git commit -m '<NAME OF ASSIGNMENTS TO TURN IN>'
git push
```

Go to website of your repo on github github.com/<username>/<repo name>

Click the green button

Add a more specific comment if you feel you need to

Click the green confirmation button

YOU'RE DONE!!! (and techincally you've commited to an open source project!!)
