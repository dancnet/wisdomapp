<script>
    export let color = null;
    import { createEventDispatcher } from 'svelte';
    import colors from '../colors_palette';
    const dispatch = createEventDispatcher();

    let color_name = '', selected_color = null, listcolor = '';
    if (color !== null) {
        color_name = (colors.find(i => i.background === color)).name
    }
    $: {
        selected_color = colors.find(i => i.name === color_name);
        if (selected_color) {
            dispatch('cs', selected_color);
            listcolor = 'w3-' + selected_color.name;
        } else {
            listcolor = '';
        }
    }
</script>

<div class="w3-round-large w3-border nooverlap">
    <input placeholder="Select a color." bind:value={color_name} class="w3-input {listcolor}" list="browsers">
    <datalist id="browsers">
        {#each colors as color}
        <option value={color.name}>
        {/each}
    </datalist>
    <div class="colors">
        {#each colors as color}
        <button class="w3-btn w3-small w3-{color.name}" on:click={() => color_name = color.name}>
            {#if selected_color && selected_color.name === color.name}x{/if}
        </button>
        {/each}
    </div>
</div>

<style>
.colors {
    display: flex;}
.colors button {
    flex: 1;
    padding: 0;
    height: 25px;
}
.nooverlap {
    overflow: hidden;
}
</style>