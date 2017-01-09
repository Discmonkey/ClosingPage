var PDFDisplay = {
    controller: function(){},
    bindings: {
        path: '='
    },
    template: '<object style="width:100%;height:100%;" data="{($ctrl.path)}" type="application/pdf">' +
    '<p>A pdf <a href="{($ctrl.path)}"> To the pdf </a></p> </object>'
};