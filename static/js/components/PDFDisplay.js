var PDFDisplay = {
    controller: function($uibModal){
        this.slideIndex = 0;
        if (this.modal === undefined)
            this.modal = false;

        this.left = function() {
            if(this.slideIndex > 0) {
                this.slideIndex -=1;
            }
        };

        this.right = function() {
            if(this.slideIndex < this.slides.length) {
                this.slideIndex += 1;
            }
        };

        this.showModal = function (){
            if (!this.modal) {
                $uibModal.open({
                    template: '<pdf-display slides="$modal.slides" modal="true"></pdf-display>',
                    controller: DocumentModal({slides: this.slides}),
                    controllerAs: '$modal',
                    windowClass: 'document-modal'
                });
            }
        };
    },
    bindings: {
        slides: '=',
        modal: '=?'
    },
    templateUrl: '/partials/pdf-display.pug'
};