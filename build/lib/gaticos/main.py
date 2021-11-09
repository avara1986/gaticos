import logging
from random import randint
from typing import List, Text

import click

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class PhraseGenerator:
    """
    Esta clase genera aleatoriamente una frase dada por el atributo list_phases
    """

    list_phases: List[Text] = [
        "A llorar a la llorería!",
        "jajaja, no se de que me hablas, salu2",
        "Ánimo colega",
    ]

    @classmethod
    def gen_random_phrase(cls) -> Text:
        """
        Devuelve un elemento de tipo string aleatorio de los valores posibles de self.list_phases
        :return:
        """
        rand_index = randint(0, len(cls.list_phases) - 1)
        return cls.list_phases[rand_index]


@click.group(invoke_without_command=True)
@click.option("--count", "-c", "count", default=1, help='Número de miaus')
def main(count: int = 1) -> None:
    """Este comando ayuda a interactuar con gaticos"""
    for _ in range(count):
        click.echo("Miau!")


@main.command()
def animame():
    """
    Devuelve una frase random
    :return:
    """
    phrase = PhraseGenerator.gen_random_phrase()
    logger.debug("Devolviendo frase %s", phrase)
    click.echo(
        f"""
          ██            ██               {phrase}         
        ██░░██        ██░░██                      
        ██░░▒▒████████▒▒░░██                ████  
      ██▒▒░░░░▒▒▒▒░░▒▒░░░░▒▒██            ██░░░░██
      ██░░░░░░░░░░░░░░░░░░░░██            ██  ░░██
    ██▒▒░░░░░░░░░░░░░░░░░░░░▒▒████████      ██▒▒██
    ██░░  ██  ░░██░░  ██  ░░  ▒▒  ▒▒  ██    ██░░██
    ██░░░░░░░░██░░██░░░░░░░░░░▒▒░░▒▒░░░░██████▒▒██
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██  
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██  
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██    
    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██    
      ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██      
        ██▒▒░░▒▒▒▒░░▒▒░░░░░░▒▒░░▒▒▒▒░░▒▒██        
          ██░░████░░██████████░░████░░██          
          ██▓▓░░  ▓▓██░░  ░░██▓▓  ░░▓▓██                             
    """
    )


if __name__ == '__main__':  # pragma: no cover
    main()
