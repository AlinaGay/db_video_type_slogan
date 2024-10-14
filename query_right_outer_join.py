import sqlite3
con = sqlite3.connect('db_video_type_slogan.sqlite')
cur = con.cursor()
results = cur.execute('''
  SELECT video_products.title,
       product_types.title
  FROM video_products
  RIGHT JOIN product_types ON video_products.type_id = product_types.id;
''')
for result in results:
    print(result)

con.close()


# The same
'''
SELECT video_products.title,
       product_types.title
FROM product_types
LEFT JOIN video_products ON video_products.type_id = product_types.id;
'''
