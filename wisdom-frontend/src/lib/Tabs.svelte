<script>
    export let components;
    export let show = 0;
</script>

<div class="w3-bar w3-border-bottom container">
    {#each components as component, index (index)}
    <button class="w3-bar-item w3-button box" class:w3-light-grey={show === index} on:click={() => show=index}>
        <i class="fa-{component.fa[0]} fa-{component.fa[1]}"></i> {component.name}
    </button>
    {/each}
</div>

<svelte:component this={components[show].component} />

<style>
    .container {
        display: flex;
    }
    .box {
        flex: 1;
    }
</style>