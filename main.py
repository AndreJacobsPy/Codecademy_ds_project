from restaurantData import types, restaurant_data
from searching import search_restaurants, sort_restaurants


intro = '''
--------------------------------
*                              *
*                              *
* Welcome to HTown Restaurants *
*                              *
*                              *
--------------------------------

Options:
'''

print(intro, end='')
options_dict = {i[0]: i for i in types}

for letter, selection in options_dict.items():
    print(f'{letter} -> {selection}')
print()

again = True
while again:
    user_selection = input('What type of food do you want to eat? ')
    if user_selection not in options_dict:
        print('Your selection is not in Houston...')
        continue
    type_of_food = options_dict[user_selection]
    print(f'You have chosen {type_of_food}')

    restaurants = search_restaurants(restaurant_data, type_of_food)
    sorting = input('How do you wnat to sort the recommendations? (p for price, r for rating, n for none): ')
    match sorting:
        case 'p':
            restaurants = sort_restaurants(restaurants, price=True)
        case 'r':
            restaurants = sort_restaurants(restaurants)

    for restaurant in restaurants:
        print('------------------------------------------------', end='\n\n')
        print(f'Name: {restaurant[1]}')
        print(f'Price: {restaurant[2]}')
        print(f'Rating: {restaurant[3]}')
        print(f'Address: {restaurant[4]}')
        print()
        print('------------------------------------------------', end='\n\n')

    again_str = input('Do you want to see more restaurants? (yes / no): ').lower()
    match again_str:
        case 'yes':
            again = True
        case 'no':
            again = False
        case other:
            print('Please enter yes or no')
            again_str = input('Do you want to see more restaurants? (yes / no): ')

    print('Thank you for using the HTown Recommender!')
        

