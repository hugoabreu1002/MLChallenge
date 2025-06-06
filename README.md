# Code Challenge #

This repo contains all files for the code challenge for the opening 
*"Talent - Talent Profiling & Assessment - Machine Learning Engineer."*
For this challenge you'll be in charge of running an end-to-end data science
project related to the involuntary turnover.


### Task

People are at the heart of our business. Recruiting and hiring are
time-consuming processes. We assign the employee to a client as soon as the
hiring process finishes. Most of the time, we have great matches between
clients and developers. However, employees can be seen as low-performant by
the client.

As a company, we'd love to detect employees who are at high-risk quickly. If
we find these people quickly, we can develop their talent and make everyone
happy. Otherwise, we may need to terminate the employee's contract due to the
lack of projects and clients. This type of termination is called involuntary
turnover.

In this challenge, you'll need to help the Talent Team find which employees
are at higher risk of quitting the company due to low performance. If you can
successfully find these people, we can create training programs so they can
improve their output while developing themselves. If we fail these people,
they may end up losing their job as we may be unable to assign them to a
different project.

To do that, the Talent Team provided you with data. Now it's your turn to
transform data into insights and a model.


#### Dataset
This dataset is about the employees of an IT company. The main purpose of 
the challenge is to find which employees are under a high-risk of having 
a low-performance ticket (E=True). Here you find a list of variables which
are already hot-encoded.

* 'E' (Target variable): Is the employee a case of involuntary turnover? Yes
  or No.
* 'T': Time at the company in days
* Age: 
  - 'age_at_start=25:35',
  - 'age_at_start=35:45',
  - 'age_at_start=45:100'
* Gender: 
  - 'Gender=Male',
* On going studies?:
  - 'is_studying=Yes', 
* Education:
  - 'education=02 - Undergraduate',
  - 'education=03 - College Degree',
  - 'education=04 - MBA/Masters/Ph.D.',
* Seniority:
  - 'seniority=02 - Junior',
  - 'seniority=03 - Semi Senior',
  - 'seniority=04 - Senior',
  - 'seniority=05 - Architect',
* Country of Residence:
  - 'country_of_residence=Brazil',
  - 'country_of_residence=Colombia',
  - 'country_of_residence=Dominican Republic',
  - 'country_of_residence=Ecuador',
  - 'country_of_residence=Guatemala',
  - 'country_of_residence=Mexico',
  - 'country_of_residence=Other',
  - 'country_of_residence=Peru', 
  - 'country_of_residence=United States',
  - 'country_of_residence=Venezuela',
* Salary
  - 'salary_bins=Q_2',
  - 'salary_bins=Q_3',
  - 'salary_bins=Q_4',
  - 'salary_bins=Q_5',
* Last performance assessment by manager
  - 'last_perfor_assess=2 - Regular/Good Performance',
  - 'last_perfor_assess=3 - Excellent Performance',
* Project headcount
  - 'project_headcount=1 - Small [2 - 10]',
  - 'project_headcount=2 - Medium [10 - 50]',
  - 'project_headcount=3 - Large [50 - 100]',
  - 'project_headcount=4 - Very Large [>100]',


### Folder organization

```{bash}
.
├── /data - Datasets (training and test data)
├── /notebooks - Notebooks for exploration and modeling
├── /models - Serialized models
├── /src - Modules
├── /test - JSON file for test the REST Api
└── README.md
```


#### Required functionality

1. Fork the project repository;
2. Create a notebook and run an exploratory data analysis and modeling;
  - Comment your notebook cells, describing your rationale and decisions;
  - Inspect data completion;
  - Check how the variables relate to the target outcome;
  - Create a model that predicts the chances of involuntary turnover (column
   `E`);
  - Report model metrics;
  - Place your models (including preprocessing steps) in the `models` folder;
3. Save all project libraries and frameworks (i.e., requirements.txt) 
4. Make sure you document the README with all instructions needed to
   replicate your code;
5. Create an REST API inside a Docker container that receives the JSON
   located in `test/api_test.json`
   returns the prediction probability. 


#### Grading

Version Control
- Readme is well-documented and describe the general process
- Project runs inside a virtual env / container?
- Does the project have a commit history?

Exploratory Data Analysis
- Run data quality checks
- Check how variables relate to the target outcome (E) using good visualization and tables
- Provide comments and description for each analysis

Modeling
- Split data strategy (train, validation, test)
- Optimized model with hyperparameter search
- Train the final model with all available data
- Report proper classification or survival analysis metrics
- Saved models inside `models` folder
- Dependencies are stored inside a requirements.txt
- Provide comments and description for each decision?

Deployment
- Does the REST Api work?
- Dockerimage is optimized for serving the predictions?
- Does the REST Api has auto generated documentation?
- Does project specify libraries and Python version?

#### Tools

At BairesDev, we rely on Python to build our data products. We expect you to
use Python and its data-science libraries for this project. As the time is
short, you may want to use Auto-ML libraries.


### Time limit

* We respect your time. Please don't spend more than 3 hours max trying to
  solve the challenge. 


### Submission

Share your repository with the technical interviewer: 
henrique.pinto[at]bairesdev.com . Make sure to include any instructions on 
how to run the app in the README.md
