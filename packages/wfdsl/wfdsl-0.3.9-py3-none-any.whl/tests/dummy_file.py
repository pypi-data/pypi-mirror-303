parallel:
    bio_data = 'bio_data'
with:
    img_data = 'img_data'
with:
    text_data = 'text_data'

print(bio_data)
print(img_data)
print(text_data)

task process_data(data_type):
    if data_type == 'bio':
        print("Processing bio_data")
    cinky = "cinky"
    print(cinky)

# Function definition
# task process_data(data_type):
#     # global bio_data, img_data, text_data
#     if data_type == 'bio':
#         print(f"Processing {bio_data}")
#     elif data_type == 'img':
#         print(f"Processing {img_data}")
#     else:
#         print(f"Processing {text_data}")

# For loop
data_types = ['bio', 'img', 'text']
# for data_type in data_types:
#     process_data(data_type)
#     # process_data(data_type)
# print(cinky)

parfor data_type in data_types:
    print('cinky')

