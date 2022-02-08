import pandas as pd

active_enemies = []
active_schemes = []
active_items = []

possible_enemies = []
possible_schemes = []
possible_items = []

main_villain = []
main_scheme = []

def clear():
    possible_schemes.clear()
    possible_enemies.clear()
    possible_items.clear()
    main_villain.clear()
    main_scheme.clear()

def parse_cards(sets, num_pl, mode):
    vil_df = pd.read_csv('enemies.csv')
    vil_df = vil_df[vil_df['set'] in sets]