import time

time = time.ctime()  # get time and date
# values to change
encrypting_values = {'a':'42=?X', 'b':'54f#@', 'c':'89*D%', 'e':'x^l89', 'f':'94/*@!', 'g':'89$gX',
                'h':'Qw2@j', 'i':'Lk9*1', 'j':'+09Po', 'k':'kl89*', 'l':'oi&89', 'm':'rg6&7',
            'n':'pi&u2', 'o':'Ja@$4', 'p':'Op*6k', 'q':'.- P6', 'r':'Mi+t2', 's':'Mak2@', 
        't':'Abs2#', 'u':'Bg@23', 'v':'34$Ty', 'w':'Rst%5', 'x':'a. st', 'y':'A @13',
    'z':'Stu=5', 'Z':'Tus+5', ' ':'8S8h&', '  ':'4+sCf', '   ':'k<j0*', '    ':'Q2/\n',
    '\n':'Hj)\n', '\t':'Aw4$1', '\'':'1oiU&*', '\"':'jJ22@', '\r':'Bc2@1', '@':'wh8@2',
        '#':'LjK8&', '!':'DfD#4', '`':'JuK&5', '~':r'VX5%c', '$':'reT5%', '%':'r+4\n',
            '^':'xzV$4', '*':'Aw2@2', '&':'>x3#G', '+':'09*Hh', '-':'/.Hh6', '_':'0*lKJ',
                '=':'Z@x34', '/':'rS4$J', '?':'T0+yz', '<':'aS7&P', '>':'Vv@31', ',':'cx+09',
                    '.':'Aas!1', ':':'Ssd@2', ';':'T3#t5', '0':'B7b&n', '1':'Nm8*8', '2':'M*yu6',
                    'd':'Zzx@2', '3':'Xxc#3', '4':'Ccv$4', '5':'Vvb&7', '6':'Bbn*8', '7':'Nnm(9',
                '8':'Ssd%5', '9':'Nn5#1', '10':'Rrs&2', '11':'Jjt^5', '100':'Aas)1', '101':'Zzx$2',
            'A':5*'t@7\n', 'B':'89D&J', 'C':'J*K8x', 'D':'852!D', 'E':'82d#!', 'F':'k8)45',
        'G':'As#$q', 'H':'!t7%9', 'I':'8/#sA', 'J':'59-+@', 'K':'23&lM', 'L':'E5&s9',
    'M':'A3$$q', 'N':'!t6^9', 'O':'//#sA', 'P':'59l+@', 'Q':'89&lM', 'R':'So&s9',
        'S':'Sd&89', 'T':'F9*r5', 'U':'85$lD', 'V':'4S#59', 'W':r'8%56aA',
            'X':'89!zW', 'Y':r'*94%sX','(':'85@45', ')':'85^kz', "\\":'Qwe4@', '|':'@fg28',
                1:'h65$$', 2:r'L82%$', 3:'**gFk', 4:r'vb@s9', 5:'a-_-s', 6:r'|abc|', 7:r'<\s/>', 8:'op(a)', 9:'/+Sx$', 0:'l>>8X'
}
# values to get back
decrypting_values = {'42=?X':'a', '54f#@':'b', '89*D%':'c', 'x^l89':'e', '94/*@!':'f', '89$gX':'g',
                'Qw2@j':'h', 'Lk9*1':'i', '+09Po':'j', 'kl89*':'k', 'oi&89':'l', 'rg6&7':'m',
            'pi&u2':'n', 'Ja@$4':'o', 'Op*6k':'p', '.- P6':'q', 'Mi+t2':'r', 'Mak2@':'s', 
        'Abs2#':'t', 'Bg@23':'u', '34$Ty':'v', 'Rst%5':'w', 'a. st':'x', 'A @13':'y',
    'Stu=5':'z', 'Tus+5':'Z', '8S8h&':' ', '4+sCf':'  ', 'k<j0*':'   ', 'Q2/\n':'    ',
    'Hj)\n':'\n', 'Aw4$1':'\t', '1oiU&*':'\'', 'jJ22@':'\"', 'Bc2@1':'\r', 'wh8@2':'@',
        'LjK8&':'#', 'DfD#4':'!', 'JuK&5':'`', r'VX5%c':'~', 'reT5%':'$', 'r+4\n':'%',
            'xzV$4':'^', 'Aw2@2':'*', '>x3#G':'&', '09*Hh':'+', '/.Hh6':'-', '0*lKJ':'_',
                'Z@x34':'=', 'rS4$J':'/', 'T0+yz':'?', 'aS7&P':'<', 'Vv@31':'>', 'cx+09':',',
                    'Aas!1':'.', 'Ssd@2':':', 'T3#t5':';', 'B7b&n':'0', 'Nm8*8':'1', 'M*yu6':'2',
                    'Zzx@2':'d', 'Xxc#3':'3', 'Ccv$4':'4', 'Vvb&7':'5', 'Bbn*8':'6', 'Nnm(9':'7',
                'Ssd%5':'8', 'Nn5#1':'9', 'Rrs&2':'10', 'Jjt^5':'11', 'Aas)1':'100', 'Zzx$2':'101',
            5*'t@7\n':'A', '89D&J':'B', 'J*K8x':'C', '852!D':'D', '82d#!':'E', 'k8)45':'F',
        'As#$q':'G', '!t7%9':'H', '8/#sA':'I', '59-+@':'J', '23&lM':'K', 'E5&s9':'L',
    'A3$$q':'M', '!t6^9':'N', '//#sA':'O', '59l+@':'P', '89&lM':'Q', 'So&s9':'R',
        'Sd&89':'S', 'T''F9*r5':'T', '85$lD':'U', '4S#59':'V', r'8%56aA':'W',
            '89!zW':'X', r'*94%sX':'Y','85@45':'(', '85^kz':')', 'Qwe4@':"\\", '@fg28':'|',
                'h65$$':1, r'L82%$':2, '**gFk':3, 'vb@s9':4, 'a-_-s':5, r'|abc|':6, r'<\s/>':7, 'op(a)':8, r'/+Sx$':9, 'l>>8X':0
}
def store_data(container, data):
    for char in range(len(data)):
        container.append(encrypting_values[data[char]])
    container = container.copy()

