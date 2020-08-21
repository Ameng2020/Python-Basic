import re


##要进行中文分词，必须要求数据格式全部都是中文，需求过滤掉特殊符号、标点、英文、数字等。当然了用户可以根据自己的要求过滤自定义字符。
# x = 'a12121assa'
# x = '1我爱你1'
# r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
# 
# print(re.sub(r1, '', x))
# 
# 
# 
# #过滤掉数字
# L = ['小明', 'xiaohong', '12', 'adf12', '14']
# for i in range(len(L)):
#     if re.findall(r'^[^\d]\w+', L[i]):
#         print(re.findall(r'^\w+$', L[i])[0])

emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+      # username
            @                      # @ symbol
            [a-zA-Z0-9.-]+         # domain name
            (\.[a-zA-Z]{2,4}){1,2} # dot-something
            )''', re.VERBOSE)


a = "{'EventRegistrationID': '54438', 'FormTimeStamp': '09/10/18 10:13:56', 'SSNumber': '4723', 'FirstName': 'Andrew', 'LastName': 'Houck', 'HIDTATaskForceMember': '0', 'WhichTaskForce': '', 'SwornLawEnforcement': '1', 'CriminalAnalyst': '0', 'OtherOrgType': '0', 'Address2': '', 'City': 'Burlington', 'State': 'NC', 'ZipCode': '27215', 'PhoneWork': '336-229-3500', 'CellPhone': '336-337-4981', 'FaxNumber': '', 'EmailAddress': 'pwallace@burlingtonnc.gov', 'SubmitReg': '', 'IPAddress': '96.10.149.98', 'InternalNotes': '', 'Approved': '0', 'Password': '', 'LastUpdate': '', 'DoNotSend': '0', 'EventFormNameCancelled': '', 'Cancelled': '0', 'GAOkey': 'N/A', 'DOB': '', 'VerifyEmailAddress': '', 'Submit': '', 'EventFormName': 'Mid-LevelManagementforPolice10-09-10-2018', 'DidNotAttend': '0', 'AgencyType': 'Local', 'ArrestPowers': '', 'ConfirmationNumber': '', 'ReferringURL': '', 'SupervisorPhoneWork': '336-229-3517', 'AlternateEmail': '', 'AgencyOrganizationName': '', 'OtherOrgDescription': '', 'Address1': '267 West Front Street', 'RespondByStart': '', 'C-NSDTS': '', 'guid': 'ee3fd727-47be-4f43-b881-f88819468abc', 'EventFormNameWaitingList': '', 'RegFormType': '', 'EventCost': '0', 'Blacklisted': '0', 'BlacklistedComments': '', 'IndentifyingInfo': '', 'DietaryNeeds': '', 'DrugGrowthSolution': '', 'DrugGrowthFactors': '', 'SupervisorEmailAddress': 'skatkowski@burlingtonnc.gov', 'DateCancelled': '', 'fullname': 'Andrew Houck', 'SentCertificate': '1', 'CourseCode': '', 'AgencyOrganization': 'Burlington Police Department', 'AuthorizationCode': '', 'CCFirstName': '', 'CCLastName': '', 'CCAddress': '', 'CCNumber': '', 'CCExpire': '', 'CCSecurityCode': '', 'CCZip': '', 'CCCountry': '', 'SupervisorFullName': 'Lt. Katkowski', 'PositionTitleRank': 'MPO', 'SurveyCompleted': '0', 'NSBounceSoft': '0', 'NSBounceHard': '0', 'Processed': '0', 'NSFormName': '', 'EmailAddressConfirm': '', 'Attachment': '', 'EmailAttachmentsOnly': '0', 'Deactivated': '0', 'PreeventSurveyCompleted': '0', 'FollowUpSurveyCompleted': '0', 'EventBuilderApprovalLevelID': '', 'Clearence': '', 'MiddleName': ''}"
emails=[]
for groups in emailRegex.findall(a):
    emails.append(groups[0])
    print(emails)

for email in emails:
    
    print(email)