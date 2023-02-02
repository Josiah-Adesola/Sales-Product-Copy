import os
import openai
import streamlit as st

openai.api_key = os.environ.get("OPENAI_API_KEY")

def main():
    st.title("Product Description Generator")
    st.image("product.jpg")
    notes = st.text_area("Enter a product information:")
    if st.button("Generate Description"):
        with st.spinner("Generating description..."):
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Write a production description based on the below information:\n\nProduct: {notes}",
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