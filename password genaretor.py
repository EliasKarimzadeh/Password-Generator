""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    | $  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\  $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @                      ELIAS KARIMZADEH                            @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @              GitHub: github.com/EliasKarimzadeh                  @ \ $ |
    | $ \ @             Linkdin: in/elias-karimzadeh-a7a9b8283               @ / $ |
    | $ / @            Instagram : instagram.com/elyaskarymzade              @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |
    | $ \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ $ |
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|"""
    
    
import string
import random
import os
os.system('cls')


MAX_NUMBER_PW = 12
MIN_NUMBER_PW = 4

seting_ferst = {
    'Uppercase' : True,
    'Lowercase' : True,
    'Numbercase' : True,
    'Symbolcase' : True,
    'Spasecase' : False,
    'lenght' : 8
}


def if_all_false(str_false):
    if str_false == 5 :
        print('You cannot select any character!!!')
        print('Plese try again .')
        return False
    return True

def check_carect_enter_user(user_input): #
    '''return True and False or None -> entry invalid '''
    if user_input in ['y' , 'n' , '']:
        if user_input == 'n':
            return False
        return True
    print('Plese Enter a valid entry.')
    print('Plese try agine .')
    
    
def check_carect_enter_number_user(user_number): #
    '''Number recognition by user_number'''
    if user_number == '':
        return True   
    if user_number.isdigit() == True :
        if MIN_NUMBER_PW < int(user_number) < MAX_NUMBER_PW :
            return True
        else:
            print(f'The Password must by number between {MIN_NUMBER_PW} and {MAX_NUMBER_PW} .')
            print('Plese try again.')
    else:
        print('Plese Enter number.')
        print('Plese try again.')
        
        
def set_number(seting , key , val):
    while True:
        user_number_input = input('Plese Enter lenght Password .'
                                        f'Defult is {val} (enter -> {val}) :')
        if check_carect_enter_number_user(user_number_input) == True:
            if user_number_input == '':
                return True
            else:
                seting[key] = user_number_input
                return True


def change_seting(seting): #
    '''chenged dictionary seting by geeting input user'''
    while True :
        str_false = 0
        for key , val in seting.items():
            while True:
                if key != 'lenght':
                    input_seting = input(f'Do you want {key}? Defult is {val}: '
                                                '(y->Yes , n->No , enter->Yes): ')
                    input_seting = check_carect_enter_user(input_seting)
                    if input_seting in [True , False]:
                        if input_seting == False :
                            str_false += 1
                        seting[key] = input_seting
                        break
                    pass
                
                else:
                    if set_number(seting , key , val):
                        break
        if if_all_false(str_false) == True:
            break           

    
                    
    
def welcome(seting):
    print('-'*20)
    print('Welcom to Password Gnarator'
          '\nThis app development by EKDEVELIPER')
    print('-'*20)
    print(f'The seting Password Gnarator {seting}.')
    while True:
        user_input_seting = input('Do you change the seting?(y->Yes , n->No , enter->Yes)')
        user_checked = check_carect_enter_user(user_input_seting)
        if  user_checked in [True , False]:
            if user_checked == True :
                print('-' * 5 , 'Setting' , '-' * 5)
                change_seting(seting_ferst)
                break
            break
        pass
    
    
def if_user_dontlike_password(): # 
    while True:
        user_input_OK = input('Do you want chang Password ? (y->Yes , n->No , enter->Yes) :')
        if check_carect_enter_user(user_input_OK) in [True , False]:
            if check_carect_enter_user(user_input_OK) == False :
                print('Thans for you')
                print('Plese do not share the password with others and be diligent in maintaining it.')
                return 'N'
            return "Y"
        
    
#### seting sit and genarator start

def password_generetor(seting_ferst):
    ferst_password = ''
    final_password = ''
    if seting_ferst['Uppercase'] == True :
        ferst_password += string.ascii_uppercase
    if seting_ferst['Lowercase'] == True :
        ferst_password += string.ascii_lowercase
    if seting_ferst['Numbercase'] == True :
        ferst_password += string.digits
    if seting_ferst['Symbolcase'] == True :
        ferst_password += string.punctuation
    if seting_ferst['Spasecase'] == True :
        ferst_password += ' '
    while True :
        for _ in range(int(seting_ferst['lenght'])):
            final_password += random.choice(ferst_password)
        print('-' * 20)
        print(f'Your password : {final_password}')
        print('-' * 20)
        if if_user_dontlike_password() == "Y":
            final_password = ''
            pass
        else:
            break


def ran():
    welcome(seting_ferst) 
    # sit seting
    password_generetor(seting_ferst)
    
ran()