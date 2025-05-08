import axios from 'axios';

const api = axios.create({
    baseURL: '/api', // or 'http://localhost:8000/api' if not proxying
    withCredentials: true,
});

export const fetchMeals = () => api.get('/meals');
export const createMeal = (meal) => api.post('/meals', meal);

export const fetchIngredients = () => api.get('/ingredients');
