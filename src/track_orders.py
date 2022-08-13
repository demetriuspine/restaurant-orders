class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders_list = []

    def __len__(self):
        orders_list_len = len(self.orders_list)
        return orders_list_len

    def add_new_order(self, customer, order, day):
        self.orders_list.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        count = dict()
        for name, order, day in self.orders_list:
            if name == customer:
                if order not in count:
                    count[order] = 1

                count[order] += 1

        most_ordered_dish_per_customer = max(count, key=count.get)

        return most_ordered_dish_per_customer

    def get_never_ordered_per_customer(self, customer):
        orders = {
            order for name, order, day in self.orders_list if name == customer
            }
        menu = {
            order for name, order, day in self.orders_list
        }
        never_ordered_per_customer = menu - orders
        return never_ordered_per_customer

    def get_days_never_visited_per_customer(self, customer):
        visited_days = {
            day for name, order, day in self.orders_list if name == customer
            }
        days = {
            day for name, order, day in self.orders_list
        }

        days_never_visited_per_customer = days - visited_days

        return days_never_visited_per_customer

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
