def cels_to_fahr(cels: float) -> float:
    return (cels * 9/5) + 32

def fahr_to_cels(fahr: float) -> float:
    return (fahr - 32) * 5/9

def meters_to_kilometers(meters: float) -> float:
    return meters / 1000

def kilometers_to_meters(kilometers: float) -> float:
    return kilometers * 1000