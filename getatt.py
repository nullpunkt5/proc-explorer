import os
import click

@click.command()
@click.option('--get', type=unicode, help='The /proc file you want to look for.')
def prox(get):
	os.system("tail -vn +1 /proc/*/" + get)


if __name__ == '__main__':
    prox()
