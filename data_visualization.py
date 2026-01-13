"""Data Processing and Visualization: Given a dataset containing information about students' test scores,
fetch the data from an API, calculate the average score, and create a bar chart to visualize the data."""

import requests
import matplotlib.pyplot as plt
url="https://mocki.io/v1/3782f371-7788-485c-b44f-ea6dd5deee6b"
response=requests.get(url)
data=response.json()

stu_names=[]
avg_scores=[]

for student in data:
    subjects=student["subjects"]
    length=len(subjects)
    avg=sum(subjects.values())/length
    stu_names.append(student["student_name"])
    avg_scores.append(avg)
    #print(student["student_name"],"Average:",avg)
    
plt.figure(figsize=(12,6))
plt.bar(stu_names,avg_scores)
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Average Score per Student")
plt.xticks(rotation=90)  
plt.tight_layout()
plt.show()