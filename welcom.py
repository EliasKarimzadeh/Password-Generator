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
    

from check import check
from  seting  import seting_ferst
from set import check_seting as cs
def welcome(seting):
    print('-'*20)
    print('Welcom to Password Gnarator'
          '\nThis app development by EKDEVELIPER')
    print('-'*20)
    print(f'The seting Password Gnarator {seting}.')
    while True:
        user_input_seting = input('Do you change the seting?(y->Yes , n->No , enter->Yes)')
        user_checked = check.check_carect_enter_user(user_input_seting)
        if  user_checked in [True , False]:
            if user_checked == True :
                print('-' * 5 , 'Setting' , '-' * 5)
                cs.change_seting(seting_ferst)
                break
            break
        pass