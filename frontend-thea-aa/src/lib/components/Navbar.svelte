<script lang="ts">
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu'
	import Bell from 'lucide-svelte/icons/bell'
	import logo from '$lib/assets/logo_without_text.png'
</script>

<nav class="flex items-center justify-between px-6 py-3">
	<!-- logo (no extra horizontal padding, just the outer px‑6) -->
	<a href="/" class="flex items-center">
		<img src={logo} alt="app logo" class="h-16 w-auto select-none" />
	</a>

	<!-- right‑hand links / actions -->
	<div class="flex items-center gap-6">
		<a href="/about" class="p-2 text-sm font-medium hover:underline"> About </a>

		<DropdownMenu.Root>
			<!-- give the trigger the same p‑2 so its hit‑box matches the About link -->
			<DropdownMenu.Trigger class="p-2">
				<Bell class="h-6 w-6" />
			</DropdownMenu.Trigger>

			<DropdownMenu.Content>
				<DropdownMenu.Group>
					<DropdownMenu.Label>Placeholder Dropdown</DropdownMenu.Label>
					<DropdownMenu.Separator />
					<DropdownMenu.Item>Dropdown item below separator</DropdownMenu.Item>
				</DropdownMenu.Group>
			</DropdownMenu.Content>
		</DropdownMenu.Root>
	</div>
</nav>
