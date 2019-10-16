import pygeoip
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    blue = '\033[94m'
banner = bcolors.RED + """

    
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
      
            [+] EYE OF FALCON v1.0 [+]
                
                [Programming by CJ]


 [!This is a special tool for me group kingdom falcons!]

              $[insta:cj_johnson111]$
    
    
    
    
"""
print(banner)
gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr(input(bcolors.YELLOW + 'Enter the target ip:'))
for key,val in res.items():
	print(bcolors.blue + '%s : %s' % (key,val))

