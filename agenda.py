#-*- coding: utf-8 -*-
import click
import archivos

@click.command()
@click.option('--registro', nargs=3, type=str)
def mostrar_registro(registro):
    click.echo('%s / %s / %s' % registro)

@click.command()
@click.option('--registro_r', nargs=3, type=str)
def grabar_datos(registro_r):
    archivos.grabar_registro('datos.txt',registro_r)

"""def existe(existe):
    archivos.existe_archivo(existe)"""

if __name__ == '__main__':
   # mostrar_registro()
    grabar_datos()
