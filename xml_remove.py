from pandas import *
from bs4 import BeautifulSoup

desc = []
job_requirement = []

data_frame = pandas.read_csv("wuzzuf.csv",encoding="ISO-8859-1")

for index, row in data_frame.iterrows():
      soup = BeautifulSoup(row['description'],"lxml")
      soup2 = BeautifulSoup(row['job_requirements'], "lxml")
      desc.append(soup.get_text())
      job_requirement.append(soup2.get_text())
      print (index ,soup.get_text())

data_frame['description']=desc
data_frame['job_requirements']=job_requirement
data_frame.to_csv("Pythonoututf8.csv",encoding="UTF-8", index=False )
