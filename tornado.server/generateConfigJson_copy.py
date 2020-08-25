import json
import numpy as np
import math

totalConfig = 10
questionNum = 27
# category = ["A","B"]
totalCategory = []
randomIndex = np.arange(1,11,1)
totalA = ['A'+str(x) for x in randomIndex ]
totalB = ['B'+str(x) for x in randomIndex ]
print(randomIndex)
print(totalA)
print(totalB)
for i in range(totalConfig):
    initA = np.random.randint(0,2,27)
    totalCategory.append(initA)
    initB = np.array([abs(x-1) for x in initA])
    totalCategory.append(initB)
print(totalCategory)





totalQA = [
        "Does the Orange cluster overlap with the Blue one?",
      "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?",
      "Which cluster overlaps with the largest number of clusters?",
    "Does the Orange cluster overlap with the Blue one?",
      "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?",
      "Which cluster overlaps with the largest number of clusters?",
    "Does the Orange cluster overlap with the Blue one?",
    "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?",
    "Which cluster overlaps with the largest number of clusters?",
    "Does the Orange cluster overlap with the Blue one?",
    "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?",
    "Which cluster overlaps with the largest number of clusters?",
        "Does the Orange cluster overlap with the Blue one?",
      "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?",
      "Which cluster overlaps with the largest number of clusters?",
    "Does the Orange cluster overlap with the Blue one?",
    "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?",
    "Which cluster overlaps with the largest number of clusters?",
    "Does the Orange cluster overlap with the Blue one?",
    "Which cluster has the largest portion overlapped by the Green cluster, Orange or Red?",
    "Which cluster overlaps with the largest number of clusters?",
    "Does the Orange cluster overlap with the Blue one?",
    "Which cluster has the largest portion overlapped by the Yellow cluster, Blue or Brown?",
    "Which cluster overlaps with the largest number of clusters?",
    "Does the Orange cluster overlap with the Blue one?",
    "Which cluster has the largest portion overlapped by the Blue cluster, Yellow or Purple?",
    "Which cluster overlaps with the largest number of clusters?"
]
questionContent = {
    0:[
        {
          "name": "red",
          "code": "#e41a1c"
        },
        {
          "name": "blue",
          "code": "#377eb8"
        },
        {
          "name": "green",
          "code": "#4daf4a"
        },
        {
          "name": "orange",
          "code": "#ff7f00"
        }
      ],
    1:[
        {
          "name": "red",
          "code": "#e41a1c"
        },
        {
          "name": "blue",
          "code": "#377eb8"
        },
        {
          "name": "green",
          "code": "#4daf4a"
        },
        {
          "name": "orange",
          "code": "#ff7f00"
        },
         {
          "name": "yellow",
          "code": "#ffff33"
        },
         {
          "name": "brown",
          "code": "#a65628"
        }
      ],
    2:[
        {
          "name": "red",
          "code": "#e41a1c"
        },
        {
          "name": "blue",
          "code": "#377eb8"
        },
        {
          "name": "green",
          "code": "#4daf4a"
        },
        {
          "name": "orange",
          "code": "#ff7f00"
        },
         {
          "name": "yellow",
          "code": "#ffff33"
        },
         {
          "name": "brown",
          "code": "#a65628"
        },
          {
          "name": "purple",
          "code": "#984ea3"
        },
          {
          "name": "pink",
          "code": "#f781bf"
        }

      ]
}

documentIndex = ['A','B']
for j in range(totalConfig*2):
    tmpAllJson = {
  "1": {
    "pagetype": "userinfopage",
    "divstyle": "position:absolute;top:30%;left:10%",
    "tablestyle": {
      "border": "1",
      "bordercolor": "steerblue",
      "cellpadding": "10px",
      "cellspacing": "0"
    },
    "tablecaption": "Info",
    "trandtd": [
      {
        "display": "Age",
        "tdtype": "text",
        "name": "age",
        "type": "text"
      },
      {
        "display": "gender",
        "tdtype": "radio",
        "option": [
          {
            "display": "Female",
            "type": "radio",
            "name": "gender",
            "value": "F",
            "checked": "checked"
          },
          {
            "display": "male",
            "type": "radio",
            "name": "gender",
            "value": "M",
            "checked": "none"
          }
        ]
      },
      {
        "display": "Academic studies",
        "tdtype": "radio",
        "option": [
          {
            "display": "Science/Engineering",
            "type": "radio",
            "name": "studyinterest",
            "value": "Science Engineering",
            "checked": "checked"
          },
          {
            "display": "Humanities and Social sciences",
            "type": "radio",
            "name": "studyinterest",
            "value": "Humanities and Social sciences",
            "checked": "none"
          },
          {
            "display": "Others",
            "type": "radio",
            "name": "studyinterest",
            "value": "Others",
            "checked": "none"
          }
        ]
      },
      {
        "display": "Academic Level",
        "tdtype": "radio",
        "option": [
          {
            "display": "Undergraduate",
            "type": "radio",
            "name": "academiclevel",
            "value": "Undergraduate",
            "checked": "checked"
          },
          {
            "display": "Post graduate (MSc, PhD)",
            "type": "radio",
            "name": "academiclevel",
            "value": "Post graduate (MSc, PhD)",
            "checked": "none"
          },
          {
            "display": "Other",
            "type": "radio",
            "name": "academiclevel",
            "value": "Other",
            "checked": "none"
          }
        ]
      },
      {
        "display": "Assess your experience in Data Visualization",
        "tdtype": "radio",
        "option": [
          {
            "display": "None",
            "type": "radio",
            "name": "experience",
            "value": "None",
            "checked": "checked"
          },
          {
            "display": "Little",
            "type": "radio",
            "name": "experience",
            "value": "Little",
            "checked": "none"
          },
          {
            "display": "Medium or pretty good",
            "type": "radio",
            "name": "experience",
            "value": "Medium or pretty good",
            "checked": "none"
          },
          {
            "display": "Very good",
            "type": "radio",
            "name": "experience",
            "value": "Very good",
            "checked": "none"
          }
        ]
      }
    ]
  },
    }

    for i in range(0,27):
        tmpAllJson[str(i+2)] = {}

        imgIndex = math.floor(i / 3)
        contentIndex = math.floor(i/9)

        if i%3==0:
            tmpoptiontype = "radiotext"
            content =   [
        {
          "name": "yes"
        },
        {
          "name": "no"
        }
      ]
        else:
            tmpoptiontype = "radiocolor"
            content = questionContent[contentIndex]
        tmp = {
            "pagetype": "questionoptionpage",
            "imgsrc": "/totalConfig/"+documentIndex[totalCategory[j][imgIndex]]+"/"+str(imgIndex)+".png",
            "questionname":totalQA[i],
            "optiontype":tmpoptiontype,
            "optioncontent":content
        }
        tmpAllJson[str(i + 2)] = tmp
        print(tmp)
    documentName = "../totalConfig/"+"config"+str(j)+".json"
    with open(documentName,"w",encoding="utf-8")as f:
        f.write(json.dumps(tmpAllJson))
    f.close()


# for i in range(10):
#     totalCategory[totalA[i]] =


# for i in range(10):
    # tmpA =