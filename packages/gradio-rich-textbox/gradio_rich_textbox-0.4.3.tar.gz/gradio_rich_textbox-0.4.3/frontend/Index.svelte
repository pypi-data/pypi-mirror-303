<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { BlockTitle } from "@gradio/atoms";
	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { tick } from "svelte";
	import {bbcodeParser} from "./utils";

	export let gradio: Gradio<{
		change: never;
		submit: never;
		input: never;
	}>;
	export let label = "Textbox";
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value = "";
	export let show_label: boolean;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus | undefined = undefined;
	export let value_is_output = false;
	export let interactive: boolean;
	export let rtl = false;

	let el: HTMLDivElement;
	const container = true;

	function handle_change(): void {
		gradio.dispatch("change");
		if (!value_is_output) {
			gradio.dispatch("input");
		}
	}

	async function handle_keypress(e: KeyboardEvent): Promise<void> {
		await tick();
		if (e.key === "Enter") {
			e.preventDefault();
			gradio.dispatch("submit");
		}
	}

	let is_being_edited = false;
	let _value = "";
	$: {
		_value = bbcodeParser.bbcodeToHtml(value || "");
	}

	async function handle_blur(): Promise<void> {
		await tick();
		if (!interactive) {
			return;
		}
		value = el.innerText
		is_being_edited = false;
		el.innerText = "";
	}

	async function handle_focus(): Promise<void> {
		await tick();
		if (!interactive) {
			el.blur();
			return;
		}
		is_being_edited = true;
	}

	$: if (value === null) value = "";

	// When the value changes, dispatch the change event via handle_change()
	// See the docs for an explanation: https://svelte.dev/docs/svelte-components#script-3-$-marks-a-statement-as-reactive
	$: value, handle_change();
</script>

<Block
	{visible}
	{elem_id}
	{elem_classes}
	{scale}
	{min_width}
	allow_overflow={false}
	padding={true}
>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
		/>
	{/if}

	<label class:container>
		<BlockTitle {show_label} info={undefined}>{label}</BlockTitle>

		<div
			data-testid="textbox"
			contenteditable=true
			class="text-container"
			class:disabled={!interactive}
			bind:this={el}
			on:keypress={handle_keypress}
			on:blur={handle_blur}
			on:focus={handle_focus}
			role="textbox" 
			tabindex="0"
			dir={rtl ? "rtl" : "ltr"}
		>
		{#if is_being_edited}
			{value}
		{:else}
			{@html _value}
		{/if}
		</div>
	</label>
</Block>

<style>
	label {
		display: block;
		width: 100%;
	}
	.container > div.text-container
	{
		border: var(--input-border-width) solid var(--input-border-color);
		border-radius: var(--input-radius);
	}

	div.text-container {
		display: block;
		position: relative;
		outline: none !important;
		box-shadow: var(--input-shadow);
		background: var(--input-background-fill);
		padding: var(--input-padding);
		width: 100%;
		color: var(--body-text-color);
		font-weight: var(--input-text-weight);
		font-size: var(--input-text-size);
		line-height: var(--line-sm);
		border: none;
	}
	div.text-container:disabled
	{
		-webkit-text-fill-color: var(--body-text-color);
		-webkit-opacity: 1;
		opacity: 1;
	}

	div.text-container:focus {
		box-shadow: var(--input-shadow-focus);
		border-color: var(--input-border-color-focus);
	}
</style>
