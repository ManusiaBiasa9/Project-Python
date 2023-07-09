from tabulate import tabulate

class Transaction():
    def __init__ (self):
        self.order_item = dict()

    def add_item (self, item_name, item_qty, item_price):
        self.order_item.update({item_name: [item_qty, item_price]})

        try:
            self.item_qty = int(item_qty)
            self.item_price = int(item_price)
        except:
            print("Jumlah dan harga barang harus berupa angka")
    def update_item_name(self, item_name, new_item_name):
        temp = self.order_item[item_name]
        self.order_item.pop(item_name)
        self.order_item.update({new_item_name:temp})

    def update_item_qty(self, item_name, new_item_qty):
        self.order_item[item_name][0] = new_item_qty

    def update_item_price(self, item_name, new_item_price):
        self.order_item[item_name][1] = new_item_price

    def show_order(self):
        show_order = []
        header = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        show_order.append(header)

        n = 0

        for key, value in self.order_item.items():
            n += 1
            table_no = n
            item_name = key
            item_qty = value[0]
            item_price = value[1]
            total = item_qty * item_price
            item_data = [table_no, item_name, item_qty, item_price, total]
            show_order.append(item_data)

        print(tabulate(show_order, tablefmt="fancy_grid"))

    def delete_item(self, item_name):
        try:
            self.order_item.pop(item_name)
            print(f"Anda berhasil menghapus pesanan {item_name}")
            print("")
        except KeyError:
            print(f"Nama barang {item_name} tidak terdapat pada daftar pemesanan")

    def reset_transaction(self):
        transaction = {}
        self.order_item = transaction
        print("Anda tidak memiliki daftar pesanan")

    def check_order(self):
        for key, value in self.order_item.items():
            item_name = key
            item_qty = value[0]
            item_price = value[1]

        if type(item_name) == str and type(item_qty) == int and type(item_price) == int:
            print("Pemesanan sudah benar")
        else:
            print("Terdapat kesalahan input data/pesanan")

    def total_price(self):
        self.total_price = 0
        for value in self.order_item.values():
            item_qty = value[0]
            item_price = value[1]
            self.total_price += (item_qty * item_price)
        if self.total_price <= 200000:
            dapat_diskon = False
            diskon = 0.0
        else:
            dapat_diskon = True
            if self.total_price > 500000:
                diskon = 0.1
            elif self.total_price > 300000:
                diskon = 0.08
            elif self.total_price > 200000:
                diskon = 0.05
        self.final_price = self.total_price * (1 - diskon)

        if dapat_diskon:
            print(f"Selamat Anda mendapatkan diskon sebesar {diskon *100:.0f}%, \n sehingga Anda hanya perlu membayar Rp.{self.final_price:.2f}")
        else:
            print(f"Total yang Anda harus bayar adalah Rp.{self.total_price}")
            