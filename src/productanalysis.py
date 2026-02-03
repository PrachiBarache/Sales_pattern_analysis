from src.anlysisbasket import prepare_basket, run_apriori, generate_rules

basket = prepare_basket(df)
frequent_items = run_apriori(basket)
rules = generate_rules(frequent_items)

rules[["antecedents", "consequents", "support", "confidence", "lift"]].head(10)
