import nltk
import csv
from pandas import *
# nltk.download()

Dic =[]



if __name__ == "__main__":
    data_frame = pandas.read_csv("Pythonout.csv", encoding="ISO-8859-1")
    for name, group in data_frame.groupby('job_industry_1'):
        for index, row in group.iterrows():
            wordList = row['description'].split()
            # to extract most frequent from requirment
            # wordList = row['job_requirements'].split()
            n= nltk.FreqDist(wordList)
        most_freq=n.most_common(50)
        # if you want to plot every frequent word per industry
        # n.plot()
        print(name,n.most_common(50))
        Dic.append([name ,n.most_common(50)])
        with open("desc.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(Dic)


