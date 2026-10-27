const form = document.getElementById('port-checker-form');
const host = document.getElementById('host');
const port = document.getElementById('port');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const hostValue = host.value.trim();
    if (!hostValue) {
        result.textContent = 'Please enter a host';
        return;
    }
    const portValue = Number(port.value.trim());
    if (!port.value.trim() || !Number.isInteger(portValue) ||
        portValue < 1 || portValue > 65535) {
        result.textContent = 'Please enter a valid port (1-65535)';
        return;
    }
    result.textContent = 'Checking...';
    await sendData(hostValue, portValue);
});

async function sendData(hostValue, portValue) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                host: hostValue,
                port: portValue
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        result.innerHTML = `
    <h2>Port Check Result</h2>
    <p><strong>Hostname:</strong> ${data.host}</p>
    <p><strong>Port:</strong> ${data.port}</p>
    <p><strong>Status:</strong> ${data.status}</p>
    <p><strong>Message:</strong> ${data.message}</p>
`;
    } catch (error) {
        result.textContent = 'Unable to connect to the server.';
        console.error(error);
    }
}