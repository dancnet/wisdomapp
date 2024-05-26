<script>
    import MindMap from '$lib/MindMap.svelte';
    import { nodes_data } from '$lib/store';
    nodes_data.reload();
</script>

{#if $nodes_data.length > 0}
    <MindMap data={$nodes_data} on:refresh={nodes_data.reload} />
{/if}