<script>
    import Editor from "$lib/Editor.svelte";
    import { node_selected } from '$lib/store';
    import { query } from '$lib/api';

    let text = null

    query(`/nodes/${$node_selected}`).then(result => { text = result.markdown });
    const save = text => {
        query(`/nodes/${$node_selected}`, 'PUT', {markdown: text});
    }
</script>

{#if text !== null}
<Editor on:change={e => save(e.detail)} value={text} />
{/if}