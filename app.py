from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('HealthCareData.pkl', 'rb') as f:
    model = pickle.load(f)
    
print(type(model))

# Define feature columns to be used for prediction
FEATURE_COLUMNS = [
    'Gender', 'Type of alcohol consumed', 'Hepatitis B infection',
    'Hepatitis C infection', 'Diabetes Result', 'Obesity',
    'Family history of cirrhosis/ hereditary', 'Duration of alcohol consumption(years)',
    'TCH', 'HDL', 'Hemoglobin  (g/dl)', 'PCV  (%)', 'Total Count', 'Polymorphs  (%) ',
    'Lymphocytes  (%)', 'Eosinophils   (%)', 'Basophils  (%)', 'Total Bilirubin    (mg/dl)',
    'Direct    (mg/dl)', 'Total Protein     (g/dl)', 'Albumin   (g/dl)',
    'AL.Phosphatase      (U/L)', 'SGOT/AST      (U/L)'
]

def to_int(input_data):
    # Define mappings
    gender_map = {'male': 0, 'female': 1}
    type_map = {'branded': 0, 'country': 1, 'both': 2}
    hep_map = {'positive': 1, 'negative': 0}
    diabetes_map = {'YES': 1, 'NO': 0}
    yes_no_map = {'yes': 1, 'no': 0}

    # Convert categorical values to integers
    input_data[0] = gender_map.get(input_data[0], -1)  # Default to -1 if not found
    input_data[1] = type_map.get(input_data[1], -1)
    input_data[2] = hep_map.get(input_data[2], -1)
    input_data[3] = hep_map.get(input_data[3], -1)
    input_data[4] = diabetes_map.get(input_data[4], -1)
    input_data[5] = yes_no_map.get(input_data[5], -1)
    input_data[6] = yes_no_map.get(input_data[6], -1)
    
    # Convert numeric features to integers
    for i in range(7, 23):
        try:
            input_data[i] = float(input_data[i])  # Convert to float first, then cast to int
        except ValueError:
            input_data[i] = -1  # Default to -1 if conversion fails
    
    return input_data


# Set NumPy print options
np.set_printoptions(precision=2, suppress=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Extract features from form
        input_features = [request.form.get(feature) for feature in FEATURE_COLUMNS]
        
        # Check for any None values in input_features
        for i, feature in enumerate(input_features):
            if feature is None:
                return f"Missing input for feature: {FEATURE_COLUMNS[i]}"
            
        #Convert the nput_features into integers
        input_features_updated = to_int(input_features)

        # Convert the features into an array for prediction
        input_array = np.array(input_features_updated).reshape(1, -1)
        
        # Debug: print the input array shape and content
        print(f"Input array shape: {input_array.shape}")
        print(f"Input array features: {input_features_updated}")
        print(f"Input array content: {input_array}")

        # Make prediction
        prediction = model.predict(input_array)
        result = 'Patient is suffering from liver cirrhosis' if prediction[0] == 1 else 'Patient is not suffering from liver cirrhosis'
        
        # Render the submit.html template with the prediction result
        return render_template('submit.html', result=result)
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
