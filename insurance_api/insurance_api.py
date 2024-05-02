from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - in a real scenario, this would come from a database
policies = [
    {
        "id": "123456",
        "name": "Life Insurance Policy",
        "provider": "ABC Insurance",
        "category": "Life",
        "coverage_details": "Provides coverage up to ₹1,000,000 in case of death.",
        "premium_amount": 5000,
        "terms_and_conditions": "Policy terms and conditions..."
    },
    {
        "id": "789012",
        "name": "Health Insurance Policy",
        "provider": "XYZ Insurance",
        "category": "Health",
        "coverage_details": "Covers hospitalization expenses up to ₹500,000/year.",
        "premium_amount": 8000,
        "terms_and_conditions": "Policy terms and conditions..."
    }
]

@app.route('/policies', methods=['GET'])
def get_policies():
    return jsonify(policies)

@app.route('/policies/<string:policy_id>', methods=['GET'])
def get_policy(policy_id):
    policy = next((p for p in policies if p['id'] == policy_id), None)
    if policy:
        return jsonify(policy)
    return jsonify({'message': 'Policy not found'}), 404

@app.route('/policies/search', methods=['GET'])
def search_policies():
    filtered_policies = policies
    
    # Filter by insurer
    insurer = request.args.get('insurer')
    if insurer:
        filtered_policies = [p for p in filtered_policies if p['provider'] == insurer]
    
    # Filter by category
    category = request.args.get('category')
    if category:
        filtered_policies = [p for p in filtered_policies if p['category'] == category]
    
    # Filter by premium range
    premium_min = request.args.get('premium_min')
    premium_max = request.args.get('premium_max')
    if premium_min and premium_max:
        filtered_policies = [p for p in filtered_policies if premium_min <= p['premium_amount'] <= premium_max]

    return jsonify(filtered_policies)

if __name__ == '__main__':
    app.run(debug=True)
