import os
import click

@click.command()
@click.option('--find', type=str, help="The /proc/sys parameter you want to look for.")

def prox(find):
	os.system("find /proc/sys/ -name " + find + " | xargs cat")

if __name__ == '__main__':
    prox()
