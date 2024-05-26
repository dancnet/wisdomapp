<script>
    import Color from "$lib/Color.svelte";
    import { nodes_data, node_selected } from '$lib/store';
    import { query } from '$lib/api';

    const setcolor = event => {
        query(`/nodes/${$node_selected}`, 'PUT', {background_color: event.detail.background, text_color: event.detail.text}).then(result => { nodes_data.reload(); });
    };
    let color = $nodes_data.find(i => i.id === $node_selected)['background-color'];
</script>

<div class="w3-container">
    <div class="w3-section">
        <Color {color} on:cs={setcolor} />
    </div>
</div>

<style>
</style>