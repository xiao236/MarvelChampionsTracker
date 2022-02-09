import pandas as pd
import villain
import scheme
import items

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

def to_int(val, num_pl):
    if "x" in val:
        val = val[:-1]
        hp = int(val)
        return hp * num_pl
    else:
        return int(val)

def parse_cards(sets, num_pl, mode):
    vil_df = pd.read_csv('enemies.csv')
    vil_df = vil_df[vil_df['set'].isin(sets)]

    sch_df = pd.read_csv('schemes.csv')
    sch_df = sch_df[sch_df['set'].isin(sets)]

    it_df = pd.read_csv('items.csv')
    it_df = it_df[it_df['set'].isin(sets)]

    for row in vil_df.itertuples():
        name = row[1]
        hp = to_int(row[3], num_pl)
        atk = int(row[4])
        sch = int(row[5])

        new_vil = villain.villain(name, hp, atk,sch,row[6])
        if row[2] == "villain":
            main_villain.append(new_vil)
        else:
            possible_enemies.append(new_vil)

    for row in sch_df.itertuples():
        name = row[1]
        start = to_int(row[3], num_pl)
        inc = to_int(row[4], num_pl)
        end = to_int(row[5], num_pl)

        new_sch = scheme.scheme(name, start, inc, end, row[6], row[7])
        if row[2] == "main":
            main_scheme.append(new_sch)
        else:
            possible_schemes.append(new_sch)
    for row in it_df.itertuples():
        possible_items.append(items.items(row[1],int(row[2]),int(row[3]),row[4], row[5]))

    if mode == "standard":
        main_villain.pop(0)
    else:
        main_villain.pop(2)

    print(len(main_villain))
    print(len(main_scheme))
    print(len(possible_schemes))
    print(len(possible_enemies))
    print(len(possible_items))