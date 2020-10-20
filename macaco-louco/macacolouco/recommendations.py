from typing import Optional, List, Dict, Any
from .dao_mongo import MongoDB


class Recommendation:
    def __init__(self, *args, **kwargs):
        self.db = MongoDB()
        self.limit = 20
        super().__init__(*args, **kwargs)

    def compute(self, product_sku: Optional[str]) -> List[Dict[str, Any]]:
        if product_sku == "all":
            recommendations = self.db.recommendations().find_one()
        else:
            recommendations = self.db.recommendations().find_one(
                {"source_item_id": product_sku}
            )

        products = [
            j[0]
            for j in sorted(
                recommendations["items_scores"].items(),
                key=lambda i: i[1],
                reverse=True,
            )
        ][:self.limit]

        return self.db.products().find({"sku": {"$in": products}})
