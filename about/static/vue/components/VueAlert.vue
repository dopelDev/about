<template>
	<div>
		<div v-if="showAlert" class="title alert" :class="{'alert-success': isSuccess, 'alert-danger': !isSuccess}">
			<p class="has-text-centered color4">{{ message }}</p>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				showAlert: false,
				isSuccess: false,
				message: ''
			};
		},
		mounted() {
			const form = document.getElementById('form');
			if (form) {
				form.addEventListener('submit', this.handleSubmit);
			}
		},
		methods: {
			handleSubmit(e) {
				e.preventDefault();
				const formData = new FormData(e.target);

				fetch(e.target.action, {
					method: 'POST',
					body: formData,
				})
					.then(response => response.json())
					.then(data => {
						if (data.success) {
							this.triggerAlert(true, 'Send message success!');
						} else {
							this.triggerAlert(false, 'Error : message fail!');
						}
					})
					.catch(() => {
						this.triggerAlert(false, 'Error : message fail!');
					});
			},
			triggerAlert(success, message) {
				this.showAlert = true;
				this.isSuccess = success;
				this.message = message;
				setTimeout(() => this.showAlert = false, 3000);
			}
		},
		beforeUnmount() {
			const form = document.getElementById('form');
			if (form) {
				form.removeEventListener('submit', this.handleSubmit);
			}
		}
	};
</script>