def write(data, file):
    for char in range(len(data)):
        file.write(data[char])
# lists for storing encrypted data
decrypt = []
message = []
user_passwd = []
pgp_key = []

# Starting PGP service
print(50*'\n')
print('wellcome to PGP Server')
# create an account and PGP keys
while 1:  # user details
    user_ID = input('Create your user ID\n=> ')
    print('\n'*50)
    ask_sign_name = input('Enter your full name\n=> ')
    ask_sign_email = input('Enter your emial ID.\n=> ')
    ask_sign_phone = input('Enter your mobile NO.\n=> ')
    print(50*'\n')
    print('Password should be 10 digit')
    print('"Space", "A" and "%" is not allowed')
    print('Password should contain a upper and lower case character')
    make_passwd = input('create your password\n=>  ')
    if (len(make_passwd)<10):
        print('Error Password is less than 10')
    else:
        break
# Content to create PGP keys
content = (make_passwd+' '+ ask_sign_email.split("@")[1].split(".")[0] +'PGP KEY'+ str(time) + ask_sign_name)
store_data(pgp_key, content)
# create PGP Pvt key
Key = input('Enter location to store Key\n=>')
with open(Key, 'w') as pvp:
# writing created PGP keys in "ALPGP.txt" file
# PGP public key writing start
    store_data(user_passwd, make_passwd)
    pvp.write('-------Begin PGP key--------\n')
    write(user_passwd, pvp)
    pvp.write(2*'\n')
    write(pgp_key, pvp)
    pvp.write('\n--------End PGP key--------\n')
    user_passwd = user_passwd.copy()
print(50*'\n')
# sign in
ask_userID = input('Enter your user ID')
ask_PGP = input('Enter location of PGP key\n')
# check details
PGP = open(ask_PGP, 'r')
line = 0
for i in PGP:
    line += 1
    if (line==2):
        print('\n'*50)
        for a in range(len(i)):
            if (i[a:a+5] in user_passwd):
                print('Password Match')
                break
            else:
                print('invalid Password')
            PGP.close()
# work engine
while 1:
# get and store encrypted message
    ask_message_file = input('Enter location of Message to encrypt\n=> ')
    with open(ask_message_file, 'r') as msg:
        for char in msg.read():
            message.append(encrypting_values[char])
            print(50*'\n')
# contain encrypted message
    enc_msg = input('Enter location to store encrypted Message\n=> ')
    with open(enc_msg, 'w') as enc:
        write(message, enc)
        print(50*'\n')
# decrypt message and store it
    dec_msg = input('Enter location to store decrypted message\n=> ')
    with open(dec_msg, 'w') as dec:  # contain decrypt file
        for char in message:
            decrypt.append(decrypting_values[char])
        write(decrypt, dec)
    print('Do you want to encrypt other message?')
# Restart
    opt_yes = ('1', 'y')
    opt_no = ('2', 'n')
    restart = input('Press 1 or y for continue and Press 2 or n for exit\n')
    if (restart in opt_yes):
        print(50*'\n')
        break
    elif (restart in opt_no):
        print('\n'*50)
        print('Thanks for using')
        break
    else:
        print('You entered an invalid key')
print('\n'*50)
