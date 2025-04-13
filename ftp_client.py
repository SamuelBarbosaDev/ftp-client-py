from ftplib import FTP


def connect(
    host: str, 
    username: str, 
    password:str, 
    port:int
) -> FTP:
    """
    Estabelece uma conexão com o servidor FTP.

    host: Endereço do servidor FTP.\n
    username: Nome de usuário para autenticação.\n
    password: Senha para autenticação.\n
    port: Porta de conexão do servidor FTP.\n
    return: Instância conectada do FTP.\n
    """
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host=str(host), port=int(port))

    if username:
        if password:
            ftp.login(user=username, passwd=password)
        else:
            raise ValueError('Password required')
    else:
        ftp.login()

    return ftp

def listDir(ftp: FTP, dir: str) -> list:
    """
    Lista o conteúdo de um diretório no servidor FTP.

    ftp: Instância da conexão FTP.\n
    dir: Caminho do diretório a ser listado.\n
    return: Lista de strings contendo os detalhes dos itens no diretório.\n
    """
    dirs = list()
    ftp.retrlines("LIST", dirs.append)
    return dirs

def download(ftp: FTP, file: str, saveFilePath: str):
    """
    Faz o download de um arquivo do servidor FTP.

    ftp: Instância da conexão FTP./n
    file: Nome do arquivo no servidor a ser baixado./n
    saveFilePath: Caminho local onde o arquivo será salvo./n
    """
    print("+"*10+"\n"+ saveFilePath)
    with open(saveFilePath, 'wb') as fp:
        ftp.retrbinary(f'RETR {file}', fp.write)

    ftp.quit()

def upload(ftp: FTP, filePath: str, saveFilePath: str):
    """
    Faz o upload de um arquivo local para o servidor FTP.

    ftp: Instância da conexão FTP./n
    filePath: Caminho completo do arquivo local a ser enviado./n
    saveFilePath: Caminho no servidor onde o arquivo será armazenado./n
    """
    with open(filePath, 'rb') as file:
        ftp.storbinary(f'STOR {saveFilePath}', file)
    print(f"Upload concluído: {filePath} -> {saveFilePath}")
