const getIngredientsAutocomplete = () => document.getElementById("ingredients-autocomplete");
const getIngredientInput = () => document.getElementById("ingredient");
const getIngredientAmount = () => document.getElementById("ingredient-amount");

const handleIngredientClick = (item) => {
  const name = item.dataset.name;

  const ingredientInput = getIngredientInput();
  const ingredientAmount = getIngredientAmount();

  ingredientInput.value = name;
  ingredientAmount.focus();

  ingredientsAutocomplete.innerHTML = "";
};

const clearIngredientInputs = () => {
  const ingredientInput = getIngredientInput();
  const ingredientAmount = getIngredientAmount();

  ingredientInput.value = "";
  ingredientAmount.value = "";
  ingredientInput.focus();
}
