from selenium import webdriver


banner = '\033[94m' """
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

                   [CJBOT V1.0]

                [Programming by CJ]


 [!This is a special tool for me group kingdom falcons!]

              $[insta:cj_johnson111]$





"""
print(banner)

driver = webdriver.Chrome('/Users/cj/Desktop/package/chromedriver')

driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group:')
msg= input('Enter your message:')

count = int(input('Enter the count:'))

input('Enter anything after scanning QR code:')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in  range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()

