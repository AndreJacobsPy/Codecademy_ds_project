from restaurantData import restaurant_data
import heapq

def search_restaurants(array, food_type):
    restaurants = []
    for i in array:
        if i[0] == food_type:
            restaurants.append(i)
    
    return restaurants

def sort_restaurants(array, price=False):
    if price:
        return sorted(array, key=lambda x: int(x[2]))
    return sorted(array, key=lambda x: int(x[3]), reverse=True)


if __name__ == '__main__':
    pizza_places = search_restaurants(restaurant_data, 'pizza')
    print(sort_restaurants(pizza_places))
