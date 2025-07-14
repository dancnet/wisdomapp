import mitt from 'mitt';
export const bus = mitt();
export const bus_listen = (event, handler) => {
    bus.on(event, handler);
    return () => bus.off(event, handler);
}