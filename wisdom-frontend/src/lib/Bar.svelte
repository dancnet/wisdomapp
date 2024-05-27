<script>
    import { node_selected, show_modal, mindmaps_data, selected_mindmap, nodes_data } from '$lib/store';
    const view = () => {show_modal.set('view_node')};
    const edit = () => show_modal.set('edit_node');
    const random = () => {show_modal.set('random_node')};
    const quiz = () => {show_modal.set('quiz')};
    const search = () => {show_modal.set('search')};
    const manage_mindmaps = () => {show_modal.set('manage_mindmaps')};
    mindmaps_data.reload();
    const set_mindmap = id => {
        selected_mindmap.set(id);
        nodes_data.reload();
    }
</script>

<div class="w3-bar w3-pink">
    {#if $node_selected}
    <button class="w3-bar-item w3-btn" on:click={view}><i class="fa-regular fa-file-lines"></i> View</button>
    <button on:click={edit} class="w3-bar-item w3-btn"><i class="fa-regular fa-pen-to-square"></i> Edit</button>
    <button class="w3-bar-item w3-btn" on:click={random}><i class="fa-solid fa-dice"></i> Random</button>
    <button class="w3-bar-item w3-btn" on:click={quiz}><i class="fa-regular fa-lightbulb"></i> Quiz</button>
    {:else}
    <div class="w3-dropdown-hover">
        <button class="w3-button w3-pink w3-hover-pink"><b>Wisdom App</b> <i class="fa fa-caret-down"></i></button>
        <div class="w3-dropdown-content w3-bar-block w3-card-4">
            {#each $mindmaps_data as mindmap (mindmap.id)}
            <button on:click={() => set_mindmap(mindmap.id)} class="w3-bar-item w3-button" class:w3-pink={mindmap.id === $selected_mindmap}><i class="fa-solid fa-book-open-reader"></i> {mindmap.name}</button>
            {/each}
            <button on:click={manage_mindmaps} class="w3-bar-item w3-button"><i class="fa-solid fa-cogs"></i> Manage Mind Maps</button>
            <button on:click={search} class="w3-bar-item w3-button"><i class="fa-solid fa-magnifying-glass"></i> Search</button>
        </div>
    </div>
    {/if}
</div>

<style>
    .w3-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    .w3-dropdown-hover {
        z-index: 3;
    }
    .w3-dropdown-content {
        max-height: calc(100vh - 44px);
        overflow-y: auto;
    }
    .w3-dropdown-content::-webkit-scrollbar {
        display: none;
    }
</style>