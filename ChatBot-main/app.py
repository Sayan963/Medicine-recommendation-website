from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)
# app.run(host='127.0.0.1',port=5001)
@app.route("/")

def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)

def get_Chat_response(user_input):
    # Process user input related to medical queries
    # Here, we will assume that any user input containing the word "medicine" is considered a medical query
    # if "medicine" in user_input.lower():
        # Call the medicine recommendation function to get recommended medicines based on user input
        recommendation = get_Medicine_recommendation(user_input)
        return recommendation
    # else:
    #     # For non-medical queries, return a generic response
    #     return "I'm sorry, I can only provide recommendations for medical queries at the moment."

def get_Medicine_recommendation(user_input):
    # Dummy medicine recommendation logic for demonstration purposes
    recommendations = []
    
    # Process user input (e.g., symptoms or medical condition)
    # and generate medicine recommendations based on predefined rules or algorithms
    if "headache" in user_input.lower():
        recommendations.append("Aspirin dose 1 after meal")
        recommendations.append("Ibuprofen Dose 1 before sleep")
    if "fever" in user_input.lower():
        recommendations.append("Acetaminophen 3 days 1 tablet after meal")
        recommendations.append("Paracetamol dose 1 if fever")
    if "cough" in user_input.lower():
        recommendations.append("Dextromethorphan 7 days 3 times 5 ml")
        recommendations.append("Guaifenesin 3 days 1 tablet after meal")
    if "hospitals" in user_input.lower():
        recommendations.append("Apollo Gleneagles Hospital")
        recommendations.append("Ruby General Hospital")
    if "doctors" in user_input.lower():
        recommendations.append("Dr. Shubham Pal")
        recommendations.append("Dr. Saikat Samanta")
    if "emergency" in user_input.lower():
        recommendations.append("Ambulance Contact No 1 - 999")
        recommendations.append("Ambulance Contact No 2 - 990") 
    if "medicineshop" in user_input.lower():
        recommendations.append("Apollo Pharmacy contact -789")
        recommendations.append("Medicine hall - 567") 
    if "help" in user_input.lower():
        recommendations.append("Saikat Ghosh - 999999999")
        recommendations.append("Debayan Das - 9080808080")  
 

    # If no recommendations found, provide a generic response
    if not recommendations:
        return "I'm sorry, I couldn't find any specific medicine recommendations for your query. Please consult a healthcare professional for personalized advice."
    
    # Format and return the recommendations as a string
    return recommendations

if __name__ == '__main__':
 app.run(port=5001) 
