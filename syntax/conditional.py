#!C:\Users\super\AppData\Local\Programs\Python\Python37-32\python.exe

user_id = input('Enter ID : ')
user_pwd = input('Enter Password : ')

if user_id == 'sangumee' and user_pwd == '111111':
    print('Login Success with ' + user_id)
elif user_id == 'egoing' and user_pwd == '222222':
    print('Login Success with '+user_id)
else:
    print('Wrong Information')


'''
if user_id == 'sangumee':
    if user_pwd == '111111':
        print('Login Success')
    else:
        print('Wrong Password!!')
else:
    print('Wrong ID')
'''

'''
if user_input == '111111':
    print('Login Success')
else:
    print('Wrong Password!!')
'''
