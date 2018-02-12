

examples of how to deal with the api


https://evaapi123.localtunnel.me/user/get
{"users": []}

https://evaapi123.localtunnel.me/user/add/yes & face-vec & Danish & username123 & pass123
"{done:true}"

https://evaapi123.localtunnel.me/user/get
{"users": [[1, "yes", "face-vec", "Danish", "username123", "pass123"]]}

https://evaapi123.localtunnel.me/user/del/1
"{done:true}"

https://evaapi123.localtunnel.me/user/get
{"users": []}


###############################################################################################

https://evaapi123.localtunnel.me/note/get
{"notes": []}

https://evaapi123.localtunnel.me/note/add/sendername & thisisthenote & thisisthetime & 7
"{done:true}"

https://evaapi123.localtunnel.me/note/get
{"notes": [[1, "sendername", "thisisthenote", "thisisthetime", 7]]}

https://evaapi123.localtunnel.me/note/del/1
"{done:true}"

https://evaapi123.localtunnel.me/note/get
{"notes": []}



###############################################################################################


https://evaapi123.localtunnel.me/alarm/get
{"alarms": []}

https://evaapi123.localtunnel.me/alarm/add/thisisalarmtime & 6
"{done:true}"

https://evaapi123.localtunnel.me/alarm/get
{"alarms": [[1, "thisisalarmtime", 6]]}

https://evaapi123.localtunnel.me/alarm/del/1
"{done:true}"

https://evaapi123.localtunnel.me/alarm/get
{"alarms": []}



###############################################################################################


https://evaapi123.localtunnel.me/todo/get
{"todos": []}

https://evaapi123.localtunnel.me/todo/add/thisisthetodo & 2
"{done:true}"

https://evaapi123.localtunnel.me/todo/get
{"todos": [[1, "thisisthetodo ", 2]]}

https://evaapi123.localtunnel.me/todo/del/1
"{done:true}"

https://evaapi123.localtunnel.me/todo/get
{"todos": []}

###############################################################################################

https://evaapi123.localtunnel.me/reminder/get
{"reminders": []}

https://evaapi123.localtunnel.me/reminder/add/thisisthetime & thisisthereminder & 8
"{done:true}"

https://evaapi123.localtunnel.me/reminder/get
{"reminders": [[1, "thisisthetime", "thisisthereminder", 8]]}

https://evaapi123.localtunnel.me/reminder/del/1
"{done:true}"
https://evaapi123.localtunnel.me/reminder/get
{"reminders": []}