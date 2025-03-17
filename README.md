# NetFang

NetFang é uma ferramenta de rede escrita em Python, inspirada no Netcat. Ela permite abrir conexões TCP, ouvir portas, executar comandos remotamente e transferir dados entre dispositivos.

## Recursos
- Modo servidor para escutar conexões
- Modo cliente para conectar a servidores remotos
- Execução remota de comandos
- Comunicação simples e eficiente entre máquinas

## Requisitos
- Python 3.x

## Instalação
Clone o repositório ou baixe o script:
```bash
git clone https://github.com/Tiago22a/NetFang.git
cd NetFang
```

## Uso

### Modo Servidor (Escutar Conexões)
Para escutar na porta 4444:
```bash
python NetFang.py -p 4444 -l
```

### Modo Cliente (Conectar a um Servidor)
Para conectar a um servidor na porta 4444:
```bash
python NetFang.py -t 192.168.1.100 -p 4444
```

### Execução de Comandos Remotos
Para iniciar o servidor e executar um comando assim que um cliente se conectar:
```bash
python NetFang.py -p 4444 -l -e "ls -la"
```

## Exemplo de Uso
1. Inicie o servidor em uma máquina:
   ```bash
   python NetFang.py -p 4444 -l
   ```
2. Conecte-se ao servidor de outra máquina:
   ```bash
   python NetFang.py -t 192.168.1.100 -p 4444
   ```
3. Agora você pode enviar comandos diretamente na shell remota!

## Contribuição
Sinta-se à vontade para contribuir abrindo issues e pull requests!

## Licença
Este projeto é distribuído sob a licença MIT.

