import subprocess, os, math, shlex, sys
hist = []

while True: 
    try: 
        entrada = input(os.getcwd() + " psh> ")
        if entrada.strip() == "":   
            continue 
        elif entrada == "history": 
            hist.append(entrada)   
            for i in range(len(hist)):
                print(i, hist[i]) 
            continue
        elif entrada == "!!": 
            if len(hist) == 0:       
                print("Sem registro ")
                continue
            else: 
                entrada = hist[-1]   
                print("Executando: " + entrada)
                subprocess.run(shlex.split(entrada))
                hist.append(entrada)
                continue
        elif entrada.startswith("!"): 
            try: 
                num_str = entrada[1:]       
                n = int(num_str)            
                if n < 0 or n >= len(hist):
                    print("Índice inválido")
                    continue
                entrada = hist[n]          
                print("Executando: " + entrada)
                subprocess.run(shlex.split(entrada))
                hist.append(entrada)
                continue
            except ValueError: 
                print("Uso incorreto de !n")
                continue
        elif entrada.startswith("cd"): 
            partes = entrada.split()
            if len(partes) == 1:  
                new_dir = os.path.expanduser("~")
            else: 
                new_dir = partes[1]
            if os.path.isdir(new_dir): 
                os.chdir(new_dir)
            else: 
                print("Diretório inválido")
                continue
        else: 
            subprocess.run(shlex.split(entrada))
            hist.append(entrada)
    except KeyboardInterrupt: 
        print("Programa encerrado...")
        break
