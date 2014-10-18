#-*- coding: utf-8 -*-
import click
import archivos

@click.command()
@click.option('--registro', nargs=3, type=str)


def mostrar_registro(registro):
    click.echo('%s / %s / %s' % registro)


def grabar_datos(registro):
    archivos.grabar_registro('datos.txt',registro)


"""def existe(existe):
    archivos.existe_archivo(existe)"""


if __name__ == '__main__':
   # mostrar_registro()
    grabar_datos()
