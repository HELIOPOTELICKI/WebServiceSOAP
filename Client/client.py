from zeep import Client
from builtins import input


class Album:
    pass


def novoAlbum():
    ret = Album()
    ret.titulo = input('Digite o titulo do album: ')
    ret.artista = input('Digite o/a artista do album: ')
    ret.gravadora = input('Digite a gravadora do album: ')
    ret.ano = int(input('Digite o ano do album: '))
    return ret


def main():
    client = Client('http://localhost:8000/?wsdl')
    print('#-=-# Biblioteca Musical #-=-#')
    while True:
        print('\nMENU:')
        print('1) Inserir album')
        print('2) Listar albuns')
        print('0) Sair')
        op = str(input('> '))

        if op.strip() == '1':
            #album = novoAlbum()
            print client.service.addAlbumInData()
        elif op.strip() == '2':
            ls = client.service.retornaAlbuns()
            for album in ls:
                print('')
                print('Codigo:', album.codigo)
                print('Titulo:', album.titulo)
                print('Artista:', album.artista)
                print('Gravadora:', album.gravadora)
                print('Ano:', album.ano)
        elif op.strip() == '0':
            break
        else:
            print('Opcao invalida! insira novamente.')


if __name__ == '__main__':
    main()
