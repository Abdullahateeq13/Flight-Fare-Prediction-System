# Flight Fare Prediction System

1. Create an Environment
    - 1.1 Create a virtual environment using conda ```create -p <venv_name> python==version```
    - 1.2 Activate that virtual environment using ```conda activate <venv_name>```    

2. Setup Github Repository
    - 2.1 Initiate a Git
    - 2.2 Sync the folder with remote repository
    - 2.3 Create a ```readme.md``` file and push it in a repository
    - 2.4 Create a ```.gitignore``` file 

3. Create a ```requirements.txt``` file.
    - 3.1 Add all the packages you need to install in the file.


4. Create a ```setup.py``` file.

5. Create a ```__init__.py``` file in a ```src``` folder.

6. Now create a components folder inside src folder.
    - 6.0 Components are like all the modules that we are create and use in the project, and this is only for a training purpose.
    - 6.1 Create a ```__init__.py``` inside the components folder, so that we can export it as a package and can import wherever wants.
    - 6.2 Create a ```data_ingestion.py``` file, Data Ingestion means reading a data from a database or from different file locations or from different databases, wherever the data is located. Data Ingestion is part of a module of an entire project.

    - 6.3 Create a ```data_transformation.py``` After reading the data, we have to change/transform the data, So the code related to trasnformation will be written in this file, like changing categorical features to numerical features, handle one hot encoding, label encoding and other different different things.

    - 6.4 Create a ```model_trainer.py``` file, In this file, we will train the model, all the training code will be written here, how many different kinds of model i have to used, confusion matrix if i am solving classification problem, R square and adjusted R square if i am solving regression problem


