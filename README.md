# Gift Exchange
#### Video Demo: https://youtu.be/eEMnw39kd_w
#### Description:
This project generates a Gift Exchange given a list of Participants. Individuals can be set to "not match" with one other participant while creating the Gift Exchange list. My family performs a three couple gift exchange each winter holiday season, and other tools we used either did not sufficiently randomize the exchange or did not allow for excluding specific matches.

##### Files
- **project.py:** Python file containing the code for the project.
- **README.md:** This file.
- **requirements.txt:** Specifies the required installable modules from pip
- **test_project.py:** a pytest python file used to test three of the functions in project.py

##### Design Choices
There were several design revisions to this solution. Overall this took two weeks to solve. My initial concept had too many features (saving files, complex menus, multiple exchanges, multiple no-matches for each participant).

Initially I created a class for an Exchange and a class for a Participant. I added class functions to help store and recall information. This made it so I didn't need any additional functions that I could test with pytest. Through iterations I discovered the correct balance, though i believe there are more object oriented ways of solving this problem.

I need to make note that I found pyge by Seth Black on pypi: https://pypi.org/project/pyge/. Black's explanatory page at: https://www.sethserver.com/python/secret-santa-gift-exchange.html gave me the inspiration to use a truth table to determine who could and couldn't give or recieve a gift.

Before that discovery, I was attempting to quantify my intuitive (and rather uneededly recursive method) of determining who could be matched. This brought me to figuring out how to make, address, and manipulate a numpy 2d array.
