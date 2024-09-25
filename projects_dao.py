import mysql.connector
    
def get_all_products():
    try:
        print("started")
        contr = mysql.connector.connect(user='root', password='ZEElabs1!',
                                    host='localhost',
                                    database='grocery_store')
        cursor = contr.cursor()

        query = ("""SELECT products.product_id, products.name, products.uniit_of_measure, products.price_per_unit, unit_of_measurement.uom_name
                FROM products inner join unit_of_measurement on products.uniit_of_measure=unit_of_measurement.uom_id""")

        cursor.execute(query)
        response = []
        for (product_id,name,uniit_of_measure,price_per_unit, uom_name) in cursor:
            response.append(
                {
                    "product_id": product_id,
                    'name': name,
                    "unit_of_measure_id": uniit_of_measure,
                    "price_per_unit": price_per_unit,
                    "uom_name": uom_name

                }

            )
            
        contr.close()
        return response
    except mysql.connector.Error as e:
        print("error", e)
        #print(dir(mysql.connector))

       
if __name__ == "__main__":
    print(get_all_products())