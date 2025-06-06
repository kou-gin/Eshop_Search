# model/eshop_logic.py

from dao.eshop_dao import EshopDAO

class EshopLogic:
    def execute(self, es):
        """
        EshopWord オブジェクト es に含まれる検索条件に基づき、
        DAO を使って検索結果（件数とリスト）を取得して、es に格納する。
        """
        dao = EshopDAO()

        # 検索条件に基づき件数とリストを取得
        es.total_count = dao.get_total_count(
            es.search_location,
            es.search_shop,
            es.search_category_id,
            es.search_mode
            
        )
        es.list = dao.get_list_by_conditions(
            es.search_location,
            es.search_shop,
            es.search_category_id,
            es.search_mode
        )
