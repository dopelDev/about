<template>
	<section class="container">
		<div class="columns color4">
			<div class="column is-2 is-desktop">
				<div class="block">
					<figure class="image">
						<div class="image-profile">
							<span class="image-profile-text-backup">Profile picture of Pedro 'dopeldev' Gonzales</span>
						</div>
					</figure>
				</div>
			</div>
			<div class="column auto">
				<div class="block">
				<h1 class="title is-2"><span :class="{'faded': isFaded }">{{ names[currentIndex] }}</span> Gonzales</h1>
				<p class="subtitle is-4">Software Developer</p>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
	export default {
		name: 'Header',
		data() {
			return {
				title: 'Header',
				names: ['"Dopeldev"', 'Pedro'],
				currentIndex: 0,
				isFaded: false
			}
		},
		methods: {
			namesTransform() {
				this.isFaded = true;
				setTimeout(() => {
					this.currentIndex = (this.currentIndex + 1) % this.names.length;
					this.isFaded = false;
				}, 2000)
			}
		},
		mounted() {
			this.namesTransform();
			setInterval(this.namesTransform, 4000)
		},
		beforeDestroy() {
			clearInterval(this.namesTransform);
		}
	};
</script>

<style scoped>
h1 span {
	transition: all 2.0s ease-in-out;
	opacity: 1;
}
	.faded {
		opacity: 0.1;
	}
</style>

