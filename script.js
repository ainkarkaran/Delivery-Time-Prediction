const form = document.getElementById("predictionForm");
const result = document.getElementById("result");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const inputData = {
        Distance_km: parseFloat(document.getElementById("Distance_km").value),
        Weather: document.getElementById("Weather").value,
        Traffic_Level: document.getElementById("Traffic_Level").value,
        Time_of_Day: document.getElementById("Time_of_Day").value,
        Vehicle_Type: document.getElementById("Vehicle_Type").value,
        Preparation_Time_min: parseFloat(document.getElementById("Preparation_Time_min").value),
        Courier_Experience_yrs: parseFloat(document.getElementById("Courier_Experience_yrs").value)
    };

    result.textContent = "Predicting...";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(inputData)
        });

        const data = await response.json();

        if (data.success) {
            result.textContent = `${data.prediction} ${data.unit}`;
        } else {
            result.textContent = "Error: " + data.error;
        }

    } catch (error) {
        result.textContent = "Failed to connect to API";
        console.error(error);
    }
});
