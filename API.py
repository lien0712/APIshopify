import requests
import json

API_KEY = "b3f8ea965824416c38ede65ae4aa5ceb"
PASSWORD = "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"

SHOP_DOMAIN = "{}:{}@c06768.myshopify.com".format(API_KEY, PASSWORD)
url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN

epsmartcollection = "smart_collections.json"
epcustomcollection = "custom_collections.json"
epproducts = "products.json"
epcustomers = "customers.json"
epoerders = "orders.json"
epnewproduct = "products.json"

img1 = "https://xuconcept.com/wp-content/uploads/2023/03/chup-anh-giay.jpg"
img2 = "https://xuconcept.com/wp-content/uploads/2023/03/an-giay-nen-trang.jpg"

headers = {
    "Content-Type": "application/json",
}


def create_custom_collection():
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "custom_collection": {
            "title": "demo",
            "body_html": "Products which belong to shoe’s type manually go to this custom collection.",
            "published_scope": "web",
        }
    }
    customCollection = requests.post(url + epcustomcollection, json=data, headers=headers)

    return customCollection


def create_custom_smart_collection():
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "smart_collection": {
            "title": "demo1",
            "body_html": "Products which belong to shoe’s type manually go to this custom collection.",
            "published_scope": "web",
            "rules": [{
                "column": "type",
                "relation": "equals",
                "condition": "sneaker",
            }],
        }
    }
    smartCollection = requests.post(url + epsmartcollection, json=data, headers=headers)
    if smartCollection.status_code == 201:
        # The smart collection was created successfully
        print("Smart Collection created successfully")
    else:
        # An error occurred
        print("Error creating Smart Collection: %s" %
              smartCollection.status_code)
    # print(smartCollection.json())
    # print(smartCollection.json()['smart_collection']['id'])
    return smartCollection.json()


def create_new_product():
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "product": {
            "title": "new",
            "body_html": "<b>New style<b>",
            "product_type": "sneaker",
        }
    }
    newproduct = requests.post(url + epnewproduct, json=data, headers=headers)
    if newproduct.status_code == 201:
        # The smart collection was created successfully
        print("Product created successfully")
    else:
        # An error occurred
        print("Error creating product: %s" %
              newproduct.status_code)
    return newproduct.json()


def add_2_option():
    headers = {
        "Content-Type": "application/json",
    }
    product_id = 8370306253091
    data = {
        # "sku": "147",
        # "quantity": 10,
        # "price": 100,
        "product": {
            # "sku": "sku01",
            # "quantity": 10,
            # "price": "100",

            "variants": [
                # {
                #     "sku": "sku01",
                #     "quantity": 10,
                #     "price": "100",
                # },
                {
                    "option1": "black",
                    "option2": "35",
                },
                {
                    "option1": "black",
                    "option2": "36",
                },
                {
                    "option1": "black",
                    "option2": "37",
                }
            ],
            "options": [
                {
                    "name": "Colors",
                    "position": 1,
                    "values": ["black", "white"]
                },
                {
                    "name": "Size",
                    "position": 2,
                    "values": ["35", "36", "37"]
                }
            ],
        }
    }
    newproduct = requests.post(url + f"products/{product_id}.json", json=data, headers=headers)
    if newproduct.status_code == 201:
        # The smart collection was created successfully
        print("Smart Collection created successfully")
    else:
        # An error occurred
        print("Error creating Smart Collection: %s" %
              newproduct.status_code)
    return newproduct.json()


def create_custom():
    data = {
        "customer": {
            "email": "vuthilien7121@gmail.com",
            "last_name": "lien",
            "adresses": [
                {
                    "first_name": "Mother",
                    "last_name": "Lastnameson",
                    "company": "",
                    "address1": "123 Oak St",
                    "address2": "",
                    "city": "Ottawa",
                    "province": "Ontario",
                    "country": "Canada",
                    "zip": "123 ABC",
                    "phone": "555-1212",
                }
            ]
        }
    }
    new_customer = requests.post(url + epcustomers, json=data, headers=headers)
    return new_customer.json()


def create_order():
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "order": {
            "line_items": [
                {
                    # "variant_id":8367871066403,
                    "title": "Giày Thể thao Nam - Nữ Biti's Hunter X Festive Frosty White DSMH03500TRG/DSWH03500TRG (Trắng)",
                    "price": 1000000,
                    "grams": 0.5,
                    "quantity": 2,
                }],
            "customer": {
                "first_name": "Paul",
                "last_name": "Mor",
                "email": "paul@gmail.com",
            },
            # "billing_address":{
            #     "first_name":"Paul",
            #     "last_name":"Mor",
            #     "address1":"VN",
            #     "phone":"5555555"
            # },
            "shipping_address": {
                "first_name": "Jane",
                "last_name": "Smith",
                "address1": "123 Fake Street",
                "phone": "777-777-7777",
                "city": "Fakecity",
                "province": "Ontario",
                "country": "Canada",
                "zip": "K2P 1L4"
            }
        }
    }
    new_order = requests.post(url + epoerders, json=data, headers=headers)
    print(url + epoerders)
    if new_order.status_code == 201:
        # The smart collection was created successfully
        print("Order created successfully")
    else:
        # An error occurred
        print("Error creating Order: %s" %
              new_order.status_code)
    return new_order.json()


