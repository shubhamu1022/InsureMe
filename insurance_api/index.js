    fetch('http://127.0.0.1:5000/policies')
        .then(response => response.json())
        .then(data => {
            console.log('Fetched data:', data); // Log fetched data to console
            const policiesDiv = document.getElementById('policies');
            if (data.length === 0) {
                policiesDiv.innerHTML = '<p>No policies found.</p>';
            } else {
                // Loop through the data and create HTML elements to display policies
                data.forEach(policy => {
                    const policyElement = document.createElement('div');
                    policyElement.innerHTML = `
                        <h2>${policy.name}</h2>
                        <p><strong>Provider:</strong> ${policy.provider}</p>
                        <p><strong>Coverage Details:</strong> ${policy.coverage_details}</p>
                        <p><strong>Premium Amount:</strong> ${policy.premium_amount}</p>
                        <p><strong>Terms and Conditions:</strong> ${policy.terms_and_conditions}</p>
                        <hr>
                    `;
                    policiesDiv.appendChild(policyElement);
                });
            }
        })
        .catch(error => console.error('Error fetching data:', error));
