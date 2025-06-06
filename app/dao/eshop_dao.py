
# dao/eshop_dao.py

from dao.db_connector import get_connection
from model.eshop import Eshop

class EshopDAO:
    def find_all(self):
        """
        テーブル 'eshops' の全件取得を行い、Eshop オブジェクトのリストとして返す。
        """
        eshops = []
        sql = "SELECT * FROM eshops ORDER BY id DESC"
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                eshop = Eshop(
                    id=row.get("id"),
                    location=row.get("location"),
                    shop=row.get("shop"),
                    detail=row.get("detail")
                )
                eshops.append(eshop)
        except Exception as e:
            print("Error in find_all:", e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

        return eshops

    def get_list_by_conditions(self, location="", shop="", category_id="", mode="AND"):
        sql = "SELECT * FROM eshops"
        conditions = []
        params = []

        if location:
            conditions.append("location LIKE %s")
            params.append(f"%{location}%")
        if shop:
            conditions.append("shop LIKE %s")
            params.append(f"%{shop}%")
        if category_id:
            conditions.append("category_id = %s")
            params.append(category_id)

        if conditions:
            joiner = " AND " if mode == "AND" else " OR "
            sql += " WHERE " + joiner.join(conditions)
        sql += " ORDER BY id DESC LIMIT 200"

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, tuple(params))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [Eshop(**row) for row in rows]

    def get_total_count(self, location="", shop="", category_id="", mode="AND"):
        sql = "SELECT COUNT(*) AS total FROM eshops"
        conditions = []
        params = []

        if location:
            conditions.append("location LIKE %s")
            params.append(f"%{location}%")
        if shop:
            conditions.append("shop LIKE %s")
            params.append(f"%{shop}%")
        if category_id:
            conditions.append("category_id = %s")
            params.append(category_id)

        if conditions:
            joiner = " AND " if mode == "AND" else " OR "
            sql += " WHERE " + joiner.join(conditions)

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, tuple(params))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row["total"] if row else 0


    def get_category_list(self):
        sql = "SELECT id, category FROM categories ORDER BY id"
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def insert_one(self, eshop):
        """
        Eshop オブジェクトの内容を 'eshops' テーブルに1件挿入する。
        """
        sql = """
            INSERT INTO eshops (location, shop, detail, category_id)
            VALUES (%s, %s, %s, %s)
        """
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (eshop.location, eshop.shop, eshop.detail, eshop.category_id))
            conn.commit()
        except Exception as e:
            print("Error in insert_one:", e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