def update_image_product():
    product_id = 8370030641443
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "image": {
            "id": 41553431396643,
            "product_id": product_id,
            "src": img2,
        }
    }
    updateproduct = requests.put(url + f"products/{product_id}/images.json", json=data, headers=headers)
    if updateproduct.status_code == 201:
        print("Smart Collection created successfully")
    else:
        print("Error creating Smart Collection: %s" %
              updateproduct.status_code)
    return updateproduct.json()


def create_image_product(product_id: int):
    # product_id=8370030641443
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "image": {
            "product_id": product_id,
            "position": 1,
            "src": "https://xuconcept.com/wp-content/uploads/2023/03/chup-anh-giay.jpg",
        }
    }
    new_image = requests.post(url + f"products/{product_id}/images.json", json=data, headers=headers)
    print(url + f"products/{product_id}/images.json")
    if new_image.status_code == 201:
        print("update image successfully")
    else:
        print("Error upadate image: %s" %
              new_image.status_code)
    return new_image.json()


def update_price_product(variants_id: int):
    # variants_id=45142952509731
    # product_id=8369881121059
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "variant":
            {
                "id": variants_id,
                "price": 100,
                # "compare_at_price": 150,
                # "inventory_management": "shopify",
            }

    }

    updateproduct = requests.put(url + f"variants/{variants_id}.json", json=data, headers=headers)
    print(url + f"variants/{variants_id}.json")
    print(updateproduct.text)
    if updateproduct.status_code == 201:
        print("update price successfully")
    else:
        print("Error update price: %s" %
              updateproduct.status_code)
    return updateproduct.json()


def add_option(product_id):
    # Set end point
    end_point_for_specific_product = f"products/{product_id}.json"
    # Create Product Variant Data with two options
    variants_data = {
        "title": "My Product Variant",
        "product": {
            "variants": [

                {
                    "option1": "Red",
                    "option2": "42",
                    "sku": "sku12345",
                    "price": 10.00,
                },
                {
                    "option1": "White",
                    "option2": "43",
                    "sku": "sku12345",
                    "price": 10.00,

                },
            ],
            "options": [
                {
                    "name": "Color",
                    "position": 1,
                    "values": [
                        "Red",
                        "White",
                        "Green",
                        "Blue",
                        "Orange"
                    ]
                },
                {
                    "name": "Size",
                    "position": 2,
                    "values": [
                        "35", "36", "37", "38", "39", "40", "41",
                        "42", "43", "44"
                    ]
                }
            ],
        }
    }
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point_for_specific_product
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY,
        "Content-Type": "application/json",
    }
    # Make the API request
    response = requests.put(url, data=json.dumps(variants_data),
                            headers=headers)
    # Check the response status code
    if response.status_code == 200:
        # The Product variants was created successfully
        print("Product variants added successfully")
    else:
        # An error occurred
        print("Error Adding Product Variants: %s" %
              response.status_code)
    return response.json()


def update_quantity(inventory_item_id, available):
    # inventory item id in variants.json, is id of each variant
    # You can use the inventory item ID to query the InventoryLevel resource to retrieve the location and quantity for an inventory item.
    tracked = {
        "inventory_item": {
            "tracked": True
        }
    }
    requests.put(url + f"inventory_items/{inventory_item_id}.json", json=tracked, headers=headers)
    ep_get_level = f"inventory_levels.json?inventory_item_ids={inventory_item_id}"
    inventory_level = requests.get(url + ep_get_level, headers=headers)
    print(inventory_level.json())
    location_id = inventory_level.json()["inventory_levels"][0]["location_id"]
    print(location_id)
    quantity = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available,

    }
    ep_set_quantity = "inventory_levels/set.json"
    update_quantity = requests.post(url + ep_set_quantity, json=quantity, headers=headers)
    return update_quantity.json()


def update_product(product):
    # print(product)
    # product_id=8367862612259
    # variants_id=45143535059235
    create_image_product(product['product']['id'])
    for variant in product['product']['variants']:
        update_price_product(variant['id'])
        # update_quantity(variant['inventory_item_id'], available


def delete_smart_collection(smcollection_id):
    delsmartCollection = requests.delete(url + f"smart_collections/{smcollection_id}.json")
    print(url + f"smart_colelctions/{smcollection_id}.json")
    print(delsmartCollection.text)
    if delsmartCollection.status_code == 200:
        # The smart collection was created successfully
        print("Smart Collection delete successfully")
    else:
        # An error occurred
        print("Error delete Smart Collection: %s" %
              delsmartCollection.status_code)
    return delsmartCollection.json


