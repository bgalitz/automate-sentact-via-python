# automate-sentact-via-python
Pilot

Building a script interface for Sentact completed jobs into PeopleSoft Express Issue

The workflow:
Sentact sends text file via email every morning (for the previous day)
The file represents items issued to floors via the warehouse
The file needs to be dumped to a specific folder (tbd)
The job runs twice a day
  -it checks the folder
  -if there is a file it opens it and begins reading line-by-line
  -each line contains the cost center, psoft number and qty issued
  -for each line it goes to the express issue page in peoplesoft
  -it enters the data in the corresponding fields

This essentially replaces the need for a person to issue the item in Sentact and then deduct the item from Peoplesoft.

Current estimates are 200 items per day (on average). 
At over a minute per entry - that's over 3 hours of redundant labor that this is saving.
In addition, the accuracy will increase for all the times staff is issuing but not deducting in a timely manner.

The job is running a day behind but the accuracy will still be acheived.

The initial job was build in autohotkey but based primarily on x,y coordinates per page.
This made for a volatile system. 
Looking forward to this implementation solving the need to have someone push the job.
Leave the pc running and time this to run twice a day? (9am & 1pm)
