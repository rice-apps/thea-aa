<script>
	// ========================================
	// +layout.svelte
	// Shared layout wrapper for all routes.
	// It gets applied to global styles and adds a Navbar.
	// ========================================
	import '../app.css'
	import Navbar from '$lib/components/Navbar.svelte'
</script>

<div class="w-screen">
	<Navbar />
</div>

<!-- Slot for child route content -->
<slot></slot>
