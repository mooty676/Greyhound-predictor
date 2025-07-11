def predict_top_4(df):
    df["FormScore"] = df["Form"].apply(lambda f: sum([int(c) if c.isdigit() else 8 for c in f[:5]]))
    top_4 = df.sort_values(by="FormScore").head(4)
    return top_4["Name"].tolist()
