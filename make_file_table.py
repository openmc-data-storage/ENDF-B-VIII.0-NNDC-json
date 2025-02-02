import os


REACTION_NAME = {
    1: "(n,total)",
    2: "(n,elastic)",
    3: "(n,nonelastic)", # added
    4: "(n,level)",
    5: "(n,misc)",
    11: "(n,2nd)",
    16: "(n,2n)",
    17: "(n,3n)",
    18: "(n,fission)",
    19: "(n,f)",
    20: "(n,nf)",
    21: "(n,2nf)",
    22: "(n,na)",
    23: "(n,n3a)",
    24: "(n,2na)",
    25: "(n,3na)",
    27: "(n,absorption)",
    28: "(n,np)",
    29: "(n,n2a)",
    30: "(n,2n2a)",
    32: "(n,nd)",
    33: "(n,nt)",
    34: "(n,n3He)",
    35: "(n,nd2a)",
    36: "(n,nt2a)",
    37: "(n,4n)",
    38: "(n,3nf)",
    41: "(n,2np)",
    42: "(n,3np)",
    44: "(n,n2p)",
    45: "(n,npa)",
    91: "(n,nc)",
    101: "(n,disappear)",
    102: "(n,gamma)",
    103: "(n,p)",
    104: "(n,d)",
    105: "(n,t)",
    106: "(n,3He)",
    107: "(n,a)",
    108: "(n,2a)",
    109: "(n,3a)",
    111: "(n,2p)",
    112: "(n,pa)",
    113: "(n,t2a)",
    114: "(n,d2a)",
    115: "(n,pd)",
    116: "(n,pt)",
    117: "(n,da)",
    152: "(n,5n)",
    153: "(n,6n)",
    154: "(n,2nt)",
    155: "(n,ta)",
    156: "(n,4np)",
    157: "(n,3nd)",
    158: "(n,nda)",
    159: "(n,2npa)",
    160: "(n,7n)",
    161: "(n,8n)",
    162: "(n,5np)",
    163: "(n,6np)",
    164: "(n,7np)",
    165: "(n,4na)",
    166: "(n,5na)",
    167: "(n,6na)",
    168: "(n,7na)",
    169: "(n,4nd)",
    170: "(n,5nd)",
    171: "(n,6nd)",
    172: "(n,3nt)",
    173: "(n,4nt)",
    174: "(n,5nt)",
    175: "(n,6nt)",
    176: "(n,2n3He)",
    177: "(n,3n3He)",
    178: "(n,4n3He)",
    179: "(n,3n2p)",
    180: "(n,3n2a)",
    181: "(n,3npa)",
    182: "(n,dt)",
    183: "(n,npd)",
    184: "(n,npt)",
    185: "(n,ndt)",
    186: "(n,np3He)",
    187: "(n,nd3He)",
    188: "(n,nt3He)",
    189: "(n,nta)",
    190: "(n,2n2p)",
    191: "(n,p3He)",
    192: "(n,d3He)",
    193: "(n,3Hea)",
    194: "(n,4n2p)",
    195: "(n,4n2a)",
    196: "(n,4npa)",
    197: "(n,3p)",
    198: "(n,n3p)",
    199: "(n,3n2pa)",
    200: "(n,5n2p)",
    203: "(n,Xp)",
    204: "(n,Xd)",
    205: "(n,Xt)",
    206: "(n,X3He)",
    207: "(n,Xa)",
    301: "heating",
    444: "damage-energy",
    649: "(n,pc)",
    699: "(n,dc)",
    749: "(n,tc)",
    799: "(n,3Hec)",
    849: "(n,ac)",
    891: "(n,2nc)",
    901: "heating-local",
}
REACTION_NAME.update({i: f"(n,n{i - 50})" for i in range(51, 91)})
REACTION_NAME.update({i: f"(n,p{i - 600})" for i in range(600, 649)})
REACTION_NAME.update({i: f"(n,d{i - 650})" for i in range(650, 699)})
REACTION_NAME.update({i: f"(n,t{i - 700})" for i in range(700, 749)})
REACTION_NAME.update({i: f"(n,3He{i - 750})" for i in range(750, 799)})
REACTION_NAME.update({i: f"(n,a{i - 800})" for i in range(800, 849)})
REACTION_NAME.update({i: f"(n,2n{i - 875})" for i in range(875, 891)})


def get_json_filenames(directory):
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filenames.append(filename)
    return filenames


# Ac_225_ENDFB-8.0_n_102_294K
# to
# Ac 225 ENDFB-8.0 n,_102_294K


json_filenames = get_json_filenames(directory="json_files")
# print(json_filenames)
modified_filenames = []

for i, filename in enumerate(json_filenames):
    tokens = filename.split('_')
    print(tokens)

    # .replace('_', ' ')
    reaction_description = REACTION_NAME[int(tokens[4])]

    file_description = (
        tokens[0]  # Li
        + tokens[1]
        + " "  # 6
        + tokens[2]  # ENDFB-8.0
        + " "
        + reaction_description
        + " MT"+tokens[4]  # 444
        + ' ' +tokens[5].split('.')[0]  # 294K
    )

    modified_filenames.append(
        {"id": i,
         "element": tokens[0], # Li
         "nucleons": tokens[1], # 6
         "library": tokens[2], # ENDFB-8.0
         "reaction": reaction_description, #(n,2n)
         "MT": tokens[4], # 444
         "temperature": tokens[5].split('.')[0]}
    )

print(modified_filenames)

import json
with open("table_data.json", 'w') as f:
    json.dump(modified_filenames, f, indent=4)


# [
#     {"id": 0, "name": "Ac_225_END", "value": 1},