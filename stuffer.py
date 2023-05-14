import random,os,sys
from tqdm import tqdm

def isn(a):
    b=str(a)
    while b.isnumeric()==False:
        b=input("[!]Invaild input.Please retype:")
    return b

try:
    
    print("Siliconioa Stuffer , Version 1.1a")
    print("[!]Warings!This may cause unexcepted damage to your system.")
    nam = input("[*]Enter the filename:")
    f=open(nam,"w")
    len = int(isn(input("[*]Enter the file size:")))
    how = int(isn(input("[*]Select which type of characters to stuff: [1]unreadable [2]readable [3]hybrid:")))
    for i in tqdm(range(len),unit="Byte(s)",unit_scale=True):
        f.write(chr(random.randint(32-32*(how%2),31+95*(how//2))))
    f.close()
    print('[*]Stuffed file generated: %s' % os.path.join(os.getcwd(), nam))
    print("[*]Added file size:"+str(len//1048576)+"MiB(s)"+str((len-1048576*(len//1048576))//1024)+"KiB(s)"+str(len%1024)+"Byte(s)")

except:
    print("[!] Fatal error!Please run this script again...")
