var PPTDisplay = {
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
                $uibModal.open(DocumentModal('<ppt-display slides="$modal.slides" modal="true"></ppt-display>',
                    {slides: this.slides}));
            }
        };

        this.keyUp = function (e){
            if (e.keyCode == 39)
                this.right();
            else if (e.keyCode == 37)
                this.left();
        };
    },
    bindings: {
        slides: '=',
        modal: '=?'
    },
    templateUrl: '/angular-components/ppt-display.pug'
};
