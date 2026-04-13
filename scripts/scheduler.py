# Instagram Content Automation Hub
# Niches: Parenting (@firstblinkmamababysleep) & Finance (@cashfromsystem)

import datetime

def generate_post_ideas():
    print("--- 🚀 Instagram Content Strategy [June 2026] ---")
    
    # Content pillars for your specific niches
    strategy = {
        "Parenting": [
            "Reel: 5 signs your baby is ready for a nap",
            "Carousel: Hidden sleep patterns you need to know",
            "Post: Why routine matters more than luck"
        ],
        "Finance/AI": [
            "Reel: How I use AI to make $100 in 7 days",
            "Carousel: Best faceless niche ideas for introverts",
            "Post: Tools I use: Canva + ElevenLabs + CapCut"
        ]
    }
    
    today = datetime.date.today()
    print(f"Plan generated on: {today}\n")
    
    for niche, ideas in strategy.items():
        print(f"Target Niche: {niche}")
        for i, idea in enumerate(ideas, 1):
            print(f"  {i}. {idea}")
        print("-" * 30)

if __name__ == "__main__":
    generate_post_ideas()
