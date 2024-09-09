// Fetch JSON data and display it in tables
fetch('2024-09-09.json')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('tables');

        // Function to create a table from an array of objects
        function createTable(title, dataArray) {
            if (!dataArray || dataArray.length === 0) return; // Skip empty sections

            const table = document.createElement('table');
            const thead = document.createElement('thead');
            const tbody = document.createElement('tbody');

            // Create table header
            const headerRow = document.createElement('tr');
            Object.keys(dataArray[0]).forEach(key => {
                const th = document.createElement('th');
                th.textContent = key;
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);

            // Create table body
            dataArray.forEach(item => {
                const row = document.createElement('tr');
                Object.values(item).forEach(value => {
                    const td = document.createElement('td');
                    td.textContent = value !== null ? value : 'N/A'; // Handle null values
                    row.appendChild(td);
                });
                tbody.appendChild(row);
            });

            // Add title and append the table
            const titleElement = document.createElement('h2');
            titleElement.textContent = title;
            table.appendChild(thead);
            table.appendChild(tbody);
            container.appendChild(titleElement);
            container.appendChild(table);
        }

        // Function to handle individual JSON objects, not arrays
        function createTableFromObject(title, obj) {
            if (!obj || Object.keys(obj).length === 0) return; // Skip empty sections

            const table = document.createElement('table');
            const tbody = document.createElement('tbody');

            // Add table rows for each key-value pair in the object
            for (const key in obj) {
                const row = document.createElement('tr');

                const keyCell = document.createElement('td');
                keyCell.textContent = key;
                row.appendChild(keyCell);

                const valueCell = document.createElement('td');
                valueCell.textContent = obj[key] !== null ? obj[key] : 'N/A'; // Handle null values
                row.appendChild(valueCell);

                tbody.appendChild(row);
            }

            // Add title and append the table
            const titleElement = document.createElement('h2');
            titleElement.textContent = title;
            table.appendChild(tbody);
            container.appendChild(titleElement);
            container.appendChild(table);
        }
        
        // Process Black market data
        createTableFromObject('Black Market', data.Black);
        const black_line = document.createElement('hr')
        container.appendChild(black_line)
        // Process DateTime info
        const date_time_text = document.createElement('h2')
        date_time_text.textContent = "This applies for the data shown from here on"
        container.appendChild(date_time_text)
        createTableFromObject('DateTime', data.DateTime);
        const date_line = document.createElement('hr')
        container.appendChild(date_line)

        // Process Stats data
        const StatsDiv = document.createElement('div');
        const StatsText = document.createElement('h2');
        StatsText.textContent = 'Statistics tables for Each Transaction Type';
        StatsDiv.appendChild(StatsText);
        container.appendChild(StatsDiv);
        
        createTable('Cash Buying', data.Stats['Cash Buying']);
        createTable('Cash Selling', data.Stats['Cash Selling']);
        createTable('Transactional Buying', data.Stats['Transactional Buying']);
        createTable('Transactional Selling', data.Stats['Transactional Selling']);
        
        // Line
        const StatsLine = document.createElement('hr');
        // StatsDiv.appendChild(StatsLine);
        container.appendChild(StatsLine);

        
        
        // Process Filtered data
        const FileterdDiv = document.createElement('div');
        const FileteredText = document.createElement('h2');
        FileteredText.textContent = "Filetered Tables for Each Transaction Type";
        FileterdDiv.appendChild(FileteredText);
        container.append(FileterdDiv)

        createTable('Cash Buying', data.Filtered['Cash Buying']);
        createTable('Cash Selling', data.Filtered['Cash Selling']);
        createTable('Transactional Buying', data.Filtered['Transactional Buying']);
        createTable('Transactional Selling', data.Filtered['Transactional Selling']);
        
        // Line to separate Filtered with Rates
        const FilteredLine = document.createElement('hr')
        container.appendChild(FilteredLine)

        // Process Rates data (for each bank)
        for (const bank in data.Rates) {
            createTable(`${bank} Rates`, data.Rates[bank]);
            const line = document.createElement('hr')
            container.appendChild(line)
        }

        // Process Aggregate data
        createTable('Aggregate Data', data.Aggregate);

    })
    .catch(error => {
        console.error('Error fetching JSON:', error);
    });
