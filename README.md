# Student Performance Indicator - End-to-End Machine Learning Project

This project predicts the math scores of students based on various features such as gender, ethnicity, parental level of education, lunch type, test preparation course, and their writing and reading scores. It aims to build robust project pipelines and more by integrating machine learning with a simple web interface. The application predicts math scores based on student data and uses a machine learning model trained on real-world datasets.

## Key Features
- **Machine Learning Pipeline**: Build robust pipelines for ML tasks (data preprocessing, model training, and evaluation).
- **Web Interface**: User-friendly frontend to collect data and display predictions.
- **End-to-End Workflow**: From data input to model prediction, the entire system works as an integrated solution.
- **Deployment Ready**: Flask-based application that can be deployed as a web service.

## Screenshots
Below are some screenshots of the frontend of the application:

### Screenshot 1
![Screenshot 2025-04-27 141540](https://github.com/user-attachments/assets/39a72c81-5be6-493b-85ca-ef00291d6ee0)

### Screenshot 2
![Screenshot 2025-04-27 141603](https://github.com/user-attachments/assets/5eedfdde-ff2a-443d-8d54-1f5895d3352c)

## Technologies Used
- **Python**
- **Flask**
- **Pandas & NumPy**
- **Machine Learning Pipelines**
- **Bootstrap 5 (for UI)**
- **Jupyter Notebook**
- **GitHub**

## Installation

Follow the steps below to run this project locally:

### Steps to Install

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/student-performance-indicator.git
   cd student-performance-indicator

2. **Create and activate the Conda environment**:

    Create a new Conda environment with the necessary dependencies. Make sure you have conda installed. If not, you can download and install it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

    ```bash
    conda env create -f environment.yml
    # Create a Conda environment
    conda create --name student-env python=3.9 -y
    conda activate student-env

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the Flask app**:
   ```bash
   python app.py

5. **Navigate to localhost**:
   Once the Flask app is running, follow these steps:

   1. Open your web browser.
   2. Navigate to http://127.0.0.1:5000/ or http://localhost:5000/.
   3. Use the application to predict math scores based on student attributes!

#### Contributing
Feel free to fork this project, improve it, and submit pull requests!

#### License
This project is MIT Licensed. See the LICENSE file for more details.
