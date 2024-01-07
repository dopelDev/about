<template>
	<div>
		<div class="title">WORK</div>
		<div v-if="showAlert" class="alert" :class="{'alert-success': isSuccess, 'alert-danger': !isSuccess}">
			{{ message }}
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
							this.triggerAlert(true, 'Formulario enviado con éxito!');
						} else {
							this.triggerAlert(false, 'Error al enviar el formulario.');
						}
					})
					.catch(() => {
						this.triggerAlert(false, 'Error al enviar el formulario.');
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

