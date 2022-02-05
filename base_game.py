import villain
import scheme
import items
import config

def rhino_setup(mode,num_pl):
    if mode:
        config.main_villain.append(villain.villain("Rhino", 14 * num_pl, 2, 1))
        config.main_villain.append(villain.villain("Rhino", 15 * num_pl, 3, 1))
    else:
        config.main_villain.append(villain.villain("Rhino", 15 * num_pl, 3, 1))
        config.main_villain.append(villain.villain("Rhino", 16 * num_pl, 4, 1))
    config.main_scheme.append(scheme.scheme("The Break-In!", 0, num_pl, 7 * num_pl))
    config.possible_items(items.items("Armored Rhino Suit", 0, 0))
    config.possible_items(items.items("Charge", 3, 0))
    config.possible_items(items.items("Enhanced Ivory Horn", 1, 0))
    config.possible_enemies(villain.villain("Hydra Mercenary", 3, 1, 0))
    config.possible_enemies(villain.villain("Sandman", 4, 3, 2))
    config.possible_enemies(villain.villain("Shocker", 3, 2, 1))
    config.possible_schemes(scheme.scheme("Breakin' & Takin'", 2+num_pl,0,0))
    config.possible_schemes(scheme.scheme("Crowd Control", 2*num_pl, 0, 0))

def klaw_setup(mode,num_pl):
    if mode:
        config.main_villain.append(villain.villain("Klaw",12*num_pl,0,2))
        config.main_villain.append(villain.villain("Klaw",18*num_pl,1,2))
    else:
        config.main_villain.append(villain.villain("Klaw", 18 * num_pl, 1,2))
        config.main_villain.append(villain.villain("Klaw", 22 * num_pl, 2,3))
    config.main_scheme.append(scheme.scheme("Underground Distribution", 0, num_pl, 6 * num_pl))
    config.main_scheme.append(scheme.scheme("Secret Rendezvous", 0, num_pl, 8 * num_pl))
    config.possible_items.append(items.items("Sonic Converter", 1, 0))
    config.possible_items.append(items.items("Solid-Sound Body", 0, 0))
    config.possible_enemies.append(villain.villain("Armored Guard",3,1,0))
    config.possible_enemies.append(villain.villain("Weapons Runner", 2, 1, 1))
    config.possible_schemes.append(scheme.scheme("Illegal Arms Factory",3+num_pl,0,0))
    config.possible_schemes.append(scheme.scheme("The \"Immortal\" Klaw", 3 * num_pl, 0,0))

def ultron_setup(mode, num_pl):
    if mode:
        config.main_villain.append(villain.villain("Ultron", 17*num_pl, 2, 1))
        config.main_villain.append(villain.villain("Ultron", 22 * num_pl, 2, 2))
    else:
        config.main_villain.append(villain.villain("Ultron", 22 * num_pl, 2, 2))
        config.main_villain.append(villain.villain("Ultron", 27 * num_pl, 4, 2))
    config.main_scheme.append(scheme.scheme("The Crimson Cowl", 0, num_pl, 3 * num_pl))
    config.main_scheme.append(scheme.scheme("Assault on NORAD", 0, num_pl, 10 * num_pl))
    config.main_scheme.append(scheme.scheme("Countdown to Oblivion", 0, num_pl, 5 * num_pl))
    config.possible_items.append(items.items("Program Transmitter", 0, 1))
    config.possible_items.append(items.items("Upgraded Drones", 0, 0))
    config.possible_enemies.append(villain.villain("Advanced Ultron Drone", 4, 1, 1))
    config.possible_schemes.append(scheme.scheme("Drone Factory", 4, 0, 0))
    config.possible_schemes.append(scheme.scheme("Invasive AI", 3*num_pl, 0, 0))
    config.possible_schemes.append(scheme.scheme("Ultron's Imperative", 2 * num_pl, 0, 0))

def risky_business_setup(mode, num_pl):
    if mode:
        config.main_villain.append(villain.villain("Green Goblin", 14*num_pl, 3, 2))
        config.main_villain.append(villain.villain("Green Goblin", 18*num_pl, 4, 2))
    else:
        config.main_villain.append(villain.villain("Green Goblin", 18 * num_pl, 4, 2))
        config.main_villain.append(villain.villain("Green Goblin", 22 * num_pl, 4, 3))
    config.main_scheme.append(scheme.scheme("Hostile Takeover", 2*num_pl, num_pl, 7*num_pl))
    config.main_scheme.append(scheme.scheme("Corporate Acquisition", num_pl, 2*num_pl, 10*num_pl))
    config.possible_enemies(villain.villain("Hired Gun", 3, 2, 2))
    config.possible_enemies(villain.villain("Private Security Specialist", 4, 1, 0))
    config.possible_schemes(scheme.scheme("Collapsing Bridge", 2*num_pl, 0, 0))
    config.possible_schemes(scheme.scheme("Oscorp Manufacturing", 2 *num_pl, 0, 0))
    config.possible_schemes(scheme.scheme("Payoff", 2*num_pl, 0, 0))

