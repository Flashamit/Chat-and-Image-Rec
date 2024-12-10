import ollama
import streamlit as st


uploaded_image = st.file_uploader("Upload an Image for Analysis", type=["png", "jpg", "jpeg"])

# Process uploaded image
if uploaded_image and st.button("Process Image"):
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    # Save uploaded image locally for processing
    image_path = f"./uploaded_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_image.getbuffer())
    
    
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'Provide only the name of the fruit and Calorie, Carbohydrates, Fiber, Protein, Fat count of the specified fruit without any additional details or explanations.',
            'images': [image_path]
        }]
    )
    
    # Display response
    st.write(response['message']['content'])
    print(response['message']['content'])
