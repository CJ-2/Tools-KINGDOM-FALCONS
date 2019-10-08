from requests import Session
class color:
    HEADER = '\033[94m'

def CheckPublicIP():
    try:
        with Session() as ses:
            res = ses.get("https://api.ipify.org/?format=json")
            if (res.status_code == 200):
                return res.json()["ip"]
            return None
    except:
        return None
    pass
    
def IsProxyWorking(proxy):
    try:
        with Session() as ses:
            ses.proxies.update(proxy)
            res = ses.get("https://api.ipify.org/?format=json")
            if (res.status_code == 200):
                if(res.json()["ip"] != CheckPublicIP() and CheckPublicIP != None):
                    return True
            return False
    except:
        return False
    pass

def PrintSuccess(message, username, *argv):
    print("[ OK ] ", end="")
    print("[", end="")
    print(username, end="")
    print("] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

# Spam 1
# self-harm 2
# drug 3
# nudity 4
# violence 5
# Hate speech 6
# Harassment and bullying 7
# Tradition of ldentity 8
# The child is a minor 11

def PrintChoices():
    print(color.HEADER+"""    
    +----------------------+--------+
    |   type of complaint  | Numara |
    +----------------------+--------+
    | Spam                 |      1 |
    | self-harm            |      2 |
    | drug                 |      3 |
    | nudity               |      4 |
    | violence             |      5 |
    | Hate speech          |      6 |
    | bullying             |      7 |
    | Tradition of ldentity|      8 | 
    | The child is a minor |     11 |
    +----------------------+--------+
    """)

def GetInput(message, *argv):
    print("[ ? ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    return input()

def PrintFatalError(message, *argv):
    print("[ X ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintError(message, username, *argv):
    print("[ X ] ", end="")
    print("[", end="")
    print(username, end="")
    print("] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintStatus(message, *argv):
    print("[ * ] ", end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")
    pass

def PrintBanner():
    banner ='\033[94m'  """
    
    
                                       {KINGDOM FALCONS}
                               _________________________________
                               |               CJ              |
                               |             Shadow            |
                               |            Abo miras          |
                               |            0xSilver           |
                               |             Dr.mim            |
                               |            Abo Saleh          |
                               |           Abo Tarikhm         |
                               |           Abo Mazen           |
                               _________________________________
                                       
                                            CJspam V1.0
                                            
                                         Programming by CJ
                    ---------------------------------------------------------
                        This is a special tool for me group kingdom falcons
                                           
                                        insta:cj_johnson111
      
         
    """
    print(banner)
    pass

def LoadUsers(path):
    ret = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "").replace("\r","")
                user = line.split(" ")[0]
                password = line.split(" ")[1]
                ret.append({
                    "user": user,
                    "password": password
                })
                pass
            pass
        return ret
    except:
        PrintFatalError("'users.txt'File does not exist!")
        exit(0)
    pass

def LoadProxies(path):
    ret = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.replace("\n", "").replace("\r","")
                ip = line.split(":")[0]
                port = line.split(":")[1]
                ret.append({
                    "ip": ip,
                    "port": port
                })
                pass
            pass
        return ret
    except:
        PrintFatalError("'proxy.txt' File does not exist !")
        exit(0)
    pass
