document.getElementById('scroll-to-form').addEventListener('click', scroll_to_form);
function scroll_to_form() {
	const div = document.getElementById('form');
	div.scrollIntoView({behavior: 'smooth'});
}
