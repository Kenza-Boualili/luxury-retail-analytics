# 💎 Luxury Retail Analytics — Performance & Client Segmentation Dashboard

<p align="center">
  <img src="assets/dashboard_overview.png" alt="Luxury Retail Dashboard Overview" width="100%">
</p>

---

## Executive Summary

This project delivers an end-to-end business intelligence solution tailored for high-end luxury houses (*Maison de Luxe*). Designed to align with the analytical standards of leading prestige groups like **LVMH, Hermès, and Kering**, this interactive platform synthesizes flagship boutique performance, category distribution, average order value (AOV), and high-net-worth client dynamics (VIP / VIC segmentation).

The architecture spans the full data analytics lifecycle:
1. **Data Engineering & Preparation** via Python (`pandas`, `numpy`).
2. **Relational Querying & KPI Extraction** via SQL (`sqlite3`).
3. **Interactive Executive Visualization** via Power BI (*Minimalist Dark & Gold Theme*).

---

## 🛠️ Technical Architecture & Stack

| Layer | Technology | Usage & Functionality |
| :--- | :--- | :--- |
| **Data Engine** | `Python 3.10+` | Dataset orchestration, transaction modeling, schema normalization |
| **Database** | `SQL (SQLite / PostgreSQL)` | Relational querying, aggregation, client tier distribution |
| **Visual Analytics** | `Power BI Desktop` | Interactive dashboarding, dynamic slicers, DAX measures |
| **Documentation** | `Markdown / VS Code` | Technical reporting and executive insights |

---

## 📊 Business Metrics & Key Performance Indicators

* **Total Revenue:** `€40.00M`
* **Average Order Value (AOV):** `€7,940`
* **Top Flagship Location:** `Paris — Faubourg Saint-Honoré (€12M)`
* **Core Product Category:** `Leather Goods / Maroquinerie (67.22%)`
* **Client Segmentation:** High contribution from VIP & Very Important Clients (VIC) relative to total volume.

---

## 💻 Relational Database Interrogation (`queries.sql`)

```sql
-- ============================================================
-- LUXURY RETAIL ANALYTICS — EXECUTIVE QUERIES
-- ============================================================

-- 1. Revenue & Average Order Value (AOV) by Flagship Boutique
SELECT 
    store_name,
    COUNT(transaction_id) AS total_transactions,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_order_value
FROM transactions
GROUP BY store_name
ORDER BY total_revenue DESC;

-- 2. Top 5 Revenue-Generating Product Identifiers
SELECT 
    product_id,
    category,
    COUNT(transaction_id) AS units_sold,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM transactions
GROUP BY product_id, category
ORDER BY total_revenue DESC
LIMIT 5;

-- 3. Revenue Distribution by Client Loyalty Tier (VIP / VIC / Standard)
SELECT 
    tier,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(SUM(total_amount) * 100.0 / (SELECT SUM(total_amount) FROM transactions), 2) AS revenue_percentage
FROM transactions
GROUP BY tier
ORDER BY total_revenue DESC;
```

---

## 🎯 Strategic Business Recommendations

### 1. Capitalisation sur le Flagship Paris Faubourg Saint-Honoré
* **Constat :** Paris surpasse l'ensemble des points de vente internationaux avec 12 M€ de Chiffre d'Affaires.
* **Action :** Analyser les facteurs clés de succès (allocation de stock, expérience client en boutique, formation des *Client Advisors*) afin de modéliser et répliquer ces pratiques à Tokyo-Ginza et New York-Fifth Avenue.

### 2. Stratégie de Rétention et d'Engagement VIC (Very Important Clients)
* **Constat :** La clientèle VIP et VIC représente un levier disproportionné de chiffre d'affaires par rapport au nombre d'acheteurs.
* **Action :** Renforcer les programmes de *Clienteling* exclusifs (privatisation de salons VIP, invitations aux défilés, accès anticipé aux pièces de Haute Maroquinerie).

### 3. Diversification du Mix-Produit (Cross-Selling)
* **Constat :** La Maroquinerie génère à elle seule plus de 67 % des revenus globaux.
* **Action :** Développer des stratégies de vente croisée (*cross-selling*) lors des achats de sacs iconiques pour diriger les clients vers le Prêt-à-porter, l'Horlogerie ou la Joaillerie.

### 4. Plan d'Action pour les Boutiques à Fort Panier Moyen
* **Constat :** Certaines boutiques affichent un volume de transactions plus faible mais un AOV très élevé.
* **Action :** Adapter le *visual merchandising* et l'assortiment de produits réservé aux boutiques comme London - New Bond Street ou Milan pour maximiser les ventes à très forte valeur ajoutée.

---

<p align="center">
  <i>Designed for Executive Analytics & Luxury Retail Strategy</i>
</p>