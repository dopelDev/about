<template>
	<div>
		<div v-if="showAlert" class="title alert" :class="{'alert-success': isSuccess, 'alert-danger': !isSuccess}">
			<p class="has-text-centered">{{ message }}</p>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				showAlert: false,
				isSuccess: false,
				message: '',
				csrfToken: '',
			};
		},
		mounted() {
			const csrfToken = document.querySelector('meta[name="csrf-token"]');
			if (csrfToken) {
				this.csrfToken = csrfToken.content;
				console.log(csrfToken)
			}
			const form = document.getElementById('form');
			if (form) {
				form.addEventListener('submit', this.handleSubmit);
			}
		},
		methods: {
			handleSubmit(e) {
				e.preventDefault();

				const formData = new FormData(e.target);
				formData.append('csrf_token', this.csrfToken);

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
						if (data.csrf_token) {
							this.csrfToken = data.csrf_token;
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
			const form = document.querySelector('form');
			if (form) {
				form.removeEventListener('submit', this.handleSubmit);
			}
		}
	};
</script>

<style scoped>
.alert {
    padding: 10px;
    border-radius: 5px;
    margin: 10px 0;
}

.alert-success {
    background-color: #d4edda;
    border-color: #c3e6cb;
    color: #155724;
}

.alert-danger {
    background-color: #f8d7da;
    border-color: #f5c6cb;
    color: #721c24;
}

</style>
