<script>
    import Modal from "$lib/Modal.svelte";
    import Editor from "$lib/Editor.svelte";
    import { query } from '$lib/api';
    import { selected_mindmap } from '$lib/store';
    let search_phrase = "";
    let content = null;
    let timeout;
    let nodes_current = [];
    let nodes_others = [];
    const trigger_search = () => {
        if (timeout) clearTimeout(timeout);
        timeout = setTimeout(search, 800);
    }
    const search = () => {
        content = null;
        query('/search', 'GET', {query: search_phrase}).then(response => {
            nodes_current = response.filter(node => node.mindmap_id === $selected_mindmap);
            nodes_others = response.filter(node => node.mindmap_id !== $selected_mindmap)
        });
    }
</script>

<Modal>
    <input bind:value={search_phrase} on:input={trigger_search} class="w3-input" type="text" placeholder="Starting searching...">
    {#each nodes_current as node (node.id)}
    <button on:click={() => content = node.markdown} class="w3-button w3-border w3-margin w3-round">{node.topic}</button>
    {/each}
    {#each nodes_others as node (node.id)}
    <button on:click={() => content = node.markdown} class="w3-button w3-border w3-margin w3-round w3-opacity">{node.topic}</button>
    {/each}
    {#if content !== null}
    {#key content}
    <Editor value={content} readonly={true} />
    {/key}
    {/if}
    <div slot="footer"></div>
</Modal>