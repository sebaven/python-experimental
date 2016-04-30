import urllib

def read_text():
    message = open("/Users/sebastien/Documents/workspace/python-programs/samples/message.txt")
    content = message.read()
    message.close()
    return content

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    response = connection.read()
    connection.close()
    return response
    
message = read_text()
check = check_profanity(message)
if "true" in check:
    print("Profanity Alert!!!!")
elif "false" in check:
   print("Hurray no mistakes!!!")
else:
  print("Could not scan the document properly.")
