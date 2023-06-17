<h1>RPA E-mail Report</h1> 

<p> This is a small project created for academic purposes. The objective of this
project is to build a RPA code that analyzes database originated information and
automatically sends an E-mail Report regarding simulated purchase orders.</p>

### Packages used:
+ pyautogui
+ time
+ pyperclip

<p>This automation mainly relies on the pyautogui package to automatically control
the mouse and keyboard to perform actions described below.</p>

<p> Disclaimer: the website used in this project was created as a form of simulating a
log in process and the data presented in "Compras.csv" is fictitious and only used
for purpose academic.</p>

## Getting the data
<p>The data is collected from an online database, in order to download it we need to
input our credentials.</p>

https://github.com/Hugo-Hattori/RPA_email_report/blob/23fae2a2136cd9124ba430c975e3fd721e55ff5d/RPA_email_report.py#L28-L44

## Data Analysis
<p>The data acquired in question is presented in "Compras.csv". Now we need to access
the .csv file and process the data in order to extract the output necessary for the report.</p>

https://github.com/Hugo-Hattori/RPA_email_report/blob/23fae2a2136cd9124ba430c975e3fd721e55ff5d/RPA_email_report.py#L50-L55

## Sending the E-mail Report
<p>The last step is to send the e-mail report containing the output previously extracted
from the "Compras.csv" file.</p>

https://github.com/Hugo-Hattori/RPA_email_report/blob/23fae2a2136cd9124ba430c975e3fd721e55ff5d/RPA_email_report.py#L69-L97