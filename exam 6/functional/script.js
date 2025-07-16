const form = document.getElementById('form');
const confirmInfo = document.querySelector('.confirm-info');
const nameInput = form['name'];
const EmailInput = form['email'];
const destinationInput = form['destination'];
const travelersInput = form['travelers'];
const dateInput = form['date'];

const orders = JSON.parse(localStorage.getItem('orders')) || [];

const addOrder = (name, email, destination, travelers, date) => {
    orders.push({
        name,
        email,
        destination,
        travelers,
        date
    })

    localStorage.setItem('orders', JSON.stringify(orders));
    return {name, email, destination, travelers, date};
}

const createOrderElement = ({name, email, destination, travelers, date}) => {
    const orderDiv = document.createElement('div');
    const orderName = document.createElement('h2');
    const orderEmail = document.createElement('p');
    const orderDestination = document.createElement('p');
    const orderTravelers = document.createElement('p');
    const orderDate = document.createElement('p');

    orderName.innerText = `Order Name: ${name}`
    orderEmail.innerText = `Order Email: ${email}`
    orderDestination.innerText = `Destination: ${destination}`
    orderTravelers.innerText = `Number of travelers: ${travelers}`
    orderDate.innerText = `Travel Date: ${date}`

    orderDiv.append(orderName,orderEmail, orderDestination, orderTravelers, orderDate);
    confirmInfo.appendChild(orderDiv);
};

confirmInfo.style.display = orders.length === 0 ? 'none': 'flex';

orders.forEach(createOrderElement);

form.onsubmit = e => {
    e.preventDefault()

    const newOrder = addOrder(
        nameInput.value,
        EmailInput.value,
        destinationInput.value,
        travelersInput.value,
        dateInput.value
    )

    createOrderElement(newOrder)

        nameInput.value = ''
        EmailInput.value = ''
        destinationInput.value= ''
        travelersInput.value= ''
        dateInput.value= ''
}