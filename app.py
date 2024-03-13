import streamlit as st
from ultralytics import YOLO
from mxnum import image_pathimg

# Define a function to perform YOLO prediction and save the annotated image
def perform_yolo_prediction(image_path):
    # Define the path togcl your trained model file
    model_path = "best.pt"

    # Create a YOLO object instancedocker 
    model = YOLO(model_path)

    # Perform prediction on the image
    results = model.predict(image_path, show=True, save=True)
    print("Result:",results)
    print("Imagesavedpath :", image_pathimg() )

    # Extract the path of the annotated image
    annotated_image_path = image_pathimg()

    # Return the path to the annotated image
    return annotated_image_path

# Create a Streamlit app
def main():
    st.title("Dentalchair Object Detection")

    # Allow user to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded image to a temporary directory
        temp_image_path = "temp_image.jpg"
        with open(temp_image_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # Perform YOLO prediction and get the path to the annotated image
        annotated_image_path = perform_yolo_prediction(temp_image_path)

        # Display the annotated image
        st.image(annotated_image_path, use_column_width=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
