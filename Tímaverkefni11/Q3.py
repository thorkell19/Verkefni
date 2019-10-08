def get_emails():
    email_list = []
    mail = input("Email address: ")
    while mail != "q":
        email_list.append(mail)
        mail = input("Email address: ")
    return email_list

def get_names_and_domains(email_list):
    splitlist = []
    for email in email_list:
        split_email = tuple(email.split("@"))
        splitlist.append(split_email)
    return splitlist

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)