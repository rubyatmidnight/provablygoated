# provablygoated
A few python local provable fairness verifiers for goated.com


### EXAMPLE USAGE

WINDOWS: I CBA TO DO OTHER TUTORIALS IF YOU ARE USING LINUX YOU PROBABLY KNOW ALREADY

Any recent version of python will likely do (3.x+)

Very simple: Once python is installed and set to path (find a tutorial to install python locally if you haven't and don't know how), in a cmd window, open to the path in explorer. For Windows 11, you can shift + right click into the explorer window where the script is and click open powershell,
or you can open cmd from the search menu and navigate to the folder where either of the .py files you want to use are.

For example, 

`cd C:\Users\YourName\Downloads`

Once there, you can enter `ls` to see a list of files in the location to make sure it's there, and to remember the name. 
then enter into cmd,

`py limbo.py` or `py dice.py`

It will prompt you for the unhashed server seed and client seed, as well as how many rolls you want to generate. Theoretically, it can handle as many as you want, but something like excel can only handle about a million rows gracefully. I would suggest not generating more than 500,000 at once unless you know what you're doing. 

This will generate the list of rolls that can then be checked either by having rolled beforehand on the website (specificaly goated.com, this will not work for other sites!)

What you do with the csv file is your business, but my dice and limbo spreadsheets in my stake repo will also work for these very well!
