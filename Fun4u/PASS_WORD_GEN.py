import string
import random 

if __name__ == "__main__":
    ps_low = string.ascii_lowercase
    # print(Lower)
    ps_upp = string.ascii_uppercase
    # print(Upper)
    ps_dig = string.digits
    # print(Digit)
    ps_pun = string.punctuation
    # print(Puntution)
    ps_len = int(input('Enter the password_length\n'))
    ps = []
    ps.extend(list(ps_low))
    ps.extend(list(ps_upp))
    ps.extend(list(ps_dig))
    ps.extend(list(ps_pun))
    # print(ps)
    random.shuffle(ps)
    # print(ps)
    print('Your Pass word is ...')
    # print("".join(ps[0:ps_len]))
    print("".join(random.sample(ps,ps_len)))
    print('')
    






