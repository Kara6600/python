from product import Product

# создаем объект типа Product
my_product = Product("Ноутбук", 50000)

# вызываем методы и выводим результаты
print(my_product.get_name())            # название продукта
print(my_product.get_price())           # цена продукта
print(my_product.get_product_info())     # строка с названием и ценой