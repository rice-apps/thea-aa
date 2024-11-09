<script lang="ts">
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu'
	import Bell from 'lucide-svelte/icons/bell'
</script>

<nav class="flex">
	<div class="grow">
		<a class="inline-block bg-gray-400 px-6 py-3" href="/">LOGO</a>
	</div>
	<div class="flex">
		<a href="/about inline-block">About</a>

		<DropdownMenu.Root>
			<DropdownMenu.Trigger><Bell /></DropdownMenu.Trigger>
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
