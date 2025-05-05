import React from 'react';
import { useEffect, useState } from 'react';
import { fetchMeals, createMeal } from './api';

export default function App() {
    const [meals, setMeals] = useState([]);
    const [name, setName] = useState('');

    useEffect(() => {
        fetchMeals().then((res) => setMeals(res.data));
    }, []);

    const handleAdd = async () => {
        const newMeal = await createMeal({ name, description: '' });
        setMeals((m) => [...m, newMeal.data]);
        setName('');
    };

    return (
        <div>
            <h1>Meals</h1>
            <ul>{meals.map((meal) => <li key={meal.id}>{meal.name}</li>)}</ul>
            <input
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="New meal"
            />
            <button onClick={handleAdd}>Add</button>
        </div>
    );
}
