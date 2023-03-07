import os
import openai
import streamlit as st

openai.api_key = st.secrets["api_key"]

def main():
    st.title("Product Sales Copy Generator")
    st.image("product.jpg")
    notes = st.text_area("Enter a short product description:")
    
    if st.button("Generate sales copy"):
        with st.spinner("Generating description..."):
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Write a compelling sales copy for social media users with short headline, subheadline, bulleted points, each point on separate lines, and call to action, based on the below information:\n\nProduct: {notes}",
            temperature=0.8,
            max_tokens=503,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            
            description = response['choices'][0]['text']
            st.subheader("Generated description: ")
            st.success(description)
            
        
if __name__ == "__main__":
    main()
