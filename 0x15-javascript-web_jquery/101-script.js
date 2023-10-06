$(document).ready(function () {
	// When the user clicks on DIV#add_item: a new element is added to the list
	$('div#add_item').on('click', () => {
		$('ul.my_list').append('<li>Item</li>');
	})

	// When the user clicks on DIV#remove_item: the last element is removed from the list
	$('div#remove_item').on('click', () => {
		$('ul.my_list li:last').remove();
	})

	// When the user clicks on DIV#clear_list: all elements of the list are removed
	$('div#clear_list').on('click', () => {
		$('ul.my_list').empty();
	})
});
