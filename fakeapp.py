
import streamlit as st
import joblib

# मोडेल लोड गर्ने
model = joblib.load('nepali_news_detector_model.pkl')

st.set_page_config(page_title="नेपाली फेक न्यूज डिटेक्टर", layout="centered")
st.title("🔍 नेपाली फेक न्यूज डिटेक्टर")
st.markdown("यो एउटा AI आधारित सिस्टम हो जसले समाचारको सत्यता जाँच्न मद्दत गर्छ।")

news_text = st.text_area("समाचार यहाँ पेस्ट गर्नुहोस्:", height=200)

if st.button("सत्यता जाँच्नुहोस्"):
    if news_text.strip():
        prediction = model.predict([news_text])[0]
        prob = model.predict_proba([news_text])
        confidence = max(prob[0]) * 100
        
        if prediction == 'Fake':
            st.error(f"🚨 यो समाचार **फेक** हुन सक्ने सम्भावना {confidence:.2f}% छ।")
        else:
            st.success(f"✅ यो समाचार **वास्तविक** हुन सक्ने सम्भावना {confidence:.2f}% छ।")
    else:
        st.warning("कृपया पहिले केही टेक्स्ट लेख्नुहोस्।")
