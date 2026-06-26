#LISTAS
POSITIVE_LIST = ["good", "nice", "awesome", "genius", "fun", "amazing"]
NEGATIVE_LIST = ["bad", "horrible", "boring", "terrible", "awful", "shit"]

def scoring(list):
    positive_score = 0
    negative_score = 0
    score = 0
    for word in list:
        if word in POSITIVE_LIST:
            positive_score += 1
        elif word in NEGATIVE_LIST:
            negative_score += 1
    score = positive_score - negative_score
    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    elif score == 0:
        sentiment = "Neutral"
        
    return sentiment