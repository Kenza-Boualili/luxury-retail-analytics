import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Fixer la graine pour que les résultats soient reproductibles
np.random.seed(42)

# 1. Génération des Boutiques phares
stores = pd.DataFrame({
    'store_id': ['ST01', 'ST02', 'ST03', 'ST04', 'ST05'],
    'store_name': ['Paris - Faubourg Saint-Honoré', 'Tokyo - Ginza', 'New York - Fifth Avenue', 'Milan - Via Montenapoleone', 'London - New Bond Street'],
    'region': ['Europe', 'Asia', 'North America', 'Europe', 'Europe']
})

# 2. Génération des Produits (Maroquinerie, Joaillerie, etc.)
categories = ['Maroquinerie', 'Prêt-à-porter', 'Joaillerie', 'Horlogerie', 'Parfums & Beauté']
products = pd.DataFrame({
    'product_id': [f'P{i:03d}' for i in range(1, 21)],
    'category': np.random.choice(categories, 20, p=[0.3, 0.3, 0.1, 0.1, 0.2]),
    'unit_price': np.random.choice([450, 1200, 2500, 5000, 12000, 25000], 20)
})

# 3. Génération des Clients (avec segmentation VIP)
customers = pd.DataFrame({
    'customer_id': [f'C{i:04d}' for i in range(1, 201)],
    'tier': np.random.choice(['Standard', 'VIP', 'VIC (Very Important Client)'], 200, p=[0.7, 0.2, 0.1])
})

# 4. Génération des Transactions (sur 1 an)
start_date = datetime(2025, 1, 1)
n_transactions = 5000

dates = [start_date + timedelta(days=int(np.random.randint(0, 365))) for _ in range(n_transactions)]
store_ids = np.random.choice(stores['store_id'], n_transactions, p=[0.3, 0.25, 0.2, 0.15, 0.1])
product_ids = np.random.choice(products['product_id'], n_transactions)
customer_ids = np.random.choice(customers['customer_id'], n_transactions)
quantities = np.random.choice([1, 2], n_transactions, p=[0.9, 0.1]) # Panier rare dans le luxe

transactions = pd.DataFrame({
    'transaction_id': [f'T{i:05d}' for i in range(1, n_transactions + 1)],
    'date': dates,
    'store_id': store_ids,
    'product_id': product_ids,
    'customer_id': customer_ids,
    'quantity': quantities
})

# Calcul du montant total par transaction
transactions = transactions.merge(products, on='product_id')
transactions['total_amount'] = transactions['quantity'] * transactions['unit_price']

# Sauvegarde des fichiers CSV dans ton dossier de projet
transactions.to_csv('luxury_transactions.csv', index=False)
stores.to_csv('luxury_stores.csv', index=False)
products.to_csv('luxury_products.csv', index=False)
customers.to_csv('luxury_customers.csv', index=False)

print("Jeu de données généré avec succès dans ton dossier !")
