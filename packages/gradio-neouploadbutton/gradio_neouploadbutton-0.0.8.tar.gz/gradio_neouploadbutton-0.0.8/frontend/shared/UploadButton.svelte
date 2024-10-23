<script lang="ts">
	import { tick, createEventDispatcher } from "svelte";
	import { BaseButton } from "@gradio/button";
	import { prepare_files, type FileData, type Client } from "@gradio/client";
    import { on } from "events";
    import exp from "constants";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let loading_message: string;
	export let label: string | null;
	export let oldLabel: string | null;
	export let interactive: boolean;
	export let oldInteractive: boolean;
	export let value: null | FileData | FileData[];
	export let file_count: string;
	export let file_types: string[] = [];
	export let root: string;
	export let size: "sm" | "lg" = "lg";
	export let icon: FileData | null = null;
	export let scale: number | null = 1;
	export let min_width: number | undefined = undefined;
	export let variant: "primary" | "secondary" | "stop" = "secondary";
	export let disabled = false;
	export let max_file_size: number | null = null;
	export let upload: Client["upload"];

	const dispatch = createEventDispatcher();

	let hidden_upload: HTMLInputElement;
	let accept_file_types: string | null;

	if (file_types == null) {
		accept_file_types = null;
	} else {
		file_types = file_types.map((x) => {
			if (x.startsWith(".")) {
				return x;
			}
			return x + "/*";
		});
		accept_file_types = file_types.join(", ");
	}

	function open_file_upload(): void {
		dispatch("click");
		hidden_upload.click();
	}

	async function load_files(files: FileList): Promise<void> {
		let _files: File[] = Array.from(files);

		if (!files.length) {
			return;
		}
		if (file_count === "single") {
			_files = [files[0]];
		}
		let all_file_data = await prepare_files(_files);
		await tick();

		try {
			all_file_data = (
				await upload(all_file_data, root, undefined, max_file_size ?? Infinity)
			)?.filter((x) => x !== null) as FileData[];
		} catch (e) {
			dispatch("error", (e as Error).message);
			return;
		}
		value = file_count === "single" ? all_file_data?.[0] : all_file_data;
		dispatch("change", value);
		dispatch("upload", value);
	}

	async function load_files_from_upload(e: Event): Promise<void> {
		const target = e.target as HTMLInputElement;
		if (!target.files) return;
		oldLabel = label;
		oldInteractive = interactive;
		label = typeof loading_message !== 'undefined' ? loading_message : oldLabel;
		interactive = typeof loading_message !== 'undefined' ? false : true;
		dispatch("labelChange", label);
		dispatch("interactiveChange", interactive);
		await load_files(target.files);
		label = oldLabel;
		interactive = oldInteractive;
		dispatch("labelChange", label);
		dispatch("interactiveChange", interactive);
	}

	function drag_over(e: DragEvent) {
		e.preventDefault();
		e.stopPropagation();
	}

	async function drop_files(e: DragEvent): Promise<void> {
		console.log("drop");
		const de = e as DragEvent;
		e.preventDefault();
		e.stopPropagation();
		const files = e.dataTransfer?.files;
		if (!files) return;
		oldLabel = label;
		oldInteractive = interactive;
		label = typeof loading_message !== 'undefined' ? loading_message : oldLabel;
		interactive = typeof loading_message !== 'undefined' ? false : true;
		dispatch("labelChange", label);
		dispatch("interactiveChange", interactive);
		await load_files(files);
		label = oldLabel;
		interactive = oldInteractive
		dispatch("labelChange", label);
		dispatch("interactiveChange", interactive);
		
	}

	function clear_input_value(e: Event): void {
		const target = e.target as HTMLInputElement;
		if (target.value) target.value = "";
	}
</script>

<input
	class="hide"
	accept={accept_file_types}
	type="file"
	bind:this={hidden_upload}
	on:change={load_files_from_upload}
	on:click={clear_input_value}
	multiple={file_count === "multiple" || undefined}
	webkitdirectory={file_count === "directory" || undefined}
	mozdirectory={file_count === "directory" || undefined}
	data-testid="{label}-upload-button"
/>

<BaseButton
	{size}
	{variant}
	{elem_id}
	{elem_classes}
	{visible}
	on:click={open_file_upload}
	{scale}
	{min_width}
	{disabled}
>
	<div role="presentation" class="dragdrop" on:dragover={drag_over} on:drop={drop_files}>
	{#if icon}
		<img class="button-icon" src={icon.url} alt={`${value} icon`} />
	{/if}
	<slot> {label} </slot>
	</div>
</BaseButton>

<style>
	.hide {
		display: none;
	}
	.dragdrop {
		width: 100%;
		height: 100%;
	}
	.button-icon {
		width: var(--text-xl);
		height: var(--text-xl);
		margin-right: var(--spacing-xl);
	}
</style>
