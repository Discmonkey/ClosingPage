var GIFDisplay = {
    controller: function(){
        this.path = "";
    },
    bindings: {
        path: '='
    },
    template: '<img style="width:100%;height:100%;" ng-src="{($ctrl.path)}">'
};