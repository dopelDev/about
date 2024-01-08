<template>
	<div class="block">
		<div @click="open = true">home</div>
		<Teleport to="body">
		<div v-if="open" class="modal">
			<div class="message is-info">
				<div class="message-header">
					<h1 class="has-text-centered">申し訳ございません</h1>
				</div>
				<div @click="open = false" class="message-body">
					<p>This page is in development</p>
				</div>
			</div>
		</div>
		</Teleport>
	</div>
</template>

<script>
	export default {
		name: 'Home',
		data() {
			return {
				open: false
			}
		},
	}
</script>

<style scoped>
.modal {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	z-index: 999;
	display: flex;
	justify-content: center;
	align-items: center;
}
.close-button {
	background-color: red;
}
</style>

