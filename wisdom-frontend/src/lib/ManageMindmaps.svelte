<script>
    import Modal from "$lib/Modal.svelte";
    import SavedNow from "$lib/SavedNow.svelte";
    import { mindmaps_data, nodes_data, selected_mindmap } from '$lib/store';
    import { query } from "./api";

    const remove = m => {
        if (prompt(`To delete the mindmap, type it's name: ${m.name}`) === m.name) {
            if ($selected_mindmap === m.id) {
                selected_mindmap.set(1);
                nodes_data.reload();
            }
            query(`/mindmaps/${m.id}`, 'DELETE');
            mindmaps_data.reload();
        }
    }
    const save = (id, name) => {
        query(`/mindmaps/${id}`, 'PUT', {name});
        mindmaps_data.reload();
    }
    const add = () => {
        query('/mindmaps/', 'POST', {name: 'New Mindmap'});
        mindmaps_data.reload();
    }
    
</script>

<Modal>
    <div class="w3-container w3-section">
        <ul class="w3-ul w3-card-2">
            {#each $mindmaps_data as mindmap (mindmap.id)}
            <li class="w3-display-container">
                <input value={mindmap.name} on:change={e => save(mindmap.id, e.target.value)} type="text" class="w3-input">
                <button on:click={() => remove(mindmap)} class="w3-button w3-transparent w3-display-right" disabled={mindmap.id === 1}>
                    <i class="fa-regular fa-trash-can"></i>
                </button>
            </li>
            {/each}
            <li class="w3-display-container right">
                <button class="w3-button" on:click={add}><i class="fa-regular fa-square-plus"></i></button>
            </li>
        </ul>
    </div>

    <div slot="footer">
        <SavedNow />
    </div>
</Modal>

<style>
    li {
        padding: 0;
    }
    .right {
        text-align: right;
    }
</style>