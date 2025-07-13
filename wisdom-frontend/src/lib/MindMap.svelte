<script>
    import { onMount } from 'svelte';
    import jsMind, { node } from 'jsmind';
    import 'jsmind/draggable-node';
    import 'jsmind/style/jsmind.css';
    import { node_selected, show_modal, selected_mindmap } from '$lib/store';
    import { bus } from '$lib/bus'; 
    import { query } from '$lib/api';
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    export let data;
    let jmContainer;
    let jm;

    bus.on('insert_node', () => {
        const node = jm.get_node($node_selected);
        add_new_node({
            parentid: $node_selected,
            direction: node.direction
        });
    });

    const add_new_node = data => {
        let parent = jm.get_node(data.parentid);
        let background_color = parent.data['background-color'];
        let text_color = parent.data['foreground-color'];
        query(`/mindmaps/${$selected_mindmap}/nodes/`, 'POST', {background_color, text_color, ...data}).then(result => {
            // console.log(result);
            node_selected.set(result.id);
            location.reload();
            // dispatch('refresh');
        });
    }

    const edit_node = (id, data) => {
        query(`/nodes/${id}`, 'PUT', data).then(result => {
            // console.log(result);
            location.reload();
            // dispatch('refresh');
        });
    }

    const remove_node = async id => {
        if (confirm("Are you sure you want to delete that node?")) {
            let result = await query(`/nodes/${id}`, 'DELETE')
            // console.log(result);
        }
        location.reload();
        // dispatch('refresh');

    }

    const mindnode_update = data => {
        const node = jm.get_node(data.data[0]);
        switch(data.evt) {
            // add new
            case 'insert_node_after':
                add_new_node({
                    parentid: node.parent.id,
                    direction: data.data[4]
                });
                break;
            case 'add_node':
                add_new_node({
                    parentid: data.data[0],
                    direction: data.data[4]
                });
                break;
            // edit
            case 'update_node':
                edit_node(data.data[0], {
                    topic: data.data[1]
                });
                break;
            case 'move_node':
                edit_node(data.data[0], {
                    parentid: data.data[2],
                    direction: data.data[3]
                });
                break;
            case 'expand_node':
                edit_node(data.node, {
                    expanded: 1
                });
                break;
            case 'collapse_node':
                edit_node(data.node, {
                    expanded: 0
                });
                break;
            case 'remove_node':
                remove_node(data.data[0]);
                break;
        }
    }
  
    onMount(() => {
        const mind = {
            meta: {
                name: 'Wisdom App',
                author: 'jirafa',
                version: '1',
            },
            format: 'node_array',
            data
        };
        const options = {
            container: jmContainer,
            editable: true,
            theme: 'primary',
            shortcut: {
                handles: {
                    'edit_node': (jm, e) => {
                        if ($node_selected !== null) show_modal.set('edit_node');
                    },
                    'view_node': (jm, e) => {
                        if ($node_selected !== null) show_modal.set('view_node');
                    },
                    'quiz': (jm, e) => {
                        if ($node_selected !== null) show_modal.set('quiz');
                    },
                    'random_node': (jm, e) => {
                        if ($node_selected !== null) show_modal.set('random_node');
                    }
                },
                mapping: {
                    edit_node: 69,
                    view_node: 86,
                    quiz: 81,
                    random_node: 82
                }
            }
        };
        jm = new jsMind(options);
        jm.show(mind);
        // Move and edit what is in memory.
        if ($node_selected) {
            jm.scroll_node_to_center($node_selected);
            jm.select_node($node_selected);
        }
        // Listen for changes reported by jsMind.
        jm.add_event_listener((type, data) => {
            // jsMind.event_type 1 --> show; 2 --> resize; 3 --> edit; 4 --> select
            if ([1,3].includes(type) && data.evt) mindnode_update(data);
            if (type === 4) node_selected.set(jm.get_selected_node().id);

        });
        // Listen for clicks on the jsMind container to cancel selected node.
        jmContainer.addEventListener('click', () => {
            if (jm.get_selected_node() === null) node_selected.set(null);
        });
    });
  </script>
  
  <div bind:this={jmContainer} class="jsmind-container"></div>
  
  <style>
        .jsmind-container {
            height: 100%;
        }
  </style>