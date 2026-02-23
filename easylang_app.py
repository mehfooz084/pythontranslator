import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="EasyLang Translator", layout="centered")

st.title("🌐 EasyLang Translator")

langs = list(GoogleTranslator().get_supported_languages(as_dict=True).keys())

src_lang = st.selectbox("Source Language", langs, index=langs.index("english"))
dest_lang = st.selectbox("Target Language", langs, index=langs.index("hindi"))

text_input = st.text_area("Enter Text to Translate")

if st.button("Translate"):
    if text_input.strip():
        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text_input)
        st.success("Translated Text:")
        st.text_area("Output", translated, height=150)
    else:
        st.warning("Please enter some text.")
