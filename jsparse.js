fetch('2024-09-03.json')
.then(response => response.json())
.then(data => {

    const first_row = data.Stats['Cash Buying'][0];
    const h1 = document.createElement('h1');
    h1.appendChild(first_row.Currency);
    h1.appendChild(first_row.Highest);
    h1.appendChild(first_row.Lowest);
    
    // document.write(data.Stats['Cash Buying'].Highest);
})
.catch(error => console.error('Error fetching the JSON file:', error));


// document.write("Yes")