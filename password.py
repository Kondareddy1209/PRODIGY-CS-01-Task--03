import re
def check_password_strength(password):
    strength=0
    feedback=[]
    if len(password)>=8:
        strength+=1
    else:
        feedback.append("password contains atleast 8 characters")
    if re.search(r'[A-Z]',password):
        strength+=1
    else:
        feedback.append("password contains atleast one upper case letter ")
    if re.search(r'[a-z]',password):
        strength+=1
    else:
        feedback.append("password contains atleast one lower case letter ")
    if re.search(r'[!@#$%^&*()<>,.:+=|]',password):
        strength+=1
    else:
        feedback.append("password contains atleast one special characters")
    if re.search(r'[0-9]',password):
        strength+=1
    else:
        feedback.append("password contains atlest one letter ")
    if strength==5:
        return"password is very strong",feedback
    elif strength==4:
        return"password is strong",feedback
    elif strength==3:
        return"password is medium",feedback
    elif strength==2:
        return "password is weak",feedback
    elif strength==1:
        return "password is too weak",feedback
    
password=input("Enter the password: ")
strength,feedback=check_password_strength(password)
print(f"password strength : {strength}")
for suggestion in feedback:
    print(suggestion)


