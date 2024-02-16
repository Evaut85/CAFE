def main():
    menu = {
        "лате": 50,
        "американо": 45,
        "еспресо": 40,
        "чізкейк": 60,
    }
    order = {}

    while True:
        print("Меню:")
        for item, price in menu.items():
            print(f"{item}: {price} грн")

        product = input("Введіть товар (або 'закінчити' для завершення замовлення): ").lower()
        if product == 'закінчити':
            break

        if product not in menu:
            print("Товар відсутній в меню.")
            add_new_product = input("Бажаєте додати новий товар? (так/ні): ").lower()
            if add_new_product == 'так':
                price = int(input("Введіть ціну за одиницю товару: "))
                menu[product] = price
            else:
                continue

        quantity = int(input("Введіть кількість: "))
        order[product] = order.get(product, 0) + quantity

    print("\nЗамовлення:")
    total_cost = 0
    for product, quantity in order.items():
        price = menu[product]
        cost = price * quantity
        total_cost += cost
        print(f"{product}: {quantity} x {price} грн = {cost} грн")

    print(f"Загальна вартість замовлення: {total_cost} грн")


if __name__ == "__main__":
    main()