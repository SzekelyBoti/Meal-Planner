import { useEffect, useState } from 'react';
import { fetchMeals, createMeal, fetchIngredients } from './api';

export default function App() {
    const [meals, setMeals] = useState([]);
    const [name, setName] = useState('');
    const [instructions, setInstructions] = useState('');
    const [ingredients, setIngredients] = useState([]);
    const [selectedIds, setSelectedIds] = useState([]);

    useEffect(() => {
        fetchMeals().then(res => setMeals(res.data));
        fetchIngredients().then(res => setIngredients(res.data));
    }, []);

    const handleAdd = async () => {
        const payload = {
            name,
            description: '',
            calories: null,
            instructions,
            ingredient_ids: selectedIds
        };
        const newMeal = await createMeal(payload);
        setMeals(m => [...m, newMeal.data]);
        setName('');
        setInstructions('');
        setSelectedIds([]);
    };

    const toggleIngredient = (id) => {
        setSelectedIds(ids =>
            ids.includes(id) ? ids.filter(x => x !== id) : [...ids, id]
        );
    };

    return (
        <div style={{ padding: 20 }}>
            <h1>Meals</h1>
            <ul>
                {meals.map(m => (
                    <li key={m.id}>
                        <strong>{m.name}</strong>
                        <p>{m.instructions}</p>
                        <p>
                            Ingredients: {m.ingredients.map(i => i.name).join(', ')}
                        </p>
                    </li>
                ))}
            </ul>

            <h2>Add a Meal</h2>
            <input
                value={name}
                onChange={e => setName(e.target.value)}
                placeholder="Meal name"
            />
            <br/>

            <textarea
                value={instructions}
                onChange={e => setInstructions(e.target.value)}
                placeholder="Preparation instructions"
                rows={4}
                cols={50}
            />
            <br/>

            <fieldset>
                <legend>Select Ingredients</legend>
                {ingredients.map(i => (
                    <label key={i.id} style={{ display: 'block' }}>
                        <input
                            type="checkbox"
                            checked={selectedIds.includes(i.id)}
                            onChange={() => toggleIngredient(i.id)}
                        />
                        {i.name}
                    </label>
                ))}
            </fieldset>

            <button onClick={handleAdd}>Add Meal</button>
        </div>
    );
}
