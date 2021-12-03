
Analyzing an per income data accordind to year, gender,degree
My aim is to get the graphs below

1-) How many person attended to analyze for each year
2-) Education level distribution by years
3-) Gender distributionby years
4-) Education level distribution by gender
5-) Avarage of per hour income distribution by years
6-) Avarage of per hour income distribution by Genders
7-) Avarage of per hour income distribution by Degree
8-) Avarage of per hour income distribution by years and genders
9-) Avarage of per hour income distribution by year and degree

###############################################################
The topics I aim to learn with this program are as follows

1-) Handle a csv file
2-) Use a simpe data model with sqlite database
3-) Use simple INSERT proecess
4-) Use simple SELECT process with WHERE query for filter
5-) Manage result of query data from database  
6-) Write and read json file
7-) Use matplotlib package for visualization

###############################################################

To run this code

1-) Check python3 
    open terminal and run below command
    $ python3 --version
    if not installed python , you have to install python 

2-) Virtual Environment 
If you do not want the current package versions of the packages 
to be downloaded in the future to be affected, 
I recommend you to activate the virtual environment.

to activate virtual environment , open terminal in the directory where you want to run the project
and run below command
$ python3 -m venv projectName-env
now created a new environment , we have to activate , to this
for windows : $ projectName-env\Scripts\activate.bat
for unix or MacOS : $ source projectName-env/bin/activate
now virtual environment is activated
to deactivate run below command 
$ deactivate

3-) install requirement packages

check the below script this library
$ pip show matplotlib

if no library install library with below script
$ pip install matplotlib

4-) download data Set
this dataset is already available on github
if you want  
download item of CPSSW9204.csv this link : https://vincentarelbundock.github.io/Rdatasets/datasets.html

5-) Run uploadToDb.py for
    $ python3 uploadToDb.py
    read csv file
    store to database
    cretae db.sqlite

6-) Run analytic.py for 
    $ python3 analytic.py
    calculate total attendence according to different variables
    calculate avarage incomes per hour according to different variables
    print some results
    create data.json file for next step

7-) Run visualization.py for
    $ python3 visualization.py
    read from data.json file
    prepare data for visualization
    show graphs

NOTE : you have to run third part after first and second part   
When you run the visualization.py , the program ask to you
which report you want to see
you can select range (1-9) reports 
for exit you have to enter -1 
