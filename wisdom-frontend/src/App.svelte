<script>
    import MindMapWrapper from '$lib/MindMapWrapper.svelte';
    import Bar from '$lib/Bar.svelte';
    import EditNode from '$lib/EditNode.svelte';
    import ManageMindmaps from '$lib/ManageMindmaps.svelte';
    import RandomNode from '$lib/RandomNode.svelte';
    import Quiz from '$lib/Quiz.svelte';
    import Search from '$lib/Search.svelte';
    import { show_modal } from '$lib/store';
</script>

<main class="container">
    <div>
        <Bar />
    </div>
    <div class="content w3-light-grey">
        <MindMapWrapper />
    </div>
</main>

{#if $show_modal === 'edit_node'}
<EditNode />
{:else if $show_modal === 'manage_mindmaps'}
<ManageMindmaps />
{:else if $show_modal === 'random_node'}
<RandomNode />
{:else if $show_modal === 'quiz'}
<Quiz />
{:else if $show_modal === 'search'}
<Search />
{/if}

<style>
    .container {
        display: flex;
        flex-direction: column;
        height: 100vh;
    }
    .content {
        flex-grow: 1;
    }
</style>
