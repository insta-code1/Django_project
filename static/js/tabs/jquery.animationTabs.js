$(document).ready(function () {
    "use strict";
    $('#horizontalTab').responsiveTabs({
        rotate: false,
        startCollapsed: 'accordion',
        collapsible: 'accordion',
        setHash: true,
        animation: 'slide',
        disabled: [4],
        activate: function (e, tab) {
            $('.info').html('Tab <strong>' + tab.id + '</strong> activated!');
        },
        activateState: function (e, state) {
            //console.log(state);
            $('.info').html('Switched from <strong>' + state.oldState + '</strong> state to <strong>' + state.newState + '</strong> state!');
        }
    });

});
