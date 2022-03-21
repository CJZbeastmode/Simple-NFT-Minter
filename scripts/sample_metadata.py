from config import TOKEN_ATTRIBUTES

attributes = []

for i in range(len(TOKEN_ATTRIBUTES)):
    dict = {"trait_type": TOKEN_ATTRIBUTES[i][0], "value": TOKEN_ATTRIBUTES[i][1]}
    attributes.append(dict)

metadata_template = {
    "name": "",
    "description": "",
    "image": "",
    "attributes": attributes,
}
