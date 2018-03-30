# CSSE
For Software Process Course in Auburn University Software Engineering

## Purpose
The premise of this project is to create a program in Python that will serve as functions on AWS Lambda using various software developement processes and disciplines, with the focus being Test Driven Developement (TDD).

#### We are to record specifically the following inside of a spreadsheet during our project: 

### Plan	
Record estimated/actual LOC, nuber of components, and time of our primary deliverable(s). Not including test code.					

### Acceptance
Develop acceptance tests for the specified black box.  Not including tests for items that are not part of the specifications (meaning, items over and above the specs -- these tests will appear in your individual unit test files).  Write the expected results at planning time.  Modify if necessary later.  Don’t write actual results in advance.

### Time Log
Use the "sandbox" activity to record time spent experimenting with the assignment requirements.					

### Historical Data	
Record your process and product data from all previous programming assignments.  Do this as part of the planning activity.					

### Lessons Learned	
This tab is optional. Used to record great ideas, suggestions, etc.					


## Project Description
We are developing a set of microservices that derives geographic position from star sighting information. Each microservice receives its input as a Python dictionary represented by a URL-encoded string and outputs its result as UTF-8 string of a Python dictionary. This assignment has you to write a function that adjusts celestial sightings based on the circumstances of how the sighting was made.   						
## Specification by Example						
The following is an example of how your customer plans to use the code:						
						
#### Example Code 
```
import dispatch as dispatch						
sighting = {'op':'adjust', 'observation':'015d04.9', 'height':'6.0', 'temperature':'72','pressure':'1010', 'horizon':'artificial'}						
result1 = dispatch.dispatch(sighting)						
sighting['op']='predict' 						
sighting['name']='Betelgeuse' 						
sighting['date']='2016-01-17' 						
sighting['time']='03:15:42' 						
result2 = dispatch.dispatch(sighting)						
```

#### AWL Lambda Example						
https://2kr26wpool.execute-api.us-east-1.amazonaws.com/prod/navigate/?op=adjust&observation=015d04.9&height=6.0&temperature=72&pressure=1010&horizon=artificial						
https://2kr26wpool.execute-api.us-east-1.amazonaws.com/prod/navigate/?op=predict&observation=015d04.9&height=6.0&temperature=72&pressure=1010&horizon=artificial&name=Betelgeuse&date=2016-01-17%time=03%3A15%3A42

## Process
#### Plan Project	
  - Transfer process information from the previous assignment (record in Historical Data tab) 
  - Write as many acceptance tests as you feel are necessary to understand the assignment (record in Acceptance tab)
  - Guess projected LOC and number of components (classes) (record in Plan tab)
  - Guess projected effort (in minutes)	(record in Plan tab)
#### Construction	
  - repeat		
    - select/write a test case and run it as a red light test		
	  - while the test is not red		
	    - diagnose why the test was not red		
	    - if the problem was due to incorrect test code		
	      - fix the defect and log it in the change log
	    - else		
	      - continue to the next red light test		
	    - build enough production code to make the test pass		
	    - run the test as a green light test		
	    - while the test is not green		
	      - fix the defect and log it in the change log	
	      - run the test as a green light test		
	    - clean up the code as appropriate		
  - until test coverage is sufficient and all tests pass		
  - Commit all code to git.		

#### Review	
  - Perform rubber duck review of test code		

#### Refactor	
  - Refactor production code to remove odious smells		
#### Post Mortem	
  - Record acceptance test results		Acceptance
  - Count production LOC (in Plan tab)
  - Count components (in Plan tab)

#### Release	
  - Commit all code to git.		
  - Push to GitHub.com		
  - Deploy code to AWS Lambda		
  - Upload completed spreadsheet to Github		
			
#### Monitor	
  - Record time spent in each activity. (Time Log)
  - Record defects, changes to requirements. (Change Log)

