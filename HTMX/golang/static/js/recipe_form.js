const ingredientsAutocomplete = document.getElementById("ingredients-autocomplete");

const ingredientInput = document.getElementById("ingredient");

const ingredientAmount = document.getElementById("ingredient-amount");

const handleIngredientClick = (item) => {
  const name = item.dataset.name;

  ingredientInput.value = name;
  ingredientAmount.focus();

  ingredientsAutocomplete.innerHTML = "";
};

const clearIngredientInputs = () => {
  ingredientInput.value = "";
  ingredientAmount.value = "";
  ingredientInput.focus();
}
