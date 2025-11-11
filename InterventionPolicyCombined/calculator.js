
const behavior_data =  {
    "Electricity (carbon price on power generation)": {
            "implemented": 2.5,
            "no tax ": 0.0
        },
        "Road fuels (carbon price on petrol & diesel)": {
            "implemented": 3.85,
            "no tax ": 0.0
        },
         "Aviation (carbon price on air travel)": {
            "implemented": 0.9,
            "no tax ": 0.0
        },
       "Food (carbon price on meat & dairy)": {
            "implemented": 8.3,
            "no tax ": 0.0
        },
        "Imported foods (carbon price on food miles)": {
            "implemented": 0.6,
            "no tax ": 0.0
        },
        "Waste (carbon price on landfill)": {
            "implemented": 0.2,
            "no tax ": 0.0
        }
};

function createBehaviorSelectors() {
    const behaviorsDiv = document.getElementById('behaviors');
    for (let behavior in behaviorData) {
        const container = document.createElement('div');
        container.className = 'behavior-container';
        
        const label = document.createElement('label');
        label.innerText = behavior;
        label.className = 'behavior-label';
        container.appendChild(label);
        
        const select = document.createElement('select');
        select.dataset.behavior = behavior;
        select.onchange = updateTotalFootprint;
        
        for (let level in behaviorData[behavior]) {
            const option = document.createElement('option');
            option.value = behaviorData[behavior][level];
            option.innerText = level;
            select.appendChild(option);
        }
        
        container.appendChild(select);
        behaviorsDiv.appendChild(container);
    }
}

// Function to update the total carbon footprint
function updateTotalFootprint() {
    let totalFootprint = 0.0;
    const selects = document.querySelectorAll('select');
    selects.forEach(select => {
        totalFootprint += parseFloat(select.value);
    });
    document.getElementById('total-footprint').innerText = totalFootprint.toFixed(1);
}

// Initialize the behavior selectors on page load
window.onload = createBehaviorSelectors;
