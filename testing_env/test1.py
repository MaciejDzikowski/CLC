import click


@click.command()
@click.argument("name")
@click.option("-t", "--test")
def run(name, test):
    print(name)
    print(test)


@click.command(options_metavar='<options>')
@click.option('--count', default=1, help='number of greetings',
              metavar='<int>')
@click.argument('name', metavar='<name>')
def hello(count, name):
    """This script prints hello <name> <int> times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    run()
