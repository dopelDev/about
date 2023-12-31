<template>
	<section class="container">
		<div class="columns color4">
			<div class="column is-2">
				<figure class="image is-128x128">
					<img class="is-rounded" src="" alt="Profile picture of Pedro 'dopeldev' Gonzales">
				</figure>
			</div>
			<div class="column auto">
				<h1 class="title is-2">Pedro GG "Dopeldev" Gonzales</h1>
				<p class="subtitle is-4">Software Developer</p>
			</div>
		</div>
	</section>
</template>

<script>
	export default {
		name: 'Header',
		data() {
			return {
				title: 'Header'
			}
		},
		props: {
			img: String,
		},
	}
</script>

<style scoped>

</style>

