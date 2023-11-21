const getIngredientsAutocomplete = () => document.getElementById("ingredients-autocomplete");
const getIngredientInput = () => document.getElementById("ingredient");
const getIngredientAmount = () => document.getElementById("ingredient-amount");
const getIngredientsList = () => document.getElementById("ingredients-list");

const handleIngredientClick = (item) => {
  const name = item.dataset.name;

  const ingredientInput = getIngredientInput();
  const ingredientAmount = getIngredientAmount();

  ingredientInput.value = name;
  ingredientAmount.focus();

  const ingredientsAutocomplete = getIngredientsAutocomplete();
  ingredientsAutocomplete.innerHTML = "";
};

const clearIngredientInputs = () => {
  const ingredientInput = getIngredientInput();
  const ingredientAmount = getIngredientAmount();
  const ingredientsAutocomplete = getIngredientsAutocomplete();

  ingredientInput.value = "";
  ingredientAmount.value = "";
  ingredientsAutocomplete.innerHTML = "";
  ingredientInput.focus();
}

const getIngredients = () => {
  const ingredientsAutocomplete = getIngredientsList();
  const ingredients = Array.from(ingredientsAutocomplete.querySelectorAll("li"));

  return ingredients.map((ingredient) => {
    const name = ingredient.dataset.name;
    const amount = ingredient.dataset.amount;

    return { name, amount };
  });
}
