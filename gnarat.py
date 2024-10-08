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
    

import random 
import string
from qotion import if_user_dontlike_password

if __name__ == '__main__':
    print('khar khodete Gozo')

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