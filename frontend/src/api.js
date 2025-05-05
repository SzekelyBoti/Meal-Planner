import axios from 'axios';
export const fetchMeals = () => axios.get('/api/meals');
export const createMeal = (meal) => axios.post('/api/meals', meal);
