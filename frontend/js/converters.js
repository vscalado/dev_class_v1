// Funções de conversão
async function convertLength() {
    const input = document.getElementById('lengthInput').value;
    const fromUnit = document.getElementById('lengthFromUnit').value;
    const toUnit = document.getElementById('lengthToUnit').value;
    const resultElement = document.getElementById('lengthResult');

    if (!input) {
        resultElement.textContent = 'Digite um valor para converter';
        return;
    }

    try {
        const result = await apiCall('converters/length', 'POST', {
            value: parseFloat(input),
            from_unit: fromUnit,
            to_unit: toUnit
        });

        resultElement.textContent = `${input} ${fromUnit} = ${result.result} ${toUnit}`;
    } catch (error) {
        resultElement.textContent = 'Erro ao converter valor';
        console.error('Erro na conversão:', error);
    }
}

async function convertVolume() {
    const input = document.getElementById('volumeInput').value;
    const fromUnit = document.getElementById('volumeFromUnit').value;
    const toUnit = document.getElementById('volumeToUnit').value;
    const resultElement = document.getElementById('volumeResult');

    if (!input) {
        resultElement.textContent = 'Digite um valor para converter';
        return;
    }

    try {
        const result = await apiCall('converters/volume', 'POST', {
            value: parseFloat(input),
            from_unit: fromUnit,
            to_unit: toUnit
        });

        resultElement.textContent = `${input} ${fromUnit} = ${result.result} ${toUnit}`;
    } catch (error) {
        resultElement.textContent = 'Erro ao converter valor';
        console.error('Erro na conversão:', error);
    }
}