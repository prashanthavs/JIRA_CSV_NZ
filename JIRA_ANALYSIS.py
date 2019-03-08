from jira import JIRA
import csv
import os
from time import gmtime, strftime

list = []
dict = {}





def query():


 jira = JIRA(basic_auth=('$$USERNAME', '$$PASSWORD'),options={'server': 'https://cnwyjira.atlassian.net'})  ##Authentication

 ## This is the JQL query . Substitue other queries if neccessary.

 query='project = BIDM AND status not in (Closed, done, Verified, "Production Monitoring") AND type in ("BIDM Projects Sub-Tasks", "BIDM Data Modeling Support", "BIDM Production Support", "BIDM Prod Support Sub-Tasks", "BIDM Prod Support Incident", "BIDM Prod Support Enhancement") ORDER BY assignee, key '

 i=0
 x=0
 value = ''
 master_summary = ''
 master_id = ''

 ## The fields below are case-consistent so please use either upper or lower consistently
 for j in range(5):

  print("Extracting Issue Range from ",x,"to", x+100)

  for issue in jira.search_issues(query,startAt=x,maxResults=500,fields="*all"):



    for link in issue.fields.issuelinks:


         if hasattr(link, "outwardIssue"):
             value = link.outwardIssue.key
             master_summary=link.outwardIssue.fields.summary
             master_id = link.id


         elif hasattr(link, "inwardIssue"):

             value = link.inwardIssue.key
             master_summary = link.inwardIssue.fields.summary
             master_id=link.id







    if issue.fields.assignee is None:

        assigned=""

    else:
        assigned=issue.fields.assignee.displayName

    list=(issue.id,issue.key,issue.fields.summary,assigned,issue.fields.reporter.displayName,issue.fields.issuetype.name,issue.fields.status.name,value,master_id,master_summary,issue.fields.customfield_15009,issue.fields.customfield_15010,strftime("%Y-%m-%d", gmtime()) )

    dict[i]=list

    i=i+1;
    value=''
    master_summary = ''
    master_id=''

  print("Extract Successful ")
  x=x+100






def flat_file():    # writing the list of lists to a flat file .



        for i in dict:
                 with open('output.csv', 'a',encoding='UTF-8') as myfile:
                     wr = csv.writer(myfile,dialect='excel',lineterminator="\n")
                     wr.writerow(dict[i])
                     print(i,dict[i])



def netteza():   #NZ-LOAD

   os.chdir("C:\Program Files (x86)\IBM Netezza Tools\Bin")

   os.system('nzload.exe -host npsdwh -u $$USERNAME -pw $$PASSWORD -db SANDBOX -t JIRA_ISSUE_LIST -delim "," -dateDelim "-" -fillRecord -maxErrors 200 -nullvalue "" -LfInString -lf c:\\logs\\nzload.txt -df C:\\Users\\pxakundi\\PycharmProjects\\new\\output.csv')


   os.remove("C:\\Users\\pxakundi\\PycharmProjects\\new\\output.csv")

   os.startfile("c:\\logs\\nzload.txt")


query()
flat_file()
netteza()