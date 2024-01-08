<template>
	<div class="container is-desktop px-6">
		<div class="columns is-mobile">
			<div class="column">
				<div @click="forUrlDiscord" @mouseover="showMessage = true" @mouseleave="showMessage = false" class="div-mouseover title is-2 has-text-centered px-6"> 󰙯 </div>
				<div v-if="showMessage" class="div-mouseover title is-5 has-text-centered text-color4">Discord</div>
			</div>
			<div class="column">
				<div @click="forUrlGitHub" @mouseover="showMessage = true" @mouseleave="showMessage = false" class="div-mouseover title is-2 has-text-centered px-6">  </div>
				<div v-if="showMessage" class="div-mouseover title is-5 has-text-centered text-color4">Github</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'SocialMedia',
		data() {
			return {
				showMessage: false,
			}
		},
		methods: {
			forUrlDiscord() {
				window.open('https://discord.gg/FwxaFJ2h5H', '_blank');
			},
			forUrlGitHub() {
				window.open('https://github.com/dopelDev', '_blank');
			}
		},
	}
</script>

<style scoped>
.div-mouseover {
	color: #cacabc;
}
.div-message {
	color: #cacabc;
}
</style>

