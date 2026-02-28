RISK_KEYWORDS = [
    "suicide", "kill myself", "end my life",
    "hurt myself", "giving up", "want to disappear",
    "can't go on"
]

MOOD_KEYWORDS = {
    "sad": ["sad", "lonely", "empty", "hopeless", "low"],
    "stressed": ["stressed", "overwhelmed", "pressure", "exhausted"],
    "anxious": ["anxious", "worried", "panic", "nervous"],
    "angry": ["angry", "frustrated", "irritated", "mad"],
    "happy": ["happy", "calm", "relieved", "good"]
}

def detect_risk(text):
    text = text.lower()
    return any(word in text for word in RISK_KEYWORDS)

def detect_mood(text):
    text = text.lower()
    for mood, words in MOOD_KEYWORDS.items():
        for w in words:
            if w in text:
                return mood
    return "neutral"