def mutagen_formula_setup(mode, num_pl):
    if mode:
        config.main_villain.append(villain.villain("Green Goblin", 16 * num_pl, 2, 1))
        config.main_villain.append(villain.villain("Green Goblin", 18 * num_pl, 2, 2))
    else:
        config.main_villain.append(villain.villain("Green Goblin", 18 * num_pl, 2, 2))
        config.main_villain.append(villain.villain("Green Goblin", 20 * num_pl, 3, 2))
    config.main_scheme.append(scheme.scheme("Unleashing the Mutagen", 2*num_pl, num_pl, 7*num_pl))
    config.main_scheme.append(scheme.scheme("Mutagen Cloud", 4*num_pl, 0, 11*num_pl))
    config.possible_items.append(items.items("Goblin Glider", 1, 0))
    config.possible_items.append(items.items("Hysteria", 0, 0))
    config.possible_items.append(items.items("Pumpkin Bombs", 0, 0))
    config.possible_enemies.append(villain.villain("Goblin Knight", 7, 2, 2))
    config.possible_enemies.append(villain.villain("Goblin Soldier", 5, 1, 1))
    config.possible_enemies.append(villain.villain("Goblin Thrall", 3, 1, 1))
    config.possible_enemies.append(villain.villain("Monster", 6, 3, 1))
    config.possible_schemes.append(scheme.scheme("Goblin Reinforcements", 2, 0, 0))
    config.possible_schemes.append(scheme.scheme("Goblin Nation", 2*num_pl, 0, 0))
    config.possible_schemes.append(scheme.scheme("Overrun", num_pl, 0, 0))

def add_LoH():
    config.possible_schemes.append(scheme.scheme("Legions of Hydra", 3, 0, 0))
    config.possible_enemies.append(villain.villain("Madame Hydra", 6, 2, 2))
    config.possible_enemies.append(villain.villain("Hydra Soldier", 4, 2, 1))

def add_MoE(num_pl):
    config.possible_schemes.append(scheme.scheme("The Masters of Evil", 3*num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Radioactive Man", 7, 1, 1))
    config.possible_enemies.append(villain.villain("Whirlwind", 6, 2, 1))
    config.possible_enemies.append(villain.villain("Tiger Shark", 6, 3, 1))
    config.possible_enemies.append(villain.villain("Melter", 5, 3, 1))

def add_BS(num_pl):
    config.possible_schemes.append(scheme.scheme("Bomb Scare", 2+num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Hydra Bomber", 2, 1, 1))

def add_UA():
    config.possible_schemes.append(scheme.scheme("Under Attack", 3, 0, 0))
    config.possible_items.append(items.items("Vibranium Armor", 0, 0))
    config.possible_items.append(items.items("Concussion Blasters", 1, 0))

def add_tDC():
    config.possible_schemes.append(scheme.scheme("The Doomsday Chair", 8, 0, 0))
    config.possible_enemies.append(villain.villain("MODOK", 8, 2, 2))
    config.possible_items.append(items.items("Biomechanical Upgrades", 0, 0))

def add_GG():
    config.possible_items.append(items.items("Goblin Glider", 1, 0))
    config.possible_items.append(items.items("Pumpkin Bombs", 0, 0))

def add_aMoT():
    config.possible_schemes.append(scheme.scheme("A Mess of Things", 2, 0, 0))
    config.possible_enemies.append(villain.villain("Scorpion", 7, 3, 3))

def add_PD(num_pl):
    config.possible_schemes.append(scheme.scheme("Power Drain", 2*num_pl ,0, 0))
    config.possible_enemies.append(villain.villain("Electro", 6, 2, 2))

def add_RI(num_pl):
    config.possible_schemes.append(scheme.scheme("Running Interference", num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Tombstone", 9, 3, 2))
    config.possible_items.append(items.items("All Tied Up", 0, 0))
    config.possible_items.append(items.items("Media Coverage", 0, 0))

def she_hulk(num_pl):
    config.possible_schemes.append(scheme.scheme("Personal Challenge", 3+num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Titania", 6, 0, 1))
    config.possible_items.append(items.items("Genetically Enhanced", 0, 0))

def spider_man(num_pl):
    config.possible_schemes.append(scheme.scheme("Highway Robbery", 3*num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Vulture", 4, 3, 1))

def black_panther(num_pl):
    config.possible_schemes.append(scheme.scheme("Usurp the Throne", 3*num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Killmonger", 5, 2, 2))

def captain_marvel(num_pl):
    config.possible_schemes.append(scheme.scheme("The Psyche-Magnitron", 3+num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Yon-Rogg", 5, 3, 2))

def black_widow(num_pl):
    config.possible_enemies.append(villain.villain("Taskmaster", 4, 0, 0))
    config.possible_schemes.append(scheme.scheme("Killer for Hire", 3+num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Hydra Mercenary", 3, 1, 0))

def thor():
    config.possible_schemes.append(scheme.scheme("Family Feud", 2, 0, 0))
    config.possible_enemies.append(villain.villain("Loki", 4, 2, 2))
    config.possible_enemies.append(villain.villain("Frost Giant", 4, 3, 1))

def ms_marvel(num_pl):
    config.possible_schemes.append(scheme.scheme("Generation Why?", 2*num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Thomas Edison",3,1,3))
    config.possible_enemies.append(villain.villain("Edison's Giant Robot", 8, 2, 1))

def iron_man(num_pl):
    config.possible_schemes.append(scheme.scheme("Imminent Overlord", 3+num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Whiplash", 4, 3, 2))

def captain_america(num_pl):
    config.possible_schemes.append(scheme.scheme("Hit Squad", 3*num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Baron Zemo", 5, 3, 1))
    config.possible_enemies.append(villain.villain("Hydra Soldier", 4, 2, 1))

def doctor_strange(num_pl):
    config.possible_schemes.append(scheme.scheme("Open the Dark Dimension", 3*num_pl, 0, 0))
    config.possible_enemies.append(villain.villain("Baron Mordo", 5, 2, 2))
    config.possible_items.append(items.items("Counterspell", 0, 0))