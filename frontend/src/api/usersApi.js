export const getPersons = async () => {

    const url = 'http://localhost:8000/persons/';
    const config = {
        method: 'GET'
    };
    const response = await fetch(url,config);
    const responseData = await response.json();
    console.log(responseData);
};