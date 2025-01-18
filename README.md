# Us-Visa-Approval-Prediction

# git command
```
To kanow the git version

        git --version

initialize git command for the local folder

        git init

configure the git

        git config --global user.name "<yur name>"

        git config --global user.email "<your email>"

clone the folder from central repository

        git clone <url of the central repository>

command to check the status of the git

        git status

send the changes into the staging area of local repository (your system)

        git add .   

        git add README.md  (send only the README file to the staging)

commit the changes to the local repository (your local system)

        git commit -m "<your commit message>"

know the branch of the folder

        git  branch

how to make branch as main branch for pushing to the central repository

        git branch -M main

how to check that is there is connection between local and central repository

        git remote -v

how to make connection between the local repository (main) to the central repository (origin)

        git remote add origin <url of the central repository>

How to push the files to the cetral repository (origin) from the local repository (main)

        git push origin main

how to restore the file form staging area

        git restore <file name>

```

# conda environment
```
how to create new conda environment

        conda create -n <env_name> python=3.8 -y
        conda create --name <env_name> python=3.8 -y

Activate the conda environment 

        conda activate <enviroment_name>

Deactivate the active conda environment

        conda deactivate

List all the package installed under particular conda environment

        pip list

To list all the package installed in anaconda including all conda environment

        conda list

to know all the list of conda environment. the one with * is the active environment

        conda env list

how to know the present conda environment

        echo $CONDA_DEFAULT_ENV

delete the conda environment

    -all = removes all the package installed under the conda environment

        conda remove --name <ENV_NAME> --all
        conda env remove -n <ENV_NAME>

```

# install all the package along with local package (folder) with setup.py file written in requirements.txt file

```
        pip install -r requirements.txt
```
