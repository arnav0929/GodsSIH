from database import *
from voice_recognition import *
from speak import *

def jobsportal(userID):
    speak("We have following categories to select from")
    categ=job_category()
    category="none"
    aflag=False
    for cat in categ:
        if aflag==True: break
        speak(cat)
        speak("are you interested in this category ?")
        ans=takeCommand()
        
        if 'no' in ans or 'donot' in ans or 'do not' in ans or 'not interested' in ans: continue
        if 'yes' in ans or 'yeah' in ans or 'sure' in ans or 'done' in ans or 'interested'in ans:
            speak("here is the list of available jobs")
            jobs=get_jobs(cat)
            for job in jobs:
                speak("Job title "+job[1])
                speak("salary "+str(job[2])+"rupees")
                speak("Job Description "+job[3])
                speak("Skills Required "+job[4])
                speak("want to apply ?")
                ans=takeCommand()
                if 'no' in ans or "don't" in ans or "do not" in ans:
                    speak("Okay, let me see any other job")
                elif 'yes' in ans or 'yeah' in ans or 'sure' in ans:
                    apply(job[0], userID)
                    speak("applied for this job")
                    speak("hurray")
                    speak("Want to apply for more jobs ?")
                    an=takeCommand()
                    if 'yes' in an or 'i want' in an or 'sure' in an or 'ok' in an: continue
                    elif 'no' in an or 'i do not' in an or "don't" in an :
                        aflag=True
                        break 
                elif 'exit' in ans or 'quit' in ans: break
            speak("signing off from job portal")

# jobsportal(1)