from sqlalchemy import create_engine, text


db_connection_str = 'mysql+pymysql://253zViqMi1Pyfkj.root:Dig2KoqwUVk7fMON@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/test?charset=utf8mb4'


engine = create_engine(db_connection_str, connect_args={
             "ssl": {
                 "ssl_ca": "/etc/ssl/isrgrootx1.pem"
             }
         })


def load_products_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from product"))
  result_all = result.all()
  column = result.keys()
  result_dicts = []
  for row in result_all:
     result_dicts.append(dict(zip(column, row)))
  return result_dicts



def add_product_to_db(name, quantity):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO product(name, quantity) VALUES (:name, :quantity)"
        )

        conn.execute(
            query,
            {
                "name": name,
                "quantity": quantity
            },
        )
        conn.commit()



def delete_product_from_db(id):
    with engine.connect() as conn:
        query = text(
            "DELETE FROM product WHERE id= :id;"
        )

        conn.execute(
            query,
            {
                "id": id,
            },
        )
        conn.commit()

      
    

def update_product_in_db(id,name, quantity):
    with engine.connect() as conn:
        query = text(
            "UPDATE product SET name = :name, quantity = :quantity WHERE id = :id;"
        )

        conn.execute(
            query,
            {
               "id" : id,
                "name": name,
                "quantity": quantity
            },
        )
        conn.commit()    
      

