%%writefile app.py
import streamlit as st
import joblib
import re

# यहाँ हामीले अघि बनाएको मोडेल र क्लीनिंग फंक्सन चाहिन्छ
# यो उदाहरणका लागि सिम्पल राखिएको छ
def clean_nepali_text(text):
    text = re.sub(r'[^\u0900-\u097F\s]', '', text)
    return text

st.title("🇳🇵 नेपाली फेक न्यूज डिटेक्टर")
st.write("समाचारको शीर्षक वा विवरण तल पेस्ट गर्नुहोस् र जाँच्नुहोस्।")

news_input = st.text_area("समाचार यहाँ राख्नुहोस्:", height=200)

if st.button("जाँच्नुहोस्"):
    if news_input:
        # यहाँ तपाईंको ट्रेन्ड मोडेल (model_pipeline) लोड गर्नुपर्छ
        # अहिलेका लागि हामीले अघि बनाएको model_pipeline प्रयोग गरिरहेका छौं
        # (नोट: वास्तविक एपमा मोडेललाई पहिले joblib.dump गरेर लोड गरिन्छ)
        
        # यहाँ परीक्षणको लागि मोडेल कल गर्ने (यो डेमो मात्र हो)
        # prediction = model_pipeline.predict([clean_nepali_text(news_input)])
        # st.header(f"नतिजा: {prediction[0]}")
        
        st.success("मोडेलले यो समाचारलाई विश्लेषण गर्दैछ...")
        # यहाँ तपाईंको प्रेडिक्सन लोजिक राख्नुहोस्
    else:
        st.warning("कृपया केही टेक्स्ट लेख्नुहोस्।")
