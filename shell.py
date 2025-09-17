import subprocess, os, shlex

hist = []

def executar_comando(cmd):
    """Executa comando externo e adiciona ao histórico"""
    try:
        subprocess.run(shlex.split(cmd))
        hist.append(cmd)
    except FileNotFoundError:
        print("Comando não encontrado:", cmd)

while True: 
    try: 
        entrada = input(os.getcwd() + " psh> ")
        if not entrada.strip():   
            continue 
        elif entrada in ["exit", "quit"]:
            print("Saindo do shell...")
            break
        elif entrada == "history": 
            for i in range(len(hist)):
                print(i, hist[i]) 
            continue
        elif entrada == "!!": 
            if not hist:       
                print("Sem registro ")
                continue
            else: 
                entrada = hist[-1]
            print("Executando:", entrada)
            executar_comando(entrada)
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
            partes = entrada.split(maxsplit=1)
            if len(partes) == 1:  
                new_dir = os.path.expanduser("~")
            else: 
                new_dir = partes[1]
            if os.path.isdir(new_dir): 
                os.chdir(new_dir)
            else: 
                print("Diretório inválido")
            hist.append(entrada)
            continue
        else: 
            subprocess.run(entrada, shell=True)
            hist.append(entrada)
    except KeyboardInterrupt: 
        print("Programa encerrado...")
        break
