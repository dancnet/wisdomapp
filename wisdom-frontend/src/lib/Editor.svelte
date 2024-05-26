<script>
    export let value = ""
    export let readonly = false;

    import CodeMirror from 'codemirror';
    import 'codemirror/lib/codemirror.css';
    import 'codemirror/mode/markdown/markdown';
    import 'codemirror/mode/javascript/javascript';
    import 'codemirror/mode/python/python';
    import 'codemirror/mode/shell/shell';
    import 'codemirror/addon/mode/overlay.js';
    import { extras } from '$lib/cm_extras';
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
  
    let textArea;
    let editor;
  
    onMount(() => {
        editor = CodeMirror.fromTextArea(textArea, {
            lineNumbers: true,
            mode: 'markdown',
            readOnly: readonly
        });
        extras(editor, dispatch);
        return () => {
            editor.toTextArea();
        };
    });

    setTimeout(() => {
        editor.refresh();
    }, 500);
</script>
  
<textarea bind:this={textArea}>{value}</textarea>
  
<style>
    :global(.CodeMirror) {
        height: auto;
        min-height: 55px;
    }
    :global(.CodeMirror-linewidget > img) {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 0 auto;
    }
</style>