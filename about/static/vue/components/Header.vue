<template>
	<section class="container">
		<div class="columns color4">
			<div class="column is-2">
				<figure class="image">
					<div class="image-profile">
						<span class="image-profile-text-backup">Profile picture of Pedro 'dopeldev' Gonzales</span>
					</div>
				</figure>
			</div>
			<div class="column auto">
				<h1 class="title is-2">Pedro "Dopeldev" Gonzales</h1>
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

