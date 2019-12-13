import re

def PatternMatching(Pattern, Genome):
    positions = []
    for occ in re.finditer(f"(?=({Pattern}))", Genome):
        positions.append(occ.start())
    
    return positions