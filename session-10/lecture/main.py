from pathlib import Path
path = Path(__file__).parent / 'eureka.txt'

with path.open(mode='a', encoding='utf-8') as file:
    file.write("King: The water? You speak in riddles, old man. Did you leave your senses behind at the bathhouse?\n")
    file.write("Archimedes: No, that is where I found them!\n")