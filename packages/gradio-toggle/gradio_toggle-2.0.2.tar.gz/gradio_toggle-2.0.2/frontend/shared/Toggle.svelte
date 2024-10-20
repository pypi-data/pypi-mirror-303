<script lang="ts">
	import type { SelectData } from "@gradio/utils";
	import { createEventDispatcher } from "svelte";

	export let value = false;
	export let label = "Toggle";
	export let interactive: boolean;

	const dispatch = createEventDispatcher<{
		change: boolean;
		select: SelectData;
	}>();

	$: value, dispatch("change", value);
	$: disabled = !interactive;

	async function handle_enter(
		event: KeyboardEvent & { currentTarget: EventTarget & HTMLInputElement }
	): Promise<void> {
		if (event.key === "Enter") {
			value = !value;
			dispatch("select", {
				index: 0,
				value: event.currentTarget.checked,
				selected: event.currentTarget.checked
			});
		}
	}

	async function handle_input(
		event: Event & { currentTarget: EventTarget & HTMLInputElement }
	): Promise<void> {
		value = event.currentTarget.checked;
		dispatch("select", {
			index: 0,
			value: event.currentTarget.checked,
			selected: event.currentTarget.checked
		});
	}
</script>

<label class:disabled>
	<div class="toggle-wrapper">
		<input
			bind:checked={value}
			on:keydown={handle_enter}
			on:input={handle_input}
			{disabled}
			type="checkbox"
			class="toggle-checkbox"
			name="test"
			data-testid="toggle-switch"
		/>
		<span class="toggle-slider"></span>
	</div>
	<span>{label}</span>
</label>

<style>
	:root {
	  --toggle-width: 40px;
	  --toggle-height: 20px;
	  --toggle-slider-color: #ccc;
	  --toggle-slider-color-selected: #4caf50;
	  --toggle-knob-color: white;
	  --toggle-border-radius: 30px;
	  --toggle-transition: 0.4s;
	}

	.toggle-wrapper {
		position: relative;
		width: var(--toggle-width);
		height: var(--toggle-height);
	}

	.toggle-checkbox {
		opacity: 0;
		width: 0;
		height: 0;
	}

	.toggle-slider {
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background-color: var(--toggle-slider-color);
		border-radius: var(--toggle-border-radius);
		transition: var(--toggle-transition);
	}

	.toggle-slider:before {
		position: absolute;
		content: "";
		height: var(--toggle-height);
		width: var(--toggle-height);
		left: 0px;
		bottom: 0;
		background-color: var(--toggle-knob-color);
		border-radius: 50%;
		transition: var(--toggle-transition);
	}

	.toggle-checkbox:checked + .toggle-slider {
		background-color: var(--toggle-slider-color-selected);
	}

	.toggle-checkbox:checked + .toggle-slider:before {
		transform: translateX(var(--toggle-width));
	}

	label {
		display: flex;
		align-items: center;
		cursor: pointer;
		color: var(--toggle-label-text-color);
		font-size: 14px;
	}

	input[disabled],
	.disabled {
		cursor: not-allowed;
	}

	input:hover {
		cursor: pointer;
	}
</style>
