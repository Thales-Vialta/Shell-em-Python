# Shell em Python (`psh`)

Este projeto implementa um **shell interativo simples** em Python, chamado `psh` (Python Shell), que permite executar comandos do sistema operacional, navegar entre diretórios, e manter um histórico de comandos com funcionalidades semelhantes às de shells como Bash ou Zsh.

---

## 📜 Descrição

O `psh` é uma aplicação de terminal que simula o comportamento básico de um shell Unix-like. Ele suporta:

* Execução de comandos externos (`ls`, `echo`, `mkdir`, etc.)
* Comando `cd` para trocar de diretório
* Comando `history` para exibir o histórico de comandos
* Execução de comandos anteriores com `!!` (último comando) ou `!n` (comando de índice `n`)
* Tratamento de erros básicos (como comandos ou diretórios inválidos)
* Suporte para sair com `exit` ou `quit`
* Tratamento de `KeyboardInterrupt` (`Ctrl+C`) para encerramento limpo

---

## Como executar

Certifique-se de ter o Python 3 instalado.

```bash
python3 psh.py
```

Você verá um prompt semelhante a este:

```bash
/home/usuario psh>
```

A partir daí, você pode começar a digitar comandos como faria em um terminal normal.

---

## Funcionalidades

### Execução de Comandos

Digite qualquer comando válido do seu sistema, por exemplo:

```
psh> ls
psh> echo "Olá, mundo!"
```

### Comando `cd`

Para trocar de diretório:

```
psh> cd /caminho/para/pasta
```

Se nenhum caminho for especificado, ele volta para o diretório home:

```
psh> cd
```

### Histórico de Comandos

Mostra todos os comandos digitados até o momento:

```
psh> history
0 ls
1 cd ..
2 echo "Olá"
```

### Reexecutar Comandos

* `!!` — executa o último comando do histórico.
* `!n` — executa o comando de índice `n` do histórico (ex: `!2`).

---

## Comandos Especiais

| Comando     | Ação                                         |
| ----------- | -------------------------------------------- |
| `exit`      | Encerra o shell                              |
| `quit`      | Encerra o shell                              |
| `history`   | Mostra o histórico de comandos               |
| `!!`        | Executa o último comando do histórico        |
| `!n`        | Executa o comando no índice `n` do histórico |
| `cd [path]` | Muda para o diretório especificado           |

---

## Observações

* O código contém um pequeno **erro de digitação** na função `executar_comando`:

  ```python
  subprocess.runsplit(cmd, shell = True)  # ← ERRADO
  ```

  Deveria ser:

  ```python
  subprocess.run(cmd, shell = True)       # ← CORRETO
  ```

* O código não trata saída de erros de forma detalhada, mas exibe mensagens básicas para comandos inválidos ou diretórios inexistentes.

---

## 📄 Licença

Este projeto é apenas para fins educacionais. Sinta-se à vontade para modificá-lo, estudar e usá-lo como base para criar um shell mais completo.

---

## 🙋‍♂️ Autor

Desenvolvido por Thales Vialta
PowerShell em Python 
