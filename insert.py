import json
import psycopg2
from config import load_config

JSON_FILE_PATH = "input/products_output.json"

def insert_products_from_json():
    sql = """
        INSERT INTO products (
            id,
            price,
            name,
            url_key,
            images_url,
            description
        )
        VALUES(
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        ON CONFLICT (id) DO NOTHING;
    """
    config = load_config()
    batch_size = 1000
    batch = []
    total_inserted = 0
    # Read file json
    try:
        with open(JSON_FILE_PATH,'r',encoding='utf-8') as f:
         products = json.load(f)
    except FileNotFoundError as fnfe:
        print('File json not found')
        return
    except json.JSONDecodeError as json_err:
        print('Invalid json')
        return
    
    # connect DB to insert 
    try:
         with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for product in products:
                    # Check ID 
                    try:
                        prod_id = int(product.get('id'))
                    except(ValueError,TypeError) as error:
                        print(error)
                        continue

                    name = product.get('name','')
                    # price = product.get('price') or 0
                    raw_price = product.get('price')
                    try:
                        price = float(raw_price) if raw_price is not None else 0
                    except(ValueError,TypeError):
                        price = 0
                    

                    url_key = product.get('url_key','')
                    description = product.get('description','')
                    images = product.get('images_url',[])
                    images_str = ";".join(images) if isinstance(images,list) else str(images)

                    record = (prod_id,price,name,url_key,images_str,description)

                    batch.append(record)

                    if len(batch) >= batch_size:
                        try:
                            cur.executemany(sql,batch)
                            conn.commit()
                            total_inserted += len(batch)
                            print(f"   Đã nạp: {total_inserted:,} sản phẩm...")
                        except(Exception,psycopg2.DatabaseError) as error:
                            print('Error',error)
                            conn.rollback()
                        finally:
                            batch = []
                if batch:
                    try:
                        cur.executemany(sql,batch)
                        conn.commit()
                        total_inserted += len(batch)
                        print(f"Đã nạp: {total_inserted:,} sản phẩm...")
                    except(Exception,psycopg2.DatabaseError) as error:
                        print('Error',error)
                        conn.rollback()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    

if __name__ == "__main__":
    insert_products_from_json()
    