def delete_product(product_id):
    delproduct = requests.delete(url + f"products/{product_id}.json")
    # print(url + f"smart_colelctions/{product_id}.json")
    # print(delproduct.text)
    if delproduct.status_code == 200:
        # The smart collection was created successfully
        print("product delete successfully")
    else:
        # An error occurred
        print("Error delete product: %s" %
              delproduct.status_code)
    return delproduct.json


def delete_customer(customer_id):
    delcustom = requests.delete(url + f"customers/{customer_id}.json")
    # print(url + f"smart_colelctions/{product_id}.json")
    # print(delproduct.text)
    if delcustom.status_code == 200:
        # The smart collection was created successfully
        print("customer delete successfully")
    else:
        # An error occurred
        print("Error delete customer: %s" %
              delcustom.status_code)
    return delcustom.json


def delete_order(order_id):
    response_delorder = requests.delete(url + f"orders/{order_id}.json")
    # print(url + f"smart_colelctions/{product_id}.json")
    # print(delproduct.text)
    if response_delorder.status_code == 200:
        # The smart collection was created successfully
        print("order delete successfully")
    else:
        # An error occurred
        print("Error delete order: %s" %
              response_delorder.status_code)
    return response_delorder.json


def delete_all_custom_collection():
    collections = requests.get(url + "custom_collections.json")
    print(collections.json())
    for i in collections.json()['custom_collections']:
        print(i['id'])
        delsmartCollection = requests.delete(url + f"custom_collections/{i['id']}.json")
        if delsmartCollection.status_code == 200:
            # The smart collection was created successfully
            print("Custom Collection delete successfully")
        else:
            # An error occurred
            print("Error delete Custom Collection: %s" %
                  delsmartCollection.status_code)


def delete_all_smart_collection():
    collections = requests.get(url + "smart_collections.json")
    print(collections.json())
    for i in collections.json()['smart_collections']:
        print(i['id'])
        delsmartCollection = requests.delete(url + f"smart_collections/{i['id']}.json")
        if delsmartCollection.status_code == 200:
            # The smart collection was created successfully
            print("Smart Collection delete successfully")
        else:
            # An error occurred
            print("Error delete Smart Collection: %s" %
                  delsmartCollection.status_code)


def delete_all_product(product):
     # product = requests.get(url + "products.json")
    # print(product.json())
    for i in product.json()['products']:
        print(i['id'])
        # print(i)
        product = requests.delete(url + f"products/{i['id']}.json")
        if product.status_code == 200:
            # The smart collection was created successfully
            print(" Delete all product successfully")
        else:
            # An error occurred
            print("Delete all products: %s" %
                  product.status_code)


def delete_all_order():
    orders = requests.get(url + "orders.json")
    print(orders.json())
    for i in orders.json()['orders']:
        print(i['id'])
        delOrder = requests.delete(url + f"orders/{i['id']}.json")
        if delOrder.status_code == 200:
            # The smart collection was created successfully
            print(" Delete all product successfully")
        else:
            # An error occurred
            print("Delete all products: %s" %
                  delOrder.status_code)


def delete_all_customer():
    customers = requests.get(url + "customers.json")
    print(customers.json())
    for i in customers.json()['customers']:
        print(i['id'])
        delCustomer = requests.delete(url + f"customers/{i['id']}.json")
        if delCustomer.status_code == 200:
            # The smart collection was created successfully
            print(" Delete all customer successfully")
        else:
            # An error occurred
            print("Delete all products: %s" %
                  delCustomer.status_code)


def delete_all():
    delete_all_order()
    delete_all_customer()
    delete_all_product()
    delete_all_custom_collection()


if __name__ == '__main__':
    # delete_all_customer()
    # delete_all_order()
    # delete_all_product()
    # delete_all_collection()
    # customer=create_custom()
    # print(customer)
    # delete_customer(customer['customer']['id'])
    #  custom_collection=create_custom_collection()
    # smart_collection = create_custom_smart_collection()
    # n=251
    # for i in range(n):
    #     product = create_new_product()
    #     print(i)
    # for i in range(n//50+1):
    #     print(i)
    #     delete_all_product()

    # for i in range(50):
    #     product = create_new_product()
    #     print(i)

    # while product_id not found -> break
    product = requests.get(url + "products.json")
    # print(product.json())
    # print(type(product.json()['products']))
    while len(product.json()['products']) > 0:
        product = requests.get(url + "products.json")
        delete_all_product(product)
        # if(len(product.json()['products']==0)):
        #     break

    # delete_all_smart_collection()
    # print(smart_collection)
    # print(smart_collection['smart_collection']['id'])
    # delete_smart_collection(smart_collection['smart_collection']['id'])
    # product = create_new_product()
    # delete_product(product['product']['id'])
    # product_option = add_option(product['product']['id'])
    # order=create_order()
    # print(create_order())
    # delete_order(order['order']['id'])
    # update_product(product_option)
    # update_quantity(47246224884003,150)
