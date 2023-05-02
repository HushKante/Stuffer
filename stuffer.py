import random,os,sys

def isn(a):
    b=str(a)
    while b.isnumeric()==False:
        b=input("[!]Invaild input.Please retype:")
    return b

print("Siliconioa Stuffer , Version 1.0a")
print("[!]Warings!This may cause unexcepted damage to your system.")
nam = input("[*]Enter the filename:")
len = int(isn(input("[*]Enter the file size:")))
how = int(isn(input("[*]Select which type of characters to stuff: [1]unreadable [2]readable [3]hybrid:")))
f=open(nam,"w")
for i in range(len):
    f.write(chr(random.randint(32-32*(how%2),31+96*(how//2))))
f.close()
print('[*]Stuffed file generated: %s' % os.path.join(os.getcwd(), nam))
print("[*]File size:"+str(len//1048576)+"MiB(s)"+str((len-1048576*(len//1048576))//1024)+"KiB(s)"+str(len%1024)+"Byte(s)")

#Written by HushKante ,2023.5.1
