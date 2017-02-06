var GIFDisplay = {
    controller: function(){},
    bindings: {
        slides: '='
    },
    template: '<img style="width:100%;height:100%;" src="{($ctrl.slides)}">'
};