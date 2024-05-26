<script>
    import NodeContent from '$lib/NodeContent.svelte';
    import Attachments from '$lib/Attachments.svelte';
    import Questions from '$lib/Questions.svelte'
    import Options from '$lib/Options.svelte';
    import Modal from '$lib/Modal.svelte';
    import Tabs from '$lib/Tabs.svelte';
    import SavedNow from '$lib/SavedNow.svelte';
    const tabs_components = [
        {name: 'Content', component: NodeContent, fa: ['regular', 'file-lines']},
        {name: 'Attachments', component: Attachments, fa: ['solid', 'paperclip']},
        {name: 'Questions', component: Questions, fa: ['regular', 'circle-question']},
        {name: 'Options', component: Options, fa: ['solid', 'gears']}
    ];
</script>

<Modal>
    <div>
        <Tabs components={tabs_components} />
    </div>
    <div slot="footer">
        <SavedNow />
    </div>
</Modal>