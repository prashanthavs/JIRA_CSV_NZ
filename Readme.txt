1.) Replace the user name and password at the below line in function query():

jira = JIRA(basic_auth=('$$USERNAME', '$$PASSWORD'),options={'server': 'https://cnwyjira.atlassian.net'})  ##Authentication


2.)  Replace the user name and password at the below line in function Netteza():

   os.system('nzload.exe -host npsdwh -u $$USERNAME -pw $$PASSWORD -db SANDBOX -t JIRA_ISSUE_LIST -delim "," -dateDelim "-" -fillRecord -maxErrors 200 -nullvalue "" -LfInString -lf c:\\logs\\nzload.txt -df C:\\Users\\pxakundi\\PycharmProjects\\new\\output.csv')


3.) Replace the directory of the file generated ,  in the last argument for the statements below. 
  

   os.system('nzload.exe -host npsdwh -u $$USERNAME -pw $$PASSWORD -db SANDBOX -t JIRA_ISSUE_LIST -delim "," -dateDelim "-" -fillRecord -maxErrors 200 -nullvalue "" -LfInString -lf c:\\logs\\nzload.txt -df C:\\Users\\pxakundi\\PycharmProjects\\new\\output.csv')
    
   Append the same argument in the below statement
   
   os.remove("C:\\Users\\pxakundi\\PycharmProjects\\new\\output.csv")
   
   
4.) Create a Folder c:\\logs  , if you don't already have one . 