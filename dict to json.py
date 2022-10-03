import json

dictionary= {
             "result":[
                {
                    "name":"vishal",
                    "current learning":"json",
                    "emotion":"happy"
                },
                {
                    "name":"siva",
                    "current learning":"flask",
                    "emotion":"happy"
                },
                {
                    "name":"ashmi",
                    "current learning":"sql",
                    "emotion":"happy"
                }
                  ]
            }  
result = json.dumps(dictionary)                      
print(result) 