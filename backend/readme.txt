

examples of how to deal with the api


http://mshahzaib.pythonanywhere.com/user/get
{"users": []}

http://mshahzaib.pythonanywhere.com/user/add/yes & face-vec & Danish & username123 & pass123
"{done:true}"

http://mshahzaib.pythonanywhere.com/user/get
{"users": [[1, "yes", "face-vec", "Danish", "username123", "pass123"]]}

http://mshahzaib.pythonanywhere.com/user/del/1
"{done:true}"

http://mshahzaib.pythonanywhere.com/user/get
{"users": []}


###############################################################################################

http://mshahzaib.pythonanywhere.com/note/get
{"notes": []}

http://mshahzaib.pythonanywhere.com/note/add/sendername & thisisthenote & thisisthetime & 7
"{done:true}"

http://mshahzaib.pythonanywhere.com/note/get
{"notes": [[1, "sendername", "thisisthenote", "thisisthetime", 7]]}

http://mshahzaib.pythonanywhere.com/note/del/1
"{done:true}"

http://mshahzaib.pythonanywhere.com/note/get
{"notes": []}



###############################################################################################


http://mshahzaib.pythonanywhere.com/alarm/get
{"alarms": []}

http://mshahzaib.pythonanywhere.com/alarm/add/thisisalarmtime & 6
"{done:true}"

http://mshahzaib.pythonanywhere.com/alarm/get
{"alarms": [[1, "thisisalarmtime", 6]]}

http://mshahzaib.pythonanywhere.com/alarm/del/1
"{done:true}"

http://mshahzaib.pythonanywhere.com/alarm/get
{"alarms": []}



###############################################################################################


http://mshahzaib.pythonanywhere.com/todo/get
{"todos": []}

http://mshahzaib.pythonanywhere.com/todo/add/thisisthetodo & 2
"{done:true}"

http://mshahzaib.pythonanywhere.com/todo/get
{"todos": [[1, "thisisthetodo ", 2]]}

http://mshahzaib.pythonanywhere.com/todo/del/1
"{done:true}"

http://mshahzaib.pythonanywhere.com/todo/get
{"todos": []}

###############################################################################################

http://mshahzaib.pythonanywhere.com/reminder/get
{"reminders": []}

http://mshahzaib.pythonanywhere.com/reminder/add/thisisthetime & thisisthereminder & 8
"{done:true}"

http://mshahzaib.pythonanywhere.com/reminder/get
{"reminders": [[1, "thisisthetime", "thisisthereminder", 8]]}

http://mshahzaib.pythonanywhere.com/reminder/del/1
"{done:true}"
http://mshahzaib.pythonanywhere.com/reminder/get
{"reminders": []}