<!-- <script lang="ts">
	import L from 'leaflet'
	import { getContext, onDestroy } from 'svelte'
	let classNames = undefined
	export { classNames as class }
	class Control extends L.Control {
		constructor(el, position) {
			super({ position })
			this.el = el
		}
		onAdd() {
			return this.el
		}
		onRemove() {}
	}

    interface ControlProps {
        position: 'topleft' | 'topright' | 'bottomleft' | 'bottomright'
    }

	/** position: 'topleft' | 'topright' | 'bottomleft' | 'bottomright' */
	export let position

	/** The control instance created by this component */
	export let control = undefined
	const map = getContext('map')()

	function createControl(container) {
		control = new Control(container, position).addTo(map)
		return {
			destroy() {
				control.remove()
				control = undefined
			}
		}
	}
</script>

<div style="display:hidden">
	<div use:createControl class={classNames}>
		{#if control}
			<slot {control} />
		{/if}
	</div>
</div> -->
