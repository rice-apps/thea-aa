<script>
	export let message = ''
	export let visible = false
	export const duration = 3000
</script>

<div class="toast {visible ? '' : 'hidden'}">{message}</div>

<style>
	.toast {
		position: fixed;
		top: 20px;
		left: 50%;
		transform: translateX(-50%);
		background: #333;
		color: white;
		padding: 10px 20px;
		border-radius: 5px;
		opacity: 1;
		transition: opacity 0.5s ease;
	}
	.hidden {
		opacity: 0;
	}
</style>
