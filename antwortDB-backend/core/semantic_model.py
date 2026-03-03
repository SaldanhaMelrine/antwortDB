SEMANTIC_MODEL = {

    "olist_order_items_dataset": {
        "role": "fact",
        "grain": "one row per product within an order",
        "measures": ["price", "freight_value"],
        "keys": ["order_id", "product_id", "seller_id"]
    },

    "olist_order_payments_dataset": {
        "role": "fact",
        "grain": "one payment transaction per order",
        "measures": ["payment_value"],
        "keys": ["order_id"]
    },

    "olist_orders_dataset": {
        "role": "dimension",
        "entity": "orders",
        "keys": ["order_id", "customer_id"]
    },

    "olist_products_dataset": {
        "role": "dimension",
        "entity": "products",
        "keys": ["product_id"]
    },

    "olist_customers_dataset": {
        "role": "dimension",
        "entity": "customers",
        "keys": ["customer_id"]
    },

    "olist_sellers_dataset": {
        "role": "dimension",
        "entity": "sellers",
        "keys": ["seller_id"]
    }
}