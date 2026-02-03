from src.featureengineering import compute_rfm,assign_rfm_scores

rfm = compute_rfm(df)
rfm = assign_rfm_scores(rfm)

rfm.head()
#segmentation defining
rfm["Segment"] = "Low Value"
rfm.loc[(rfm["R"] >= "4") & (rfm["F"] >= "4"), "Segment"] = "Champions"
rfm.loc[(rfm["R"] <= "2") & (rfm["F"] >= "4"), "Segment"] = "Loyal"
rfm.loc[(rfm["R"] <= "2") & (rfm["F"] <= "2"), "Segment"] = "At Risk"
